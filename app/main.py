from fastapi import FastAPI
from app.api.ruta import router as rutas_router
from app.api.archivos import router as archivos_router

app = FastAPI(
    title="viaCol",
    description="viaCol is a web application that allows users to upload and share files securely.",
    version="1.0.0"
)

# Registro de routers
app.include_router(rutas_router)
app.include_router(archivos_router)

@app.get("/")
def leer_raiz():
    return {"message": "Welcome to viaCol!"}