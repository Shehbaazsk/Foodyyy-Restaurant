# Generated by Django 4.1.2 on 2022-11-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_remove_order_user_order_price_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]