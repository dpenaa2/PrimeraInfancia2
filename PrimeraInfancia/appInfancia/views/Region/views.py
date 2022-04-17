from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from appInfancia.models import Regionales
from appInfancia.forms import RegionForm
from django.urls import reverse_lazy
from django.shortcuts import render


class RegionListView(ListView):
    models = Regionales
    template_name = 'region/list.html'

    def get_queryset(self):
        return Regionales.objects.order_by('idregional')
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Regiones'
        context['module'] = 'Regiones'
        print(reverse_lazy('appInfancia:region_list'))
        return context


class RegionCreateView(CreateView):
    models = Regionales
    form_class = RegionForm
    template_name = 'region/create.html'
    success_url = reverse_lazy('appInfancia:region_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Regiones'
        context['module'] = 'Regiones'
        context['action'] = 'Guardar'
        return context


class RegionUpdateView(UpdateView):
    model = Regionales
    form_class = RegionForm
    template_name = 'region/create.html'
    success_url = reverse_lazy('appInfancia:region_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Regiones'
        context['module'] = 'Regiones'
        context['action'] = 'Editar'
        return context


class RegionDeleteView(DeleteView):
    model = Regionales
    template_name = 'region/delete.html'
    success_url = reverse_lazy('appInfancia:region_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Regiones'
        context['action'] = 'Eliminar'
        context['list_url'] = reverse_lazy('appInfancia:region_list')
        return context
