

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from appInfancia.models import CentroZonal
from appInfancia.forms import CentroZonalForm
from django.urls import reverse_lazy


class CentroZonalListView(ListView):
    models = CentroZonal
    template_name = 'centrozonal/list.html'


    def get_queryset(self):
        return CentroZonal.objects.order_by('idcentro_zonal')
        return context

    def get_context_data(self,  **kwargs):
        centrozonal = super().get_context_data(**kwargs)
        centrozonal['title'] = 'Lista de Centros Zonales'
        centrozonal['module'] = 'Centro Zonal'
        print(reverse_lazy('appInfancia:centrozonal_list'))
        return centrozonal

class CentroZonalCreateView(CreateView):
    models = CentroZonal
    form_class = CentroZonalForm
    template_name = 'centrozonal/create.html'
    success_url = reverse_lazy('appInfancia:centrozonal_list')



    def get_context_data(self, **kwargs):
        centrozonal = super().get_context_data(**kwargs)
        centrozonal['title'] = 'Crear Centros Zonales'
        centrozonal['module'] = 'CentroZonal'
        centrozonal['action'] = 'Guardar'
        return centrozonal

class CentroZonalUpdateView(UpdateView):
    model = CentroZonal
    form_class = CentroZonalForm
    template_name = 'centrozonal/create.html'
    success_url = reverse_lazy('appInfancia:centrozonal_list')

    def get_context_data(self, **kwargs):
        centrozonal = super().get_context_data(**kwargs)
        centrozonal['title'] = 'Editar Centros Zonales'
        centrozonal['module'] = 'CentroZonal'
        centrozonal['action'] = 'Editar'
        return centrozonal

class CentroZonalDeleteView(DeleteView):
    model = CentroZonal
    template_name = 'centrozonal/delete.html'
    success_url = reverse_lazy('appInfancia:centrozonal_list')

    def get_context_data(self, **kwargs):
        centrozonal = super().get_context_data(**kwargs)
        centrozonal['module'] = 'CentroZonal'
        centrozonal['action'] = 'Eliminar'
        centrozonal['list_url'] = reverse_lazy('appInfancia:centrozonal_list')
        return centrozonal


