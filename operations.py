import csv
from typing import List
from models import Pelicula, Director

ARCHIVO_PELICULAS = 'csv_data/peliculas.csv'
ARCHIVO_DIRECTORES = 'csv_data/directores.csv'

# Guardar lista de películas en CSV
def guardar_peliculas_csv(peliculas: List[Pelicula]):
    with open(ARCHIVO_PELICULAS, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(Pelicula.__annotations__.keys())
        for peli in peliculas:
            escritor.writerow(peli.dict().values())

# Cargar lista de películas desde CSV
def cargar_peliculas_csv() -> List[Pelicula]:
    try:
        with open(ARCHIVO_PELICULAS, mode='r') as archivo:
            lector = csv.DictReader(archivo)
            return [Pelicula(**fila) for fila in lector]
    except FileNotFoundError:
        return []

# Guardar directores en CSV
def guardar_directores_csv(directores: List[Director]):
    with open(ARCHIVO_DIRECTORES, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(Director.__annotations__.keys())
        for director in directores:
            escritor.writerow(director.dict().values())

# Cargar directores desde CSV
def cargar_directores_csv() -> List[Director]:
    try:
        with open(ARCHIVO_DIRECTORES, mode='r') as archivo:
            lector = csv.DictReader(archivo)
            return [Director(**fila) for fila in lector]
    except FileNotFoundError:
        return []
