from django import forms

from sigma_accounting.accounting.warehouse_endpoints import SignaEndpoints


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=64)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = None

    def clean(self):
        cleaned_data = super().clean()
        endpoint = SignaEndpoints()
        endpoint_response = endpoint.login(
            email=cleaned_data['email'],
            password=cleaned_data['password']
        )

        if endpoint_response.status_code != 200:
            raise forms.ValidationError('Invalid email or password')

        self.token = endpoint_response.json()['token']
