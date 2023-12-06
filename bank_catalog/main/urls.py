from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main_page'),
    path('/bank', views.index, name='banks'),
    path('logout', views.index, name='logout'),
]
