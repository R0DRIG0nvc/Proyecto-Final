from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from inventory.models import ProductCategory, Product
from inventory.forms import FormProductCategory
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
                             'quantity': x.product_set.all().count(),
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
    data = {}
    template_name = 'inventory/product.html'
    if request.POST['action'] == 'datatable':
        data = []
        if request.POST['search[value]'] == '':
            query = Product.objects.all()[int(request.POST['start']):int(
                request.POST['start']) + int(request.POST['length'])]
            json = {"recordsTotal": Product.objects.all().count(),
                    "recordsFiltered": Product.objects.all().count()}
        else:
            query = Product.objects.filter(
                Q(name__icontains=request.POST['search[value]']))
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
                            'quantity': x.product_set.all().count(),
                            'action': '<div data-pk=' + str(x.pk) + '>\
                                        <button class="btn btn-primary edit mr-2 edit" data-toggle="modal" data-target="#modalCategory">Editar</button>'
                            + statusButton +
                            '<button class="btn btn-danger mr-2 delete">Eliminar</button>\
                                    </div>'
                            })
        json['data'] = data
        return JsonResponse(json)
    return render(request, template_name, data)
