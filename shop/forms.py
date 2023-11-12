from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'product_name', 'license_term', 'category_name', 'product_price', 'currency_type']


