from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Cerebro Central IA - Omnicanal")

class ComandoDispositivo(BaseModel):
    dispositivo_tipo: str
    dispositivo_id: str
    accion: str
    parametros: dict = {}

@app.get("/")
def inicio():
    return {"estado": "El cerebro de la IA está activo y funcionando 24/7, señor"}

@app.post("/controlar")
def ejecutar_comando_fisico(comando: ComandoDispositivo):
    tipo = comando.dispositivo_tipo.lower()
    
    if tipo == "tv":
        resultado = f"Enviando señal para '{comando.accion}' a la televisión ID: {comando.dispositivo_id}"
    elif tipo == "camara":
        resultado = f"Abriendo flujo de video en vivo de la cámara: {comando.dispositivo_id}"
    elif tipo == "carro":
        resultado = f"Ejecutando '{comando.accion}' en el vehículo ID: {comando.dispositivo_id}"
    elif tipo == "celular":
        resultado = f"Rastreando o enviando comando al celular ID: {comando.dispositivo_id}"
    else:
        raise HTTPException(status_code=400, detail="Dispositivo no reconocido por el cerebro.")

    return {
        "status": "exito",
        "accion_ejecutada": resultado
    }
