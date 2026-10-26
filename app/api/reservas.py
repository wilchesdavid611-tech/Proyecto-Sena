from fastapi import APIRouter
from app.schemas.reserva_schema import ReservaRegistro

# El prefix "/reservas" hace que todas las rutas de este archivo empiecen por ahí automáticamente
router = APIRouter(prefix="/reservas", tags=["Módulo de Reservas y Tiquetes - Lorena"])

@router.post("/")
async def crear_reserva(reserva: ReservaRegistro):
    # Más adelante aquí irá la conexión a MongoDB para guardar el tiquete real
    return {
        "mensaje": f"Reserva confirmada para la silla {reserva.numero_silla}.",
        "estado_pago": reserva.estado,
        "datos_recibidos": reserva
    }

@router.get("/{id_usuario}")
async def obtener_reservas_usuario(id_usuario: str):
    # Más adelante aquí buscaremos en MongoDB todos los pasajes comprados por este id_usuario
    return {
        "mensaje": f"Buscando el historial de viajes para el pasajero {id_usuario}.",
        "reservas": [] 
    }