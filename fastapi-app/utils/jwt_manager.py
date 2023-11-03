from jwt import encode, decode
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
JWT_KEY = os.getenv("JWT_KEY")

def create_token(data: dict, expiration_minutes: int = 120) -> str:
  # Define la fecha de vencimiento
  expires = datetime.utcnow() + timedelta(minutes=expiration_minutes)

  # Agrega los datos de expiración al payload del token
  payload = {
    "matricula": data["matricula"],
    "rol": [data["rol"]],
    "exp": expires  # Fecha de vencimiento
  }

  # Crea el token JWT
  token: str = encode(payload=payload, key=JWT_KEY, algorithm="HS256")
  return token

def validate_token(token: str) -> dict:
  data: dict = decode(token, key=JWT_KEY, algorithms=["HS256"])
  return data