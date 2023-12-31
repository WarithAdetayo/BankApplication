# Generated by Django 3.2.19 on 2023-06-23 16:34

import banktransaction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banktransaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banktransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='banktransaction',
            name='reference_number',
            field=models.CharField(default=banktransaction.models.generate_transaction_reference, editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='banktransaction',
            name='transaction_type',
            field=models.CharField(choices=[('SEND', 'SEND'), ('RECEIVE', 'RECEIVE')], max_length=10),
        ),
    ]
