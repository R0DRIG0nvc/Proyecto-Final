from django.db import models
from shoppingcart.models import Buy
from django.contrib.auth.models import User

# Create your models here.


class Send(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
