from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'password', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password': forms.PasswordInput(attrs={'class': 'form-check-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }