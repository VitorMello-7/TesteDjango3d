from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from pathlib import Path
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator
import numpy as np
import json
import os

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Sample3d index.")

def uploadCoord(request):
    # Renderiza a página principal com o gráfico 3D
    return render(request, "Sample3d/uploadCoord.html")

def surface_from_xyz(request):
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

    # É necessário pelo menos 3 pontos para interpolar em 2D
    if len(pontos) < 3:
        return JsonResponse({"x": [], "y": [], "z": [], "meta": {"nx": 0, "ny": 0}})

    # Pontos (lon, lat) e valores (depth) com mesmo comprimento
    coords2d = np.array([(p['Longitude'], p['Latitude']) for p in pontos], dtype=float)
    pDep = np.array([p['Depth'] for p in pontos], dtype=float)

    # LinearNDInterpolator aceita pontos diretamente (internamente monta a triangulação)
    try:
        interp = LinearNDInterpolator(coords2d, pDep)
    except Exception:
        # Em caso de falha na triangulação (pontos colineares, duplicados, etc.)
        return JsonResponse({"x": [], "y": [], "z": [], "meta": {"nx": 0, "ny": 0}})

    margin = 0.02
    lons = coords2d[:, 0]
    lats = coords2d[:, 1]
    xmin, xmax = float(lons.min()), float(lons.max())
    ymin, ymax = float(lats.min()), float(lats.max())
    xr = xmax - xmin
    yr = ymax - ymin
    xmin -= xr * margin; xmax += xr * margin
    ymin -= yr * margin; ymax += yr * margin
    
    nx, ny = 120, 120
    gx = np.linspace(xmin, xmax, nx)
    gy = np.linspace(ymin, ymax, ny)
    GX, GY = np.meshgrid(gx, gy)

    Gz = interp(GX, GY)

    # Retorna grade completa: gx, gy e matriz Z (com None no lugar de NaN)
    Z = Gz.tolist()
    # Substituir NaN por None para JSON serializável
    for j in range(len(Z)):
        row = Z[j]
        for i in range(len(row)):
            val = row[i]
            if val != val:  # NaN check
                row[i] = None

    payload = {
        "gx": gx.tolist(),
        "gy": gy.tolist(),
        "Z": Z,
        "meta": {"nx": int(nx), "ny": int(ny)}
    }
    
    return JsonResponse(payload)

