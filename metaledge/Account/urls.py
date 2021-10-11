from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('buy_register/', views.buy_register, name='buy_register'),
    path('sell_register/', views.sell_register, name='sell_register'),
    path('buy_login/',views.buy_login, name='buy_login'),
    path('sell_login/',views.sell_login, name='sell_login'),
    path('sell_info/',views.sell_info, name='sell_info'),
    path('buy_info/',views.buy_info, name='buy_info'),

]
