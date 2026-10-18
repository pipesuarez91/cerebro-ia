from fastapi import FastAPI, HTTPException

app = FastAPI(title="Cerebro Central IA - Omnicanal")

@app.get("/")
def inicio():
    return {"estado": "El cerebro de la IA está activo y funcionando 24/7, señor"}

@app.post("/controlar")
async def ejecutar_comando_fisico(datos: dict):
    tipo = datos.get("dispositivo_tipo", "").lower()
    dispositivo_id = datos.get("dispositivo_id", "desconocido")
    accion = datos.get("accion", "ninguna")
    
    if tipo == "tv":
        resultado = f"Enviando señal para '{accion}' a la televisión ID: {dispositivo_id}"
    elif tipo == "camara":
        resultado = f"Abriendo flujo de video en vivo de la cámara: {dispositivo_id}"
    elif tipo == "carro":
        resultado = f"Ejecutando '{accion}' en el vehículo ID: {dispositivo_id}"
    elif tipo == "celular":
        resultado = f"Rastreando o enviando comando al celular ID: {dispositivo_id}"
    else:
        raise HTTPException(status_code=400, detail="Dispositivo no reconocido por el cerebro, señor.")

    return {
        "status": "exito",
        "accion_ejecutada": resultado
    }
