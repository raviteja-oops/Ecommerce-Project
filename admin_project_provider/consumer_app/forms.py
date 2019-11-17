from django import forms
from .models import ConsumerDetailsModel


class ConsumerDetailsForm(forms.ModelForm):
    class Meta:
        model = ConsumerDetailsModel
        fields = '__all__'