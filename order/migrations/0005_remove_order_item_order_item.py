# Generated by Django 4.1.2 on 2022-11-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_cart'),
        ('order', '0004_alter_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='restaurant.cart'),
        ),
    ]