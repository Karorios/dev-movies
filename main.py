from fastapi import FastAP
from fastapi import HTTPException
from starlette.responses import JSONResponse
from typing import List
from models import Pelicula, Director, PeliculaRespuesta, DirectorRespuesta
from operations.pelicula_ops import (
    cargar_peliculas_csv, guardar_peliculas_csv,
    cargar_directores_csv, guardar_directores_csv
)

app = FastAPI()

# Cargar datos desde CSV al iniciar
peliculas: List[Pelicula] = cargar_peliculas_csv()
directores: List[Director] = cargar_directores_csv()

@app.get("/")
async def inicio():
    return {"mensaje": "La API de peliculas esta activa 🎬"}

# Crear una nueva película
@app.post("/peliculas", response_model=Pelicula)
async def agregar_pelicula(pelicula: Pelicula):
    if any(p.id == pelicula.id for p in peliculas):
        raise HTTPException(status_code=400, detail="El ID de la peliicula ya existe")
    peliculas.append(pelicula)
    guardar_peliculas_csv(peliculas)
    return pelicula

# Listar todas las películas
@app.get("/peliculas", response_model=List[PeliculaRespuesta])
async def listar_peliculas():
    return peliculas

# Filtrar películas por género
@app.get("/peliculas/filtro/{genero}", response_model=List[Pelicula])
async def filtrar_por_genero(genero: str):
    resultado = [p for p in peliculas if p.genero.lower() == genero.lower()]
    return resultado

# Buscar películas por título
@app.get("/peliculas/buscar/{titulo}", response_model=List[Pelicula])
async def buscar_por_titulo(titulo: str):
    return [p for p in peliculas if titulo.lower() in p.titulo.lower()]

# Eliminar película por ID (trazabilidad conservada)
@app.delete("/peliculas/{pelicula_id}")
async def eliminar_pelicula(pelicula_id: int):
    for pelicula in peliculas:
        if pelicula.id == pelicula_id:
            peliculas.remove(pelicula)
            guardar_peliculas_csv(peliculas)
            return {"mensaje": f"Pelicula con ID {pelicula_id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Pelicula no encontrada")

# Crear un nuevo director
@app.post("/directores", response_model=Director)
async def agregar_director(director: Director):
    if any(d.id == director.id for d in directores):
        raise HTTPException(status_code=400, detail="El ID del director ya existe")
    directores.append(director)
    guardar_directores_csv(directores)
    return director

# Listar todos los directores
@app.get("/directores", response_model=List[DirectorRespuesta])
async def listar_directores():
    return directores

# Manejo personalizado de excepciones HTTP
@app.exception_handler(HTTPException)
async def manejar_errores_http(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensaje": f"Error: {exc.detail}"}
    )
