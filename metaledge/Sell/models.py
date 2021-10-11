from django.db import models

from Account.models import User,Seller,Buyer

# Create your models here.
class Product(models.Model):
    
    seller = models.ForeignKey(Seller, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    name = models.CharField(max_length=50,null=True)
    type_choice = {
        ('copper','copper'),
        ('stell','stell'),
        ('aluminium,','aluminium'),
        ('iron','iron'),
        ('brass','brass'),
    }

    type = models.CharField(max_length=50, null=True, choices=type_choice, default='copper')
    description = models.CharField(max_length=300,null=True)
    price = models.IntegerField(null=True)
    
