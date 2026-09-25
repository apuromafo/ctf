# Echo Pwn Maze — 404_juego

Mini-juego web estilo TryHackMe: guía a Echo por 10 nodos (laberintos), recoge la
estrella (overdrive), esquiva el firewall y llega a la salida. Al completar el
nivel 10 entras al ranking (`ranking/scores.db`, entradas en Base64).

## Requisitos

- Python 3.8+ (solo librería estándar)
- Navegador moderno

## Cómo jugar

```bash
cd 404_juego
python Juego.py            # abre el navegador solo
python juego_gui.py        # ventanita launcher (tkinter): iniciar/detener, URL, log
```

Abre `http://localhost:8000/maze.html` (si el 8000 está ocupado, prueba
8001–8009 automáticamente y lo indica en consola).

| Opción | Efecto |
|---|---|
| `python Juego.py --port 8123` | Puerto inicial distinto |
| `python Juego.py --no-browser` | No abre el navegador solo |

Controles: **flechas** o **WASD**.

## Mecánica

1. Atraviesa el laberinto del nivel 1 al 10.
2. La **estrella** da OVERDRIVE (8 s de inmunidad + atraviesas muros).
3. El **firewall** (triángulo) te persigue a mitad de tu velocidad; si te toca
   sin inmunidad, reinicia el nivel. Siempre hay doble pasillo / bypass para
   rodearlo.
4. Al salir del nivel 10, ingresa tu alias: se guarda en el ranking del
   servidor **y** en local (`localStorage`, clave `pwn_scores`).

## Estructura

```
404_juego/
├── Juego.py              Servidor + API de ranking
├── juego_gui.py          Launcher con GUI (tkinter, plan B al navegador)
├── maze.html             Juego (frontend, sin dependencias)
├── json/nivel1..10.json  Mapas: spawn, exit, star, enemy_spawn, maze (0=libre, 1=muro)
├── personaje/            Sprites SVG (echo, villano, estrella, meta)
├── ranking/scores.db     Ranking: una entrada Base64 por línea
├── dev/
│   ├── generador_nivel.py  Regenera los 10 mapas (doble pasillo + bypass)
│   └── genera_personaje.py Regenera los SVG
├── README.md
└── CHANGELOG.md
```

## API del servidor

| Endpoint | Método | Descripción |
|---|---|---|
| `/maze.html`, `/json/*`, `/personaje/*` | GET | Archivos estáticos |
| `/get_token` | GET | `{"csrf_token": "..."}` (un solo uso) |
| `/save_ranking` | POST | `{"user","lvl","csrf_token"}` → `200 OK` / `403` si el token es inválido o reused |
| `/api/ranking` | GET | `{"scores": ["<b64>", ...]}` |

Formato de entrada del ranking (antes de Base64):

```
2026-01-08 - User: Apuromafo - Lvl: 10
```

## Notas de diseño

- Los mapas garantizan: spawn/estrella/salida/enemigo en celdas libres,
  ruta completa conectada, pasillos de 2 celdas y bypass alrededor del
  enemigo (verificado por BFS en el generador).
- El frontend funciona standalone (doble clic a `maze.html` usa solo ranking
  local) o contra `Juego.py` (ranking persistente en servidor).
- `pwn_scores` en `localStorage` guarda las entradas ya codificadas en
  Base64, igual que `scores.db`.
