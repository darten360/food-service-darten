from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormsCookTests(TestCase):

    def test_cook_creation_form(self):
        form_data = {
            "username": "username",
            "password1": "23232lll",
            "password2": "23232lll",
            "first_name": "first_name",
            "last_name": "last_name",
            "position": "Cook",
            "years_of_experience": 3
        }
        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
