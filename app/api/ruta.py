from fastapi import APIRouter
from app.schemas.ruta_schema import RutaRegistro

# El prefix "/rutas" organiza todas las URLs de Jhonny
router = APIRouter(prefix="/rutas", tags=["Módulo de Rutas y Viajes - Jhonny"])

@router.post("/")
async def crear_ruta(ruta: RutaRegistro):
    # Más adelante aquí se guardará la ruta en la colección de MongoDB
    return {
        "mensaje": f"Ruta {ruta.origen} - {ruta.destino} configurada exitosamente.",
        "datos_ruta": ruta
    }

@router.get("/")
async def listar_rutas():
    # Más adelante aquí buscaremos todas las rutas disponibles en la base de datos
    return {
        "mensaje": "Mostrando todas las rutas intermunicipales activas de Viacol.",
        "rutas": []
    }