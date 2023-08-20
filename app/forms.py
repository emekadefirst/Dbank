from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'fullname', 'password')


class SubtractBalanceForm(forms.Form):
    amount = forms.DecimalField(label='Amount to Subtract', min_value=0.01)



class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
