import os
import tkinter as tk
from tkinter import messagebox, ttk


class MainView:

  def __init__(self, root, restaurante_servicio, usuario_actual):
    self.root = root
    self.root.title("Restaurante App - Panel Principal")
    self.root.geometry("950x650")
    self.servicio = restaurante_servicio
    self.usuario_actual = usuario_actual

    # Cargar recursos de la carpeta assets obligatoriamente
    self._cargar_assets()

    self._crear_interfaz()
    self.cargar_productos()
    self.cargar_usuarios()
    self.cargar_ventas()

  def _cargar_assets(self):
    self.logo_img = None
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
      try:
        self.logo_img = tk.PhotoImage(file=logo_path)
      except Exception:
        pass

  def _crear_interfaz(self):
    # Cabecera con identidad visual y logotipo obligatorios
    header_frame = ttk.Frame(self.root, padding=10)
    header_frame.pack(fill="x", padx=10, pady=5)

    if self.logo_img:
      lbl_logo = ttk.Label(header_frame, image=self.logo_img)
      lbl_logo.pack(side="left", padx=5)

    lbl_titulo = ttk.Label(
        header_frame,
        text="Sistema de Gestión - Restaurante App",
        font=("Arial", 14, "bold"),
    )
    lbl_titulo.pack(side="left", padx=10)

    lbl_user = ttk.Label(
        header_frame,
        text=f"Usuario: {self.usuario_actual.usuario} ({self.usuario_actual.rol})",
        font=("Arial", 10),
    )
    lbl_user.pack(side="right", padx=5)

    # Sistema de pestañas (Notebook)
    self.notebook = ttk.Notebook(self.root)
    self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

    self.tab_productos = ttk.Frame(self.notebook)
    self.notebook.add(self.tab_productos, text="Gestión de Productos")
    self._crear_seccion_productos(self.tab_productos)

    self.tab_usuarios = ttk.Frame(self.notebook)
    self.notebook.add(self.tab_usuarios, text="Consulta de Usuarios")
    self._crear_seccion_usuarios(self.tab_usuarios)

    self.tab_ventas = ttk.Frame(self.notebook)
    self.notebook.add(self.tab_ventas, text="Gestión de Ventas")
    self._crear_seccion_ventas(self.tab_ventas)

  def _crear_seccion_productos(self, parent):
    frame_izq = ttk.LabelFrame(
        parent, text=" Formulario de Productos ", padding=15
    )
    frame_izq.pack(side="left", fill="y", padx=10, pady=10)

    frame_der = ttk.LabelFrame(parent, text=" Lista de Productos ", padding=15)
    frame_der.pack(side="right", fill="both", padx=10, pady=10, expand=True)

    ttk.Label(frame_izq, text="ID Producto:").grid(
        row=0, column=0, sticky="w", pady=5
    )
    self.txt_id = ttk.Entry(frame_izq, width=20)
    self.txt_id.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(frame_izq, text="Nombre:").grid(
        row=1, column=0, sticky="w", pady=5
    )
    self.txt_nombre = ttk.Entry(frame_izq, width=20)
    self.txt_nombre.grid(row=1, column=1, pady=5, padx=5)

    ttk.Label(frame_izq, text="Precio:").grid(
        row=2, column=0, sticky="w", pady=5
    )
    self.txt_precio = ttk.Entry(frame_izq, width=20)
    self.txt_precio.grid(row=2, column=1, pady=5, padx=5)

    ttk.Label(frame_izq, text="Categoría:").grid(
        row=3, column=0, sticky="w", pady=5
    )
    self.txt_categoria = ttk.Entry(frame_izq, width=20)
    self.txt_categoria.grid(row=3, column=1, pady=5, padx=5)

    frame_botones = ttk.Frame(frame_izq)
    frame_botones.grid(row=4, column=0, columnspan=2, pady=15)

    ttk.Button(
        frame_botones, text="Registrar", command=self.registrar_producto
    ).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(
        frame_botones, text="Consultar", command=self.consultar_producto
    ).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(
        frame_botones, text="Actualizar", command=self.actualizar_producto
    ).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(
        frame_botones, text="Eliminar", command=self.eliminar_producto
    ).grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(
        frame_botones, text="Limpiar", command=self.limpiar_formulario
    ).grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

    columns = ("id", "nombre", "precio", "categoria")
    self.tree_productos = ttk.Treeview(
        frame_der, columns=columns, show="headings", height=15
    )
    self.tree_productos.heading("id", text="ID")
    self.tree_productos.heading("nombre", text="Nombre")
    self.tree_productos.heading("precio", text="Precio")
    self.tree_productos.heading("categoria", text="Categoría")

    self.tree_productos.column("id", width=60, anchor="center")
    self.tree_productos.column("nombre", width=150, anchor="w")
    self.tree_productos.column("precio", width=80, anchor="e")
    self.tree_productos.column("categoria", width=120, anchor="w")

    scrollbar = ttk.Scrollbar(
        frame_der, orient="vertical", command=self.tree_productos.yview
    )
    self.tree_productos.configure(yscrollcommand=scrollbar.set)
    self.tree_productos.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

  def _crear_seccion_usuarios(self, parent):
    frame_usuarios = ttk.LabelFrame(
        parent, text=" Usuarios Registrados en el Sistema ", padding=15
    )
    frame_usuarios.pack(fill="both", expand=True, padx=10, pady=10)

    columns = ("usuario", "rol")
    self.tree_usuarios = ttk.Treeview(
        frame_usuarios, columns=columns, show="headings", height=10
    )
    self.tree_usuarios.heading("usuario", text="Nombre de Usuario")
    self.tree_usuarios.heading("rol", text="Rol")
    self.tree_usuarios.column("usuario", width=250, anchor="w")
    self.tree_usuarios.column("rol", width=200, anchor="w")

    scrollbar = ttk.Scrollbar(
        frame_usuarios, orient="vertical", command=self.tree_usuarios.yview
    )
    self.tree_usuarios.configure(yscrollcommand=scrollbar.set)
    self.tree_usuarios.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

  def _crear_seccion_ventas(self, parent):
    frame_izq = ttk.LabelFrame(parent, text=" Registrar Nueva Venta ", padding=15)
    frame_izq.pack(side="left", fill="y", padx=10, pady=10)

    frame_der = ttk.LabelFrame(
        parent, text=" Historial de Ventas Registradas ", padding=15
    )
    frame_der.pack(side="right", fill="both", padx=10, pady=10, expand=True)

    # Selección de Usuario
    ttk.Label(frame_izq, text="Seleccionar Usuario:").pack(
        anchor="w", pady=5
    )
    self.combo_usuarios = ttk.Combobox(frame_izq, state="readonly", width=25)
    self.combo_usuarios.pack(pady=5)

    # Selección de Producto
    ttk.Label(frame_izq, text="Seleccionar Producto:").pack(
        anchor="w", pady=5
    )
    self.combo_productos = ttk.Combobox(frame_izq, state="readonly", width=25)
    self.combo_productos.pack(pady=5)

    # Botón asociado a command= ejecutando el callback de venta
    ttk.Button(
        frame_izq, text="Registrar Venta", command=self.callback_registrar_venta
    ).pack(pady=20, fill="x")

    # Tabla de Ventas (Treeview)
    columns = ("id_venta", "usuario", "producto", "fecha")
    self.tree_ventas = ttk.Treeview(
        frame_der, columns=columns, show="headings", height=12
    )
    self.tree_ventas.heading("id_venta", text="ID Venta")
    self.tree_ventas.heading("usuario", text="Usuario")
    self.tree_ventas.heading("producto", text="Producto")
    self.tree_ventas.heading("fecha", text="Fecha y Hora")

    self.tree_ventas.column("id_venta", width=70, anchor="center")
    self.tree_ventas.column("usuario", width=120, anchor="w")
    self.tree_ventas.column("producto", width=150, anchor="w")
    self.tree_ventas.column("fecha", width=140, anchor="center")

    scrollbar = ttk.Scrollbar(
        frame_der, orient="vertical", command=self.tree_ventas.yview
    )
    self.tree_ventas.configure(yscrollcommand=scrollbar.set)
    self.tree_ventas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

  def registrar_producto(self):
    id_p = self.txt_id.get().strip()
    nom = self.txt_nombre.get().strip()
    pre = self.txt_precio.get().strip()
    cat = self.txt_categoria.get().strip()

    if not id_p or not nom or not pre:
      messagebox.showwarning("Aviso", "Complete los campos obligatorios.")
      return

    try:
      p_float = float(pre)
    except ValueError:
      messagebox.showerror("Error", "El precio debe ser un número válido.")
      return

    if self.servicio.agregar_producto(id_p, nom, p_float, cat):
      messagebox.showinfo("Éxito", "Producto registrado correctamente.")
      self.cargar_productos()
      self.limpiar_formulario()
    else:
      messagebox.showerror("Error", "El ID del producto ya existe.")

  def consultar_producto(self):
    id_p = self.txt_id.get().strip()
    p = self.servicio.buscar_producto(id_p)
    if p:
      self.txt_nombre.delete(0, tk.END)
      self.txt_nombre.insert(0, p.nombre)
      self.txt_precio.delete(0, tk.END)
      self.txt_precio.insert(0, str(p.precio))
      self.txt_categoria.delete(0, tk.END)
      self.txt_categoria.insert(0, p.categoria)
    else:
      messagebox.showerror("No encontrado", "El producto especificado no existe.")

  def actualizar_producto(self):
    id_p = self.txt_id.get().strip()
    nom = self.txt_nombre.get().strip()
    pre = self.txt_precio.get().strip()
    cat = self.txt_categoria.get().strip()

    try:
      p_float = float(pre)
    except ValueError:
      messagebox.showerror("Error", "Precio inválido.")
      return

    if self.servicio.actualizar_producto(id_p, nom, p_float, cat):
      messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
      self.cargar_productos()
      self.limpiar_formulario()
    else:
      messagebox.showerror("Error", "No se pudo actualizar el producto.")

  def eliminar_producto(self):
    id_p = self.txt_id.get().strip()
    if messagebox.askyesno("Confirmar", "¿Desea eliminar este producto?"):
      if self.servicio.eliminar_producto(id_p):
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        self.cargar_productos()
        self.limpiar_formulario()
      else:
        messagebox.showerror("Error", "No se encontró el producto a eliminar.")

  def limpiar_formulario(self):
    self.txt_id.delete(0, tk.END)
    self.txt_nombre.delete(0, tk.END)
    self.txt_precio.delete(0, tk.END)
    self.txt_categoria.delete(0, tk.END)

  def cargar_productos(self):
    for item in self.tree_productos.get_children():
      self.tree_productos.delete(item)
    productos = self.servicio.obtener_productos()
    for p in productos:
      self.tree_productos.insert(
          "", "end", values=(p.id, p.nombre, p.precio, p.categoria)
      )

    # Actualizar combobox de ventas también
    self.combo_productos["values"] = [p.nombre for p in productos]

  def cargar_usuarios(self):
    for item in self.tree_usuarios.get_children():
      self.tree_usuarios.delete(item)
    usuarios = self.servicio.obtener_usuarios()
    for u in usuarios:
      self.tree_usuarios.insert("", "end", values=(u.usuario, u.rol))

    # Actualizar combobox de ventas también
    self.combo_usuarios["values"] = [u.usuario for u in usuarios]

  def callback_registrar_venta(self):
    """Callback exigido por la Semana 15 asociado mediante command="""
    usuario_sel = self.combo_usuarios.get()
    producto_sel = self.combo_productos.get()

    if not usuario_sel or not producto_sel:
      messagebox.showwarning(
          "Aviso", "Debe seleccionar un usuario y un producto."
      )
      return

    # Delegar la operación completamente al servicio
    exito = self.servicio.registrar_venta(usuario_sel, producto_sel)

    if exito:
      messagebox.showinfo("Éxito", "Venta registrada con éxito.")
      self.cargar_ventas()
      self.combo_usuarios.set("")
      self.combo_productos.set("")
    else:
      messagebox.showerror("Error", "No se pudo registrar la venta.")

  def cargar_ventas(self):
    for item in self.tree_ventas.get_children():
      self.tree_ventas.delete(item)
    for v in self.servicio.obtener_ventas():
      self.tree_ventas.insert(
          "", "end", values=(v.id_venta, v.usuario, v.producto, v.fecha)
      )