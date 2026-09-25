# Changelog — 404_juego

## 2026-09-25 — Launcher GUI (`juego_gui.py`)
- Ventanita tkinter (plan B al navegador automático): puerto configurable,
  Iniciar/Detener servidor, URL visible, Abrir navegador, Copiar URL y log
  en vivo. Uso: `python juego_gui.py [--port 8000]`.
- No toca `Juego.py`: lo lanza como subproceso con `--no-browser`.

## 2026-09-25 — Juego funcional + doble pasillo

### Servidor (`Juego.py`)
- Sirve desde su propia carpeta (`BASE_DIR`): ya no se rompe al lanzarlo desde otro cwd.
- Nuevo `GET /api/ranking` (lee `ranking/scores.db`).
- `POST /save_ranking` robusto: valida `Content-Length`, JSON y campos
  `user` (máx. 32, sin saltos de línea) / `lvl` (1–10); códigos 400/403/411/413/500.
- Token CSRF de un solo uso (reuso → 403, verificado).
- Fallback de puerto 8000–8009 si el 8000 está ocupado; flags `--port`, `--no-browser`.
- `ThreadingTCPServer`, ruta absoluta de `scores.db`, crea `ranking/` si falta.
- Corrige append cuando `scores.db` no termina en `\n` (antes concatenaba y
  corrompía dos entradas en una línea).

### Frontend (`maze.html`)
- `winGame()` reconectado al servidor: `GET /get_token` → `POST /save_ranking`,
  con fallback a ranking local si no hay servidor.
- `updateRankingUI()` mezcla ranking del servidor + local.
- Base64 seguro UTF-8 (`btoa/atob` rompían con tildes/ñ/emoji).
- Colisión estricta: se eliminó el truco `onWall` que permitía atravesar muros.
- Enemigo: persecución en 4 direcciones (sin diagonales a través de muros),
  avanza 1 celda cada 2 pasos del jugador (antes igualaba tu velocidad y en
  pasillos de 1 celda era in-esquivable).
- `sanitizeLevel()`: failsafe que abre spawn/estrella/salida si un mapa viejo
  los trae en muro y reubica al enemigo a ruta válida.
- Celdas de camino ya no muestran el "0"; controles WASD además de flechas;
  guards ante JSON corrupto / `localStorage` dañado.

### Mapas (`json/nivel1..10.json`)
- Spawn `[1,1]` estaba en muro en los 10 niveles → abierto.
- Enemigo en `[7,7]` (muro, inmóvil) → reubicado a celdas libres y luego al
  punto medio del tramo estrella→salida de cada nivel.
- **Doble pasillo**: ruta ensanchada a 2 celdas + bypass tallado alrededor de
  cada enemigo (con el enemigo bloqueado, la salida sigue siendo alcanzable;
  verificado por BFS, bordes intactos).

### Generador (`dev/generador_nivel.py`)
- Marca la celda inicial al abrir caminos (el spawn ya no queda en muro).
- Pasillos de doble ancho, segunda ruta por el lado opuesto (loops),
  enemigo anclado a celda libre cercana al centro con bypass garantizado,
  reintentos con distinta aleatoriedad hasta pasar verificación BFS.
- Rutas con `BASE_DIR`: genera en `json/` correcto sin importar el cwd.
