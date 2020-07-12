from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
