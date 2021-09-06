from django.test import TestCase

from .admin import UserAccountForm
from .models import UserAccount

class UserAccountTestCase(TestCase):
  def test_iban_is_validated(self):
    """Harry Honest has a valid IBAN, validation should be successful"""
    harry = {'first_name':'Harry', 'last_name':'Honest', 'iban':'DE68210501700012345678'}
    self.assertTrue(UserAccountForm(data=harry).is_valid())

  def test_iban_is_validated(self):
    """Simon Shifty has an invalid IBAN, validation should fail"""
    simon = {'first_name':'Simon', 'last_name':'Shifty', 'iban':'DE69210501700012345678'}
    self.assertFalse(UserAccountForm(data=simon).is_valid())
      

