from django.urls import path

from system.views.authentication_views import AuthenticationView, LogoutView
from system.views.employee_register_views import EmployeeRegisterView
from system.views.employees_list_views import EmployeesListView
from system.views.home_views import HomeView

urlpatterns = [
    path("", AuthenticationView.as_view(), name="authentication"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", HomeView.as_view(), name="home"),
    path("employees/", EmployeesListView.as_view(), name="employees-list",),
    path(
        "employees/register",
        EmployeeRegisterView.as_view(),
        name="employee-register",
    ),
]
