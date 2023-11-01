from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base
from services.rules import RuleService
from schemas.rules import Rule as RuleSchema, RuleUpdate as RuleUpdateSchema

rule_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@rule_router.get(
    path='/rules', 
    tags=['rules'], 
    status_code=status.HTTP_200_OK,
    response_model=List[RuleSchema],
    dependencies=[Depends(JWTBearer())]
  )
async def get_rules() -> List[RuleSchema]:
  db = Session()
  result = RuleService(db).get_rules()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron reglas'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@rule_router.get(
    path='/rules/{id}', 
    tags=['rules'], 
    status_code=status.HTTP_200_OK,
    response_model=RuleSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def get_rule(id: int) -> RuleSchema:
  db = Session()
  result = RuleService(db).get_rule(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la regla'})
  return result

############################################################################
# Insertar un registro
############################################################################
@rule_router.post(
    path='/rules', 
    tags=['rules'], 
    status_code=status.HTTP_200_OK,
    response_model=RuleSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def create_rule(rule: RuleSchema) -> RuleSchema:
  if rule.id:
    rule.id = None
  db = Session()
  new_rule = RuleService(db).create_rule(rule)
  return new_rule

############################################################################
# Actualizar un registro
############################################################################
@rule_router.put(
    path='/rules/{id}', 
    tags=['rules'], 
    status_code=status.HTTP_200_OK,
    response_model=RuleSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def update_rule(id: int, rule_update: RuleUpdateSchema) -> RuleSchema:
  db = Session()
  rule = RuleService(db).get_rule(id)
  if not rule:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la regla'})
  
  result = RuleService(db).update_rule(rule, rule_update)
  return result

############################################################################
# Borrar un registro
############################################################################
@rule_router.delete(
    path='/rules/{id}', 
    tags=['rules'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(JWTBearer())]
  )
async def delete_rule(id: int):
  db = Session()
  rule = RuleService(db).get_rule(id)
  if not rule:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la regla'})
  
  RuleService(db).delete_rule(rule)

  return Response(status_code=HTTP_204_NO_CONTENT)