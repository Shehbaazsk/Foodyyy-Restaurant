from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import FormView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutAddressForm
from restaurant.models import Cart
from .models import Order
# Create your views 
class CheckoutFormView(LoginRequiredMixin,FormView):
    form_class=CheckoutAddressForm
    template_name='restaurant/checkout.html'
    success_url=reverse_lazy('restaurant:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user,ordered=False)
        cart_price=0
        for price in cart:
            cart_price+=price.get_total_price()
        context['carts']=cart
        context['cart_price']=cart_price
        return context
    def post(self, request):
        form=CheckoutAddressForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            instance=form.save(commit=False)
            instance.user=request.user
            instance.first_name=cd['first_name']
            instance.last_name=cd['last_name']
            instance.phone_number=cd['phone_number']
            instance.address=cd['address']
            instance.city=cd['city']
            instance.zip_code=cd['zip_code']
            instance.save()
            cart = Cart.objects.filter(user=request.user,ordered=False)
            for item in cart:
                Order.objects.create(user=self.request.user,item=item.item,price=item.item.price,quantity=item.quantity,checkout_address=instance)
            Cart.objects.filter(user=self.request.user).delete()
        return redirect('restaurant:home')


class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = "restaurant/orders.html"
    context_object_name='orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
