from fastapi import APIRouter, Response, status, HTTPException, Depends
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base
from services.stories import StoryService
from schemas.stories import Story as StorySchema, StoryUpdate as StoryUpdateSchema

story_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@story_router.get(
    path='/stories', 
    tags=['stories'], 
    status_code=status.HTTP_200_OK,
    response_model=List[StorySchema],
    dependencies=[Depends(JWTBearer())]
  )
async def get_stories() -> List[StorySchema]:
  db = Session()
  result = StoryService(db).get_stories()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron historias'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@story_router.get(
    path='/stories/{id}', 
    tags=['stories'], 
    status_code=status.HTTP_200_OK,
    response_model=StorySchema,
    dependencies=[Depends(JWTBearer())]
  )
async def get_story(id: int) -> StorySchema:
  db = Session()
  result = StoryService(db).get_story(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la historia'})
  return result

############################################################################
# Insertar un registro
############################################################################
@story_router.post(
    path='/stories', 
    tags=['stories'], 
    status_code=status.HTTP_200_OK,
    response_model=StorySchema,
    dependencies=[Depends(JWTBearer())]
  )
async def create_story(story: StorySchema) -> StorySchema:
  if story.id:
    story.id = None
  db = Session()
  new_story = StoryService(db).create_story(story)
  return new_story

############################################################################
# Actualizar un registro
############################################################################
@story_router.put(
    path='/stories/{id}', 
    tags=['stories'], 
    status_code=status.HTTP_200_OK,
    response_model=StorySchema,
    dependencies=[Depends(JWTBearer())]
  )
async def update_story(id: int, story_update: StoryUpdateSchema) -> StorySchema:
  db = Session()
  story = StoryService(db).get_story(id)
  if not story:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la historia'})
  
  result = StoryService(db).update_story(story, story_update)
  return result

############################################################################
# Borrar un registro
############################################################################
@story_router.delete(
    path='/stories/{id}', 
    tags=['stories'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(JWTBearer())]
  )
async def delete_story(id: int):
  db = Session()
  story = StoryService(db).get_story(id)
  if not story:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la historia'})
  
  StoryService(db).delete_story(story)

  return Response(status_code=HTTP_204_NO_CONTENT)