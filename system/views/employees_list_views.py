from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from system.models import Employee


class EmployeesListView(View):
    @method_decorator(login_required)
    def get(self, request):
        employee_list = Employee.objects.filter(is_superuser=False)
        context = {
            "employee_list": employee_list,
        }
        return render(request, "system/employee_list.html", context)
