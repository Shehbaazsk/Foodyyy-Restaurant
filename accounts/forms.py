from django import forms
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserCreationForm(forms.ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields=('email','first_name','last_name','phone_no',)
        labels={'phone_no':('Phone no (optional)'),}

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2
    
    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model=CustomUser
        fields = ('first_name','last_name','email','is_active','is_staff','phone_no')

    def clean_password(self):
        return self.initial["password"]