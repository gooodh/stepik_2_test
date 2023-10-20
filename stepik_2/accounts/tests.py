from django.test import TestCase
from .models import User
from .forms import CustomUserCreationForm  #, LoginForm


class RegistrationFormTest(TestCase):

    def test_valid_registration_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'testname',
            'last_name': 'teslasttanme',
            'email': 'john.doe@example.com',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_password(self):
        form_data1 = {
            'username': 'testuser',
            'password1': '123',
            'password2': '123',
            'first_name': 'testname',
            'last_name': 'teslasttanme',
            'email': 'john.doe@example.com',

        }
        small_pass_form = CustomUserCreationForm(data=form_data1)
        self.assertFalse(small_pass_form.is_valid())
        self.assertIn('password1', small_pass_form.errors)

        form_data2 = {
            'username': 'testuser',
            'password1': 'one_password',
            'password2': 'another_password',
            'first_name': 'testname',
            'last_name': 'teslasttanme',
        }
        different_pass_form = CustomUserCreationForm(data=form_data2)
        self.assertFalse(different_pass_form.is_valid())
        self.assertIn('password2', different_pass_form.errors)

    def test_invalid_age(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'testname',
            'last_name': 'teslasttanme',
            'email': 'john.doe@example.com',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)

    def test_invalid_birth_date(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'testname',
            'last_name': 'teslasttanme',
            'email': 'john.doe@example.com',

        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('birth_date', form.errors)
