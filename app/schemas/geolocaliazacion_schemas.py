from pydantic import BaseModel, Field
from datetime import datetime

class UbicacionGPS(BaseModel):
    id_vehiculo: str = Field(..., example="VIA123", description="Placa o ID del bus")
    latitud: float = Field(..., example=4.8133, description="Coordenada de latitud (Ej: Facatativá)")
    longitud: float = Field(..., example=-74.3544, description="Coordenada de longitud")
    hora_reporte: datetime