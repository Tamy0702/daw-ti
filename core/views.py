from django.shortcuts import render, HttpResponse
from portfolio.models import portfolio as Portfolio
from portfolio.admin import PortfolioAdmin


# Create your views here.
def home (request):
    return render(request,template_name="core/home.html")

def about(request):
   return render(request,template_name="core/about.html")


def portafolio(request):
    items = Portfolio.objects.all()  # ← trae los proyectos
    return render(request, template_name="core/portfolio.html", context={'items': items})

def contacto(request):
    return render(request, template_name="core/contact.html")