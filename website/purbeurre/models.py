from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(null=False, max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name, )


class Product(models.Model):
    name = models.CharField(null=False, max_length=128, db_index=True)
    code = models.CharField(null=False, max_length=13, unique=True)
    link = models.CharField(null=True, max_length=1024)
    quantity = models.CharField(null=True, max_length=20)
    nutri_score = models.CharField(null=False, max_length=1)
    image = models.CharField(null=True, max_length=1024)

    nutriment_energy = models.FloatField(null=True)
    nutriment_sugars = models.FloatField(null=True)
    nutriment_salt = models.FloatField(null=True)
    nutriment_fat = models.FloatField(null=True)
    nutriment_saturated_fat = models.FloatField(null=True)
    nutriment_sodium = models.FloatField(null=True)
    nutriment_proteins = models.FloatField(null=True)
    nutriment_carbohydrates = models.FloatField(null=True)
    nutriment_fiber = models.FloatField(null=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name, )


class ProductSubstitute(models.Model):
    product = models.ForeignKey(Product, related_name='product_substitute_products', on_delete=models.CASCADE)
    substitute_product = models.ForeignKey(Product, related_name='product_substitute_substitute_product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='product_substitute_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'substitute_product', 'user', )

