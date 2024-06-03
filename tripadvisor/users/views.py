from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import TripUser

def homePage(request):
    return render(request, 'base/home.html')

# Create your views here.
def registerUser(request):
    return