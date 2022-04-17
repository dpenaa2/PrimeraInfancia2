

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from appInfancia.models import Nacionalidad
from appInfancia.forms import NacionalidadForm
from django.urls import reverse_lazy


class NacionalidadListView(ListView):
    models = Nacionalidad
    template_name = 'nacionalidad/list.html'

    def get_queryset(self):
        return Nacionalidad.objects.order_by('idpais')
        return context

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Nacionalidades'
        context['module'] = 'Nacionalidades'
        print(reverse_lazy('appInfancia:nacionalidad_list'))
        return context

class NacionalidadCreateView(CreateView):
    models = Nacionalidad
    form_class = NacionalidadForm
    template_name = 'nacionalidad/create.html'
    success_url = reverse_lazy('appInfancia:nacionalidad_list')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nacionalidad'
        context['module'] = 'Nacionalidades'
        context['action'] = 'Guardar'
        return context

class NacionalidadUpdateView(UpdateView):
    model = Nacionalidad
    form_class = NacionalidadForm
    template_name = 'nacionalidad/create.html'
    success_url = reverse_lazy('appInfancia:nacionalidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Nacionalidad'
        context['module'] = 'Nacionalidades'
        context['action'] = 'Editar'
        return context

class NacionalidadDeleteView(DeleteView):
    model = Nacionalidad
    template_name = 'nacionalidad/delete.html'
    success_url = reverse_lazy('appInfancia:nacionalidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Nacionalidades'
        context['action'] = 'Eliminar'
        context['list_url'] = reverse_lazy('appInfancia:nacionalidad_list')
        return context


