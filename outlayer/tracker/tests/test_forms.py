from django.test import TestCase
from django.test import Client
from tracker.forms import UserForm


class User_Form_Test(TestCase):

    #check for password accepted
    def test_valid_password_accepted(self):
        form = UserForm(data={'email': "test@email.com", 'username': "test123", 'password1': "Django@123", 'password2': "Django@123"})
        self.assertTrue(form.is_valid())

    #check for confirmation of password
    def test_invalid_password_not_confirm(self):
        form = UserForm(data={'email': "test@email.com", 'username': "test123", 'password1': "Django@123", 'password2': "Django"})
        self.assertFalse(form.is_valid())

    #check if password is similar to username 
    def test_invalid_password_similar_username(self):
        form = UserForm(data={'email': "test@email.com", 'username': "test123", 'password1': "test", 'password2': "test"})
        self.assertFalse(form.is_valid())

    #check if password is too short
    def test_invalid_password_too_short(self):
        form = UserForm(data={'email': "test@email.com", 'username': "test123", 'password1': "abcd", 'password2': "abcd"})
        self.assertFalse(form.is_valid())

    #check if username is entirely numeric
    def test_invalid_password_numeric(self):
        form = UserForm(data={'email': "test@email.com", 'username': "test123", 'password1': "12345678", 'password2': "12345678"})
        self.assertFalse(form.is_valid())

    #check if password is too common
    def test_invalid_password_too_common(self):
        form = UserForm(data={'email': "test@email.com", 'username': "test123", 'password1': "abcd", 'password2': "abcd"})
        self.assertFalse(form.is_valid())