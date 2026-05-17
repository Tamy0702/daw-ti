from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'correo', 'titulo_academico']
