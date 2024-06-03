from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import TripUserManager

# Create your models here.
class TripUser(AbstractUser):
    '''
    username: (string, unique, used for identification)
    email: (string, unique)
    password: (string, hashed)
    Used for registering and user login
    '''
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = TripUserManager()

    def __str__(self):
        return self.username
