from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *

from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
