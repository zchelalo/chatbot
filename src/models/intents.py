from config.database import Base
from sqlalchemy import Column, Integer, String, ARRAY, Text
from sqlalchemy.orm import relationship

class Intent(Base):
  __tablename__ = "intents"

  id = Column(Integer, primary_key=True)
  nombre_intent = Column(String(100), nullable=False, unique=True)
  nombre_respuesta = Column(String(150), nullable=False, unique=True)
  descripcion = Column(Text, nullable=True)
  ejemplos = Column(ARRAY(String), nullable=False)
  responses = relationship('Response', back_populates='intent')