from django.urls import path
from inventory import views


urlpatterns = [
    path('category', views.category, name="inventory_category"),
    path('product', views.product, name="inventory_product"),
]
