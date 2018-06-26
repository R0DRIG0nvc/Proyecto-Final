from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from shoppingcart.models import ShoppingCart
from inventory.models import Product
from shoppingcart.forms import FormShoppingCart, FormBuyProduct

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
    if request.POST:
        if request.POST['action'] == 'loadShoppingCart':
            htmlShopping = ''
            for x in ShoppingCart.objects.filter(client=request.user, status=False).values('name', 'pk'):
                htmlShopping += '<option value="' + str(x['pk']) + '">' + x['name'] + '</option>'
            return JsonResponse({'shoppingCart': htmlShopping})
        elif request.POST['action'] == 'addShoppingCart':
            fomrObj = FormShoppingCart(request.POST)
            if fomrObj.is_valid():
                fomrObj = fomrObj.save(commit=False)
                fomrObj.client = request.user
                fomrObj.save()
            return JsonResponse({})
        elif request.POST['action'] == 'addProdutToShoppingCart':
            formBuyProduct = FormBuyProduct(request.POST)
            if formBuyProduct.is_valid():
                formBuyProduct.save()
                return JsonResponse({'result': True})
            return JsonResponse({'result': False})
    data = {}
    data['formShopping'] = FormShoppingCart()
    data['formBuy'] = FormBuyProduct()
    template_name = "shoppingcart/products.html"
    productList = Product.objects.filter(status=True,
                                         delete=False)
    page = request.GET.get('page', 1)
    paginator = Paginator(productList, 8)
    try:
        data['products'] = paginator.page(page)
    except PageNotAnInteger:
        data['products'] = paginator.page(1)
    except EmptyPage:
        data['products'] = paginator.page(paginator.num_pages)

    return render(request, template_name, data)
