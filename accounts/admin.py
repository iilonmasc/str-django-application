from django.contrib import admin
from django import forms
import pycountry

from .models import UserAccount

# Register your models here.

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'iban']

    def clean(self):
        # remove whitespaces from "human readable" IBAN
        iban = self.cleaned_data.get('iban').replace(' ', '')

        # check for ISO 3166 country codes
        if not pycountry.countries.get(alpha_2=iban[0:2].upper()):
            raise forms.ValidationError("IBAN not valid(Country Code invalid)")
        # check iban validation code
        # - take country code and validation number
        # - convert country code characters to integers (position in alphabet + 9)
        # - append converted country code and validation to IBAN {IBAN}{Country Code}{Validation}
        # - calculate result module 97
        # - if modulo result is 1, IBAN is valid

        self.cleaned_data['iban'] = iban
        return self.cleaned_data
        
            

class UserAccountAdmin(admin.ModelAdmin):
    form = UserAccountForm
    fields = ['first_name', 'last_name', 'iban']

admin.site.register(UserAccount, UserAccountAdmin)
