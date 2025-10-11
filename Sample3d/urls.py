from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadCoord, name='uploadCoord'),
    path('surface/', views.surface_from_xyz, name='surface_from_xyz'),
]