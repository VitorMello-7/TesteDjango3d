from django.urls import path
from . import views

urlpatterns = [
    path('template/Sample3D/uploadCoord.html', views.uploadCoord, name='uploadCoord'),
]