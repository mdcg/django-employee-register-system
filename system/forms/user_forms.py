from system.models import Employee
from django.forms import EmailInput, ModelForm, PasswordInput, TextInput


class UserForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "role",
        ]

        widgets = {
            "first_name": TextInput(attrs={"class": "form-control"}),
            "last_name": TextInput(attrs={"class": "form-control"}),
            "role": TextInput(attrs={"class": "form-control"}),
            "email": EmailInput(attrs={"class": "form-control"}),
            "username": TextInput(attrs={"class": "form-control"}),
            "password": PasswordInput(attrs={"class": "form-control"}),
        }
