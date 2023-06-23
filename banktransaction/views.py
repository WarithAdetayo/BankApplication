from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import (BasicAuthentication, TokenAuthentication)

from banktransaction.models import BankTransaction
from banktransaction.serializers import (
    BankTransactionSerializer,
    BankSendTransactionSerializer,
    BankReceiveTransactionSerializer
)

# Create your views here.


class CreateSendTransactionView(generics.CreateAPIView):
    queryset = BankTransaction.objects.all()
    serializer_class = BankSendTransactionSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        serializer.save(account=self.request.user.bankaccount)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)


        if serializer.validated_data["amount"] > self.request.user.bankaccount.balance:
            # Insufficient funds
            error = "Insufficient funds"
            serializer.validated_data["status"] = "FAILED"
        else:
            account = self.request.user.bankaccount
            account.balance -= serializer.validated_data["amount"]
            account.save()
            error = None
            serializer.validated_data["status"] = "SUCCESS"

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {"error": error}
        data.update(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class CreateReceiveTransactionView(generics.CreateAPIView):
    queryset = BankTransaction.objects.all()
    serializer_class = BankReceiveTransactionSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        serializer.save(account=self.request.user.bankaccount)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        account = self.request.user.bankaccount

        # Verify that the sender can fufil the transaction
        account.balance += serializer.validated_data["amount"]
        account.save()
        serializer.validated_data["status"] = "SUCCESS"


        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {"error": None}
        data.update(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)



class BankTransactionView(generics.RetrieveAPIView):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return BankTransaction.objects.get(
            account=self.request.user.bankaccount,
            reference_number=self.kwargs['reference_number']
        )


class BankTransactionListView(generics.ListAPIView):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BankTransaction.objects.filter(account=self.request.user.bankaccount)
