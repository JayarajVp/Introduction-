from django.contrib import admin
from django.urls import path, include
from .import view 

urlpatterns = [
    path('webpage.html/',view.webpage), 
]

