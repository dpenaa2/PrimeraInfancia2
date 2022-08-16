from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from appInfancia.models import GruposEtnicos
from appInfancia.forms import GruposEtnicosForm
from django.urls import reverse_lazy


class GruposEtnicosListView(ListView):
    models = GruposEtnicos
    template_name = 'gruposetnicos/list.html'

    def get_queryset(self):
        return GruposEtnicos.objects.order_by('idgrupoetnico')
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Grupos Etnicos'
        context['module'] = 'GruposEtnicos'
        print(reverse_lazy('appInfancia:gruposetnicos_list'))
        return context


class GrupoEtnicoCreateView(CreateView):
    models = GruposEtnicos
    form_class = GruposEtnicosForm
    template_name = 'gruposetnicos/create.html'
    success_url = reverse_lazy('appInfancia:gruposetnicos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Grupo Etnico'
        context['module'] = 'GruposEtnicos'
        context['action'] = 'Guardar'
        return context


class GrupoEtnicoUpdateView(UpdateView):
    model = GruposEtnicos
    form_class = GruposEtnicosForm
    template_name = 'gruposetnicos/create.html'
    success_url = reverse_lazy('appInfancia:gruposetnicos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Grupo Etnico'
        context['module'] = 'GruposEtnicos'
        context['action'] = 'Editar'
        return context


class GrupoEtnicoDeleteView(DeleteView):
    model = GruposEtnicos
    template_name = 'gruposetnicos/delete.html'
    success_url = reverse_lazy('appInfancia:gruposetnicos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'GruposEtnicos'
        context['action'] = 'Eliminar'
        context['list_url'] = reverse_lazy('appInfancia:gruposetnicos_list')
        return context
