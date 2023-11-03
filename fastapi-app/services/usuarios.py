from models.usuarios import Usuario as UsuarioModel
from schemas.usuarios import Usuario as UsuarioSchema, UsuarioUpdate as UsuarioUpdateSchema

class UsuarioService():
  def __init__(self, db) -> None:
    self.db = db

  def get_usuarios(self):
    result = self.db.query(UsuarioModel).all()
    return result
  
  def get_usuario(self, matricula):
    result = self.db.query(UsuarioModel).where(UsuarioModel.matricula == matricula).one_or_none()
    return result
  
  def get_usuario_by_correo(self, correo):
    result = self.db.query(UsuarioModel).where(UsuarioModel.correo == correo).one_or_none()
    return result
  
  def get_usuario_by_matricula(self, matricula):
    result = self.db.query(UsuarioModel).where(UsuarioModel.matricula == matricula).one_or_none()
    return result
  
  def get_usuario_random(self):
    result = self.db.query(UsuarioModel).limit(1).one_or_none()
    return result
  
  def create_usuario(self, usuario: UsuarioSchema):
    new_usuario = UsuarioModel(**usuario.model_dump())
    self.db.add(new_usuario)
    self.db.commit()
    self.db.refresh(new_usuario)
    return new_usuario
  
  def update_usuario(self, usuario: UsuarioSchema, usuario_update: UsuarioUpdateSchema):
    for field, value in usuario_update.model_dump(exclude_unset=True).items():
      setattr(usuario, field, value)

    self.db.commit()
    self.db.refresh(usuario)
    return usuario
  
  def delete_usuario(self, usuario):
    self.db.delete(usuario)
    self.db.commit()
    return