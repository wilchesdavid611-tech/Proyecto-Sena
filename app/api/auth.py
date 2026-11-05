from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["Seguridad - David"])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "super_secreto_viacol_sena" # En producción esto va en el .env
ALGORITHM = "HS256"

def crear_token_jwt(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
async def iniciar_sesion(form_data: OAuth2PasswordRequestForm = Depends()):
   
    hash_falso_bd = pwd_context.hash("123456") 
    
    if form_data.username != "admin" or not pwd_context.verify(form_data.password, hash_falso_bd):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
  
    token = crear_token_jwt({"sub": form_data.username, "rol": "administrador"})
    return {"access_token": token, "token_type": "bearer"}