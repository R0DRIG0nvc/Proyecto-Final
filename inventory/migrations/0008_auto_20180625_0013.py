# Generated by Django 2.0.6 on 2018-06-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='img-default/productdefault.jpg', upload_to='photoproduct/'),
        ),
    ]
