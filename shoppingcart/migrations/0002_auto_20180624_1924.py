# Generated by Django 2.0.6 on 2018-06-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]