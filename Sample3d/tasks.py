import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, 'arquivoTeste', 'arquivo.txt')

pontosXyz = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        Depth, Latitude, Longitude = map(float, line.strip().split(';'))
        pontosXyz.append({
            'Depth': float(Depth),
            'Latitude': float(Latitude),
            'Longitude': float(Longitude)
        })
