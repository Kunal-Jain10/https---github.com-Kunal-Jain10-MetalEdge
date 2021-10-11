from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
# Create your models here.

class User(AbstractUser):
    
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    
    first_name = None
    last_name = None
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)
    name = models.CharField(max_length=50,null=True)
    company = models.CharField(max_length=100, null=True)
    gstin = models.CharField(max_length=15,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50,null=True)
    company = models.CharField(max_length=100, null=True)
    gstin = models.CharField(max_length=15,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
