# Generated by Django 2.0.1 on 2018-02-01 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20180130_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('id', 'order_status'),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_card', models.CharField(max_length=25)),
                ('number_card', models.PositiveIntegerField(default=0)),
                ('expiration_date', models.DateField(null=True)),
            ],
            options={
                'ordering': ('id', 'name_card', 'number_card', 'expiration_date'),
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=30)),
                ('quantity_products', models.PositiveIntegerField(default=0)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'ordering': ('id', 'name_product', 'quantity_products'),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField(null=True)),
                ('items_price', models.PositiveIntegerField(default=0)),
                ('shipping_price', models.PositiveIntegerField(default=0)),
                ('total_before_tax', models.PositiveIntegerField(default=0)),
                ('estimated_tax', models.PositiveIntegerField(default=0)),
                ('order_total', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('id', 'transaction_date', 'order_total'),
            },
        ),
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('user_id', 'street_name', 'state', 'city', 'zipcode', 'phone_number')},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name_product', 'name_brand', 'price_product', 'quantity_products_stock')},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='quantity_products_stock',
        ),
        migrations.RemoveField(
            model_name='address',
            name='special_notes',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street_name_1',
        ),
        migrations.AddField(
            model_name='address',
            name='street_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_product',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.AddField(
            model_name='transaction',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Address'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Payment'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
        migrations.AddField(
            model_name='payment',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Address'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='api.ShoppingCart', to='api.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
