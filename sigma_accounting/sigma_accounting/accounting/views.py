from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from sigma_routers.routers import SigmaEndpoints

from sigma_accounting.accounting.forms import LoginForm
from sigma_accounting.accounting.utils import encrypt_cookie, decrypt_cookie
from sigma_accounting.settings import WAREHOUSE_URL


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('accounting:items')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:    
        return super().post(request, *args, **kwargs)

    def form_valid(self, form: Any) -> HttpResponse:
        response = HttpResponse(self.success_url)
        response.set_cookie(
            'token', encrypt_cookie({'sigma_user_token': form.token})
        )
        return response


class ItemsView(TemplateView):
    template_name = 'items.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        token = request.COOKIES.get('token')
        decrypted_value = decrypt_cookie(token)

        if not decrypted_value:
            raise HttpResponseForbidden()

        token = decrypted_value['sigma_user_token']

        endpoints = SigmaEndpoints(warehouse_url=WAREHOUSE_URL)
        response = endpoints.get_items(token)

        if response.status_code != 200:
            raise HttpResponseForbidden()

        self.items = response.json()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['items'] = self.items

        print(context['items'])
        return context
