from django.urls import path
from Home import views

urlpatterns = [
    #Vista inicio (en mi caso también es el "Sobre Mi")
    path('', views.index, name="about"),
]