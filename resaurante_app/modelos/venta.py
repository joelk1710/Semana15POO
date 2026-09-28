class Venta:

  def __init__(self, id_venta, usuario, producto, fecha):
    self.id_venta = id_venta
    self.usuario = usuario
    self.producto = producto
    self.fecha = fecha

  def a_diccionario(self):
    return {
        "id_venta": self.id_venta,
        "usuario": self.usuario,
        "producto": self.producto,
        "fecha": self.fecha,
    }

  @classmethod
  def de_diccionario(cls, datos):
    return cls(
        datos.get("id_venta"),
        datos.get("usuario"),
        datos.get("producto"),
        datos.get("fecha"),
    )