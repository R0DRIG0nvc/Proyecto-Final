from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoproduct/%Y/%m/%d/', default='img-default/productdefault.jpg')
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
