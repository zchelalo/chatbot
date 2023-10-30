from fastapi import FastAPI
from docs import tags_metadata
from middlewares.error_handler import ErrorHandler
from routes.usuarios import usuario_router
from routes.auth import auth_router
from routes.intents import intent_router
from routes.responses import response_router
import os
import uvicorn

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)

app = FastAPI(
	title= 'REST API del chatbot de la Universidad Tecnológica de Nogales',
	description= 'API para el manejo y entrenamiento del chatbot de la UTN (Universidad Tecnológica de Nogales) con autenticación de usuario desarrollada con FastAPI, Rasa y PostgreSQL',
	version= '0.0.1',
	openapi_tags=tags_metadata
)

app.add_middleware(ErrorHandler)

app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(intent_router)
app.include_router(response_router)