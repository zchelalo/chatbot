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

# import yaml
import ruamel.yaml

training_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Crear domain.yml
############################################################################
@training_router.post(
    path='/training/domain', 
    tags=['training'], 
    status_code=status.HTTP_200_OK,
    # response_model=IntentSchema,
    dependencies=[Depends(JWTBearer())]
  )
def create_domain():
  db = Session()
  intents = IntentService(db).get_intents()

  respuestas = {}
  intenciones = []

  for intent in intents:
    intencion = intent.nombre_intent
    intenciones.append(intencion)

    responses = ResponseService(db).get_responses_by_intent_id(intent.id)
    respuesta = [{response.type: response.respuesta} for response in responses]

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
  yaml.width = 10000
  # yaml.explicit_start = True

  with open("domain2.yml", "w") as yaml_file:
      yaml.dump(domain_data, yaml_file)

  return domain_data

############################################################################
# Crear nlu.yml
############################################################################
@training_router.post(
    path='/training/nlu', 
    tags=['training'], 
    status_code=status.HTTP_200_OK,
    # response_model=IntentSchema,
    dependencies=[Depends(JWTBearer())]
  )
def create_nlu():
  db = Session()
  intents = IntentService(db).get_intents()

  # Crear un diccionario con los datos dinámicos
  nlu_data = {
      "version": "3.1",
      "nlu": []
    }

  for intent in intents:
    nlu_data["nlu"].append(
      {
        "intent": intent.nombre_intent,
        "examples": intent.ejemplos
      }
    )

  # Nombre del archivo NLU
  nlu_filename = "data/nlu2.yml"

  # Escribir el contenido en un archivo YAML
  yaml = ruamel.yaml.YAML()
  yaml.indent(offset=2)
  yaml.width = 10000

  with open(nlu_filename, "w") as nlu_file:
    yaml.dump(nlu_data, nlu_file)

  # Corregir la indentación de "intent" aquí
  with open(nlu_filename, "r") as nlu_file:
    nlu_content = nlu_file.read()
    nlu_content = nlu_content.replace("  - intent", "- intent")
    nlu_content = nlu_content.replace("  examples:", "  examples: |")

  with open(nlu_filename, "w") as nlu_file:
    nlu_file.write(nlu_content)

  return intents

############################################################################
# Crear stories.yml
############################################################################
@training_router.post(
    path='/training/stories', 
    tags=['training'], 
    status_code=status.HTTP_200_OK,
    # response_model=IntentSchema,
    dependencies=[Depends(JWTBearer())]
  )
def create_stories():
  db = Session()
  steps = StepService(db).get_steps_story_and_intent()

  # Crear un diccionario con el formato deseado
  stories_data  = {
    "version": "3.1",
    "stories": []
  }

  formatted_data = {}
  for step in steps:
    descripcion = step.descripcion
    intent = step.nombre_intent
    respuesta = step.nombre_respuesta

    if descripcion not in formatted_data:
      formatted_data[descripcion] = {
        "intent": [intent],
        "respuesta": [respuesta]
      }
    else:
      formatted_data[descripcion]["intent"].append(intent)
      formatted_data[descripcion]["respuesta"].append(respuesta)

  # Convertir los datos al formato de Rasa
  for descripcion, data in formatted_data.items():
    story_entry = {
      "story": descripcion,
      "steps": []
    }
    for intent, respuesta in zip(data["intent"], data["respuesta"]):
      story_entry["steps"].append({"intent": intent})
      story_entry["steps"].append({"action": respuesta})
    stories_data["stories"].append(story_entry)

  # Nombre del archivo Stories
  stories_filename = "data/stories2.yml"
    
  # Escribir el contenido en un archivo YAML
  yaml = ruamel.yaml.YAML()
  yaml.indent(offset=2)
  yaml.width = 10000

  with open(stories_filename, "w") as stories_file:
    yaml.dump(stories_data, stories_file)

  # Corregir la indentación de "intent" aquí
  with open(stories_filename, "r") as stories_file:
    stories_content = stories_file.read()
    stories_content = stories_content.replace("  - story", "- story")
    stories_content = stories_content.replace("    - intent", "  - intent")
    stories_content = stories_content.replace("    - action", "  - action")

  with open(stories_filename, "w") as stories_file:
    stories_file.write(stories_content)

  return stories_data