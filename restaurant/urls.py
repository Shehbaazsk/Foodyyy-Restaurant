from django.urls import path
from .views import HomeView,AboutView,ContactView,ItemList,ItemDetailView,add_to_cart,CartListView,delete_cart,update_cart

app_name = 'restaurant'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('menu/',ItemList,name='menu'),
    path('menu/<int:id>',ItemList,name='menu_by_category'),
    path('detail/<int:id>',ItemDetailView.as_view(),name='detail'),
    path('add-to-cart/<pk>',add_to_cart,name='addtocart'),
    path('cart',CartListView.as_view(),name='cartlist'),
    path('delete-cart/<int:id>',delete_cart,name='deletecart'),
    path('update-cart/<int:id>',update_cart,name='updatecart'),
]
