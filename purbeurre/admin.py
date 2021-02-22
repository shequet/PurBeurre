"""
Used to register models into admin view
"""

from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    """
    Admin product
    """
    search_fields = ['name', 'code', ]


admin.site.register(models.Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin category
    """
    search_fields = ['name', ]


admin.site.register(models.Category, CategoryAdmin)
