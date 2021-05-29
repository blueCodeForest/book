from django.contrib import admin
from django.urls import path
from .views import firstviewfunction
from . import views

urlpatterns = [
    path('', views.firstviewfunction),
]