from django.http import HttpResponse
from django.shortcuts import render
from .models import Coord

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Sample3d index.")

def uploadCoord(request):
    if request.method == "POST":
        depth = request.POST.get("Depth")
        latitude = request.POST.get("Latitude")
        longitude = request.POST.get("Longitude")
        coord = Coord(depth=depth, latitude=latitude, longitude=longitude)
        coord.save()
        return HttpResponse("Coordinates uploaded successfully.")
    # Adjusted template path to match your folder: Sample3d/templates/Sample3dTemplates/uploadCoord.html
    return render(request, "Sample3d/uploadCoord.html")
