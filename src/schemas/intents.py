from pydantic import BaseModel, Field, constr
from typing import Optional, List

class Intent(BaseModel):
  id: Optional[int] = None
  nombre_intent: str = Field(min_length=1, max_length=100)
  nombre_respuesta: str = Field(min_length=1, max_length=150)
  descripcion: str
  ejemplos: List[str]

  model_config = {
    "json_schema_extra" : {
      "example": {
        "nombre_intent": "saludar",
        "nombre_respuesta": "utter_saludar",
        "descripcion": "Esta intención esta diseñada con el fin de saludar al bot y que este devuelva el saludo",
        "ejemplos": [
          'Hola como estas',
          'Hey que tal',
          'Hola',
          'Buenos dias',
          'Hey',
          'Ey',
          'Holaaaa',
          'Como estas',
          '¿Como estas?'
        ]
      }
    }
  }

class IntentUpdate(BaseModel):
  nombre_intent: Optional[constr(min_length=1, max_length=100)] = None
  nombre_respuesta: Optional[constr(min_length=1, max_length=150)] = None
  descripcion: Optional[str] = None
  ejemplos: Optional[List[str]] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
        "nombre_intent": "saludar",
        "nombre_respuesta": "utter_saludar",
        "descripcion": "Esta intención esta diseñada con el fin de saludar al bot y que este devuelva el saludo",
        "ejemplos": [
          'Hola como estas',
          'Hey que tal',
          'Hola',
          'Buenos dias',
          'Hey',
          'Ey',
          'Holaaaa',
          'Como estas',
          '¿Como estas?'
        ]
      }
    }
  }