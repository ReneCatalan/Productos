from django.forms import ModelForm
from Productos.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['ID', 'Titulo', 'Precio']
        
class EditProducto(ModelForm):

    class Meta:
        model = Producto
        fields = ['ID', 'Titulo', 'Precio']
        
class UserForm(ModelForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Producto
        fields = ('username','password1', 'password2', )