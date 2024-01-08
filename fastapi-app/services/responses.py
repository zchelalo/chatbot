from models.responses import Response as ResponseModel
from schemas.responses import Response as ResponseSchema, ResponseUpdate as ResponseUpdateSchema

class ResponseService():
  def __init__(self, db) -> None:
    self.db = db

  def get_responses(self):
    with self.db as session:
      result = session.query(ResponseModel).all()
      return result
  
  def get_response(self, id):
    with self.db as session:
      result = session.query(ResponseModel).where(ResponseModel.id == id).one_or_none()
      return result
  
  def get_responses_by_intent_id(self, id):
    with self.db as session:
      result = session.query(ResponseModel).where(ResponseModel.id_intent == id).all()
      return result
  
  def create_response(self, response: ResponseSchema):
    with self.db as session:
      new_response = ResponseModel(**response.model_dump())
      session.add(new_response)
      session.commit()
      session.refresh(new_response)
      return new_response
  
  def update_response(self, response: ResponseSchema, response_update: ResponseUpdateSchema):
    with self.db as session:
      for field, value in response_update.model_dump(exclude_unset=True).items():
        setattr(response, field, value)

      session.commit()
      session.refresh(response)
      return response
  
  def delete_response(self, response):
    with self.db as session:
      session.delete(response)
      session.commit()
      return