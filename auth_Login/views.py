from django.shortcuts import render

# Create your views here.


def login(request):
    data = {}
    template_name = 'blankPage.html'
    return render(request, template_name, data)
