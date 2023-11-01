from pydantic import BaseModel
from typing import Optional

class Response(BaseModel):
  id: Optional[int] = None
  respuesta: str
  id_intent: int

  model_config = {
    "json_schema_extra" : {
      "example": {
        "respuesta": "Hola, soy grajillo! el chatbot de la UTN. Estoy para ayudarte :)",
        "id_intent": 1
      }
    }
  }

class ResponseUpdate(BaseModel):
  respuesta: Optional[str] = None
  id_intent: Optional[int] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
        "respuesta": "Hola, soy grajillo! el chatbot de la UTN. Estoy para ayudarte :)",
        "id_intent": 1
      }
    }
  }