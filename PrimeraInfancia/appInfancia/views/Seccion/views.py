from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from appInfancia.models import Seccion
from appInfancia.forms import SeccionForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class SeccionListView(ListView):
    models = Seccion
    template_name = 'seccion/list.html'

    def get_queryset(self):
        return Seccion.objects.order_by('idseccion')
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Secciones'
        context['module'] = 'Secciones'
        context['list_url'] = reverse_lazy('appInfancia:seccion_list')
        print(reverse_lazy('appInfancia:seccion_list'))
        return context


class SeccionCreateView(SuccessMessageMixin, CreateView):
    models = Seccion
    form_class = SeccionForm
    template_name = 'seccion/create.html'
    success_url = reverse_lazy('appInfancia:seccion_list')
    success_message = "was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Secciones'
        context['module'] = 'Secciones'
        context['action'] = 'Guardar'
        return context


class SeccionUpdateView(SuccessMessageMixin, UpdateView):
    model = Seccion
    form_class = SeccionForm
    template_name = 'seccion/create.html'
    success_url = reverse_lazy('appInfancia:seccion_list')
    success_message = "was Update successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Secciones'
        context['module'] = 'Secciones'
        context['action'] = 'Editar'
        return context


class SeccionDeleteView(SuccessMessageMixin,DeleteView):
    model = Seccion
    template_name = 'seccion/delete.html'
    success_message = "was Delete successfully"
    success_url = reverse_lazy('appInfancia:seccion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Secciones'
        context['action'] = 'Eliminar'
        return context
