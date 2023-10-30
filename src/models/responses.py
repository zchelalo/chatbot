from config.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class Response(Base):
  __tablename__ = "responses"

  id = Column(Integer, primary_key=True)
  respuesta = Column(Text, nullable=False)
  id_response_type = Column(Integer, ForeignKey('response_types.id'), nullable=False)
  id_intent = Column(Integer, ForeignKey('intents.id'), nullable=False)
  response_type = relationship('ResponseType', back_populates='responses')
  intent = relationship('Intent', back_populates='responses')