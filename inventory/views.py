from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from inventory.models import ProductCategory, Product
from inventory.forms import FormProductCategory, FormProduct, FormEditProduct
# Create your views here.


def category(request):
    if request.POST:
        if request.POST['action'] == 'datatable':
            data = []
            if request.POST['search[value]'] == '':
                query = ProductCategory.objects.all()[int(request.POST['start']):int(
                    request.POST['start']) + int(request.POST['length'])]
                json = {"recordsTotal": ProductCategory.objects.all().count(),
                        "recordsFiltered": ProductCategory.objects.all().count()}
            else:
                query = ProductCategory.objects.filter(Q(name__icontains=request.POST['search[value]']))
                json = {"recordsTotal": query.count(),
                        "recordsFiltered": query.count()}
            for x in query:
                status = '<label class="badge badge-danger">Desactivado</label>'
                statusButton = '<button class="btn btn-success mr-2 enable">Habilitar</button>'
                if x.status:
                    status = '<label class="badge badge-success">Activado</label>'
                    statusButton = '<button class="btn btn-warning mr-2 disable">Deshabilitar</button>'
                data.append({'category': x.name,
                             'status': status,
                             'quantity': Product.objects.filter(delete=False, category=x).count(),
                             'action': '<div data-pk=' + str(x.pk) + '>\
                                            <button class="btn btn-primary edit mr-2 edit" data-toggle="modal" data-target="#modalCategory">Editar</button>'
                                            + statusButton +
                                            '<button class="btn btn-danger mr-2 delete">Eliminar</button>\
                                        </div>'
                             })
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'addCategory':
            formCategory = FormProductCategory(request.POST)
            if formCategory.is_valid():
                formCategory.save()
            return JsonResponse({})
        elif request.POST['action'] == 'enableCategory':
            ProductCategory.objects.get(pk=request.POST['pk']).setStatus(True)
            return JsonResponse({})
        elif request.POST['action'] == 'disableCategory':
            ProductCategory.objects.get(pk=request.POST['pk']).setStatus(False)
            return JsonResponse({})
        elif request.POST['action'] == 'deleteCategory':
            ProductCategory.objects.get(pk=request.POST['pk']).deleteCategory()
            return JsonResponse({})
        elif request.POST['action'] == 'editCategory':
            categoryObj = ProductCategory.objects.get(pk=request.POST['pk'])
            if categoryObj.name != 'Sin Categoría':
                categoryObj.name = request.POST['name']
                categoryObj.save()
                return JsonResponse({'result': True})
            return JsonResponse({'result': False})
    data = {}
    data['formCategory'] = FormProductCategory()
    template_name = 'inventory/category.html'
    return render(request, template_name, data)


def product(request):
    if request.POST:
        if request.POST['action'] == 'datatable':
            data = []
            if request.POST['search[value]'] == '':
                query = Product.objects.filter(delete=False)[int(request.POST['start']):int(
                    request.POST['start']) + int(request.POST['length'])]
                json = {"recordsTotal": Product.objects.filter(delete=False).count(),
                        "recordsFiltered": Product.objects.filter(delete=False).count()}
            else:
                query = Product.objects.filter(Q(name__icontains=request.POST['search[value]']), 
                                               delete=False,)
                json = {"recordsTotal": query.count(),
                        "recordsFiltered": query.count()}
            for x in query:
                status = '<label class="badge badge-danger">Desactivado</label>'
                statusButton = '<button class="btn btn-success mr-2 enable">Habilitar</button>'
                if x.status:
                    status = '<label class="badge badge-success">Activado</label>'
                    statusButton = '<button class="btn btn-warning mr-2 disable">Deshabilitar</button>'
                data.append({'image': '<img src="' + x.image.url + '" alt="image">',
                             'name': x.name,
                             'category': x.category.name,
                             'price': x.price,
                             'quantity': x.quantity,
                             'status': status,
                             'action': '<div data-pk=' + str(x.pk) + '>\
                                            <a href=' + reverse('inventory_editProduct', kwargs={'idProduct': x.pk}) + '>\
                                                <button class="btn btn-primary edit mr-2">Editar</button>\
                                            </a>'
                                            + statusButton +
                                            '<button class="btn btn-danger mr-2 delete">Eliminar</button>\
                                        </div>'
                             })
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'enableCategory':
            Product.objects.get(pk=request.POST['pk']).setStatus(True)
            return JsonResponse({})
        elif request.POST['action'] == 'disableCategory':
            Product.objects.get(pk=request.POST['pk']).setStatus(False)
            return JsonResponse({})
        elif request.POST['action'] == 'deleteCategory':
            Product.objects.get(pk=request.POST['pk']).setDelete()
            return JsonResponse({})
    data = {}
    template_name = 'inventory/product.html'
    return render(request, template_name, data)


def addProduct(request):
    data = {}
    data['formProduct'] = FormProduct()
    if request.POST:
        data['formProduct'] = FormProduct(request.POST, request.FILES)
        if data['formProduct'].is_valid():
            data['formProduct'].save()
            return redirect('inventory_product')
    template_name = 'inventory/addProduct.html'
    return render(request, template_name, data)


def editProduct(request, idProduct):
    data = {}
    data['productObj'] = Product.objects.get(pk=idProduct)
    data['formProduct'] = FormEditProduct(instance=data['productObj'])
    if request.POST:
        data['formProduct'] = FormEditProduct(request.POST, request.FILES, instance=data['productObj'])
        if data['formProduct'].is_valid():
            data['formProduct'].save()
            return redirect('inventory_product')
    template_name = 'inventory/editProduct.html'
    return render(request, template_name, data)
