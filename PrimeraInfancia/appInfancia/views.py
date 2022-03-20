from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'index.html')

def reguionList(request):
    regionales = Regionales.objects.all()
    contexto ={
        'regionales': regionales
    }
    return render(request, 'reguion/reguionList.html', contexto)

def crearReguion(request):
    return render(request, 'reguion/crearReguion.html')
