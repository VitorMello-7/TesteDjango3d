from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadCoord, name='uploadCoord'),
    path('data/', views.data_3d, name='data_3d'),
]