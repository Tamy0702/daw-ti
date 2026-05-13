from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_portfolio, name='lista_portfolio'),
    path('subir/', views.subir_portfolio, name='subir_portfolio'),
]