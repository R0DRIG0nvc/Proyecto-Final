from django.shortcuts import render

# Create your views here.


def login(request):
    data = {}
    template_name = 'auth_Login/login.html'
    return render(request, template_name, data)
