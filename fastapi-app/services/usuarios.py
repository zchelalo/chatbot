from models.usuarios import Usuario as UsuarioModel
from schemas.usuarios import Usuario as UsuarioSchema, UsuarioUpdate as UsuarioUpdateSchema

class UsuarioService():
  def __init__(self, db) -> None:
    self.db = db

  def get_usuarios(self):
    with self.db as session:
      result = session.query(UsuarioModel).all()
      return result
  
  def get_usuario(self, matricula):
    with self.db as session:
      result = session.query(UsuarioModel).where(UsuarioModel.matricula == matricula).one_or_none()
      return result
  
  def get_usuario_by_correo(self, correo):
    with self.db as session:
      result = session.query(UsuarioModel).where(UsuarioModel.correo == correo).one_or_none()
      return result
  
  def get_usuario_by_matricula(self, matricula):
    with self.db as session:
      result = session.query(UsuarioModel).where(UsuarioModel.matricula == matricula).one_or_none()
      return result
  
  def get_usuario_random(self):
    with self.db as session:
      result = session.query(UsuarioModel).limit(1).one_or_none()
      return result
  
  def create_usuario(self, usuario: UsuarioSchema):
    with self.db as session:
      new_usuario = UsuarioModel(**usuario.model_dump())
      session.add(new_usuario)
      session.commit()
      session.refresh(new_usuario)
      return new_usuario
  
  def update_usuario(self, usuario: UsuarioSchema, usuario_update: UsuarioUpdateSchema):
    with self.db as session:
      for field, value in usuario_update.model_dump(exclude_unset=True).items():
        setattr(usuario, field, value)

      session.commit()
      session.refresh(usuario)
      return usuario
  
  def delete_usuario(self, usuario):
    with self.db as session:
      session.delete(usuario)
      session.commit()
      return