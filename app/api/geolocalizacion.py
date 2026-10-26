from fastapi import APIRouter

router = APIRouter(prefix="/geolocalizacion", tags=["Módulo de Santiago - Rastreo GPS"])

@router.post("/actualizar")
async def actualizar_ubicacion(datos_gps: dict): 
    return {
        "mensaje": "Ubicación del vehículo actualizada exitosamente",
        "datos": datos_gps
    }

@router.get("/{id_vehiculo}")
async def obtener_ubicacion(id_vehiculo: str):
    return {"mensaje": f"Buscando coordenadas actuales del vehículo {id_vehiculo}"}