from models.responses import Response as ResponseModel
from schemas.responses import Response as ResponseSchema, ResponseUpdate as ResponseUpdateSchema

class ResponseService():
  def __init__(self, db) -> None:
    self.db = db

  def get_responses(self):
    result = self.db.query(ResponseModel).all()
    return result
  
  def get_response(self, id):
    result = self.db.query(ResponseModel).where(ResponseModel.id == id).one_or_none()
    return result
  
  def get_responses_by_intent_id(self, id):
    result = self.db.query(ResponseModel).where(ResponseModel.id_intent == id).all()
    return result
  
  def create_response(self, response: ResponseSchema):
    new_response = ResponseModel(**response.model_dump())
    self.db.add(new_response)
    self.db.commit()
    self.db.refresh(new_response)
    return new_response
  
  def update_response(self, response: ResponseSchema, response_update: ResponseUpdateSchema):
    for field, value in response_update.model_dump(exclude_unset=True).items():
      setattr(response, field, value)

    self.db.commit()
    self.db.refresh(response)
    return response
  
  def delete_response(self, response):
    self.db.delete(response)
    self.db.commit()
    return