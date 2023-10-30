from models.rules import Rule as RuleModel
from schemas.rules import Rule as RuleSchema, RuleUpdate as RuleUpdateSchema

class RuleService():
  def __init__(self, db) -> None:
    self.db = db

  def get_rules(self):
    result = self.db.query(RuleModel).all()
    return result
  
  def get_rule(self, id):
    result = self.db.query(RuleModel).where(RuleModel.id == id).one_or_none()
    return result
  
  def create_rule(self, rule: RuleSchema):
    new_rule = RuleModel(**rule.model_dump())
    self.db.add(new_rule)
    self.db.commit()
    self.db.refresh(new_rule)
    return new_rule
  
  def update_rule(self, rule: RuleSchema, rule_update: RuleUpdateSchema):
    for field, value in rule_update.model_dump(exclude_unset=True).items():
      setattr(rule, field, value)

    self.db.commit()
    self.db.refresh(rule)
    return rule
  
  def delete_rule(self, rule):
    self.db.delete(rule)
    self.db.commit()
    return