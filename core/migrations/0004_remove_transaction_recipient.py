# Generated by Django 4.0.5 on 2022-06-27 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_transaction_recipient_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='recipient',
        ),
    ]
