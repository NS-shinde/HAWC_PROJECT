from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password1 = models.CharField(max_length=20)
    
    # name = models.CharField(max_length=20)
    # email = models.EmailField(max_length=20)
    # password1 = models.CharField(max_length=20)


    def __str__(self):
        return self.name
