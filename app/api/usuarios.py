from fastapi import APIRouter
from app.schemas.usuario_schema import UsuarioRegistro, UsuarioLogin

router = APIRouter(prefix="/usuarios", tags=["Módulo del Líder - Usuarios y Autenticación"])

@router.post("/registro")
async def registrar_usuario(usuario: UsuarioRegistro):
    return {
        "mensaje": f"El {usuario.rol} {usuario.nombre} fue registrado exitosamente en Viacol.",
        "datos_recibidos": usuario.correo
    }

@router.post("/login")
async def login_usuario(credenciales: UsuarioLogin):
    return {
        "mensaje": f"Bienvenido a Viacol, {credenciales.correo}.",
        "estado": "Login exitoso"
    }