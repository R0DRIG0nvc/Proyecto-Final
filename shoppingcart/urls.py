from django.urls import path
from shoppingcart import views


urlpatterns = [
    path('', views.index, name="shoppingcart_index"),
    path('shoppingcart', views.shoppingcart, name="shoppingcart_shoppingcart"),
    path('products', views.products, name="shoppingcart_products"),
]
