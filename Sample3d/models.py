from django.db import models

# Create your models here.
class Coord(models.Model):
   depth = models.FloatField() #z
   latitude = models.FloatField() #y
   longitude = models.FloatField() #x

def __str__(self):
    return f"Depth: {self.depth}, Lat: {self.latitude}, Lon: {self.longitude}"
