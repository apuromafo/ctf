# Personal Profile — TryHackMe

Scripts de perfil personal: seguimiento de progreso de salas gratuitas y descarga de la skill matrix.

## Estructura

```
Personal Profile/
├── .env                    # Cookie de sesión THM (NO se sube a git)
├── requirements.txt        # Dependencias de Python
├── README.md
├── Progreso/
│   ├── progress.py         # Progreso de salas gratuitas (gráfico + JSON)
│   ├── test_progress.py    # Pruebas unitarias de la carga de .env
│   └── progress_data_sorted.json / progreso_thm.png  # Salidas generadas
└── Skill Matrix/
    └── 00 download skill_matrix json.py  # Descarga skill matrix por segmento/rol
```

## Configuración

1. Crear el archivo `.env` en `Personal Profile/.env` con la cookie de sesión de TryHackMe:

   ```ini
   THM_CONNECT_SID=<tu connect.sid>
   ```

   La cookie se obtiene del navegador con la sesión iniciada (panel de desarrollador > Application > Cookies > `https://tryhackme.com`). Expira aproximadamente cada 24 horas.

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

> El archivo `.env` está excluido del repositorio mediante `.gitignore` (`/Tryhackme/Personal Profile/.env`). No se debe commitear.

## Uso

### Progreso de salas gratuitas (`Progreso/progress.py`)

Cuenta cuántas salas gratuitas has completado frente al total disponible y genera un gráfico de pastel y un JSON:

```bash
python "Progreso/progress.py"
```

Salidas:
- `progreso_thm.png` — gráfico (Completado / En Progreso / Sin Empezar)
- `progress_data_sorted.json` — detalle del progreso por sala

Opciones de código: `exclude_windows = True` en `fetch_free_rooms(...)` excluye salas con tag Windows.

### Tests

```bash
python "Progreso/test_progress.py"
```

## Skill Matrix (`Skill Matrix/00 download skill_matrix json.py`)

Descarga la aptitud de un usuario por segmento (`entry`, `junior`, `mid`, `senior`) y rol (`Foundational`, `Security Analyst`, `Penetration Tester`, `Security Engineer`). Requiere el mismo `.env`. Salida: `json/<segmento>_<rol>.json`.