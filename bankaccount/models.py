from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class BankAccount(models.Model):
    account_number = models.CharField(max_length=10, null=False, unique=True, editable=False)
    account_holder = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bankaccount')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    phone_number = models.CharField(max_length=15, unique=True, null=True)
    birth_date = models.DateField(null=True)

    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Account<%s, %s>" % (self.account_number, self.account_holder.username)


def generate_account_number():
    import random
    account_number = ""
    for i in range(10):
        account_number += str(random.randint(0, 9))
    return account_number


@receiver(post_save, sender=User)
def create_user_bank_account(sender, instance, created, **kwargs):
    if created:
        # Create a bank account and a login token for each registered user
        BankAccount.objects.create(
            account_holder=instance,
            account_number=generate_account_number()
        )

        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_bank_account(sender, instance, **kwargs):
    instance.bankaccount.save()
