from django import forms
from inventory.models import ProductCategory, Product


class FormProductCategory(forms.ModelForm):
    class Meta:
        model = ProductCategory
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }
        fields = ('name', )


class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nombre del producto'}),
            'category': forms.Select(attrs={'class': 'form-control',
                                            'placeholder': 'Categoría del producto'}),
            'price': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Precio del producto'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de productos'}),
            'image': forms.FileInput(attrs={'class': 'form-control file-upload-info', 
                                            'placeholder': 'Nombre del producto',
                                            }),
        }
        exclude = ('status', 'delete')


class FormEditProduct(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormEditProduct, self).__init__(*args, **kwargs)
        self.fields["image"].required = False

    class Meta:
        model = Product
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nombre del producto'}),
            'category': forms.Select(attrs={'class': 'form-control',
                                            'placeholder': 'Categoría del producto'}),
            'price': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Precio del producto'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de productos'}),
            'image': forms.FileInput(attrs={'class': 'form-control file-upload-info',
                                            'placeholder': 'Nombre del producto'}),
        }
        exclude = ('status', 'delete')
