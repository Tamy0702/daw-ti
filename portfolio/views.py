from django.shortcuts import render, redirect
from .models import portfolio
from .forms import PortfolioForm

def lista_portfolio(request):
    items = portfolio.objects.all()
    return render(request, 'portfolio/lista.html', {'items': items})

def subir_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)  # request.FILES maneja las imágenes
        if form.is_valid():
            form.save()
            return redirect('lista_portfolio')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/subir.html', {'form': form})


