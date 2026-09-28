class Usuario:

  def __init__(self, usuario, password, rol="Cliente"):
    self.usuario = usuario
    self.password = password
    self.rol = rol

  def a_diccionario(self):
    return {"usuario": self.usuario, "password": self.password, "rol": self.rol}

  @classmethod
  def de_diccionario(cls, datos):
    return cls(
        datos.get("usuario"), datos.get("password"), datos.get("rol", "Cliente")
    )