from django.shortcuts import render
from django.http import JsonResponse
from shoppingcart.models import *
from inventory.models import Product
from shoppingcart.forms import *

# Create your views here.


def index(request):
    data = {}
    template_name = 'blankPage.html'
    return render(request, template_name, data)


def shoppingcart(request):
    if request.POST:
        if request.POST['action'] == 'datatable':
            data = []
            if request.POST['search[value]'] == '':
                query = ShoppingCart.objects.all()[int(request.POST['start']):int(
                    request.POST['start']) + int(request.POST['length'])]
                json = {"recordsTotal": ShoppingCart.objects.all().count(),
                        "recordsFiltered": ShoppingCart.objects.all().count()}
            else:
                query = ShoppingCart.objects.filter(Q(name__icontains=request.POST['search[value]']))
                json = {"recordsTotal": query.count(),
                        "recordsFiltered": query.count()}
            for x in query:
                status = '<label class="badge badge-warning">En Proceso</label>'
                deleteButton = '<button class="btn btn-danger mr-2 delete">Eliminar</button>'
                if x.status:
                    status = '<label class="badge badge-success">Comprado</label>'
                    deleteButton = ''
                data.append({'name': x.name,
                             'quantity': x.buyproduct_set.all().count(),
                             'status': status,
                             'action': '<div data-pk=' + str(x.pk) + '>\
                                            <button class="btn btn-primary editar mr-2">Ver/Editar</button>'
                                            + deleteButton +
                                        '</div>'
                             })
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'delete':
            ShoppingCart.objects.get(pk=request.POST['pk']).delete()
            return JsonResponse({})
    data = {}
    data['shoppingCart'] = FormShoppingCart()
    template_name = 'shoppingcart/shoppingcart.html'
    return render(request, template_name, data)


def products(request):
    data = {}
    template_name = "shoppingcart/products.html"
    data['products'] = Product.objects.all()
    return render(request, template_name, data)
