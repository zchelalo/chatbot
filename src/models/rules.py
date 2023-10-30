from config.database import Base
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

class Rule(Base):
  __tablename__ = "rules"

  id = Column(Integer, primary_key=True)
  descripcion = Column(Text, nullable=False, unique=True)
  steps_rule = relationship('StepRule', back_populates='rule')