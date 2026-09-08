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

**Explicación:** La máquina en sí es el reto: capturar banderas (archivos) y conseguir root. No hay campo de respuesta donde enviar flags. En modo King of the Hill compites contra otros jugadores por el control del mismo host; el objetivo es rootear y mantenerte con el control de `/root/king.txt` el mayor tiempo posible. El puerto 9999 responde `king` como respuesta HTTP: es parte de la infraestructura de King of the Hill y **NUNCA** debe tocarse ni explotarse.

**Metodología:**
1. **Reconocimiento:** `nmap -sV -p-` revela 5 puertos: 22 (OpenSSH 7.6p1), 3306 (MySQL 5.7.29), 9999 (servicio KoTH `king`, infraestructura del juego, NO se toca), 15065 (HTTP Golang "Host monitoring"), 16109 (imagen JPEG) y 46969 (Telnet).
2. **Vector A — RCE web en :15065 → `bread`:** la web "Host monitoring" muestra "site down"; `gobuster` encuentra `/monitor` (interfaz "ping host"); el JS está ofuscado y en DevTools se revela `POST /api/cmd`, cuyo body se ejecuta como comando. `curl -X POST http://<IP>:15065/api/cmd -d "whoami"` da RCE; foothold estable inyectando tu clave en `/home/bread/.ssh/authorized_keys`.
3. **Vector B — MySQL :3306 → `ramen`:** credenciales por defecto `root:root`; DB `users` → tabla `User` → `ramen:noodlesRTheBest` (SSH).
4. **Vector C — Stego en :16109 → `pasta`:** `binwalk -e` (gzip→tar→`creds.txt`) o `steghide --extract` → `pasta:pastaisdynamic` (SSH).
5. **Vector D — Telnet :46969 → `food`:** el banner tiene el gretting desplazado en ROT-13/ROT-14 → `food:givemecookies`.
6. **Escalada a root:** `find / -uid 0 -perm -4000 -type f` localiza dos SUID: `/usr/bin/screen-4.5.0` (GNU Screen "screenroot", Exploit-DB 41154: compilar `libhax.c` + `rootshell.c`, subirlos por HTTP y ejecutar el disparador) y `/usr/bin/vim.basic` (editar `/etc/passwd` añadiendo un usuario UID 0). Alternativas: sudo CVE-2019-18634 (PoC saleemrashid) y CVE-2021-4034 (PwnKit/pkexec, PoC arthepsy).
7. **KoTH — Convertirse en King:** `echo "<TU_USUARIO_THM>" > /root/king.txt`; el servicio `:9999` lo lee y acredita ~10 pts/min. Defensa: bucle `while true; do echo <alias> > /root/king.txt; sleep 0.1; done &`, inmutabilidad `chattr +i /root/king.txt` (con tu propio binario `chattr`) y backdoors múltiples (clave en `/root/.ssh/authorized_keys`, shells SUID, usuario UID 0 en `/etc/passwd`).
8. **Banderas:** las flags son archivos del sistema (sin campo de envío); ubicaciones típicas: `/root/flag`, `/root/.profile`, `/root/.mysql_history`, `/home/bread/flag`, `/home/food/.flag`, `/var/flag.txt`, `/var/log/auth.log` y la tabla `users.User`. Valores `THM{...}` varían por instancia.

#### Detalle de los vectores de intrusión

**Vector A — RCE web en :15065 → usuario `bread`:**
- La web "Host monitoring" muestra "site down/maintenance". `gobuster` encuentra `/monitor` (interfaz "ping host").
- El JS frontal está ofuscado; en DevTools se revela el endpoint `POST /api/cmd`, cuyo body se ejecuta como comando.
- **RCE como `bread`:** `curl -X POST http://<IP>:15065/api/cmd -d "whoami"` → ejecuta comandos arbitrarios.
- Foothold estable: reverse shell o inyectar tu clave en `/home/bread/.ssh/authorized_keys`.

**Vector B — MySQL :3306 → usuario `ramen`:**
- Credenciales por defecto `root:root` (funcionan en este MySQL antiguo).
- DB `users` → tabla `User` → `select * from User` → credencial `ramen:noodlesRTheBest` (SSH).

**Vector C — Stego en :16109 → usuario `pasta`:**
- La imagen JPEG se analiza con `binwalk -e` (extrae gzip→tar→`creds.txt`) o `steghide --extract` → credenciales → `pasta:pastaisdynamic` (SSH).

**Vector D — Telnet :46969 → usuario `food`:**
- El banner de telnet tiene el gretting desplazado (ROT-13/ROT-14) → `food:givemecookies`.

