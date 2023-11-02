from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from dotenv import load_dotenv
import os
import httpx

chatbot_router = APIRouter()

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Utiliza las variables de entorno para obtener la ruta de rasa
RUTA_RASA = os.getenv("RUTA_RASA")

############################################################################
# Hablar con el bot
############################################################################
@chatbot_router.post(
    path='/chatbot', 
    tags=['chatbot'], 
    status_code=status.HTTP_200_OK
  )
async def talk_to_chatbot(request_data: dict):
  try:
    message = request_data.get("message")
    if message:
      async with httpx.AsyncClient() as client:
        response = await client.post(RUTA_RASA, json={"sender": "user", "message": message})
      if response.status_code == 200:
        data = response.json()
        return data[0]
      else:
        raise HTTPException(status_code=response.status_code, detail={'error': 'Error al realizar la solicitud', 'message': response.text})
    else:
      raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail={'error': 'El campo "message" es requerido en el cuerpo de la solicitud'})
  except Exception as e:
    return {'error': str(e)}