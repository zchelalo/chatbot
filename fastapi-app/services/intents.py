from models.intents import Intent as IntentModel
from schemas.intents import Intent as IntentSchema, IntentUpdate as IntentUpdateSchema

class IntentService():
  def __init__(self, db) -> None:
    self.db = db

  def get_intents(self):
    with self.db as session:
      result = session.query(IntentModel).all()
      return result
  
  def get_intent(self, id):
    with self.db as session:
      result = session.query(IntentModel).where(IntentModel.id == id).one_or_none()
      return result
  
  def create_intent(self, intent: IntentSchema):
    with self.db as session:
      new_intent = IntentModel(**intent.model_dump())
      session.add(new_intent)
      session.commit()
      session.refresh(new_intent)
      return new_intent
  
  def update_intent(self, intent: IntentSchema, intent_update: IntentUpdateSchema):
    with self.db as session:
      for field, value in intent_update.model_dump(exclude_unset=True).items():
        setattr(intent, field, value)

      session.commit()
      session.refresh(intent)
      return intent
  
  def delete_intent(self, intent):
    with self.db as session:
      session.delete(intent)
      session.commit()
      return