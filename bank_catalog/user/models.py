from django.db import models
class User(models.Model):
    user_name = models.CharField('User name', max_length=64)
    user_surname = models.CharField('User surname', max_length=64)
    user_age = models.DateField("User age")
    user_email = models.CharField('User email', max_length=256)
    user_hashpass = models.CharField('User hash pass', max_length=1024)
    bank_id = models.IntegerField('Bank ID where u are in')
# Create your models here.
