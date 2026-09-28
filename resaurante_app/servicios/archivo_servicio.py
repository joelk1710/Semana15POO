import json
import os


class ArchivoServicio:

  def cargar_json(self, ruta):
    if not os.path.exists(ruta):
      os.makedirs(os.path.dirname(ruta), exist_ok=True)
      with open(ruta, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
      return []

    try:
      with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
    except Exception:
      return []

  def guardar_json(self, ruta, datos):
    try:
      os.makedirs(os.path.dirname(ruta), exist_ok=True)
      with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
      return True
    except Exception:
      return False