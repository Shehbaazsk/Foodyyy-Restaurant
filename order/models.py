from django.db import models
from django.conf import settings
from restaurant.models import Item
import uuid

# Create your models here

class CheckoutAddress(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    zip_code=models.CharField(max_length=6)

    def __str__(self):
        return self.user.first_name
    
    

class Order(models.Model):
    order_id=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    checkout_address=models.ForeignKey(CheckoutAddress, on_delete=models.SET_NULL,blank=True,null=True)
    ordered_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.order_id} {self.item}'

    def get_total_price(self):
        return self.quantity * self.price
    