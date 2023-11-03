from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.jwt_manager import validate_token
from services.usuarios import UsuarioService
from config.database import Session

class AdminRoleBearer(HTTPBearer):
  async def __call__(self, request: Request):
    db = Session()
    auth = await super().__call__(request)
    data = validate_token(auth.credentials)

    if 'matricula' not in data:
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})

    result = UsuarioService(db).get_usuario_by_matricula(data['matricula'])

    if not result:
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})

    # Agrega lógica para verificar roles aquí
    required_roles = [1]  # Define los roles requeridos para esta ruta

    rol = data['rol']

    if not any(role in required_roles for role in rol):
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'No tienes permisos suficientes'})

    return auth

class TrainerRoleBearer(HTTPBearer):
  async def __call__(self, request: Request):
    db = Session()
    auth = await super().__call__(request)
    data = validate_token(auth.credentials)

    if 'matricula' not in data:
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})

    result = UsuarioService(db).get_usuario_by_matricula(data['matricula'])

    if not result:
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})

    # Agrega lógica para verificar roles aquí
    required_roles = [0, 1]  # Define los roles requeridos para esta ruta

    rol = data['rol']

    if not any(role in required_roles for role in rol):
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'No tienes permisos suficientes'})

    return auth