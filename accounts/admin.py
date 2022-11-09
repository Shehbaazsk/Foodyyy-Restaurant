from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group
# Register your models here.

admin.site.unregister(Group)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    list_display=('first_name','last_name','email','is_staff','is_superuser')
    readonly_fields=['date_joined',]
    fieldsets = (
        (None,{'fields':('email','password','first_name','last_name')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser','user_permissions')}),
        ('Dates',{'fields':('last_login','date_joined')})
    )
    add_fieldsets = (
        (None,{'classes':('wide',),'fields':('first_name','last_name','email','password1','password2')}),
        
    )
    search_fields = ('first_name','last_name','email')
    ordering= ('first_name','email',)
    filter_horizontal = ()

    class Meta:
        model=CustomUser