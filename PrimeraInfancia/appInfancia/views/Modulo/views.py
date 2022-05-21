from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from appInfancia.models import TipoModulo, Seccion, Catalagopregunta, Catalogorespuestas
from appInfancia.forms import TipoModuloForm, SeccionForm, CatalagopreguntaForm, CatalogorespuestasForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render


class TipoModuloListView(ListView):
    models = TipoModulo
    template_name = 'modulo/list.html'

    def get_queryset(self):
        return TipoModulo.objects.order_by('idtipo_modulo')
        return context

    def get_context_data(self, **kwargs):
        modulo = super().get_context_data(**kwargs)
        modulo['title'] = 'Lista de Modulos'
        modulo['module'] = 'Modulos'
        print(reverse_lazy('appInfancia:modulo_list'))
        return modulo


class TipoModuloCreateView(CreateView):
    models = TipoModulo
    template_name = 'modulo/create.html'
    form_class = TipoModuloForm
    second_form_class = SeccionForm
    pregunta_form_class = CatalagopreguntaForm
    respuestas_form_class = CatalogorespuestasForm
    Formtemplate_name = 'modulo/create.html'
    success_url = reverse_lazy('appInfancia:modulo_list')

    def get_context_data(self, **kwargs):
        context = super(TipoModuloCreateView, self).get_context_data(**kwargs)
        if 'moduloForm' not in context:
            context['moduloForm'] = self.form_class(self.request.GET)
        if 'sectionForm' not in context:
            context['sectionForm'] = self.second_form_class(self.request.GET)
        if 'preguntaForm' not in context:
            context['preguntaForm'] = self.pregunta_form_class(self.request.GET)
        if 'respuestasForm' not in context:
            context['respuestasForm'] = self.respuestas_form_class(self.request.GET)

        context['titleModulos'] = 'Lista de Modulos'
        context['module'] = 'Modulos'
        context['titleSeccion'] = 'Lista de Seccion'
        context['module'] = 'Seccion'

        print(reverse_lazy('appInfancia:modulo_list'))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        moduloForm = self.form_class(request.POST)
        sectionForm = self.second_form_class(request.POST)
        preguntaForm = self.pregunta_form_class(request.POST)
        respuestasForm = self.respuestas_form_class(request.POST)

        if form_class.is_valid() and second_form_class.is_valid() and pregunta_form_class.is_valid() and respuestas_form_class.is_valid():
            modulo = moduloForm.save()
            modulo.seccion = sectionForm.save()
            modulo.pregunta = preguntaForm.save()
            modulo.respuestas = respuestasForm.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(moduloForm=moduloForm, sectionForm=sectionForm, preguntaForm=preguntaForm,
                                      respuestasForm=respuestasForm))


class ModuloDeleteView(DeleteView):
    model = TipoModulo
    template_name = 'modulo/delete.html'
    success_url = reverse_lazy('appInfancia:modulo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = 'Modulo'
        context['action'] = 'Eliminar'
        context['list_url'] = reverse_lazy('appInfancia:modulo_list')
        return context
