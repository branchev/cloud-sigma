from django.http import JsonResponse

from sigma_registry.registry.models import RegisteredService
from sigma_registry.registry.forms import RegistryForm


class RegistryView(View):

    def get(self, request):
        return JsonResponse(
            list(RegisteredService.objects.values()),
            safe=False
        )

    def post(self, request):
        form = RegistryForm(request.POST)
        if form.is_valid():
            RegisteredService.objects.get_or_create(**form.cleaned_data)

        return JsonResponse({'error': form.errors}, status=400)
