from django.contrib import admin
from django.urls import path
from e_model import views

urlpatterns = [
    path("",views.cover, name='cover'),

]
