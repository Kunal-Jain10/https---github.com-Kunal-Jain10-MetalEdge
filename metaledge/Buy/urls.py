from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('buyProduct/',views.buyProduct, name='buyProduct'),
    path('buy_orders/',views.buy_orders, name='buy_orders'),
    path('buyOrder/<int:pk>',views.buyOrder, name='buyOrder'),
    
]


