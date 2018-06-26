from django.db import models
from inventory.models import Product
from django.contrib.auth.models import User

# Create your models here.


class ShoppingCart(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)


class BuyProduct(models.Model):
    shoppingcart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Buy(models.Model):
    shoppingcart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
