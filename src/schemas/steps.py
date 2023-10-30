from pydantic import BaseModel
from typing import Optional

class Step(BaseModel):
  id: Optional[int] = None
  id_story: int
  id_intent: int

  model_config = {
    "json_schema_extra" : {
      "example": {
        "id_story": 1,
        "id_intent": 1
      }
    }
  }

class StepUpdate(BaseModel):
  id_story: Optional[int] = None
  id_intent: Optional[int] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
        "id_story": 1,
        "id_intent": 1
      }
    }
  }