from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainhome, name = 'home'),
    path('about_team/', views.about_team, name = 'aboutteam'),
]
