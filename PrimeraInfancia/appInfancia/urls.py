
from django.urls import path
from .views.Region.views import *
from .views.Municipio.views import *

app_name = 'appInfancia'
urlpatterns = [

    path('Region/list', RegionListView.as_view(), name ='region_list'),
    path('Region/Create', RegionCreateView.as_view(), name ='region_create'),
    path('Region/edit/<int:pk>/',RegionUpdateView.as_view(), name ='region_edit'),
    path('Region/delete/<int:pk>/',RegionDeleteView.as_view(), name ='region_delete'),

    path('Municipio/list', MunicipioListView.as_view(), name='municipio_list'),
    path('Municipio/Create', MunicipioCreateView.as_view(), name='municipio_create'),
    path('Municipio/edit/<int:pk>/', MunicipioUpdateView.as_view(), name='municipio_edit'),
    path('Municipio/delete/<int:pk>/', MunicipioDeleteView.as_view(), name='municipio_delete')

]