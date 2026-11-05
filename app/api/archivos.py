from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
import shutil
import os
import time

router = APIRouter(prefix="/archivos", tags=["Procesamiento de Imágenes - Jhonny"])

# Directorio donde se guardarán las fotos locales
os.makedirs("uploads", exist_ok=True)

def procesar_imagen_ia_segundo_plano(nombre_archivo: str):
    # Simulamos el tiempo que tardaría un modelo de IA predictivo
    time.sleep(5)
    print(f"La imagen {nombre_archivo} ha sido analizada por la IA exitosamente.")

@router.post("/diagnostico")
async def subir_imagen_diagnostico(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    # 1. Validar que sea una imagen
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen válida.")
    
    # 2. Guardar en el directorio local del servidor
    ruta_guardado = f"uploads/{file.filename}"
    with open(ruta_guardado, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # 3. Preparación para la IA (Ejecución en BackgroundTasks)
    background_tasks.add_task(procesar_imagen_ia_segundo_plano, file.filename)
    
    return {
        "mensaje": "Imagen recibida y guardada. La IA la está procesando en segundo plano.",
        "archivo": file.filename
    }