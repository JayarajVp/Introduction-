from django.contrib import admin
from django.urls import path
from .import view 

urlpatterns = [
    path('cyber.html/',view.cyberpage), 
]
