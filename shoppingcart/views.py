from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from auth_Login.group_required import group_required
from shoppingcart.models import ShoppingCart, BuyProduct
from shoppingcart.forms import FormShoppingCart, FormBuyProduct
from inventory.models import Product


@group_required(('Cliente', 'Administrador'), login_url='auth_login')
def shoppingcart(request):
    if request.POST:
        if request.POST['action'] == 'datatable':
            data = []
            if request.POST['search[value]'] == '':
                query = ShoppingCart.objects.filter(client=request.user)[int(request.POST['start']):int(
                    request.POST['start']) + int(request.POST['length'])]
                json = {"recordsTotal": ShoppingCart.objects.filter(client=request.user).count(),
                        "recordsFiltered": ShoppingCart.objects.filter(client=request.user).count()}
            else:
                query = ShoppingCart.objects.filter(Q(name__icontains=request.POST['search[value]']),
                                                    client=request.user)
                json = {"recordsTotal": query.count(),
                        "recordsFiltered": query.count()}
            for x in query:
                status = '<label class="badge badge-warning">En Proceso</label>'
                deleteButton = '<button class="btn btn-danger mr-2 delete">Eliminar</button>'
                editButton = '<button class="btn btn-primary editar mr-2">Ver/Editar</button>'
                if x.status:
                    status = '<label class="badge badge-success">Comprado</label>'
                    editButton = '<button class="btn btn-primary editar mr-2">Ver</button>'
                    deleteButton = ''
                totalPrice = 0
                for i in x.buyproduct_set.all():
                    totalPrice += i.quantity * i.product.price

                data.append({'name': '<input type="text" data-pk=' + str(x.pk) + ' class="name" value="' + str(x.name) + '">',
                             'quantity': x.buyproduct_set.all().count(),
                             'price': totalPrice,
                             'status': status,
                             'action': '<div data-pk=' + str(x.pk) + '>\
                                            <a href=' + reverse('shoppingcart_detailCart', kwargs={'cart_id': x.pk}) + '>'
                                                + editButton +
                                            '</a>'
                                            + deleteButton +
                                        '</div>'
                             })
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'delete':
            ShoppingCart.objects.get(pk=request.POST['pk']).delete()
            return JsonResponse({})
        elif request.POST['action'] == 'name':
            cart = ShoppingCart.objects.get(pk=request.POST['pk'])
            cart.name = request.POST['name']
            cart.save()
    data = {}
    data['shoppingCart'] = FormShoppingCart()
    template_name = 'shoppingcart/shoppingcart.html'
    return render(request, template_name, data)


@group_required(('Cliente', 'Administrador'), login_url='auth_login')
def detailCart(request, cart_id):
    cart = ShoppingCart.objects.get(pk=cart_id)
    if request.POST:
        if request.POST['action'] == 'datatable':
            totalPrice = 0
            data = []
            query = cart.buyproduct_set.all()[int(request.POST['start']):int(
                request.POST['start']) + int(request.POST['length'])]
            json = {"recordsTotal": cart.buyproduct_set.all().count(),
                    "recordsFiltered": cart.buyproduct_set.all().count()}
            for x in query:
                quantityInput = x.quantity
                deleteButton = ''
                if not cart.status:
                    quantityInput = '<input type="number" data-pk=' + str(x.pk) + ' class="quantity" value="' + str(x.quantity) + '">'
                    deleteButton = '<button class="btn btn-danger mr-2 delete">Eliminar</button>'
                status = '<label class="badge badge-warning">Agotado</label>'
                if x.product.status:
                    status = x.product.quantity

                price = x.quantity * x.product.price
                totalPrice += price
                data.append({'image': '<img src="' + x.product.image.url + '"alt="Foto" class="img-thumbnail" style="with: 50px; height: 50px">',
                             'category': x.product.category.name,
                             'name': x.product.name,
                             'quantity': quantityInput,
                             'price': price,
                             'status': status,
                             'action': '<div data-pk=' + str(x.pk) + '>'
                                            + deleteButton +
                                        '</div>'
                             })
            priceButton = ''
            if not cart.status:
                priceButton = '<button type="button" class="btn btn-primary" id="buy">Finalizar compra</button>'
            data.append({'image': '',
                         'category': '',
                         'name': '',
                         'quantity': '',
                         'price': '',
                         'status': '<b>Total: </b>',
                         'action': '<span id = "total">' + str(totalPrice) + '</span>',
                         })
            data.append({'image': '',
                         'category': '',
                         'name': '',
                         'quantity': '',
                         'price': '',
                         'status': '',
                         'action': priceButton,
                         })
            json['data'] = data
            json['totalPrice'] = totalPrice
            return JsonResponse(json)
        elif request.POST['action'] == 'delete':
            BuyProduct.objects.get(pk=request.POST['pk']).delete()
            return JsonResponse({})
        elif request.POST['action'] == 'quantity':
            obj = BuyProduct.objects.get(pk=request.POST['pk'])
            price = obj.product.price * int(request.POST['val'])
            obj.quantity = request.POST['val']
            obj.save()
            data = {'val': price}
            return JsonResponse(data)
        elif request.POST['action'] == 'buy':
            cart.status = True
            cart.save()
            return JsonResponse({})
    data = {}
    data['obj'] = cart
    template_name = 'shoppingcart/detailCart.html'
    return render(request, template_name, data)


@group_required(('Cliente', 'Administrador'), login_url='auth_login')
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
