from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class StepRule(Base):
  __tablename__ = "steps_rule"

  id = Column(Integer, primary_key=True)
  id_rule = Column(Integer, ForeignKey('rules.id'), nullable=False)
  id_intent = Column(Integer, ForeignKey('intents.id'), nullable=False)
  rule = relationship('Rule', back_populates='steps_rule')
  intent = relationship('Intent', back_populates='steps_rule')