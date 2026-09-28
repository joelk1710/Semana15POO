# Restaurante App - Semana 15 (Manejo de Eventos y Ventas)

## Propósito de la Actividad
Evolución de la aplicación aplicando los fundamentos de manejo de eventos en interfaces gráficas mediante Tkinter. Se incorpora una nueva sección de gestión de ventas que relaciona usuarios y productos utilizando enlaces de eventos con `command=` y callbacks, delegando la lógica de negocio y persistencia a la capa de servicios.

## Estructura del Proyecto
- `datos/`: Archivos de persistencia en formato JSON (`productos.json`, `usuarios.json`, `ventas.json`).
- `modelos/`: Clases de entidad (`producto.py`, `usuario.py`, `venta.py`).
- `servicios/`: Lógica de negocio y manejo de archivos (`archivo_servicio.py`, `restaurante_servicio.py`).
- `ui/`: Vistas de la aplicación (`login_view.py`, `main_view.py`).
- `assets/`: Recursos gráficos obligatorios, incluyendo el logotipo del sistema (`logo.png`).
- `main.py`: Punto de entrada de la aplicación.

## Flujo de Manejo de Eventos Implementado
1. El usuario interactúa seleccionando opciones en los componentes de la interfaz.
2. Al presionar el botón de registro, se activa el parámetro `command=` enlazado al callback correspondiente.
3. El callback recolecta los datos de la interfaz y los delega a `RestauranteServicio`.
4. El servicio valida, procesa y almacena la información de forma persistente en `ventas.json`.
5. La interfaz se actualiza de manera inmediata reflejando el resultado en un componente `Treeview`.

python main.py

Credenciales de acceso predeterminadas:
Usuario: admin
Contraseña: 123