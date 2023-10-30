from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base

from services.usuarios import UsuarioService
from services.intents import IntentService
from services.responses import ResponseService
from services.stories import StoryService
from services.steps import StepService

from schemas.usuarios import Usuario as UsuarioSchema
from schemas.intents import Intent as IntentSchema
from schemas.responses import Response as ResponseSchema
from schemas.stories import Story as StorySchema
from schemas.steps import Step as StepSchema

import yaml
import ruamel.yaml

training_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Crear domain.yml
############################################################################
@training_router.post(
    path='/training', 
    tags=['training'], 
    status_code=status.HTTP_200_OK,
    # response_model=IntentSchema,
    dependencies=[Depends(JWTBearer())]
  )
def create_intent():
  db = Session()
  intents = IntentService(db).get_intents()

  respuestas = {}
  intenciones = []

  for intent in intents:
    intencion = intent.nombre_intent
    intenciones.append(intencion)

    responses = ResponseService(db).get_responses_by_intent_id(intent.id)
    respuesta = [{"text": response.respuesta} for response in responses]

    # Usamos la intención como clave y la lista de respuestas como valor
    respuestas[intent.nombre_respuesta] = respuesta

  # Agregar las intenciones al diccionario domain_data
  domain_data = {
    "version": "3.1",
    "intents": intenciones,
    "responses": respuestas,
    "session_config": {
        "session_expiration_time": 60,
        "carry_over_slots_to_new_session": True
    }
  }

  # Escribir el contenido en un archivo YAML
  yaml = ruamel.yaml.YAML()
  # yaml.explicit_start = True

  with open("domain2.yml", "w") as yaml_file:
      yaml.dump(domain_data, yaml_file)

  return domain_data