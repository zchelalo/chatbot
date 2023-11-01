from models.steps_rule import StepRule as StepRuleModel
from schemas.steps_rule import StepRule as StepRuleSchema, StepRuleUpdate as StepRuleUpdateSchema
from sqlalchemy import text

class StepRuleService():
  def __init__(self, db) -> None:
    self.db = db

  def get_steps_rule(self):
    result = self.db.query(StepRuleModel).all()
    return result
  
  def get_step_rule(self, id):
    result = self.db.query(StepRuleModel).where(StepRuleModel.id == id).one_or_none()
    return result
  
  def get_step_rule_rule_and_intent(self):
    sql = text("""
      SELECT "rules"."descripcion", "intents"."nombre_intent", "intents"."nombre_respuesta"
      FROM "steps_rule"
      INNER JOIN "rules"
      ON "steps_rule"."id_rule" = "rules"."id"
      INNER JOIN "intents"
      ON "steps_rule"."id_intent" = "intents"."id"
    """)

    result = self.db.execute(sql)
    results = result.fetchall()

    return results
  
  def create_step_rule(self, step_rule: StepRuleSchema):
    new_step = StepRuleModel(**step_rule.model_dump())
    self.db.add(new_step)
    self.db.commit()
    self.db.refresh(new_step)
    return new_step
  
  def update_step_rule(self, step_rule: StepRuleSchema, step_rule_update: StepRuleUpdateSchema):
    for field, value in step_rule_update.model_dump(exclude_unset=True).items():
      setattr(step_rule, field, value)

    self.db.commit()
    self.db.refresh(step_rule)
    return step_rule
  
  def delete_step_rule(self, step_rule):
    self.db.delete(step_rule)
    self.db.commit()
    return