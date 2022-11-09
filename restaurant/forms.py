from django import forms
from .models import Cart

class CartAddItemForm(forms.ModelForm):

    class Meta:
        model=Cart
        fields=['quantity']

    



class ContactForm(forms.Form):
    name=forms.CharField(max_length=30,label="Your Name",widget=forms.TextInput(attrs={'placeholder':"Enter Your Name",}),)
    email=forms.EmailField(max_length=50,label="Your E-mail",widget=forms.EmailInput(attrs={'placeholder':'Enter Your E-mail',}),)
    msg=forms.CharField(max_length=500,label="Messages",widget=forms.Textarea(attrs={'rows':5,'placeholder':'Write Your Message Here...'}),)