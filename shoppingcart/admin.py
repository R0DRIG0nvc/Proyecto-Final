from django.contrib import admin
from shoppingcart.models import ShoppingCart, BuyProduct, Buy
# Register your models here.


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(BuyProduct)
class BuyProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    pass
