# Generated by Django 3.1.5 on 2021-02-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0002_auto_20210201_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutriment_fiber',
            field=models.FloatField(null=True),
        ),
    ]
