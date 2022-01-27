from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = {
        'projects':Project.objects.all()
    }
    return render(request, "portfolio/portfolio.html", projects) #La clave del diccionario, es por donde itera el bucle for