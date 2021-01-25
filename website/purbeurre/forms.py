from django import forms
from .models import Product


class ProductSearchForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', )
