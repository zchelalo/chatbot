from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base
from services.steps import StepService
from schemas.steps import Step as StepSchema, StepUpdate as StepUpdateSchema

step_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@step_router.get(
    path='/steps', 
    tags=['steps'], 
    status_code=status.HTTP_200_OK,
    response_model=List[StepSchema],
    dependencies=[Depends(JWTBearer())]
  )
async def get_steps() -> List[StepSchema]:
  db = Session()
  result = StepService(db).get_steps()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron pasos'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@step_router.get(
    path='/steps/{id}', 
    tags=['steps'], 
    status_code=status.HTTP_200_OK,
    response_model=StepSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def get_step(id: int) -> StepSchema:
  db = Session()
  result = StepService(db).get_step(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el paso'})
  return result

############################################################################
# Insertar un registro
############################################################################
@step_router.post(
    path='/steps', 
    tags=['steps'], 
    status_code=status.HTTP_200_OK,
    response_model=StepSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def create_step(step: StepSchema) -> StepSchema:
  if step.id:
    step.id = None
  db = Session()
  new_step = StepService(db).create_step(step)
  return new_step

############################################################################
# Actualizar un registro
############################################################################
@step_router.put(
    path='/steps/{id}', 
    tags=['steps'], 
    status_code=status.HTTP_200_OK,
    response_model=StepSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def update_step(id: int, step_update: StepUpdateSchema) -> StepSchema:
  db = Session()
  step = StepService(db).get_step(id)
  if not step:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el paso'})
  
  result = StepService(db).update_step(step, step_update)
  return result

############################################################################
# Borrar un registro
############################################################################
@step_router.delete(
    path='/steps/{id}', 
    tags=['steps'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(JWTBearer())]
  )
async def delete_step(id: int):
  db = Session()
  step = StepService(db).get_step(id)
  if not step:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el paso'})
  
  StepService(db).delete_step(step)

  return Response(status_code=HTTP_204_NO_CONTENT)