from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=128, db_index=True)
    code = models.CharField(null=False, max_length=13, unique=True)
    link = models.CharField(null=True, max_length=1024)
    quantity = models.CharField(null=True, max_length=20)
    nutri_score = models.CharField(null=False, max_length=1)
    image = models.CharField(null=True, max_length=1024)

    def __str__(self):
        return '%s' % (self.name, )


class Category(models.Model):
    name = models.CharField(null=False, max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return '%s' % (self.name, )


class Brand(models.Model):
    name = models.CharField(null=False, max_length=255, db_index=True, unique=True)

    def __str__(self):
        return '%s' % (self.name,)


class ProductBrand(models.Model):
    product = models.ForeignKey(Product, related_name='product_brand_products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='product_brand_brands', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'brand', )


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, related_name='product_category_products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='product_category_categories', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'category', )
        verbose_name_plural = 'productCategories'


class Store(models.Model):
    name = models.CharField(null=False, max_length=255, db_index=True, unique=True)

    def __str__(self):
        return '%s' % (self.name, )


class ProductStore(models.Model):
    product = models.ForeignKey(Product, related_name='product_store_products', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='product_store_stores', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'store', )


class ProductSubstitute(models.Model):
    product = models.ForeignKey(Product, related_name='product_substitute_products', on_delete=models.CASCADE)
    substitute_product = models.ForeignKey(Product, related_name='product_substitute_substitute_product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='product_substitute_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'substitute_product', 'user', )

