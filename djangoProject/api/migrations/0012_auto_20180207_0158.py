# Generated by Django 2.0.1 on 2018-02-07 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180206_0020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id', 'name_product', 'name_brand', 'product_status')},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ('id', 'user_id', 'status_shopping_cart')},
        ),
        migrations.AlterModelOptions(
            name='shoppingcartdetails',
            options={'ordering': ('id', 'product_id', 'quantity_product')},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_id',
            new_name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_tag',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='shopping_cart_status',
        ),
        migrations.RemoveField(
            model_name='shoppingcartdetails',
            name='name_product',
        ),
        migrations.RemoveField(
            model_name='shoppingcartdetails',
            name='unitary_price_product',
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default='United State', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tags',
            field=models.ManyToManyField(default=None, to='api.Tag'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='status_shopping_cart',
            field=models.CharField(choices=[('EMPTY', 'empty'), ('FULL', 'full')], default='EMPTY', max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(default=None, max_length=140),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_product',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_brand',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable')], default='available', max_length=30),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='descripcion_tag',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name_tag',
            field=models.CharField(default=None, max_length=30),
        ),
    ]