#### Escalada a root (SUID + CVEs)

`find / -uid 0 -perm -4000 -type f 2>/dev/null` → dos binarios SUID instalados manualmente:

- **`/usr/bin/screen-4.5.0`** (SUID) → **GNU Screen "screenroot"** — [Exploit-DB 41154](https://www.exploit-db.com/exploits/41154). Compilar `libhax.c` + `rootshell.c` en local, subirlos por HTTP y ejecutar el disparador de `screen` → shell root.
- **`/usr/bin/vim.basic`** (SUID) → editar `/etc/passwd` y añadir un usuario UID 0 de backdoor (ej. `hacker:<hash>:0:0:/root:/bin/bash`) → `su hacker`.

Vías alternativas según la imagen desplegada (parcheada o no):
- **Sudo CVE-2019-18634** (PWFEEDBACK con asteriscos): PoC de saleemrashid → root.
- **CVE-2021-4034 (PwnKit/pkexec)**: PoC de arthepsy → root directo en kernels sin parchear (2022).

#### KoTH — Convertirse en King

Una vez root:
```
echo "<TU_USUARIO_THM>" > /root/king.txt
```
El servicio `:9999` lee ese archivo y te acredita los puntos (~10 pts por minuto que mantengas el control). Defensa recomendada: bucle `while true; do echo <alias> > /root/king.txt; sleep 0.1; done &`, inmutabilidad `chattr +i /root/king.txt` (con binario `chattr` propio copiado, los rivales lo borran), y backdoors múltiples (clave en `/root/.ssh/authorized_keys`, shells SUID, usuario UID 0 en `/etc/passwd`).

#### Banderas

Las flags de esta sala son **archivos en el sistema** (los walkthroughs públicos y el propio creador las redactan a propósito; no hay campo de envío). Ubicaciones típicas observadas: `/root/flag`, `/root/.profile`, `/root/.mysql_history`, `/home/bread/flag`, `/home/food/.flag`, `/var/flag.txt`, `/var/log/auth.log` y la tabla `users.User` (columna `flag`). Los valores son `THM{...}` pero varían por instancia desplegada.

```
Recon (nmap -sV -p-): 22, 3306, 9999(king), 15065, 16109, 46969
        |
        +-- RCE :15065 /api/cmd ---------------> user bread
        +-- MySQL root:root --> ramen:noodlesRTheBest -> user ramen
        +-- Stego :16109 (binwalk/steghide) ----> user pasta
        +-- Telnet :46969 rot13 ----------------> user food
        |
        v
PrivEsc: SUID screen-4.5.0 (EDB 41154) o SUID vim.basic
        |  o  sudo CVE-2019-18634 / pkexec CVE-2021-4034
        v
root shell --> echo <algo> > /root/king.txt  (King del cerro)
        |
        v
Patching/defensa: chattr +i, loops king, backdoors múltiples
```

**Lección:** En KoTH se combinan ataque y defensa: rootear rápido, asegurar el control (*king.txt*), y proteger los accesos con múltiples mecanismos mientras el enemigo intenta revertirlos. El puerto 9999 es infraestructura: nunca debe alterarse.

**Referencias:** [Official creator (NinjaJc01)](https://jc01.ninja/ctf/foodctf/) · [ChrisPritchard (GitHub)](https://github.com/ChrisPritchard/ctf-writeups/tree/master/tryhackme-koth) · [thomas-osgood (GitHub)](https://github.com/thomas-osgood/TryHackMe/tree/main/KoTH_Food_CTF) · [divu050704](https://divu050704.github.io/blog/tryhackme/koth-food-ctf) · [hellfire0x01](https://hellfire0x01.github.io/posts/KoTH-Food-CTF/) · [m3n0sd0n4ld](https://m3n0sd0n4ld.github.io/patoHackventuras/KoTH-Food-CTF) · [YouTube walkthrough](https://www.youtube.com/watch?v=cC7lGr_41xc) · [Guide To King of the Hill (blog oficial)](https://tryhackme.com/resources/blog/guide-to-king-of-the-hill)

**Learning chain:** Recon (nmap -sV -p-) → 4 vectores de intrusión (RCE /api/cmd, MySQL root:root, stego JPEG, Telnet ROT13) → users bread/ramen/pasta/food → PrivEsc SUID screen-4.5.0/vim.basic o PwnKit → root → /root/king.txt → patching y defensa del cerro

**MITRE ATT&CK:** T1046 (Network Service Scanning), T1190 (Exploit Public-Facing Application), T1210 (Exploitation of Remote Services), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - KoTH Food CTF](https://tryhackme.com/room/kothfoodctf)
