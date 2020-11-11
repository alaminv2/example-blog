from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'style': 'background : #e0ffe6'
    }))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Email address',
        'style': 'background : #e0ffe6'
    }))
    age = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Your Age',
        'style': 'background : #e0ffe6'
    }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'style': 'background : #e0ffe6'
    }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'style': 'background : #e0ffe6'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')


class loginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'style': 'background : #e0ffe6'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'style': 'background : #e0ffe6'
    }))
