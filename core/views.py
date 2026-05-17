from django.shortcuts import render, HttpResponse
from portfolio.models import portfolio as Portfolio
from portfolio.admin import PortfolioAdmin
from .models import Persona

def home(request):
    persona = Persona.objects.first()
    return render(request, template_name="core/home.html", context={'persona': persona})

def about(request):
    persona = Persona.objects.first()
    return render(request, template_name="core/about.html", context={'persona': persona})

def portafolio(request):
    persona = Persona.objects.first()
    items = Portfolio.objects.all()
    return render(request, template_name="core/portfolio.html", context={'items': items, 'persona': persona})

def contacto(request):
    persona = Persona.objects.first()
    return render(request, template_name="core/contact.html", context={'persona': persona})