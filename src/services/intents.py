from models.intents import Intent as IntentModel
from schemas.intents import Intent as IntentSchema, IntentUpdate as IntentUpdateSchema

class IntentService():
  def __init__(self, db) -> None:
    self.db = db

  def get_intents(self):
    result = self.db.query(IntentModel).all()
    return result
  
  def get_intent(self, id):
    result = self.db.query(IntentModel).where(IntentModel.id == id).one_or_none()
    return result
  
  def create_intent(self, intent: IntentSchema):
    new_intent = IntentModel(**intent.model_dump())
    self.db.add(new_intent)
    self.db.commit()
    self.db.refresh(new_intent)
    return new_intent
  
  def update_intent(self, intent: IntentSchema, intent_update: IntentUpdateSchema):
    for field, value in intent_update.model_dump(exclude_unset=True).items():
      setattr(intent, field, value)

    self.db.commit()
    self.db.refresh(intent)
    return intent
  
  def delete_intent(self, intent):
    self.db.delete(intent)
    self.db.commit()
    return