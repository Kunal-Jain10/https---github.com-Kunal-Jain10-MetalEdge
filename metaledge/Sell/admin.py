from django.contrib import admin
from Sell.models import Product

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    fields = ('image','seller', 'name', 'type', 'description', 'price')
    list_display = ('id','seller', 'name', 'type', 'description', 'price','image')

admin.site.register(Product,ProductsAdmin)