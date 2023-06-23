from django.urls import path

from banktransaction.views import (
    CreateSendTransactionView,
    CreateReceiveTransactionView,
    BankTransactionView,
    BankTransactionListView,
)

urlpatterns = [
    path("send/", CreateSendTransactionView.as_view(), name="create_send_transaction"),
    path("receive/", CreateReceiveTransactionView.as_view(), name="create_receive_transaction"),
    path("view/<str:reference_number>/", BankTransactionView.as_view(), name="view_transaction"),
    path("list/", BankTransactionListView.as_view(), name="list_transactions"),
]