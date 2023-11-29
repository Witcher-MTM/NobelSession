from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='banks'),
    path('profile', views.index, name='profile'),
    path('logout', views.index, name='logout'),
]
