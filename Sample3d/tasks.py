import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_TESTE = os.path.join(BASE_DIR, 'arquivoTeste', 'testePonto.txt')

pontosXyz = []
with open(ARQUIVO_TESTE, 'r', encoding='utf-8') as file:
    for line in file:
        depth, latitude, longitude = line.strip().split(';')
        pontosXyz.append({
            'depth': float(depth),
            'latitude': float(latitude),
            'longitude': float(longitude)
        })