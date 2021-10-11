from django.db import models

from Account.models import User,Seller,Buyer
from Sell.models import Product

# Create your models here.
class Order(models.Model):
    
    seller = models.ForeignKey(Seller, related_name='order', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order', on_delete=models.CASCADE)
    
    type_choice = {
        ('placed','placed'),
        ('dispatched','dispatched'),
        ('confirmed','confirmed'),
        ('conplete','complete'),
    }

    status = models.CharField(max_length=50, null=True, choices=type_choice, default='placed')
    quantity = models.IntegerField(null=True)
    invoice = models.FileField(upload_to='docOrder/invoices/', blank=True, null=True)    
    dispatch_slip = models.FileField(upload_to='docOrder/dispatch/', blank=True, null=True)    
    payment_slip = models.FileField(upload_to='docOrder/payment/', blank=True, null=True)    
    

    