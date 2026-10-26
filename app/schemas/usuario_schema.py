from pydantic import BaseModel, EmailStr, Field

class UsuarioRegistro(BaseModel):
    nombre: str = Field(..., min_length=3)
    correo: EmailStr = Field(...)
    contrasena: str = Field(..., min_length=6)
    rol: str = Field(...)
    telefono: str = Field(..., min_length=10)

class UsuarioLogin(BaseModel):
    correo: EmailStr = Field(...)
    contrasena: str = Field(..., min_length=6)