# KoTH Food CTF [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF — King of the Hill (KoTH) (Free Room)
* **Slug:** `kothfoodctf`
* **Link:** https://tryhackme.com/room/kothfoodctf
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** [jc01.ninja (writeup del creador NinjaJc01)](https://jc01.ninja/ctf/foodctf/) + ChrisPritchard (GitHub), thomas-osgood (GitHub), divu050704, hellfire0x01, m3n0sd0n4ld

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de competición **King of the Hill (KoTH)** para practicar el modo de juego: te enfrentas a otros jugadores por el control de una máquina Linux (Ubuntu 18.04). El objetivo NO es responder preguntas en la interfaz, sino **rootear la máquina** y mantenerte como *King* el mayor tiempo posible (el sistema de KoTH lee tu alias desde `/root/king.txt` vía el servicio del puerto 9999).
> **EN:** **King of the Hill (KoTH)** practice room for the competitive game mode: you face other players fighting for control of a Linux machine (Ubuntu 18.04). The goal is NOT to answer dashboard questions but to **root the box** and stay *King* as long as possible (the KoTH system reads your alias from `/root/king.txt` through the port 9999 service).

### Task 1 - No answer needed

> **ES:** La máquina en sí es el reto: capturar banderas (archivos) y conseguir root. No hay campo de respuesta donde enviar flags.
> **EN:** The machine itself is the challenge: capture flags (files) and reach root. There is no answer field to submit flags.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| 1. No answer needed | `No answer needed` |

## Metodología / Methodology

### 1. Reconocimiento / Recon

`nmap -sV -p- <IP>` → **5 puertos abiertos** (verificado por el writeup oficial del creador y varios walkthroughs):

| Puerto / Port | Servicio / Service |
|---|---|
| 22/tcp | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 |
| 3306/tcp | MySQL 5.7.29 |
| 9999/tcp | **Servicio KoTH `king` (infraestructura del juego — NO es un vector de ataque)** |
| 15065/tcp | Servidor HTTP en Golang ("Host monitoring") |
| 16109/tcp | Sirve una imagen JPEG |
| 46969/tcp | Telnet (Linux telnetd) |

> **ES:** El puerto 9999 responde `king` como respuesta HTTP. Es parte de la infraestructura de King of the Hill y NO se debe tocar ni explotar.
> **EN:** Port 9999 answers `king` as an HTTP response. It is part of the King of the Hill infrastructure and must NOT be touched or exploited.

### 2. Vectores de intrusión / Intrusion vectors (4 cuentas)

**Vector A — RCE web en :15065 → usuario `bread`**
- La web "Host monitoring" muestra "site down/maintenance". `gobuster` encuentra `/monitor` (interfaz "ping host").
- El JS frontal está ofuscado; en DevTools se revela el endpoint `POST /api/cmd`, cuyo body se ejecuta como comando.
- **RCE como `bread`:** `curl -X POST http://<IP>:15065/api/cmd -d "whoami"` → ejecuta comandos arbitrarios.
- Foothold estable: reverse shell o inyectar tu clave en `/home/bread/.ssh/authorized_keys`.

**Vector B — MySQL :3306 → usuario `ramen`**
- Credenciales por defecto `root:root` (funcionan en este MySQL antiguo).
- DB `users` → tabla `User` → `select * from User` → credencial `ramen:noodlesRTheBest` (SSH).

**Vector C — Stego en :16109 → usuario `pasta`**
- La imagen JPEG se analiza con `binwalk -e` (extrae gzip→tar→`creds.txt`) o `steghide --extract` → credenciales → `pasta:pastaisdynamic` (SSH).

**Vector D — Telnet :46969 → usuario `food`**
- El banner de telnet tiene el gretting desplazado (ROT-13/ROT-14) → `food:givemecookies`.

### 3. Escalada a root / Privilege escalation (SUID + CVEs)

`find / -uid 0 -perm -4000 -type f 2>/dev/null` → dos binarios SUID instalados manualmente:

- **`/usr/bin/screen-4.5.0`** (SUID) → **GNU Screen "screenroot"** — [Exploit-DB 41154](https://www.exploit-db.com/exploits/41154). Compilar `libhax.c` + `rootshell.c` en local, subirlos por HTTP y ejecutar el disparador de `screen` → shell root.
- **`/usr/bin/vim.basic`** (SUID) → editar `/etc/passwd` y añadir un usuario UID 0 de backdoor (ej. `hacker:<hash>:0:0:/root:/bin/bash`) → `su hacker`.

Vías alternativas según la imagen desplegada (parcheada o no):
- **Sudo CVE-2019-18634** (PWFEEDBACK con asteriscos): PoC de saleemrashid → root.
- **CVE-2021-4034 (PwnKit/pkexec)**: PoC de arthepsy → root directo en kernels sin parchear (2022).

### 4. KoTH — Convertirse en King / Becoming King

> **ES:** Una vez root: `echo "<TU_USUARIO_THM>" > /root/king.txt` → el servicio `:9999` lee ese archivo y te acredita los puntos (~10 pts por minuto que mantengas el control). Defensa recomendada: bucle `while true; do echo <alias> > /root/king.txt; sleep 0.1; done &`, inmutabilidad `chattr +i /root/king.txt` (con binario `chattr` propio copiado, los rivales lo borran), y backdoors múltiples (clave en `/root/.ssh/authorized_keys`, shells SUID, usuario UID 0 en `/etc/passwd`).
> **EN:** Once root: `echo "<YOUR_THM_USERNAME>" > /root/king.txt` → the `:9999` service reads that file and credits you (~10 points per minute you hold it). Recommended defense: `while true; do echo <alias> > /root/king.txt; sleep 0.1; done &`, immutability `chattr +i /root/king.txt` (keep your own `chattr` copy — rivals delete it), and multiple backdoors (key in `/root/.ssh/authorized_keys`, SUID shells, UID-0 user in `/etc/passwd`).

### 5. Banderas / Flags

> **ES:** Las flags de esta sala son **archivos en el sistema** (los walkthroughs públicos y el propio creador las redactan a propósito; no hay campo de envío). Ubicaciones típicas observadas: `/root/flag`, `/root/.profile`, `/root/.mysql_history`, `/home/bread/flag`, `/home/food/.flag`, `/var/flag.txt`, `/var/log/auth.log` y la tabla `users.User` (columna `flag`). Los valores son `THM{...}` pero varían por instancia desplegada.
> **EN:** This room's flags are **files on the system** (public walkthroughs and the creator himself deliberately redact them; there is no submission field). Typical observed locations: `/root/flag`, `/root/.profile`, `/root/.mysql_history`, `/home/bread/flag`, `/home/food/.flag`, `/var/flag.txt`, `/var/log/auth.log` and the `users.User` table (`flag` column). Values are `THM{...}` but vary per deployed instance.

## Cadena de ataque / Attack Chain

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

## Referencias / References

- **Official creator (NinjaJc01):** [THM - KoTH Food CTF](https://jc01.ninja/ctf/foodctf/)
- **ChrisPritchard (GitHub):** [ctf-writeups — tryhackme-koth (kill sheet Food + guía KoTH)](https://github.com/ChrisPritchard/ctf-writeups/tree/master/tryhackme-koth)
- **thomas-osgood (GitHub):** [TryHackMe/KoTH_Food_CTF (RCE scripts)](https://github.com/thomas-osgood/TryHackMe/tree/main/KoTH_Food_CTF)
- **divu050704:** [KoTH Food CTF](https://divu050704.github.io/blog/tryhackme/koth-food-ctf)
- **hellfire0x01:** [KoTH Food CTF](https://hellfire0x01.github.io/posts/KoTH-Food-CTF/)
- **m3n0sd0n4ld:** [KoTH-Food-CTF Writeup](https://m3n0sd0n4ld.github.io/patoHackventuras/KoTH-Food-CTF)
- **YouTube:** [KoTH Food CTF walkthrough](https://www.youtube.com/watch?v=cC7lGr_41xc)
- **Referencia de reglas KoTH:** [Guide To King of the Hill (blog oficial)](https://tryhackme.com/resources/blog/guide-to-king-of-the-hill)

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.