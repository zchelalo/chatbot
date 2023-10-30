from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.jwt_manager import validate_token
from services.usuarios import UsuarioService
from config.database import Session
from models.response_types import ResponseType

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
    else:
      response_type = db.query(ResponseType).limit(1).one_or_none()
      if not response_type:
        registros = [
          ResponseType(type='text'),
          ResponseType(type='image'),
          ResponseType(type='pdf'),
          ResponseType(type='url')
        ]
        db.add_all(registros)
        db.commit()