from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import TrainerRoleBearer
from config.database import Session, engine, Base
from services.steps_rule import StepRuleService
from schemas.steps_rule import StepRule as StepRuleSchema, StepRuleUpdate as StepRuleUpdateSchema

step_rule_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@step_rule_router.get(
    path='/steps_rule', 
    tags=['steps_rule'], 
    status_code=status.HTTP_200_OK,
    response_model=List[StepRuleSchema],
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_steps_rule() -> List[StepRuleSchema]:
  db = Session()
  result = StepRuleService(db).get_steps_rule()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron pasos para las reglas'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@step_rule_router.get(
    path='/steps_rule/{id}', 
    tags=['steps_rule'], 
    status_code=status.HTTP_200_OK,
    response_model=StepRuleSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def get_step_rule(id: int) -> StepRuleSchema:
  db = Session()
  result = StepRuleService(db).get_step_rule(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la regla'})
  return result

############################################################################
# Insertar un registro
############################################################################
@step_rule_router.post(
    path='/steps_rule', 
    tags=['steps_rule'], 
    status_code=status.HTTP_200_OK,
    response_model=StepRuleSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def create_step_rule(step_rule: StepRuleSchema) -> StepRuleSchema:
  if step_rule.id:
    step_rule.id = None
  db = Session()
  new_step_rule = StepRuleService(db).create_step_rule(step_rule)
  return new_step_rule

############################################################################
# Actualizar un registro
############################################################################
@step_rule_router.put(
    path='/steps_rule/{id}', 
    tags=['steps_rule'], 
    status_code=status.HTTP_200_OK,
    response_model=StepRuleSchema,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def update_step_rule(id: int, step_rule_update: StepRuleUpdateSchema) -> StepRuleSchema:
  db = Session()
  step_rule = StepRuleService(db).get_step_rule(id)
  if not step_rule:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la regla'})
  
  result = StepRuleService(db).update_step_rule(step_rule, step_rule_update)
  return result

############################################################################
# Borrar un registro
############################################################################
@step_rule_router.delete(
    path='/steps_rule/{id}', 
    tags=['steps_rule'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(TrainerRoleBearer())]
  )
async def delete_step_rule(id: int):
  db = Session()
  step_rule = StepRuleService(db).get_step_rule(id)
  if not step_rule:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la regla'})
  
  StepRuleService(db).delete_step_rule(step_rule)

  return Response(status_code=HTTP_204_NO_CONTENT)