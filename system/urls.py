from django.urls import path

from system.views.authentication_views import AuthenticationView, LogoutView
from system.views.home_views import HomeView
from system.views.employee_register_views import RegisterEmployeeView

urlpatterns = [
    path('', AuthenticationView.as_view(), name='authentication'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('employee/register', RegisterEmployeeView.as_view(), name='employee-register'),
]
