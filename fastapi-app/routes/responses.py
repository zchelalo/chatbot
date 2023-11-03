from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import TrainerRoleBearer
from config.database import Session, engine, Base
from services.responses import ResponseService
from schemas.responses import Response as ResponseSchema, ResponseUpdate as ResponseUpdateSchema

response_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@response_router.get(
    path='/responses', 
    tags=['responses'], 
    status_code=status.HTTP_200_OK,
    response_model=List[ResponseSchema],
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_responses() -> List[ResponseSchema]:
  db = Session()
  result = ResponseService(db).get_responses()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron respuestas'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@response_router.get(
    path='/responses/{id}', 
    tags=['responses'], 
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_response(id: int) -> ResponseSchema:
  db = Session()
  result = ResponseService(db).get_response(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la respuesta'})
  return result

############################################################################
# Insertar un registro
############################################################################
@response_router.post(
    path='/responses', 
    tags=['responses'], 
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def create_response(response: ResponseSchema) -> ResponseSchema:
  if response.id:
    response.id = None
  db = Session()
  new_response = ResponseService(db).create_response(response)
  return new_response

############################################################################
# Actualizar un registro
############################################################################
@response_router.put(
    path='/responses/{id}', 
    tags=['responses'], 
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def update_response(id: int, response_update: ResponseUpdateSchema) -> ResponseSchema:
  db = Session()
  response = ResponseService(db).get_response(id)
  if not response:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la respuesta'})
  
  result = ResponseService(db).update_response(response, response_update)
  return result

############################################################################
# Borrar un registro
############################################################################
@response_router.delete(
    path='/responses/{id}', 
    tags=['responses'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def delete_response(id: int):
  db = Session()
  response = ResponseService(db).get_response(id)
  if not response:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la respuesta'})
  
  ResponseService(db).delete_response(response)

  return Response(status_code=HTTP_204_NO_CONTENT)