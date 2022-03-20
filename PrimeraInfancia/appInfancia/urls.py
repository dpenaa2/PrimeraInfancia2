
from django.urls import path
from .views import reguionList, crearReguion, home

urlpatterns = [
    path('', home, name='index'),
    path('reguionList', reguionList, name='reguionList'),
    path('crearReguion', crearReguion, name='crearReguion')

]
