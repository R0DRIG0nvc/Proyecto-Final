from django.urls import path
from inventory import views


urlpatterns = [
    # path('index', views.index, name="inventory_index"),
    path('category', views.category, name="inventory_category"),
    path('product', views.product, name="inventory_product"),
    path('addProduct', views.addProduct, name="inventory_addProduct"),
    path('editProduct/<int:idProduct>', views.editProduct, name="inventory_editProduct"),
]
