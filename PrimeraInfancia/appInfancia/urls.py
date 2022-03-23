
from django.urls import path
from .views.Region.views import *

app_name = 'appInfancia'
urlpatterns = [
    #path('', home, name='index'),
    path('Region/list', RegionListView.as_view(), name ='region_list'),
    #path('crearReguion', crearReguion, name='crearReguion')

]