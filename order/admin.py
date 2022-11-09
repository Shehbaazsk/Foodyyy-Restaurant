from django.contrib import admin
from .models import Order,CheckoutAddress
# Register your models here.

@admin.register(CheckoutAddress)
class CheckoutAddressAdmin(admin.ModelAdmin):
    list_display=['user','first_name','phone_number','city','zip_code']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['user','order_id','item','quantity']