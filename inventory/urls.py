from django.urls import path
from inventory import views


urlpatterns = [
    path('index', views.index, name="inventory_index"),
]
