# Generated by Django 2.0.1 on 2018-02-01 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180201_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
