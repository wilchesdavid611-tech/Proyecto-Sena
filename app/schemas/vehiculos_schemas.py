from pydantic import BaseModel, Field

class VehiculoRegistro(BaseModel):
    placa: str = Field(..., min_length=6, max_length=6, example="VIA123")
    marca: str = Field(..., example="Chevrolet")
    modelo: int = Field(..., gt=1990, example=2021, description="Año de fabricación del vehículo")
    capacidad_pasajeros: int = Field(..., gt=0, example=19, description="Cantidad máxima de pasajeros sentados")
    tipo_vehiculo: str = Field(..., example="Microbús", description="Puede ser 'Microbús', 'Buseta' o 'Van'")

class VehiculoRespuesta(BaseModel):
    id_vehiculo: str = Field(..., example="65abc123def456")
    placa: str
    marca: str
    capacidad_pasajeros: int
    tipo_vehiculo: str