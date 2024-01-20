from django.shortcuts import render
from .models import Habitacion, Persona
#from django.contrib.auth.decorators import login_required

# Create your views here.
def reservas(request):
    habitaciones = Habitacion.objects.all()
    return render(request, "reservas/reservas.html", {'habitaciones' : habitaciones})
