from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ResponseType(Base):
  __tablename__ = "response_types"

  id = Column(Integer, primary_key=True)
  type = Column(String(100), nullable=False)
  responses = relationship('Response', back_populates='response_type')