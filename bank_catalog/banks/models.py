from django.db import models

class Bank(models.Model):
    bank_name = models.CharField('Bank name', max_length=64)
    bank_description = models.CharField('Bank description', max_length=255)
    bank_city = models.CharField('Bank location', max_length=255)
    bank_founder_name = models.CharField('Bank\'s founder name', max_length=64)
    bank_founder_surname = models.CharField('Bank\'s founder surname', max_length=100)
    bank_founder_birthday = models.DateTimeField('Birthday of bank owner')
    bank_found_date = models.DateTimeField('Date when bank was started')
    bank_avatar = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.bank_name
