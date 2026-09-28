from datetime import datetime
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

  def __init__(self):
    self.archivo_servicio = ArchivoServicio()
    self.ruta_productos = "datos/productos.json"
    self.ruta_usuarios = "datos/usuarios.json"
    self.ruta_ventas = "datos/ventas.json"

  def validar_usuario(self, username, password):
    datos = self.archivo_servicio.cargar_json(self.ruta_usuarios)
    for u in datos:
      if u.get("usuario") == username and u.get("password") == password:
        return Usuario.de_diccionario(u)
    return None

  def obtener_usuarios(self):
    datos = self.archivo_servicio.cargar_json(self.ruta_usuarios)
    return [Usuario.de_diccionario(u) for u in datos]

  def obtener_productos(self):
    datos = self.archivo_servicio.cargar_json(self.ruta_productos)
    return [Producto.de_diccionario(p) for p in datos]

  def obtener_ventas(self):
    datos = self.archivo_servicio.cargar_json(self.ruta_ventas)
    return [Venta.de_diccionario(v) for v in datos]

  def agregar_producto(self, id_prod, nombre, precio, categoria):
    productos = self.obtener_productos()
    for p in productos:
      if p.id == id_prod:
        return False
    nuevo = Producto(id_prod, nombre, precio, categoria)
    productos.append(nuevo)
    return self.archivo_servicio.guardar_json(
        self.ruta_productos, [p.a_diccionario() for p in productos]
    )

  def buscar_producto(self, id_prod):
    for p in self.obtener_productos():
      if p.id == id_prod:
        return p
    return None

  def actualizar_producto(self, id_prod, nombre, precio, categoria):
    productos = self.obtener_productos()
    encontrado = False
    for p in productos:
      if p.id == id_prod:
        p.nombre = nombre
        p.precio = float(precio)
        p.categoria = categoria
        encontrado = True
        break
    if encontrado:
      return self.archivo_servicio.guardar_json(
          self.ruta_productos, [p.a_diccionario() for p in productos]
      )
    return False

  def eliminar_producto(self, id_prod):
    productos = self.obtener_productos()
    filtrados = [p for p in productos if p.id != id_prod]
    if len(filtrados) < len(productos):
      return self.archivo_servicio.guardar_json(
          self.ruta_productos, [p.a_diccionario() for p in filtrados]
      )
    return False

  def registrar_venta(self, usuario, producto_nombre):
    ventas = self.obtener_ventas()
    id_v = f"V{len(ventas) + 1:03d}"
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nueva_venta = Venta(id_v, usuario, producto_nombre, fecha_actual)
    ventas.append(nueva_venta)
    return self.archivo_servicio.guardar_json(
        self.ruta_ventas, [v.a_diccionario() for v in ventas]
    )