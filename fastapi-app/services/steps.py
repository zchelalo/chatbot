from models.steps import Step as StepModel
from schemas.steps import Step as StepSchema, StepUpdate as StepUpdateSchema
from sqlalchemy import text

class StepService():
  def __init__(self, db) -> None:
    self.db = db

  def get_steps(self):
    result = self.db.query(StepModel).all()
    return result
  
  def get_step(self, id):
    with self.db as session:
      result = session.query(StepModel).where(StepModel.id == id).one_or_none()
      return result
  
  def get_steps_story_and_intent(self):
    with self.db as session:
      sql = text("""
        SELECT "stories"."descripcion", "intents"."nombre_intent", "intents"."nombre_respuesta"
        FROM "steps"
        INNER JOIN "stories"
        ON "steps"."id_story" = "stories"."id"
        INNER JOIN "intents"
        ON "steps"."id_intent" = "intents"."id"
      """)

      result = session.execute(sql)
      results = result.fetchall()

    return results
  
  def create_step(self, step: StepSchema):
    with self.db as session:
      new_step = StepModel(**step.model_dump())
      session.add(new_step)
      session.commit()
      session.refresh(new_step)
      return new_step
  
  def update_step(self, step: StepSchema, step_update: StepUpdateSchema):
    with self.db as session:
      for field, value in step_update.model_dump(exclude_unset=True).items():
        setattr(step, field, value)

      session.commit()
      session.refresh(step)
      return step
  
  def delete_step(self, step):
    with self.db as session:
      session.delete(step)
      session.commit()
      return