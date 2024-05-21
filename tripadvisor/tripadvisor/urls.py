from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('api/', include('users.urls'), name='users'),

    path('admin/', admin.site.urls),
]
