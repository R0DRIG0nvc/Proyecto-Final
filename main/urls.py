"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from auth_Login.views import loginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginUser, name='auth_login'),
    path('auth_Login/', include('auth_Login.urls'), name='auth_Login'),
    path('inventory/', include('inventory.urls'), name='inventory'),
    path('shoppingcart/', include('shoppingcart.urls'), name='shoppingcart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
