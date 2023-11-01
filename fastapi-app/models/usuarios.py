from config.database import Base
from sqlalchemy import Column, Integer, String, SmallInteger

class Usuario(Base):
  __tablename__ = "usuarios"

  matricula = Column(Integer, primary_key=True, autoincrement=False)
  nombre = Column(String(100), nullable=False)
  correo = Column(String(100), nullable=False, unique=True)
  password = Column(String(150), nullable=False)
  rol = Column(SmallInteger, nullable=False)