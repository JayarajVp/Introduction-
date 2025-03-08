from django.contrib import admin
from django.urls import path, include
from .import view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',view.about),
    path('',view.homepage),
    path('cbs/', include('cbs.urls')),
    path('webdev/', include('webdev.urls')),
    path('oth/', include('oth.urls')),
]
