from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('orders/',views.orders, name='orders'),
    path('addProduct/',views.addProduct, name='addProduct'),
    path('viewProduct/',views.viewProduct, name='viewProduct'),    
    path('productDetail/<int:pk>',views.productDetail, name='productDetail'),
    

]
