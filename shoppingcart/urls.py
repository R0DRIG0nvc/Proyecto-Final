from django.urls import path
from shoppingcart import views


urlpatterns = [
    path('', views.index, name="shoppingcart_index"),
    path('shoppingcart', views.shoppingcart, name="shoppingcart_shoppingcart"),
    path('detailCart/<int:cart_id>', views.detailCart, name="shoppingcart_detailCart"),
    path('products', views.products, name="shoppingcart_products"),
]
