from django.contrib import admin
from django import forms
import pycountry
import string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserAccount

# Register your models here.

class UserAccountForm(forms.ModelForm):
    """ModelForm needed for IBAN validation"""
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'iban']

    def change_requested_by_author(self, userdata):
        """Returns true if the current logged in user is the author of this object
        """
        current_useraccount = UserAccount.objects.get(id=self.object_id) if self.object_id else None
        if current_useraccount and current_useraccount.user != self.current_user:
            raise forms.ValidationError("Current User is not allowed to change this account!")
        return True
    def iban_is_valid(self, iban):
        """Returns True if IBAN is valid

        IBAN Structure:
         - First two characters: ISO 3166 ALHPHA-2 country code
         - Following two numbers: checksum
         - Up to 30 characters: account number and bank clearing number

        IBAN Validation:
         1. Check if country code is valid
         2. Convert each country code character to the corresponding integer position in the alphabet and add 9
         3. Generate Checksum: Append converted country code and validation number to IBAN {IBAN}{Country Code}{Validation}
         4. If IBAN Checksum % 97 == 1, the IBAN is valid
        """
        country_code = iban[0:2].upper()
        if not pycountry.countries.get(alpha_2=country_code):
            raise forms.ValidationError("IBAN not valid(Country Code invalid)")
        # ATTENTION: string.ascii_uppercase.index counts from 0, so use +10 instead of +9
        cc_integer = [str(string.ascii_uppercase.index(c)+10) for c in country_code]

        checksum = int(f'{iban[4:]}{"".join(cc_integer)}{iban[2:4]}')

        if checksum % 97 != 1:
            raise forms.ValidationError("IBAN not valid(Validation calculation invalid)")

        return True

    def clean(self):
        """Clean form data, strip whitespaces from IBAN"""
        iban = self.cleaned_data.get('iban').replace(' ', '')
        self.cleaned_data['iban'] = iban
        if self.change_requested_by_author(self.cleaned_data):
            if self.iban_is_valid(iban):
                return self.cleaned_data
        
            

class UserAccountAdmin(admin.ModelAdmin):
    """ModelAdmin needed to display UserAccountForm in django-admin"""
    form = UserAccountForm
    fields = ['first_name', 'last_name', 'iban']
    def get_form(self, request, obj=None, **kwargs):
        """Appends current logged in user to form"""
        
        form = super().get_form(request, obj, **kwargs)
        form.object_id = obj.id if obj else None
        form.current_user = request.user
        return form 
    
    def save_model(self, request, obj, form, change):
        """Override save_model() to add current logged on user"""
        obj.user = request.user
        super().save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        if obj.user == request.user:
            super().delete_model(request, obj)
        else:
            raise forms.ValidationError('You are not allowed to delete this object')


admin.site.login = login_required(admin.site.login)
admin.site.register(UserAccount, UserAccountAdmin)
