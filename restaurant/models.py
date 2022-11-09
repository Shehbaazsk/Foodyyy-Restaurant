from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class ItemCategory(models.Model):
    name=models.CharField(max_length=50)

    class meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name
    

class ItemSubCategory(models.Model):
    category=models.ForeignKey(ItemCategory, on_delete=models.PROTECT)
    name=models.CharField(max_length=50)

    class Meta:
        ordering=['name']
        verbose_name_plural='subcategories'

    def __str__(self):
        return f'{self.name} -->({self.category})'

    def get_absolute_url(self):
        return reverse("restaurant:menu_by_category",args=[self.id])
    
    

class Item(models.Model):
    sub_category=models.ForeignKey(ItemSubCategory, on_delete=models.PROTECT)
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='items/',default='default.png')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['name']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("restaurant:detail", kwargs={"id": self.id})



class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_quantity(self):
        return self.quantity

    def get_total_price(self):
        return self.quantity * self.item.price
    
    
    
