from typing import Any, Optional
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
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
        'placeholder': "Your username",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your email address",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Repeat password",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))


class MyprofileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your name",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your last name",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "username",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "email",
        'class': 'w.full py-4 px-6 rounded-xl'
    }))

# class ChangePasswordForm(PasswordChangeForm):
#     # class Meta:
#     #     model = User
#     #     fields = ('password1', )
    
#     # def __init__(self, user_id, *args, **kwargs) -> None:
#     #     super(ChangePasswordForm, self).__init__(*args, **kwargs)
#     #     self.user_id = user_id
#     # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#     #     'placeholder': "Password",
#     #     'class': 'w.full py-4 px-6 rounded-xl'
#     # }))

#     # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#     #     'placeholder': "Repeat password",
#     #     'class': 'w.full py-4 px-6 rounded-xl'
#     # }))
#     pass

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': "Old Password"})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
