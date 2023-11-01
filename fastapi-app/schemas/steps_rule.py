from pydantic import BaseModel
from typing import Optional

class StepRule(BaseModel):
  id: Optional[int] = None
  id_rule: int
  id_intent: int

  model_config = {
    "json_schema_extra" : {
      "example": {
        "id_rule": 1,
        "id_intent": 1
      }
    }
  }

class StepRuleUpdate(BaseModel):
  id_rule: Optional[int] = None
  id_intent: Optional[int] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
        "id_rule": 1,
        "id_intent": 1
      }
    }
  }