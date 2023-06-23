from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from bankaccount.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        read_only_fields = (
            'account_number',
            'account_holder',
            'balance',
            'date_created',
            'date_updated'
        )
        exclude = ["account_holder", "id"]


class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'created')


class UserSerializer(serializers.ModelSerializer):
    bankaccount = BankAccountSerializer(read_only=True)
    auth_token = AuthTokenSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'bankaccount', 'auth_token')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password', 'placeholder': 'Password'}
                }
        }
        depth = 1


    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    bankaccount = BankAccountSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password', 'bankaccount')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password', 'placeholder': 'Password'}
                }
        }

    def update(self, instance, validated_data):
        bankAccount_data = validated_data.pop('bankaccount', None)
        password = validated_data.pop('password', None)
        super().update(instance, validated_data)
        if bankAccount_data:
            bankAccount = BankAccountSerializer(instance.bankaccount, data=bankAccount_data)
            if bankAccount.is_valid(raise_exception=True):
                bankAccount.save()

        if password:
            instance.set_password(password)
            instance.save()

        return instance
