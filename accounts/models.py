from django.db import models

# Create your models here.

class UserAccount(models.Model):
    """UserAccount model for a person with an IBAN
       
       Instance variables:
       first_name -- First name of the person
       last_name -- Last name of the person
       iban -- IBAN of the person, max 34 characters according to ISO 13616-1:2020
   """
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    iban = models.CharField(max_length=34)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.iban}'
