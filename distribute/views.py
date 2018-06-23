from django.shortcuts import render

# Create your views here.


def index(request):
    data = {}
    template_name = 'Core/index.html'
    return render(request, template_name, data)
