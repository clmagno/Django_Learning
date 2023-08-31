from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category']


class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV File')
