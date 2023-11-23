from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from Accounts.forms import UserCreationFormCustom

#Imports para editar perfil
from django.http import HttpResponse, HttpResponseNotFound
from Accounts.forms import UserEditForm
from Accounts.models import Avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

#Import imagenes
from django.core.files import File

#Login
def login_view(request):
     if request.method == "POST":
     # ^ Si usuario hace clic al botón iniciar sesión...
         form_inicio = AuthenticationForm(request, data = request.POST)
         if form_inicio.is_valid():
             info = form_inicio.cleaned_data
             # ^ Si form_inicio es válido primero vacía por si ya hay algo cargado con cleaned_data
             usuario = info.get("username")
             contrasenia = info.get("password")
             user = authenticate (username = usuario, password = contrasenia)
             # ^ Carga los datos y autentica con authenticate

             if user:
                 login(request, user)
                 return render (request, "Home/index.html", {"usuario" : user})

         else:
             return render (request, "Home/index.html", {"mensaje":"Datos Incorrectos"})
             # ^ Le pregunta si es usuario o no; si lo es le permite el login y lo manda al inicio. Si no, manda un mensaje de “Datos incorrectos” y lo manda de nuevo al formulario de login

     form_inicio = AuthenticationForm() 
     # ^ form_inicio es un formulario vacío

     return render(request, "Accounts/login.html", {"form":form_inicio})


#Registrar usuario
def register_view(request):
    if request.method == "POST":
        form_register = UserCreationFormCustom(request.POST)
        if form_register.is_valid():
            usuario = form_register.cleaned_data["username"]
            form_register.save()
            return render (request, "Home/index.html", {"mensaje": f"Usuario creado"})
    
    else:
        form_register = UserCreationFormCustom()
    
    return render(request, "Accounts/register.html", {"form" : form_register})


#Editar Perfil
@login_required
def editarPerfil(request):
    usuario = request.user

    # Manejar solicitudes para favicon.ico
    if request.path == '/favicon.ico/':
        return HttpResponseNotFound()

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if hasattr(usuario, 'avatar') and usuario.avatar:
                if miFormulario.cleaned_data.get('imagen'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    # Si no se sube una imagen pone una genérica
                    imagen_por_defecto = 'media/avatares/nonavatar.png'
                    with open(imagen_por_defecto, 'rb') as f:
                        usuario.avatar.imagen.save('imagen_por_defecto.jpg', File(f))
            else:
                # Si no tiene un avatar, crea uno y guarda la imagen
                avatar = Avatar.objects.create(user=usuario)
                if miFormulario.cleaned_data.get('imagen'):
                    avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    avatar.save()
                else:
                    # Si no se sube una imagen pone una genérica
                    imagen_por_defecto = 'media/avatares/nonavatar.png'
                    with open(imagen_por_defecto, 'rb') as f:
                        avatar.imagen.save('imagen_por_defecto.jpg', File(f))

            miFormulario.save()
            return render(request, "Home/index.html")
    else:
        # Si no encuentra avatar, crea uno y pone una imagen genérica
        if not hasattr(usuario, 'avatar') or not usuario.avatar:
            avatar = Avatar.objects.create(user=usuario)
            imagen_por_defecto = 'media/avatares/nonavatar.png'
            with open(imagen_por_defecto, 'rb') as f:
                avatar.imagen.save('imagen_por_defecto.jpg', File(f))

        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)

    return render(request, "Accounts/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Accounts/editar_contrasenia.html'
    success_url = reverse_lazy('editarPerfil')