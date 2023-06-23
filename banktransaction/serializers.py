from rest_framework import serializers

from banktransaction.models import BankTransaction

class BankTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankTransaction
        exclude = ("date_updated", "id", "account",)
        read_only_fields = ("reference_number", "date_created", "status", "transaction_type")


class BankSendTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankTransaction
        exclude = ("date_updated", "id", "account", )
        read_only_fields = ("reference_number", "date_created", "status", "sender", "transaction_type")
        required_fields = ("recipient", "amount",)

    def create(self, validated_data):
        validated_data["transaction_type"] = "SEND"
        validated_data["sender"] = self.context["request"].user.bankaccount.account_number
        return super().create(validated_data)


class BankReceiveTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankTransaction
        exclude = ("date_updated", "id", "account",)
        read_only_fields = ("reference_number", "date_created", "status", "recipient")

    def create(self, validated_data):
        validated_data["transaction_type"] = "RECEIVE"
        validated_data["recipient"] = self.context["request"].user.bankaccount.account_number
        return super().create(validated_data)
