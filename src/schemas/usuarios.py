from pydantic import BaseModel, Field, constr, conint
from typing import Optional

class Usuario(BaseModel):
  matricula: int
  nombre: str = Field(min_length=1, max_length=100)
  correo: str = Field(min_length=1, max_length=100)
  password: str = Field(min_length=1, max_length=150)
  rol: int = Field(ge=0, le=1)

  model_config = {
    "json_schema_extra" : {
      "example": {
        "matricula": 12345678,
        "nombre": "Panchito",
        "correo": "panchito@gmail.com",
        "password": "Panchito_1928",
        "rol": 0
      }
    }
  }

class UsuarioUpdate(BaseModel):
  nombre: Optional[constr(min_length=1, max_length=100)] = None
  correo: Optional[constr(min_length=1, max_length=100)] = None
  password: Optional[constr(min_length=1, max_length=150)] = None
  rol: Optional[conint(ge=0, le=1)] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
        "nombre": "Panchito",
        "correo": "panchito@gmail.com",
        "password": "Panchito_1928",
        "rol": 0
      }
    }
  }

class UsuarioAuth(BaseModel):
  correo: str = Field(min_length=1, max_length=100)
  password: str = Field(min_length=1, max_length=150)

  model_config = {
    "json_schema_extra" : {
      "example": {
        "correo": "panchito@gmail.com",
        "password": "Panchito_1928"
      }
    }
  }