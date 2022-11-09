from django.urls import path
from .views import SignUpView,LoginView,PasswordChangeView,LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUpView.as_view(),name = 'signup'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('changepassword/',PasswordChangeView.as_view(),name = 'changepassword'),
    path('logout/',LogoutView.as_view(),name = 'logout'),

]
