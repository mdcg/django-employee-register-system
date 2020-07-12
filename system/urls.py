from django.urls import path

from system.views.authentication_views import AuthenticationView, LogoutView
from system.views.home_views import HomeView

urlpatterns = [
    path('', AuthenticationView.as_view(), name='authentication'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
]
