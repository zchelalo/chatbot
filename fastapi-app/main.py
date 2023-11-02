from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from docs import tags_metadata
from middlewares.error_handler import ErrorHandler

from routes.usuarios import usuario_router
from routes.auth import auth_router
from routes.intents import intent_router
from routes.responses import response_router
from routes.stories import story_router
from routes.steps import step_router
from routes.rules import rule_router
from routes.steps_rule import step_rule_router
from routes.training import training_router
from routes.chatbot import chatbot_router

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

# Configura el middleware CORS para permitir solicitudes desde cualquier origen
# app.add_middleware(
# 	CORSMiddleware,
# 	allow_origins=["*"],  # Esto permitirá solicitudes desde cualquier origen, cambia a una lista de orígenes permitidos si es necesario.
# 	allow_credentials=True,
# 	allow_methods=["*"],  # Puedes especificar los métodos HTTP permitidos
# 	allow_headers=["*"],  # Puedes especificar los encabezados permitidos
# )

app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(intent_router)
app.include_router(response_router)
app.include_router(story_router)
app.include_router(step_router)
app.include_router(rule_router)
app.include_router(step_rule_router)
app.include_router(training_router)
app.include_router(chatbot_router)