from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View

from system.forms.authentication_forms import AuthForm


class AuthenticationView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            auth_form = AuthForm()
            context = {
                "form": auth_form,
            }
            return render(request, "system/authentication.html", context)

        return redirect("home")

    def post(self, request):
        if not request.user.is_authenticated:
            auth_form = AuthForm(request.POST)

            username = auth_form.data.get("username")
            password = auth_form.data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo, {user.first_name}!")
                return redirect("home")

            messages.warning(request, "Não foi possível realizar o login.")

            context = {
                "form": auth_form,
            }
            return render(request, "system/authentication.html", context)

        return redirect("home")


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("authentication")
