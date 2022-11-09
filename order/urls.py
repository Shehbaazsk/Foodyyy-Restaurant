from django.urls import path
from .views import CheckoutFormView,OrderListView

app_name='order'

urlpatterns = [
    path("checkout/", CheckoutFormView.as_view(), name="checkout"),
    path("orders/", OrderListView.as_view(), name="orders"),
]
