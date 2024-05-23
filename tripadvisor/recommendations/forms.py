from django import forms
from django.forms import ModelForm
from .models import Recommendation

class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ['start_date', 'end_date', 'budget', 'city']
    
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    budget = forms.DecimalField(max_digits=10, decimal_places=2)
    city = forms.CharField(max_length=100)
    