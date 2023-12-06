from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='banks'),
    path('add', views.AddBank, name='create_bank')
]
