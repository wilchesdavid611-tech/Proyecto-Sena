from fastapi import APIRouter

router = APIRouter()

@router.post("/registro")
async def registrar_usuario():
    """HU01 - Endpoint para registrar pasajeros o conductores"""
    return {"mensaje": "Endpoint de registro creado correctamente"}

@router.post("/login")
async def login_usuario():
    """HU02 - Endpoint para iniciar sesión y generar token JWT"""
    return {"mensaje": "Endpoint de login creado correctamente"}