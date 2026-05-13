from django import forms
from .models import portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = ['title', 'description', 'image']