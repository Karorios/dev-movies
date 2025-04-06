from pydantic import BaseModel, Field
from typing import Optional

# Modelo para representar una película
class Pelicula(BaseModel):
    id: int
    titulo: str = Field(..., min_length=1, max_length=50)
    genero: str = Field(..., min_length=3, max_length=20)
    anio: int = Field(..., gt=1900, lt=2030)
    director_id: int

# Modelo para la respuesta simplificada de una película
class PeliculaRespuesta(BaseModel):
    titulo: str
    genero: str

# Modelo para representar un director
class Director(BaseModel):
    id: int
    nombre: str = Field(..., min_length=3, max_length=30)
    nacionalidad: Optional[str] = None

# Modelo para la respuesta simplificada del director
class DirectorRespuesta(BaseModel):
    nombre: str
