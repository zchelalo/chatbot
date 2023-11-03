from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_200_OK
from utils.jwt_manager import create_token
from schemas.usuarios import UsuarioAuth as UsuarioAuthSchema
from services.usuarios import UsuarioService
from config.database import Session
from passlib.hash import sha256_crypt

auth_router = APIRouter()

@auth_router.post(
  path='/login',
  status_code=status.HTTP_200_OK,
  tags=['auth']
)
async def login(usuario: UsuarioAuthSchema) -> dict:
  correo = usuario.correo
  password = usuario.password

  db = Session()
  result = UsuarioService(db).get_usuario_by_correo(correo)

  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})

  if sha256_crypt.verify(password, result.password):
    user = {
      'matricula': result.matricula,
      'rol': result.rol
    }
    expiration_time = 120
    token: str = create_token(user, expiration_time)
    
    return JSONResponse(status_code=HTTP_200_OK, content={'token': token})
  else:
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})