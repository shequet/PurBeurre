"""
Models of the purbeurre app
"""
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """
    Store category

    The category is unique

    Fields:
        name {CharField} -- The name of the category (max_length=255)

    Returns:
        {string} -- The name of the category
    """
    name = models.CharField(null=False, max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name,)


class Product(models.Model):
    """
    Store a product

    The product code is unique

    Fields:
        name {CharField} -- The name of the product (null=False, max_length=128, db_index=True)
        code {CharField} -- The code of the product (null=False, max_length=128, unique=True)
        link {CharField} -- The link of the product (null=True, max_length=1024)
        quantity {CharField} -- The quantity of the product (null=True, max_length=128)
        nutri_score {CharField} -- The quantity of the product (null=False, max_length=1)
        image {CharField} -- The quantity of the product (null=True, max_length=1024)
        nutriment_energy {FloatField} -- The nutriment energy of the product (null=True)
        nutriment_sugars {FloatField} -- The nutriment sugars of the product (null=True)
        nutriment_salt {FloatField} -- The nutriment salt of the product (null=True)
        nutriment_fat {FloatField} -- The nutriment fat of the product (null=True)
        nutriment_saturated_fat {FloatField} -- The nutriment saturated_fat of the product (null=True)
        nutriment_sodium {FloatField} -- The nutriment sodium of the product (null=True)
        nutriment_proteins {FloatField} -- The nutriment proteins of the product (null=True)
        nutriment_carbohydrates {FloatField} -- The nutriment carbohydrates of the product (null=True)
        nutriment_fiber {FloatField} -- The nutriment fiber of the product (null=True)
        category {ForeignKey} -- The category of the product (null=True, default=None)

    Returns:
        {string} -- The name of the product
    """

    name = models.CharField(null=False, max_length=128, db_index=True)
    code = models.CharField(null=False, max_length=128, unique=True)
    link = models.CharField(null=True, max_length=1024)
    quantity = models.CharField(null=True, max_length=128)
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
        return '%s' % (self.name,)


class ProductSubstitute(models.Model):
    """
    Store a substitute product

    Fields:
        product {ForeignKey} -- The product to be substituted
        substitute_product {ForeignKey} -- The substituted product
        user {ForeignKey} -- The user
    """
    product = models.ForeignKey(Product, related_name='product_substitute_products', on_delete=models.CASCADE)
    substitute_product = models.ForeignKey(Product, related_name='product_substitute_substitute_product',
                                           on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='product_substitute_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'substitute_product', 'user',)
