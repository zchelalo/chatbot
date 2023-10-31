from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.jwt_manager import validate_token
from services.usuarios import UsuarioService
from config.database import Session

class JWTBearer(HTTPBearer):
  async def __call__(self, request: Request):
    db = Session()
    users = UsuarioService(db).get_usuario_random()
    if users:
      auth = await super().__call__(request)
      data = validate_token(auth.credentials)

      result = UsuarioService(db).get_usuario_by_correo(data['correo'])

      if not result:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})