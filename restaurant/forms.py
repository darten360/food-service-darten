from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator
from django.forms import CheckboxSelectMultiple

from restaurant.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("position", "years_of_experience", "first_name", "last_name")


class CookUpdateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ("username", "position", "first_name", "last_name")


class CookForm(forms.ModelForm):
    MIN_YEARS = 2
    years_of_experience = forms.IntegerField(required=True, validators=[MinValueValidator(MIN_YEARS)])

    class Meta:
        model = Cook
        fields = ("years_of_experience",)


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )
