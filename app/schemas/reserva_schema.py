from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ReservaRegistro(BaseModel):
    id_usuario: str = Field(..., example="65abc123def456", description="ID del pasajero que compra")
    id_ruta: str = Field(..., example="65def456abc123", description="ID de la ruta (ej. Bogotá - Facatativá)")
    numero_silla: int = Field(..., gt=0, example=12, description="Número de la silla seleccionada")
    metodo_pago: str = Field(..., example="pse", description="Puede ser 'tarjeta', 'efectivo' o 'pse'")
    estado: Optional[str] = Field(default="pagado", example="pagado", description="Estado del tiquete")


class ReservaRespuesta(BaseModel):
    id_reserva: str = Field(..., example="RES-987654")
    id_usuario: str
    id_ruta: str
    numero_silla: int
    metodo_pago: str
    estado: str
    fecha_compra: datetime