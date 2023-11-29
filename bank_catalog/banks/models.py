from django.db import models

class Bank(models.Model):
    bank_name = models.CharField('Bank name', max_length=64)
    bank_founder_name = models.CharField('Bank\'s founder name' , max_length=64)
    bank_founder_surname = models.CharField('Bank\'s founder surname',max_length=100)
    bank_founder_city = models.CharField('City where bank was started', max_length=255)
    bank_found_date = models.DateTimeField('Date when bank was started')

    def __str__(self):
        return self.bank_name
