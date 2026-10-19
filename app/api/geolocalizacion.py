@app.websocket("/ws/v1/conductor/ubicacion")
async def emitir_ubicacion_conductor(websocket: WebSocket):
    """HU03 - WebSocket para que el conductor envíe su GPS (Calibrador Digital)"""
    await websocket.accept()
    # Aquí irá el ciclo while True para recibir coordenadas
    await websocket.send_text("Conexión WebSocket establecida para conductor")

@app.websocket("/ws/v1/pasajero/monitoreo")
async def monitorear_van_pasajero(websocket: WebSocket):
    """HU05 - WebSocket para que el pasajero vea la van en tiempo real"""
    await websocket.accept()
    # Aquí irá la lógica para enviarle las coordenadas al pasajero
    await websocket.send_text("Conexión WebSocket establecida para pasajero")

@app.post("/api/v1/rutas/reservar-cupo", tags=["Gestión de Transporte"])
async def reservar_cupo_van():
    """HU06 - Endpoint con control de concurrencia para descontar sillas"""
    return {"mensaje": "Endpoint de reserva de cupos creado"}