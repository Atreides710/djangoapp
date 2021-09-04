from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "article"

urlpatterns = [
   
]

urlpatterns += staticfiles_urlpatterns()