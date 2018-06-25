from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def setStatus(self, status):
        self.status = status
        self.save()
        return
    
    def deleteCategory(self):
        if self.name != 'Sin Categoría':
            blankCategoryObj = ProductCategory.objects.filter(name='Sin Categoría')[0]
            for x in self.product_set.all():
                x.category = blankCategoryObj
                x.save()
            self.delete()


class Product(models.Model):
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoproduct/%Y/%m/%d/', default='img-default/productdefault.jpg')
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
