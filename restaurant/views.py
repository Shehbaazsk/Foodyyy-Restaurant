from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView,ListView,DetailView,UpdateView
from .forms import ContactForm,CartAddItemForm
from .models import Item,ItemSubCategory,Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success,info


# Create your views here.

class HomeView(TemplateView):
    template_name = "restaurant/home.html"

class AboutView(TemplateView):
    template_name = "restaurant/about.html"

class ContactView(FormView):
    template_name = "restaurant/contact.html"
    form_class=ContactForm
    success_url=reverse_lazy('restaurant:home')


def ItemList(request,id=None):
    id=id
    categories=ItemSubCategory.objects.all()
    items=Item.objects.filter(available=True)
    form=CartAddItemForm()
    if id:
        items=Item.objects.filter(sub_category__id=id)
    return render(request, "restaurant/menu.html",{'category':id,'categories':categories,'items':items,'form':form})


class ItemDetailView(DetailView):
    model = Item
    template_name = "restaurant/detail.html"
    context_object_name='item'
    pk_url_kwarg='id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Item.objects.all()
        return context
    
@login_required(login_url='accounts:login')
def add_to_cart(request,pk):
    item=get_object_or_404(Item,pk=pk)
    form=CartAddItemForm(request.POST)
    cart=Cart.objects.filter(user=request.user,ordered=False,item=item)
    if cart:
        info(request, "already in cart")
    else:
        if form.is_valid():
            cd=form.changed_data
            instance=form.save(commit=False)
            instance.user = request.user
            instance.item=item
            instance.ordered=False
            instance.save()
    # cart,created=Cart.objects.get_or_create(item=item,user=request.user,ordered=False)
    return redirect("restaurant:menu")


class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = "restaurant/cartlist.html"
    context_object_name='carts'

    def get_queryset(self):
        return Cart.objects.all().filter(user=self.request.user,ordered=False)

@login_required()
def delete_cart(request,id=None):
    item=Cart.objects.get(id=id)
    item.delete()
    success(request, "Item Removed Sucessfully")
    return redirect('restaurant:cartlist')

@login_required()
def update_cart(request,id):
    id=get_object_or_404(Cart,id=id)
    form=CartAddItemForm(instance=id)
    if request.method == 'POST':
        form=CartAddItemForm(request.POST,instance=id)
        if form.is_valid():
            form.save()
    return redirect('restaurant:cartlist')


