from django.contrib import admin
from bankaccount.models import BankAccount

# Register your models here.

class BankAccountAdmin(admin.ModelAdmin):
    list_display = (
        'account_number',
        'account_holder',
        'balance',
        'phone_number',
        'birth_date',
        'address',
        'city',
        'state',
        'zipcode',
        'date_created',
        'date_updated'
    )

admin.site.register(BankAccount, BankAccountAdmin)
