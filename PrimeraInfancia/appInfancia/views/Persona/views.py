

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from appInfancia.models import Persona
from appInfancia.forms import PersonaForm
from django.urls import reverse_lazy


class PersonaListView(ListView):
    models = Persona
    template_name = 'persona/list.html'

    def get_queryset(self):
        return Persona.objects.order_by('nombres')
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Personas'
        context['module'] = 'Personas'
        print(reverse_lazy('appInfancia:persona_list'))
        return context

class PersonaCreateView(CreateView):
    models = Persona
    form_class = PersonaForm
    template_name = 'persona/create.html'
    success_url = reverse_lazy('appInfancia:persona_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Persona'
        context['module'] = 'Persona'
        context['action'] = 'Guardar'
        return context

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/create.html'
    success_url = reverse_lazy('appInfancia:persona_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Persona'
        context['module'] = 'Persona'
        context['action'] = 'Editar'
        return context

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('appInfancia:persona_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Persona'
        context['action'] = 'Eliminar'
        context['list_url'] = reverse_lazy('appInfancia:persona_list')
        return context


