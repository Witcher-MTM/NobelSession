# Generated by Django 4.2.7 on 2023-12-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0004_rename_bank_founder_city_bank_bank_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_city',
            field=models.CharField(max_length=255, verbose_name='Bank location'),
        ),
    ]