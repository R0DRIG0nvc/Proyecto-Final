from shoppingcart.models import *
from django import forms


class FormShoppingCart(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }
        fields = ('name', )
