

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from appInfancia.models import Municipios
from appInfancia.forms import MunicipioForm
from django.urls import reverse_lazy


class MunicipioListView(ListView):
    models = Municipios
    template_name = 'municipio/list.html'
    paginate_by = 10


    def get_queryset(self):
        return Municipios.objects.order_by('codigodane')
        return context

    def get_context_data(self,  **kwargs):
        municipio = super().get_context_data(**kwargs)
        municipio['title'] = 'Lista de Municipios'
        municipio['module'] = 'Municipios'
        print(reverse_lazy('appInfancia:municipio_list'))
        return municipio

class MunicipioCreateView(CreateView):
    models = Municipios
    form_class = MunicipioForm
    template_name = 'municipio/create.html'
    success_url = reverse_lazy('appInfancia:municipio_list')



    def get_context_data(self, **kwargs):
        municipio = super().get_context_data(**kwargs)
        municipio['title'] = 'Crear Municipios'
        municipio['module'] = 'Municipios'
        municipio['action'] = 'Guardar'
        return municipio

class MunicipioUpdateView(UpdateView):
    model = Municipios
    form_class = MunicipioForm
    template_name = 'Municipio/create.html'
    success_url = reverse_lazy('appInfancia:municipio_list')

    def get_context_data(self, **kwargs):
        municipio = super().get_context_data(**kwargs)
        municipio['title'] = 'Editar Municipios'
        municipio['module'] = 'Municipios'
        municipio['action'] = 'Editar'
        return municipio

class MunicipioDeleteView(DeleteView):
    model = Municipios
    template_name = 'Municipio/delete.html'
    success_url = reverse_lazy('appInfancia:municipio_list')

    def get_context_data(self, **kwargs):
        municipio = super().get_context_data(**kwargs)
        municipio['module'] = 'Municipios'
        municipio['action'] = 'Eliminar'
        municipio['list_url'] = reverse_lazy('appInfancia:municipio_list')
        return municipio


