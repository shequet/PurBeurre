from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    code = models.CharField(null=False, max_length=13)
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False)
    nutri_score = models.IntegerField(null=False)

    def __str__(self):
        return '%s' % (self.name, )
