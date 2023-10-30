from config.database import Base
from sqlalchemy import Column, Integer, Text
# from sqlalchemy.orm import relationship

class Story(Base):
  __tablename__ = "stories"

  id = Column(Integer, primary_key=True)
  descripcion = Column(Text, nullable=False, unique=True)
  # responses = relationship('Response', back_populates='intent')