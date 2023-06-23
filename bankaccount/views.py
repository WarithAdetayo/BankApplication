from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework import generics
from rest_framework import permissions


from bankaccount.serializers import (
    UserSerializer,
    UserUpdateSerializer,
    BankAccountSerializer
)

# Create your views here.

class CreateBankAccountView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class AccountView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UpdateAccountView(generics.UpdateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserUpdateSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)

    def get_object(self):
        return self.request.user

class UpdateAccountDetails(generics.UpdateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = BankAccountSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)

    def get_object(self):
        return self.request.user.bankaccount

class DeleteAccountView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)

    def get_object(self):
        return self.request.user.bankaccount

    def perform_destroy(self, instance):
        self.request.user.is_active = False
        instance.delete()
        