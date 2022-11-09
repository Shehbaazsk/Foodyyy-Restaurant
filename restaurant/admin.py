from django.contrib import admin
from .models import ItemCategory,ItemSubCategory,Item,Cart

# Register your models here.

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemSubCategory)
class ItemSubCategoryAdmin(admin.ModelAdmin):
    list_display=['name','category_id']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','name','price','sub_category','available']
    list_editable=['price','available']
    ordering=['name','available']
    search_fields=['name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user','item','quantity','ordered']
    list_filter=['ordered']





    
