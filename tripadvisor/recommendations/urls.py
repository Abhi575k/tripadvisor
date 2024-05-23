from django.urls import path

from . import views

urlpatterns = [
    path('view_trip/', views.viewTrip, name='viewTrip'),
    path('generate/', views.generateRecommendation, name='generate'),
]