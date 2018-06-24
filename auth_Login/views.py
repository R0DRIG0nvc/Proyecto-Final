from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, Group

# Create your views here.


def loginUser(request):
    data = {}
    template_name = 'auth_Login/login.html'

    logout(request)
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('inventory_index'))
            else:
                print("usuario o contraseña no validos")
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos!'
                )
        else:
            messages.error(
                request,
                'Usuario o contraseña incorrectos!'
            )
    return render(request, template_name, data)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_login'))


def registerUser(request):
    data = {}
    template_name = 'auth_Login/register.html'

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username,
                                                password=password,
                                                )
                clientGroup = Group.objects.get(name='Cliente')
                clientGroup.user_set.add(user)
                messages.success(
                    request,
                    'Cuenta creada satisfactoriamente!'
                )
                return HttpResponseRedirect(reverse('auth_login'))
            else:
                messages.error(
                    request,
                    'Este usuario ya esta en uso!'
                )
        else:
            messages.error(
                request,
                'Las contraseñas no coinciden!'
            )


    return render(request, template_name, data)
