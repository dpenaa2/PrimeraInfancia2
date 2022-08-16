from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from appInfancia.models import Lengua
from appInfancia.forms import LenguaForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class LenguaListView(ListView):
    models = Lengua
    template_name = 'lengua/list.html'

    def get_queryset(self):
        return Lengua.objects.order_by('idlengua')
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Lenguas'
        context['module'] = 'Lenguas'
        context['list_url'] = reverse_lazy('appInfancia:lengua_list')
        print(reverse_lazy('appInfancia:lengua_list'))
        return context


class LenguaCreateView(SuccessMessageMixin, CreateView):
    models = Lengua
    form_class = LenguaForm
    template_name = 'lengua/create.html'
    success_url = reverse_lazy('appInfancia:lengua_list')
    success_message = "was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Lenguas'
        context['module'] = 'Lenguas'
        context['action'] = 'Guardar'
        return context


class LenguaUpdateView(SuccessMessageMixin, UpdateView):
    model = Lengua
    form_class = LenguaForm
    template_name = 'lengua/create.html'
    success_url = reverse_lazy('appInfancia:lengua_list')
    success_message = "was Update successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar lengua'
        context['module'] = 'Lengua'
        context['action'] = 'Editar'
        return context


class LenguaDeleteView(SuccessMessageMixin,DeleteView):
    model = Lengua
    template_name = 'lengua/delete.html'
    success_message = "was Delete successfully"
    success_url = reverse_lazy('appInfancia:lengua_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Lenguas'
        context['action'] = 'Eliminar'
        return context
