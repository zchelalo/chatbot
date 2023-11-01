from pydantic import BaseModel
from typing import Optional

class Rule(BaseModel):
  id: Optional[int] = None
  descripcion: str

  model_config = {
    "json_schema_extra" : {
      "example": {
        "descripcion": "saludar siempre que el usuario lo haga"
      }
    }
  }

class RuleUpdate(BaseModel):
  descripcion: str

  model_config = {
    "json_schema_extra" : {
      "example": {
        "descripcion": "saludar siempre que el usuario lo haga"
      }
    }
  }