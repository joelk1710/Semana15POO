import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView


def main():
  servicio = RestauranteServicio()
  root = tk.Tk()
  root.title("Restaurante App")
  app = LoginView(root, servicio)
  root.mainloop()


if __name__ == "__main__":
  main()