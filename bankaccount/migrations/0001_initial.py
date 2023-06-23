# Generated by Django 3.2.19 on 2023-06-22 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(editable=False, max_length=10, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('phone_number', models.CharField(max_length=10, null=True, unique=True)),
                ('birth_date', models.DateField(null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('account_holder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bankaccount', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]