from django.urls import path
from .views.Region.views import *
from .views.Municipio.views import *
from .views.CentroZonal.views import *
from .views.Persona.views import *
from .views.Nacionalidad.views import *
from .views.Discapacidad.views import *
from .views.GruposEtnicos.views import *
from .views.Modulo.views import *
from .views.Preguntas.views import *
from .views.Lengua.views import *
from .views.Seccion.views import *

app_name = 'appInfancia'
urlpatterns = [
    # Region
    path('Region/list', RegionListView.as_view(), name='region_list'),
    path('Region/Create', RegionCreateView.as_view(), name='region_create'),
    path('Region/edit/<int:pk>/', RegionUpdateView.as_view(), name='region_edit'),
    path('Region/delete/<int:pk>/', RegionDeleteView.as_view(), name='region_delete'),

    # Municipio
    path('Municipio/list', MunicipioListView.as_view(), name='municipio_list'),
    path('Municipio/Create', MunicipioCreateView.as_view(), name='municipio_create'),
    path('Municipio/edit/<int:pk>/', MunicipioUpdateView.as_view(), name='municipio_edit'),
    path('Municipio/delete/<int:pk>/', MunicipioDeleteView.as_view(), name='municipio_delete'),

    # CentroZonal
    path('CentroZonal/list', CentroZonalListView.as_view(), name='centrozonal_list'),
    path('CentroZonal/Create', CentroZonalCreateView.as_view(), name='centrozonal_create'),
    path('CentroZonal/edit/<int:pk>/', CentroZonalUpdateView.as_view(), name='centrozonal_edit'),
    path('CentroZonal/delete/<int:pk>/', CentroZonalDeleteView.as_view(), name='centrozonal_delete'),

    # Persona
    path('Persona/list', PersonaListView.as_view(), name='persona_list'),
    path('Persona/Create', PersonaCreateView.as_view(), name='persona_create'),
    path('Persona/edit/<int:pk>/', PersonaUpdateView.as_view(), name='persona_edit'),
    path('Persona/delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),

    # Nacionalidad
    path('Nacionalidad/list', NacionalidadListView.as_view(), name='nacionalidad_list'),
    path('Nacionalidad/Create', NacionalidadCreateView.as_view(), name='nacionalidad_create'),
    path('Nacionalidad/edit/<int:pk>/', NacionalidadUpdateView.as_view(), name='nacionalidad_edit'),
    path('Nacionalidad/delete/<int:pk>/', NacionalidadDeleteView.as_view(), name='nacionalidad_delete'),

    # Discapacidad
    path('Discapacidad/list', DiscapacidadListView.as_view(), name='discapacidad_list'),
    path('Discapacidad/Create', DiscapacidadCreateView.as_view(), name='discapacidad_create'),
    path('Discapacidad/edit/<int:pk>/', DiscapacidadUpdateView.as_view(), name='discapacidad_edit'),
    path('Discapacidad/delete/<int:pk>/', DiscapacidadDeleteView.as_view(), name='discapacidad_delete'),

    # GrupoEtnico
    path('GrupoEtnico/list', GruposEtnicosListView.as_view(), name='gruposetnicos_list'),
    path('GrupoEtnico/Create', GrupoEtnicoCreateView.as_view(), name='gruposetnicos_create'),
    path('GrupoEtnico/edit/<int:pk>/', GrupoEtnicoUpdateView.as_view(), name='gruposetnicos_edit'),
    path('GrupoEtnico/delete/<int:pk>/', GrupoEtnicoDeleteView.as_view(), name='gruposetnicos_delete'),

    # Seccion
    path('Seccion/list', SeccionListView.as_view(), name='seccion_list'),
    path('Seccion/Create', SeccionCreateView.as_view(), name='seccion_create'),
    path('Seccion/edit/<int:pk>/', SeccionUpdateView.as_view(), name='seccion_edit'),
    path('Seccion/delete/<int:pk>/', SeccionDeleteView.as_view(), name='seccion_delete'),

    # Preguntas
    #path('Pregunta/list', PreguntaListView.as_view(), name='pregunta_list'),
    path('Pregunta/Create', FormsetRespuesta.as_view(), name='pregunta_create'),
    #path('Pregunta/edit/<int:pk>/', PreguntaUpdateView.as_view(), name='pregunta_edit'),
    #path('Pregunta/delete/<int:pk>/', PreguntaDeleteView.as_view(), name='pregunta_delete'),

    # Lenguas
    path('Lengua/list', LenguaListView.as_view(), name='lengua_list'),
    path('Lengua/Create', LenguaCreateView.as_view(), name='lengua_create'),
    path('Lengua/edit/<int:pk>/', LenguaUpdateView.as_view(), name='lengua_edit'),
    path('Lengua/delete/<int:pk>/', LenguaDeleteView.as_view(), name='lengua_delete'),
]
