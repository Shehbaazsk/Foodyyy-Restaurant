from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView,PasswordChangeView,LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

class SignUpView(CreateView):
    template_name="accounts/signup.html"
    form_class = CustomUserCreationForm
    success_url= reverse_lazy('accounts:login')

class LoginView(LoginView):
    template_name="accounts/login.html"
    next_page = reverse_lazy('restaurant:menu')
    redirect_authenticated_user=True
    

class LogoutView(LogoutView):
    redirect_field_name=reverse_lazy('accounts:login')
    template_name = 'accounts/logout.html'

@method_decorator(login_required,name='dispatch')
class PasswordChangeView(PasswordChangeView):
    template_name = "accounts/passwordchange.html"
    success_url= reverse_lazy('accounts:login')


