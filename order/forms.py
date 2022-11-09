from django import forms
from .models import CheckoutAddress

class CheckoutAddressForm(forms.ModelForm):
    class Meta:
        model = CheckoutAddress
        fields = '__all__'
        exclude=['user']
