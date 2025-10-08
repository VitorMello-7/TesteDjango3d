from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Coord
from pathlib import Path
from scipy.spatial import Delaunay
import json
import os

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


def data_3d(request):
    """Retorna JSON com pontos e triangulação Delaunay.

    Estrutura de retorno:
    {
      "points": [{"Depth":..,"Latitude":..,"Longitude":..}, ...],
      "simplices": [[i1,i2,i3], ...]
    }
    """
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / 'arquivoTeste' / 'testePonto.txt'
    pontos = []
    if file_path.exists():
        with file_path.open('r', encoding='utf-8') as f:
            try:
                header = next(f)
            except StopIteration:
                header = ''
            for line in f:
                parts = line.strip().split(';')
                if len(parts) < 3:
                    continue
                try:
                    depth, lat, lon = map(float, parts[:3])
                except ValueError:
                    continue
                pontos.append({
                    'Depth': depth,
                    'Latitude': lat,
                    'Longitude': lon
                })
    # Se não houver pontos suficientes para triangulação (min 3)
    simplices = []
    if len(pontos) >= 3:
        coords2d = [(p['Longitude'], p['Latitude']) for p in pontos]
        try:
            tri = Delaunay(coords2d)
            simplices = tri.simplices.tolist()
        except Exception:
            simplices = []
    return JsonResponse({'points': pontos, 'simplices': simplices})

# def carregar_pontos(request):
#     base_dir = Path(__file__).resolve().parent
#     file_path = base_dir / 'arquivoTeste' / 'arquivo.txt'
    
#     xs = [] #longitude
#     ys = [] #latitude
#     zs = [] #depth
    
#     with file_path.open('r', enconding='utf-8') as file:
#         for line in file:
#             depth, latitude, longitude = map(float, line.strip().split(';'))
#             xs.append(longitude)
#             ys.append(latitude)
#             zs.append(depth)