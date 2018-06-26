from shoppingcart.models import ShoppingCart, BuyProduct
from django import forms


class FormShoppingCart(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Carro de Compra'}),
        }
        fields = ('name', )


class FormBuyProduct(forms.ModelForm):
    class Meta:
        model = BuyProduct
        widgets = {
            'shoppingcart': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nombre del Carro de Compra'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control',
                                               'type': 'number',
                                               'min': '1',
                                               'value': '1'}),
        }
        exclude = ()
