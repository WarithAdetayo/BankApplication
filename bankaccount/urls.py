from django.urls import path

from bankaccount.views import (
    CreateBankAccountView,
    AccountView,
    UpdateAccountView,
    UpdateAccountDetails,
    DeleteAccountView
)

urlpatterns = [
    path('create/', CreateBankAccountView.as_view(), name='create'),
    path('view/', AccountView.as_view(), name='account'),
    path('update/', UpdateAccountView.as_view(), name='update'),
    path('update/details/', UpdateAccountDetails.as_view(), name='update_details'),
    path('delete/', DeleteAccountView.as_view(), name='delete')
]
