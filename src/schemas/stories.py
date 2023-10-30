from pydantic import BaseModel
from typing import Optional

class Story(BaseModel):
  id: Optional[int] = None
  descripcion: str

  model_config = {
    "json_schema_extra" : {
      "example": {
        "descripcion": "saludar"
      }
    }
  }

class StoryUpdate(BaseModel):
  descripcion: str

  model_config = {
    "json_schema_extra" : {
      "example": {
        "descripcion": "saludar"
      }
    }
  }