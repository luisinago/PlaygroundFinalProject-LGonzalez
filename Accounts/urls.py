from django.urls import path
from Accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Login
    path('login', login_view, name = "Login"),
    #Registro
    path('register', register_view, name = "Register"),
    #Logout
    path('logout', LogoutView.as_view(template_name='Accounts/logout.html'), name='Logout'),
    #Editar Perfil
    path('editarPerfil', editarPerfil, name="editarPerfil"),
    #Cambiar contraseña
    path('cambiarContrasenia', CambiarContrasenia.as_view(), name="CambiarContrasenia"),
]