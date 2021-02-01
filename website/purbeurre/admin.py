from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code', ]


admin.site.register(models.Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', ]


admin.site.register(models.Category, CategoryAdmin)
