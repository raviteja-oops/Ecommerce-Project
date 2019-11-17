from django import forms
from admin_app.models import MerchantModal
from merchant_app.models import ProductDetailsModal

class MerchantForm(forms.ModelForm):
    class Meta:
        model = MerchantModal
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductDetailsModal
        fields = "__all__"

