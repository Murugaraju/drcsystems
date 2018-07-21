
#users/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

# If you don't do this you cannot use Bootstrap CSS


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="UserEmail", max_length=30,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserRegistrationForm(forms.Form):
    # username = forms.CharField(
    #     required = True,
    #     label = 'Username',
    #     max_length = 32
    # )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget=forms.PasswordInput()
    )