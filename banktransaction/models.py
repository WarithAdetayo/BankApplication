from django.db import models
from bankaccount.models import BankAccount

import uuid
import random
import string
# Create your models here.


TRANSACTION_TYPE = (
    ("SEND", "SEND"),
    ("RECEIVE", "RECEIVE"),
)

TRANSACTION_STATUS = (
    ("SUCCESS", "SUCCESS"),
    ("FAILED", "FAILED"),
    ("PENDING", "PENDING"),
)


def generate_transaction_reference(length=10):
    # Define the characters to use for generating the reference number
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Generate a random reference number with the specified length
    reference_number = ''.join(random.choice(characters) for _ in range(length))

    return reference_number


class BankTransaction(models.Model):
    reference_number = models.CharField(max_length = 10, unique=True, null=False, default=generate_transaction_reference, editable=False)
    transaction_type = models.CharField(max_length=10, null=False, choices=TRANSACTION_TYPE)

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=10, null=False, default="PENDING", choices=TRANSACTION_STATUS)
    description = models.CharField(max_length=100, null=True)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    date_updated = models.DateTimeField(auto_now=True)
    recipient = models.CharField(max_length=10, null=True)
    sender = models.CharField(max_length=10, null=True)


    def __str__(self):
        return "Transaction<%s, %s>" % (self.reference_number, self.transaction_type)

