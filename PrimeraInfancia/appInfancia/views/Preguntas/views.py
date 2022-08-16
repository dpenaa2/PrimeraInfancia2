from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from appInfancia.models import  Catalogorespuestas
from appInfancia.forms import RespuestasForm



class FormsetRespuesta (FormView):
    template_name = 'pregunta/create.html'
    models = Catalogorespuestas
    form_class = formset_factory(RespuestasForm, extra=3)
    success_url = reverse_lazy('appInfancia:pregunta_list')

    def form_valid(self, form):
        for rta in form:
            if rta.is_valid():
                rta.save()
        return super().form_valid(form)



