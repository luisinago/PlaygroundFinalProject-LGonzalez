#from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
   
    password = None
    email = forms.EmailField(label="Email:")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    imagen = forms.ImageField(label="Avatar", required=False)
    descripcion = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'imagen', 'descripcion']