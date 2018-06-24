from django.contrib import admin
from inventory.models import ProductCategory, Product

# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass