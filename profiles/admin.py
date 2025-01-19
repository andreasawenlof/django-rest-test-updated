"""
This file is used to register the Profile model with the Django admin site.
"""
from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)
