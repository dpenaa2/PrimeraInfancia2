

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from appInfancia.models import Tipodiscapacidad
from appInfancia.forms import DiscapacidadForm
from django.urls import reverse_lazy


class DiscapacidadListView(ListView):
    models = Tipodiscapacidad
    template_name = 'discapacidad/list.html'

    def get_queryset(self):
        return Tipodiscapacidad.objects.order_by('idTipodiscapacidad')
        return context

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Discapacidades'
        context['module'] = 'Discapacidad'
        print(reverse_lazy('appInfancia:discapacidad_list'))
        return context

class DiscapacidadCreateView(CreateView):
    models = Tipodiscapacidad
    form_class = DiscapacidadForm
    template_name = 'discapacidad/create.html'
    success_url = reverse_lazy('appInfancia:discapacidad_list')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Discapacidad'
        context['module'] = 'Discapacidad'
        context['action'] = 'Guardar'
        return context

class DiscapacidadUpdateView(UpdateView):
    model = Tipodiscapacidad
    form_class = DiscapacidadForm
    template_name = 'discapacidad/create.html'
    success_url = reverse_lazy('appInfancia:discapacidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Discapacidad'
        context['module'] = 'Discapacidad'
        context['action'] = 'Editar'
        return context

class DiscapacidadDeleteView(DeleteView):
    model = Tipodiscapacidad
    template_name = 'discapacidad/delete.html'
    success_url = reverse_lazy('appInfancia:discapacidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Discapacidad'
        context['action'] = 'Eliminar'
        context['list_url'] = reverse_lazy('appInfancia:discapacidad_list')
        return context


