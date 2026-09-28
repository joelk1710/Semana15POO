import tkinter as tk
from tkinter import messagebox, ttk
from ui.main_view import MainView


class LoginView:

  def __init__(self, root, servicio):
    self.root = root
    self.root.title("Restaurante App - Login")
    self.root.geometry("400x300")
    self.root.resizable(False, False)
    self.servicio = servicio
    self._crear_widgets()

  def _crear_widgets(self):
    frame = ttk.LabelFrame(self.root, text=" Acceso al Sistema ", padding=20)
    frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=220)

    ttk.Label(frame, text="Usuario:").pack(anchor="w", pady=2)
    self.txt_user = ttk.Entry(frame, width=30)
    self.txt_user.pack(pady=5)

    ttk.Label(frame, text="Contraseña:").pack(anchor="w", pady=2)
    self.txt_pass = ttk.Entry(frame, width=30, show="*")
    self.txt_pass.pack(pady=5)

    ttk.Button(frame, text="Ingresar", command=self.verificar_login).pack(
        pady=15, fill="x"
    )

  def verificar_login(self):
    user = self.txt_user.get().strip()
    pwd = self.txt_pass.get().strip()
    usuario_valido = self.servicio.validar_usuario(user, pwd)
    if usuario_valido:
      self.root.destroy()
      root_main = tk.Tk()
      MainView(root_main, self.servicio, usuario_valido)
      root_main.mainloop()
    else:
      messagebox.showerror(
          "Error", "Usuario o contraseña incorrectos (Prueba: admin / 123)"
      )