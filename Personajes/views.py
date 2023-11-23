from Personajes.models import Sailor, Winx, Witch
from django.contrib.auth.mixins import LoginRequiredMixin

#Importación para VBC
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

#CBV Sailor Moon
class SailorListView(ListView):
    model = Sailor
    context_object_name = "sailor"
    template_name = "Personajes/sailor_lista.html"

class SailorDetailView(DetailView):
    model = Sailor
    template_name = "Personajes/sailor_detalle.html"

class SailorCreateView(CreateView):
    model = Sailor
    template_name = "Personajes/sailor_crear.html"
    success_url = reverse_lazy('ListaSailor')
    fields = ['categoria','nombre', 'planeta', 'objeto']

class SailorUpdateView(LoginRequiredMixin, UpdateView):
    model = Sailor
    template_name = "Personajes/sailor_editar.html"
    success_url = reverse_lazy('ListaSailor')
    fields = ['categoria','nombre', 'planeta', 'objeto']

class SailorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sailor
    template_name = "Personajes/sailor_borrar.html"
    success_url = reverse_lazy('ListaSailor')


#CBV Club Winx
class WinxListView(ListView):
    model = Winx
    context_object_name = "winx"
    template_name = "Personajes/winx_lista.html"

class WinxDetailView(DetailView):
    model = Winx
    template_name = "Personajes/winx_detalle.html"

class WinxCreateView(CreateView):
    model = Winx
    template_name = "Personajes/winx_crear.html"
    success_url = reverse_lazy('ListaWinx')
    fields = ['categoria','nombre', 'tipohada', 'transformacion']

class WinxUpdateView(LoginRequiredMixin, UpdateView):
    model = Winx
    template_name = "Personajes/winx_editar.html"
    success_url = reverse_lazy('ListaWinx')
    fields = ['categoria','nombre', 'tipohada', 'transformacion']

class WinxDeleteView(LoginRequiredMixin, DeleteView):
    model = Winx
    template_name = "Personajes/winx_borrar.html"
    success_url = reverse_lazy('ListaWinx')
    

#CBV W.I.T.C.H
class WitchListView(ListView):
    model = Witch
    context_object_name = "witch"
    template_name = "Personajes/witch_lista.html"

class WitchDetailView(DetailView):
    model = Witch
    template_name = "Personajes/witch_detalle.html"

class WitchCreateView(CreateView):
    model = Witch
    template_name = "Personajes/witch_crear.html"
    success_url = reverse_lazy('ListaWitch')
    fields = ['categoria','nombre', 'elemento', 'signo']

class WitchUpdateView(LoginRequiredMixin, UpdateView):
    model = Witch
    template_name = "Personajes/witch_editar.html"
    success_url = reverse_lazy('ListaWitch')
    fields = ['categoria','nombre', 'elemento', 'signo']

class WitchDeleteView(LoginRequiredMixin, DeleteView):
    model = Witch
    template_name = "Personajes/witch_borrar.html"
    success_url = reverse_lazy('ListaWitch')