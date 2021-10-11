from django.contrib import admin
from Account.models import User,Buyer,Seller

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'password', 'is_seller', 'is_buyer')
    list_display = ('username', 'email', 'is_seller', 'is_buyer')
    

admin.site.register(User,UserAdmin)
admin.site.register(Buyer)
admin.site.register(Seller)