# Geometry Dash Discord Widget Automator

Este repositorio contiene la estructura automatizada para extraer estadísticas de un jugador en Geometry Dash e integrarlas con un Widget de Discord, emulando la captura adjunta.

## Contenido del proyecto
1. **`gd_widget_layout.json`**: Este es el esquema o estructura del layout, equivalente a tu `layoutv2.json`. Asigna cada sección visual (estrellas, lunas, diamantes, etc.) a un nombre de variable. Sube este JSON al "Developer Portal" de Discord en la configuración de la UI de tu app (si usas Widgets/Linked roles).
2. **`update_stats.py`**: El script que descarga en tiempo real las estadísticas desde `gdbrowser.com` y crea un `current_gd_stats.json`.
3. **`.github/workflows/update-widget.yml`**: La automatización (GitHub Action) programada para ejecutarse cada hora.

## Cómo implementarlo en tu GitHub
1. Descomprime los archivos.
2. Súbelos a un nuevo repositorio vacío en tu cuenta de GitHub.
3. Dirígete a la pestaña **Actions** en el repositorio y asegúrate de aceptar el aviso *"I understand my workflows, go ahead and enable them"*.
4. A partir de ahora, cada hora, GitHub ejecutará el archivo Python actualizando `current_gd_stats.json` dentro de tu repositorio automáticamente.
