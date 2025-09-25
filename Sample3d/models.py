from django.db import models

# Create your models here.
class Coord(models.Model):
   depth = models.FloatField(max_length=200) #z
   latitude = models.FloatField(max_length=200) #y
   longitude = models.FloatField(max_length=200) #x

