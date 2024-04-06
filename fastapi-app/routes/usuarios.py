from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import AdminRoleBearer, TrainerRoleBearer
from config.database import Session, engine, Base
from services.usuarios import UsuarioService
from schemas.usuarios import Usuario as UsuarioSchema, UsuarioUpdate as UsuarioUpdateSchema
from passlib.hash import sha256_crypt

usuario_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@usuario_router.get(
    path='/usuarios', 
    tags=['usuarios'], 
    status_code=status.HTTP_200_OK,
    response_model=List[UsuarioSchema],
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_usuarios() -> List[UsuarioSchema]:
  db = Session()
  result = UsuarioService(db).get_usuarios()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron usuarios'})
  return result
  # return JSONResponse(status_code=HTTP_200_OK, content=result)

############################################################################
# Obtener un registro en base a la matricula
############################################################################
@usuario_router.get(
    path='/usuarios/{matricula}', 
    tags=['usuarios'], 
    status_code=status.HTTP_200_OK,
    response_model=UsuarioSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_usuario(matricula: int) -> UsuarioSchema:
  db = Session()
  result = UsuarioService(db).get_usuario(matricula)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})
  return result
  # return JSONResponse(status_code=HTTP_200_OK, content=result)

############################################################################
# Insertar un registro
############################################################################
@usuario_router.post(
    path='/usuarios', 
    tags=['usuarios'], 
    status_code=status.HTTP_200_OK,
    response_model=UsuarioSchema,
    dependencies=[Depends(AdminRoleBearer())]
  )
async def create_usuario(usuario: UsuarioSchema) -> UsuarioSchema:
  password = sha256_crypt.hash(usuario.password)
  usuario.password = password
  db = Session()
  new_usuario = UsuarioService(db).create_usuario(usuario)
  return new_usuario
  # return JSONResponse(status_code=HTTP_200_OK, content=new_usuario)

############################################################################
# Actualizar un registro
############################################################################
@usuario_router.put(
    path='/usuarios/{matricula}', 
    tags=['usuarios'], 
    status_code=status.HTTP_200_OK,
    response_model=UsuarioSchema,
    dependencies=[Depends(AdminRoleBearer())]
  )
async def update_usuario(matricula: int, usuario_update: UsuarioUpdateSchema) -> UsuarioSchema:
  db = Session()
  usuario = UsuarioService(db).get_usuario(matricula)
  if not usuario:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})
  
  if usuario_update.password:
    password = sha256_crypt.hash(usuario_update.password)
    usuario_update.password = password
  
  result = UsuarioService(db).update_usuario(matricula, usuario_update)

  return result
  # return JSONResponse(status_code=HTTP_200_OK, content=result)

############################################################################
# Borrar un registro
############################################################################
@usuario_router.delete(
    path='/usuarios/{matricula}', 
    tags=['usuarios'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(AdminRoleBearer())]
  )
async def delete_usuario(matricula: int):
  db = Session()
  usuario = UsuarioService(db).get_usuario(matricula)
  if not usuario:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})
  
  UsuarioService(db).delete_usuario(usuario)

  return Response(status_code=HTTP_204_NO_CONTENT)