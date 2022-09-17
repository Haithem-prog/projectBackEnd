from cmath import phase
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _  
from django.contrib.auth.base_user import BaseUserManager  


class CustomUserManager(BaseUserManager):  
    """  
    Custom user model manager where phone is the unique identifiers  
    for authentication instead of usernames.  
    """  
    def create_user(self, phone,password,name):  
        """  
        Create and save a User with the given phone and password.  
        """   
         
        user = self.model(phone=phone,name = name) 
        user.set_password(password)  
        user.save()  
        return user
        
  
    def create_superuser(self, name,phone, password):  
        """  
        Create and save a SuperUser with the given phone and password.  
        """  
        user = self.model(name = name, phone=phone)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)  
        user.save()  
        return user 
         
 
class CustomUser(AbstractBaseUser, PermissionsMixin):  
    username = None
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,unique=True)
    date_joined = models.DateTimeField(default=timezone.now)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)
    
      
  
    
    USERNAME_FIELD = 'phone'  
    REQUIRED_FIELDS = ['name']  
  
    objects = CustomUserManager()  
         
    
