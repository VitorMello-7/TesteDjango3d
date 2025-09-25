from django.http import HttpResponse
from .models import Coord

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Sample3d index.")

def uploadCoord(request):
    if request.method == "POST":
        depth = request.POST.get("depth")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        coord = Coord(depth=depth, latitude=latitude, longitude=longitude)
        coord.save()
        return HttpResponse("Coordinates uploaded successfully.")
    return HttpResponse("Hello, my good sir, please upload your coordinates here.")
