from django.db import models

# Create your models here.

class UserAccount(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    iban = models.CharField(max_length=34)
    # IBAN validation:
    # - 2 characters: for ISO 3166 ALHPHA-2 country code
    # - 2 numbers: checksum
    # - up to 30 characters: account number and bank clearing number
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.iban}'
