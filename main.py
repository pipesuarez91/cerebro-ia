from fastapi import FastAPI, HTTPException, Request
import os

app = FastAPI(title="Cerebro Central IA - Omnicanal")

# Token de Telegram configurado en las variables de entorno de Render
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "TOKEN_PENDIENTE")

@app.get("/")
def inicio():
    return {"estado": "El cerebro de la IA está activo y funcionando 24/7, señor"}

@app.post("/webhook/telegram")
async def recibir_mensaje_telegram(req: Request):
    datos = await req.json()
    
    # Extraemos el mensaje enviado desde Telegram
    try:
        mensaje_texto = datos["message"]["text"]
        chat_id = datos["message"]["chat"]["id"]
        nombre_usuario = datos["message"]["from"].get("first_name", "Señor")
    except Exception:
        return {"status": "ignorado"}

    # Aquí es donde el cerebro procesa la orden
    respuesta_ia = f"Hola {nombre_usuario}, he recibido tu mensaje en el servidor de la nube: '{mensaje_texto}'. ¡Todo bajo control, señor!"

    return {
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": respuesta_ia
    }

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
