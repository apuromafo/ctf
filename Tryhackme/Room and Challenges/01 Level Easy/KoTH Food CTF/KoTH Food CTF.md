# KoTH Food CTF

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `kothfoodctf` |
| **Link** | [TryHackMe](https://tryhackme.com/room/kothfoodctf) |
| **Sección** | 01 Level Easy |
| **Fuente** | [jc01.ninja (writeup del creador NinjaJc01)](https://jc01.ninja/ctf/foodctf/) + ChrisPritchard (GitHub), thomas-osgood (GitHub), divu050704, hellfire0x01, m3n0sd0n4ld |
| **Componentes** | nmap / gobuster / curl / MySQL / binwalk / steghide / telnet / SUID screen-4.5.0 / SUID vim.basic / PwnKit |
| **Impacto** | Rootear una máquina Ubuntu 18.04 en modo King of the Hill y mantenerte como King sobre /root/king.txt con backdoors múltiples |

---

**Contexto:** Sala de competición **King of the Hill (KoTH)** para practicar el modo de juego: te enfrentas a otros jugadores por el control de una máquina Linux (Ubuntu 18.04). El objetivo NO es responder preguntas en la interfaz, sino **rootear la máquina** y mantenerte como *King* el mayor tiempo posible (el sistema de KoTH lee tu alias desde `/root/king.txt` vía el servicio del puerto 9999).

## Solucionario

### Task 1: No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. **Reconocimiento:** `nmap -sV -p-` revela 5 puertos: 22 (OpenSSH), 3306 (MySQL 5.7.29), 9999 (servicio KoTH `king`, infraestructura del juego, NO se toca), 15065 (HTTP Golang "Host monitoring"), 16109 (imagen JPEG) y 46969 (Telnet).
2. **Vector A — RCE web en :15065 → `bread`:** la web "Host monitoring" muestra "site down"; `gobuster` encuentra `/monitor` (interfaz "ping host"); el JS está ofuscado y en DevTools se revela `POST /api/cmd`, cuyo body se ejecuta como comando. `curl -X POST http://<IP>:15065/api/cmd -d "whoami"` da RCE; foothold estable inyectando tu clave en `/home/bread/.ssh/authorized_keys`.
3. **Vector B — MySQL :3306 → `ramen`:** credenciales por defecto `root:root`; DB `users` → tabla `User` → `ramen:noodlesRTheBest` (SSH).
4. **Vector C — Stego en :16109 → `pasta`:** `binwalk -e` (gzip→tar→`creds.txt`) o `steghide --extract` → `pasta:pastaisdynamic` (SSH).
5. **Vector D — Telnet :46969 → `food`:** el banner tiene el gretting desplazado en ROT-13/ROT-14 → `food:givemecookies`.
6. **Escalada a root:** `find / -uid 0 -perm -4000 -type f` localiza dos SUID: `/usr/bin/screen-4.5.0` (GNU Screen "screenroot", Exploit-DB 41154: compilar `libhax.c` + `rootshell.c`, subirlos por HTTP y ejecutar el disparador) y `/usr/bin/vim.basic` (editar `/etc/passwd` añadiendo un usuario UID 0). Alternativas: sudo CVE-2019-18634 (PoC saleemrashid) y CVE-2021-4034 (PwnKit/pkexec, PoC arthepsy).
7. **KoTH — Convertirse en King:** `echo "<TU_USUARIO_THM>" > /root/king.txt`; el servicio `:9999` lo lee y acredita ~10 pts/min. Defensa: bucle `while true; do echo <alias> > /root/king.txt; sleep 0.1; done &`, inmutabilidad `chattr +i /root/king.txt` (con tu propio binario `chattr`) y backdoors múltiples (clave en `/root/.ssh/authorized_keys`, shells SUID, usuario UID 0 en `/etc/passwd`).
8. **Banderas:** las flags son archivos del sistema (sin campo de envío); ubicaciones típicas: `/root/flag`, `/root/.profile`, `/root/.mysql_history`, `/home/bread/flag`, `/home/food/.flag`, `/var/flag.txt`, `/var/log/auth.log` y la tabla `users.User`. Valores `THM{...}` varían por instancia.

**Learning chain:** Recon (nmap -sV -p-) → 4 vectores de intrusión (RCE /api/cmd, MySQL root:root, stego JPEG, Telnet ROT13) → users bread/ramen/pasta/food → PrivEsc SUID screen-4.5.0/vim.basic o PwnKit → root → /root/king.txt → patching y defensa del cerro

**MITRE ATT&CK:** T1046 (Network Service Scanning), T1190 (Exploit Public-Facing Application), T1210 (Exploitation of Remote Services), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - KoTH Food CTF](https://tryhackme.com/room/kothfoodctf)