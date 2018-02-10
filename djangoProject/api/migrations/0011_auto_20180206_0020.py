# Generated by Django 2.0.1 on 2018-02-06 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_auto_20180205_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCartDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(default=None, max_length=30)),
                ('quantity_product', models.PositiveIntegerField(default=0)),
                ('unitary_price_product', models.PositiveIntegerField(default=0)),
                ('total_price_product', models.PositiveIntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            options={
                'ordering': ('id', 'name_product', 'quantity_product'),
            },
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='address_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='card_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id', 'order_date', 'total_price')},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ('id', 'user_id', 'shopping_cart_status')},
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='name_product',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='order',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='quantity_products',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='address_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='card_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='estimated_tax',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='items_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='shopping_cart_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_before_tax',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shopping_cart_status',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='shoppingcartdetails',
            name='shopping_cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='products_cart',
            field=models.ManyToManyField(through='api.ShoppingCartDetails', to='api.Product'),
        ),
    ]
