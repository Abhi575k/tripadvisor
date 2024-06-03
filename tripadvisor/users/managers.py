from django.contrib.auth.models import BaseUserManager

class TripUserManager(BaseUserManager):
    '''
    Custom user manager for TripUser
    '''
    def create_user(self, username, email, password=None, **extra_fields):
        '''
        Create and return a regular user
        '''
        if not username:
            raise ValueError('Username is required')
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')

        user = self.model(
            username=username.lower(),
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_super_user(self, username, email, password=None, **extra_fields):
        '''
        
        '''
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(username,email,password,**extra_fields)

