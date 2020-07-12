 
import secrets

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View

# from core.forms import UserForm
# from core.models import ConfirmationToken

# from .tasks import send_confirmation_email


class AuthenticationView(View):
    def get(self, request):
        # user_form = UserForm()
        context = {
            # "form": user_form,
        }
        return render(request, "system/authentication.html", context)

    # def post(self, request):
    #     user_form = UserForm(request.POST)

    #     if user_form.is_valid():
    #         user = user_form.save()
    #         confirmation_token = ConfirmationToken.objects.create(
    #             user=user,
    #             confirmation_key=secrets.token_hex(16)
    #         )

    #         # Empilhando a task
    #         send_confirmation_email.delay(
    #             confirmation_token.confirmation_key,
    #             user.id,
    #             user.email,
    #         )

    #         messages.success(request, 'Usuário cadastrado com sucesso.')

    #         return redirect('registration')

    #     messages.warning(
    #         request, 'Verifique todos os dados antes de prosseguir.')

    #     context = {
    #         "form": user_form,
    #     }
    #     return render(request, "core/registration.html", context)