from django.urls import path
from auth_Login import views


urlpatterns = [
    path('login', views.login, name="login"),
]
