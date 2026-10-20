from fastapi import FastAPI
from app.api import usuarios
from app.api import geolocalizacion 
app = FastAPI(title="viaCol")

app.include_router(usuarios.router, prefix="/api/v1/usuarios", tags=["Seguridad"])

app.include_router(geolocalizacion.router)

@app.get("/")
def leer_raiz():
    return {"message": "Welcome to viaCol!"}