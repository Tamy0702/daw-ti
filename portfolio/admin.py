from django.contrib import admin

# Register your models here.
from .models import portfolio

class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(portfolio)
