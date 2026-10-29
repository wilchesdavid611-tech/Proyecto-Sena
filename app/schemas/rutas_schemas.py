from pydantic import BaseModel, Field

# Molde para cuando el administrador crea una nueva ruta intermunicipal
class RutaRegistro(BaseModel):
    origen: str = Field(..., min_length=3, example="Bogotá", description="Ciudad o municipio de origen")
    destino: str = Field(..., min_length=3, example="Facatativá", description="Ciudad o municipio de destino")
    precio: float = Field(..., gt=0, example=12000.0, description="Costo del tiquete en pesos colombianos")
    duracion_estimada: int = Field(..., gt=0, example=90, description="Duración aproximada del viaje en minutos")

# Molde para RESPONDER (Lo que devuelve la API cuando alguien busca viajes)
class RutaRespuesta(BaseModel):
    id_ruta: str = Field(..., example="RUT-12345")
    origen: str
    destino: str
    precio: float
    duracion_estimada: int