from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
SECRET_KEY = "super_secreto_viacol_sena"
ALGORITHM = "HS256"

def validar_token_y_rol(token: str = Depends(oauth2_scheme)):
    credenciales_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar la firma del token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        rol: str = payload.get("rol")
        if rol is None:
            raise credenciales_exception
        
        # Validar permisos (RBAC)
        if rol != "administrador":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos suficientes")
            
        return payload
    except JWTError:
        raise credenciales_exception