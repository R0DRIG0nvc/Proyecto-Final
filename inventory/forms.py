from django import forms
from inventory.models import ProductCategory


class FormProductCategory(forms.ModelForm):
    class Meta:
        model = ProductCategory
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }
        fields = ('name', )
