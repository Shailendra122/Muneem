# Generated by Django 4.0.3 on 2022-04-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_data_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_data',
            name='date_of_transaction',
            field=models.DateField(blank=True, null=True),
        ),
    ]