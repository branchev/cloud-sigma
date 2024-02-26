from django import forms

from sigma_registry.registry.models import RegisteredService


class RegistryForm(forms.ModelForm):
    class Meta:
        model = RegisteredService
        fields = ['name', 'status']
