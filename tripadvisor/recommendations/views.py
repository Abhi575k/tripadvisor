from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Recommendation
from .forms import RecommendationForm

from .services import generateTripRecommendation
from .utilities import createUniqueID

# Create your views here.

def viewTrip(request):
    return render(request, 'base/view_trip.html')

def generateRecommendation(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)

            start_date = str(request.POST.get('start_date'))
            end_date = str(request.POST.get('end_date'))
            budget = str(request.POST.get('budget'))
            city = str(request.POST.get('city'))
            # print(start_date, end_date, budget, city)
            trip = generateTripRecommendation(start_date, end_date, budget, city)
            recommendation = trip.recommendation

            prompt = trip.prompt
            form_instance.prompt = prompt
            form_instance.recommendation = recommendation
            form_instance.save()
            
            context = {}
            context['success'] = True
            context['prompt'] = prompt
            context['recommendation'] = recommendation
            return render(request, 'base/generate_trip.html', context)
        else:
            context = {}
            context['success'] = False
            context['errors'] = 'Invalid form submission'
            return render(request, 'base/generate_trip.html', context)
    else:
        context = {}
        context['success'] = False
        context['errors'] = 'Method not allowed'
        return render(request, 'base/generate_trip.html', context)