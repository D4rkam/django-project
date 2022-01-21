from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {"projects" : projects}) #La clave del diccionario, es por donde itera el bucle for