

from django.views.generic import ListView
from appInfancia.models import Regionales


class RegionListView(ListView):
    models = Regionales
    template_name = 'region/list.html'

    def get_queryset(self):
        return Regionales.objects.order_by('idregional')
        return context

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Regiones'
        return context