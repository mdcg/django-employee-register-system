 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from system.forms.authentication_forms import AuthForm


class HomeView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "system/home.html", {})
