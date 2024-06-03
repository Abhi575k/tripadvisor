from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('register/', views.registerUser, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]
