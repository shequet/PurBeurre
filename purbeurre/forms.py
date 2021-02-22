"""
Forms for the purbeurre app
"""

from django import forms
from .models import Product


class ProductSearchForm(forms.ModelForm):
    """
    Product search form
    """
    class Meta:
        """
        Product fields in the form
        """
        model = Product
        fields = ('name', )
