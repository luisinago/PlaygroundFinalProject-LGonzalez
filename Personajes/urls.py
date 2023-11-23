#Genéricos
from django.urls import path
from Personajes.views import *

#Para CBV
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#CBV Sailor
urlpatterns = [
    #Sailor Moon
    path('sailor/lista', SailorListView.as_view(), name = "ListaSailor"),
    path('sailor/nueva', SailorCreateView.as_view(), name = "NuevaSailor"),
    path('sailor/<pk>', SailorDetailView.as_view(), name = "DetalleSailor"),
    path('sailor/<pk>/editar', SailorUpdateView.as_view(), name = "EditarSailor"),
    path('sailor/<pk>/borrar', SailorDeleteView.as_view(), name = "BorrarSailor"),
    
    #Club Winx
    path('winx/lista', WinxListView.as_view(), name = "ListaWinx"),
    path('winx/nueva', WinxCreateView.as_view(), name = "NuevaWinx"),
    path('winx/<pk>', WinxDetailView.as_view(), name = "DetalleWinx"),
    path('winx/<pk>/editar', WinxUpdateView.as_view(), name = "EditarWinx"),
    path('winx/<pk>/borrar', WinxDeleteView.as_view(), name = "BorrarWinx"),
    
    #W.I.T.C.H
    path('witch/lista', WitchListView.as_view(), name = "ListaWitch"),
    path('witch/nueva', WitchCreateView.as_view(), name = "NuevaWitch"),
    path('witch/<pk>', WitchDetailView.as_view(), name = "DetalleWitch"),
    path('witch/<pk>/editar', WitchUpdateView.as_view(), name = "EditarWitch"),
    path('witch/<pk>/borrar', WitchDeleteView.as_view(), name = "BorrarWitch"),
]