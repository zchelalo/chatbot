from models.steps import Step as StepModel
from schemas.steps import Step as StepSchema, StepUpdate as StepUpdateSchema

class StepService():
  def __init__(self, db) -> None:
    self.db = db

  def get_steps(self):
    result = self.db.query(StepModel).all()
    return result
  
  def get_step(self, id):
    result = self.db.query(StepModel).where(StepModel.id == id).one_or_none()
    return result
  
  def create_step(self, step: StepSchema):
    new_step = StepModel(**step.model_dump())
    self.db.add(new_step)
    self.db.commit()
    self.db.refresh(new_step)
    return new_step
  
  def update_step(self, step: StepSchema, step_update: StepUpdateSchema):
    for field, value in step_update.model_dump(exclude_unset=True).items():
      setattr(step, field, value)

    self.db.commit()
    self.db.refresh(step)
    return step
  
  def delete_step(self, step):
    self.db.delete(step)
    self.db.commit()
    return