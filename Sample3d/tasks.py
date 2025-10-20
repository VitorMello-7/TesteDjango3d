import os
import json
import numpy as np
from scipy.spatial import Delaunay



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, 'arquivoTeste', 'testePonto.txt')

pontosXyz = []

with open(file_path, 'r', encoding='utf-8') as file:
    next(file)  # Skip header line
    for line in file:
        Depth, Latitude, Longitude = map(int, line.strip().split(';'))
        pontosXyz.append({
            'Depth': int(Depth),
            'Latitude': int(Latitude),
            'Longitude': int(Longitude)
        })

# print(pontosXyz)

def triDelaunay():
    DelaunayPoints = [(p['Longitude'], p['Latitude']) for p in pontosXyz]
    tri = Delaunay(DelaunayPoints)
    return tri.simplices.tolist()

# print(triDelaunay())

# criando malha de superfície 3D