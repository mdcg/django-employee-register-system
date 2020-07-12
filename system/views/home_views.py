from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


class HomeView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "system/home.html", {})
