# Motunui

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `motunui` | [TryHackMe](https://tryhackme.com/room/motunui) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=motunui` + websearch de walkthroughs) | SMB / pcapng (Wireshark) / API REST (v1/v2) / Cron jobs / OS Command Injection / Reutilización de credenciales / Cisco Packet Tracer (pkt) | Enumeración del share SMB → análisis de tráfico en pcapng → abuso de la API (login + jobs) → reverse shell como www-data → credenciales reutilizadas (SSH moana) → escalada a root vía credenciales en tráfico capturado. |

---

**Contexto:**

> **ES:** La sala **Motunui** es un CTF Hard que combina análisis de tráfico (Wireshark) con explotación de una API. Se parte de una máquina con SMB de acceso anónimo; en el share `traces` hay ficheros `.pcapng` que muestran el tráfico de una aplicación de sondeos ("surveys") y de una herramienta de subida de imágenes. De ahí se obtiene el subdominio `d3v3lopm3nt.motunui.thm` y, tras explorar `/docs`, una API en `api.motunui.thm:3000` con endpoints `/v1/login` y `/v2/jobs`. El nombre de la sala rinde homenaje a la aldea ficticia de la película **Moana**; la flag de usuario y la de root están relacionadas con los personajes: `m0an4_0f_M0tunu1` (Moana de Motunui) y `h34rT_r35T0r3d` (the heart restored, "el corazón restaurado", en alusión al corazón de Te Fiti que Moana devuelve).
> **EN:** The **Motunui** room is a Hard CTF that combines traffic analysis (Wireshark) with API exploitation. It starts from a machine with anonymous SMB access; the `traces` share holds `.pcapng` files showing the traffic of a "surveys" application and an image-upload tool. From there you obtain the `d3v3lopm3nt.motunui.thm` subdomain and, after checking `/docs`, an API at `api.motunui.thm:3000` with the `/v1/login` and `/v2/jobs` endpoints. The room name pays homage to the fictional village from the movie **Moana**; both flags reference the characters: `m0an4_0f_M0tunu1` (Moana of Motunui) and `h34rT_r35T0r3d` (the heart restored, echoing the heart of Te Fiti that Moana returns).

---

## Solucionario

### Task 1: Obtención de flags / Flags

**Explicación:**
Tras comprometer la API (credencial leak en `/v1/login`, command injection en el endpoint `/v2/jobs` con un cron job) se obtiene una reverse shell como `www-data`. Leyendo `read_me.md` del usuario `moana` junto con el fichero `network.pkt` (Cisco Packet Tracer) se reutilizan credenciales para acceder por SSH como `moana` → flag de usuario. La flag root se encuentra tras capturar el tráfico de la propia escalada: al intentar leer `/root/root.txt` como `www-data` uno visualiza en el pcap del tráfico HTTP el intercambio con el que `moana` consigue root.

1. THM{m0an4_0f_M0tunu1}
   THM{h34rT_r35T0r3d}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{m0an4_0f_M0tunu1}` |
| 2 | What is the root flag? | `THM{h34rT_r35T0r3d}` |

---

**Metodología:**

1. Enumeración de servicios: `nmap` revela SMB abierto a anónimo. Con `smbclient -N -L` se listan los shares y en el share `traces` se descargan los ficheros `.pcapng`.
2. Análisis de tráfico (Wireshark): los subdominios `d3v3lopm3nt.motunui.thm`, `api.motunui.thm` y el host `motunui.thm` aparecen en el tráfico HTTP. Un `dashboard.png` permite cerrar con `192.168.x.x` y el checkbox de "upload image" apuntan al desarrollo de una app.
3. Subdominio de desarrollo: `d3v3lopm3nt.motunui.thm` → panel de login de desarrollo con caption "The development under motunui" y referencia a `/docs`.
4. Documentación de la API (`api.motunui.thm:3000/docs`): endpoints `/v1/login` (POST `email`/`password`) y `/v2/jobs` (POST `image` + `script` que se ejecuta vía cron).
5. Fuerza bruta del login: `wfuzz` contra `/v1/login` con el email `maui` y una wordlist de contraseñas → solo tiene éxito `island`. La respuesta incluye un token/hash que se usa para autenticarse.
6. Command injection en `/v2/jobs`: con el token autenticado, el parámetro `script` permite inyectar comandos en el cron que procesa las imágenes. Se sube una reverse shell → conexión como `www-data`.
7. Credenciales reutilizadas: leyendo el home de `moana` se encuentra `read_me.md` y el fichero `network.pkt` (proyecto de Cisco Packet Tracer) con credenciales de red; con esas credenciales se conecta por SSH como `moana` → **user flag** en `/home/moana/user.txt`.
8. Escalada a root: monitorizando el tráfico con `tcpdump`/Wireshark se captura cómo `moana` alcanza `root` sobre HTTP; las credenciales/cookies vistas en ese pcap permiten replicar el acceso → **root flag**.

### Cadena de ataque / Attack Chain

`SMB anónimo → share traces (pcapng) → Análisis de tráfico → Subdominio d3v3lopm3nt → /docs (API) → /v1/login (credencial leak + wfuzz) → token → /v2/jobs (command injection vía cron) → Reverse shell www-data → Credenciales reutilizadas (network.pkt) → SSH moana → User flag → Captura de tráfico HTTP → Root flag`

**Learning chain:**

Enumeración SMB → Análisis de capturas pcapng → Descubrimiento de subdominios y APIs a partir de tráfico → Fuerza bruta de endpoints de login → Abuso de endpoints con cron jobs → Inyección de comandos → Reutilización de credenciales embebidas en artefactos (Packet Tracer) → Captura pasiva de tráfico para escalar privilegios.

*Lección:* La información vive en múltiples sitios a la vez: un share SMB escondía capturas de red que desvelaban la aplicación; la documentación de la API reveló endpoints abiertos; y la propia solución de escalada estaba "en el cable". Antes de romper nada, conviene enumerar y analizar el tráfico existente, porque las credenciales suelen reutilizarse en SSH, en la API y en el propio análisis del reto.

**MITRE ATT&CK:**

T1083 (File and Directory Discovery), T1040 (Network Sniffing), T1133 (External Remote Services), T1505.003 (Web Shell: Server Software), T1059.006 (Command and Scripting Interpreter: Python), T1053.003 (Scheduled Task/Job: Cron), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Motunui](https://tryhackme.com/room/motunui)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.