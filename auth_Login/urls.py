from django.urls import path
from auth_Login import views


urlpatterns = [
    path('login', views.loginUser, name="auth_login"),
    path('register', views.registerUser, name="auth_register"),
]
