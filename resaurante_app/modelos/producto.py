class Producto:

  def __init__(self, id_prod, nombre, precio, categoria):
    self.id = id_prod
    self.nombre = nombre
    self.precio = float(precio)
    self.categoria = categoria

  def a_diccionario(self):
    return {
        "id": self.id,
        "nombre": self.nombre,
        "precio": self.precio,
        "categoria": self.categoria,
    }

  @classmethod
  def de_diccionario(cls, datos):
    return cls(
        datos.get("id"),
        datos.get("nombre"),
        datos.get("precio"),
        datos.get("categoria"),
    )