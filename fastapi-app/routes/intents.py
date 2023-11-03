from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import TrainerRoleBearer
from config.database import Session, engine, Base
from services.intents import IntentService
from schemas.intents import Intent as IntentSchema, IntentUpdate as IntentUpdateSchema

intent_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@intent_router.get(
    path='/intents', 
    tags=['intents'], 
    status_code=status.HTTP_200_OK,
    response_model=List[IntentSchema],
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_intents() -> List[IntentSchema]:
  db = Session()
  result = IntentService(db).get_intents()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron intenciones'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@intent_router.get(
    path='/intents/{id}', 
    tags=['intents'], 
    status_code=status.HTTP_200_OK,
    response_model=IntentSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_intent(id: int) -> IntentSchema:
  db = Session()
  result = IntentService(db).get_intent(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la intención'})
  return result

############################################################################
# Insertar un registro
############################################################################
@intent_router.post(
    path='/intents', 
    tags=['intents'], 
    status_code=status.HTTP_200_OK,
    response_model=IntentSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def create_intent(intent: IntentSchema) -> IntentSchema:
  if intent.id:
    intent.id = None
  db = Session()
  new_intent = IntentService(db).create_intent(intent)
  return new_intent

############################################################################
# Actualizar un registro
############################################################################
@intent_router.put(
    path='/intents/{id}', 
    tags=['intents'], 
    status_code=status.HTTP_200_OK,
    response_model=IntentSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def update_intent(id: int, intent_update: IntentUpdateSchema) -> IntentSchema:
  db = Session()
  intent = IntentService(db).get_intent(id)
  if not intent:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la intención'})
  
  result = IntentService(db).update_intent(intent, intent_update)
  return result

############################################################################
# Borrar un registro
############################################################################
@intent_router.delete(
    path='/intents/{id}', 
    tags=['intents'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def delete_intent(id: int):
  db = Session()
  intent = IntentService(db).get_intent(id)
  if not intent:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la intención'})
  
  IntentService(db).delete_intent(intent)

  return Response(status_code=HTTP_204_NO_CONTENT)