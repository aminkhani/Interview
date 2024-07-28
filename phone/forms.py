from django.forms import ModelForm

from phone.models import Phone
from django import forms


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

    def clean(self):
        cleaned_data = super(PhoneForm, self).clean()
        return cleaned_data


class BrandForm(forms.Form):
    brand = forms.CharField(max_length=100, label='Phone Brand')
