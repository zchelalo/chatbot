from config.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class Response(Base):
  __tablename__ = "responses"

  id = Column(Integer, primary_key=True)
  respuesta = Column(Text, nullable=False)
  id_intent = Column(Integer, ForeignKey('intents.id'), nullable=False)
  intent = relationship('Intent', back_populates='responses')