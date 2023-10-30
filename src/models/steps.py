from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Step(Base):
  __tablename__ = "steps"

  id = Column(Integer, primary_key=True)
  id_story = Column(Integer, ForeignKey('stories.id'), nullable=False)
  id_intent = Column(Integer, ForeignKey('intents.id'), nullable=False)
  story = relationship('Story', back_populates='steps')
  intent = relationship('Intent', back_populates='steps')