from typing import Any, Optional
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    labels = {
        "username":  _('Ime'),
        "password": "Lozinka",
    }  

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Ime",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Korisničko ime",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your email address",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Lozinka",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Ponovljena lozinka",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))


class MyprofileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
    labels = {
        "first_name":  "Ime",
        "last_name": "Prezime",
        "username": "Korisničko ime",
        "email" : "email"
    }  

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Ime",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Prezime",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Korisničko ime",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Email",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

class ChangingPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Stara Lozinka",
        'class': 'w.full py-4 px-6 rounded-xl',
        'type':'password'
    }))

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Nova Lozinka",
        'class': 'w.full py-4 px-6 rounded-xl',
        'type':'password'
    }))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Potvrda nove lozinke",
        'class': 'w.full py-4 px-6 rounded-xl',
        'type':'password'
    }))
