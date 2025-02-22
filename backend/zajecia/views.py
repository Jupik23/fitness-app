from django.shortcuts import render
from .models import ZajecieFitness
# Create your views here.

def lista_zajec(request):
    zajecia  = ZajecieFitness.objects.all()
    return render(request, 'zajecia/lista_zajec.html', {'zajecia': zajecia})