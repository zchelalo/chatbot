from models.rules import Rule as RuleModel
from schemas.rules import Rule as RuleSchema, RuleUpdate as RuleUpdateSchema

class RuleService():
  def __init__(self, db) -> None:
    self.db = db

  def get_rules(self):
    with self.db as session:
      result = session.query(RuleModel).all()
      return result
  
  def get_rule(self, id):
    with self.db as session:
      result = session.query(RuleModel).where(RuleModel.id == id).one_or_none()
      return result
  
  def create_rule(self, rule: RuleSchema):
    with self.db as session:
      new_rule = RuleModel(**rule.model_dump())
      session.add(new_rule)
      session.commit()
      session.refresh(new_rule)
      return new_rule
  
  def update_rule(self, rule: RuleSchema, rule_update: RuleUpdateSchema):
    with self.db as session:
      for field, value in rule_update.model_dump(exclude_unset=True).items():
        setattr(rule, field, value)

      session.commit()
      session.refresh(rule)
      return rule
  
  def delete_rule(self, rule):
    with self.db as session:
      session.delete(rule)
      session.commit()
      return