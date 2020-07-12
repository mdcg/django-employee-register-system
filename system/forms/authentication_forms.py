from django.contrib.auth.models import User
from django.forms import EmailInput, ModelForm, PasswordInput, TextInput


class AuthForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': TextInput(attrs={
                "class": "form-control"
            }),
            'password': PasswordInput(attrs={
                "class": "form-control"
            }),
        }