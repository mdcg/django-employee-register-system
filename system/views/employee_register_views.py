from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from system.forms.user_forms import UserForm


class RegisterEmployeeView(View):
    @method_decorator(login_required)
    def get(self, request):
        user_form = UserForm()
        context = {
            "form": user_form,
        }
        return render(request, "system/employee_register.html", context)

    @method_decorator(login_required)
    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, "Funcionário cadastrado com sucesso!")
            return redirect("employee-register")

        context = {
            "form": user_form,
        }
        return render(request, "system/employee_register.html", context)
