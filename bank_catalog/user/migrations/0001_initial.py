# Generated by Django 4.2.7 on 2023-12-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, verbose_name='User name')),
                ('user_surname', models.CharField(max_length=64, verbose_name='User surname')),
                ('user_age', models.DateField(verbose_name='User age')),
                ('user_email', models.CharField(max_length=256, verbose_name='User email')),
                ('user_hashpass', models.CharField(max_length=1024, verbose_name='User hash pass')),
                ('bank_id', models.IntegerField(verbose_name='Bank ID where u are in')),
            ],
        ),
    ]