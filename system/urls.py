from django.urls import path
from system.views.authentication_views import AuthenticationView

urlpatterns = [
    path('', AuthenticationView.as_view(), name='authentication'),
]