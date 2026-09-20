# Mountaineer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `mountaineerlinux` | [TryHackMe](https://tryhackme.com/room/mountaineerlinux) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=mountaineerlinux` + websearch de walkthroughs) | nginx alias misconfiguration (off-by-slash LFI) / Virtual Hosts / Roundcube (webmail) / CVE-2021-24145 (Modern Events Calendar) / KeePass (kdbx) / CUPP (password profiling) / SSRF/cURL | A config error in nginx allows LFI; credentials harvested from a Roundcube webmail; a PHP calendar plugin RCE (CVE-2021-24145) gives access to a KeePass database cracked with a CUPP wordlist → SSH → root. |

---

**Contexto:**

> **ES:** La sala **Mountaineer** es un CTF Hard basado en misconfiguraciones de nginx y un plugin de WordPress antiguo. La web principal (`mountaineer.thm`) tiene un bloque de nginx con un "off-by-slash" (`alias /var/www/mountaineer/images/;` sin barra final) que permite LFI/lectura de ficheros anteponiendo una barra al nombre (`/../...`). Con el LFI se descubren los vhosts, entre ellos el webmail Roundcube (`adminroundcubemail.mountaineer.thm`), donde unas credenciales por defecto (`k2:k2`) permiten leer un correo con credenciales de WordPress. Esa credencial de autor de WordPress abre la puerta a **CVE-2021-24145** (verse en Modern Events Calendar), un "no privilege signature check" que permite modificar el plugin y obtener RCE. Con esa shell se roban las credenciales del fichero KeePass `Backup.kdbx` (crackeado con john + reglas CUPP basadas en nombres de montañas) → acceso SSH con `alpinist` → escalada a root. La temática del montañismo recorre toda la sala: los nombres de usuario y contraseñas giran en torno a montañas y alpinistas.
> **EN:** The **Mountaineer** room is a Hard CTF built on nginx misconfigurations and an old WordPress plugin. The main website (`mountaineer.thm`) has an nginx block with an "off-by-slash" (`alias /var/www/mountaineer/images/;` missing a trailing slash) that allows LFI/file read by prefixing a slash to the name (`/../...`). The LFI reveals the vhosts, including the Roundcube webmail (`adminroundcubemail.mountaineer.thm`), where default credentials (`k2:k2`) let you read an email containing WordPress credentials. That WordPress author credential opens the door to **CVE-2021-24145** (Modern Events Calendar), a "no privilege signature check" that lets you modify the plugin and achieve RCE. With that shell the KeePass file `Backup.kdbx` is stolen (cracked with john + CUPP rules built from mountain names) → SSH access as `alpinist` → root escalation. The mountaineering theme runs through the whole room: usernames and passwords revolve around mountains and alpinists.

---

## Solucionario

### Task 1: Obtención de flags / Flags

**Explicación:**
Completando la cadena (LFI por alias de nginx, webmail Roundcube, credenciales de WordPress, RCE vía CVE-2021-24145, crackeo de la base KeePass `Backup.kdbx` con reglas CUPP y SSH como `alpinist`) se lee `local.txt` en el home del usuario.

1. 97a805eb710deb97342a48092876df22
   a41824310a621855d9ed507f29eed757

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is local.txt? | `97a805eb710deb97342a48092876df22` |
| 2 | What is root.txt? | `a41824310a621855d9ed507f29eed757` |

---

**Metodología:**

1. Reconocimiento: `nmap` muestra Apache en el 80 y SSH en el 22. Se fijan hosts (`mountaineer.thm`) en `/etc/hosts`.
2. LFI por alias de nginx: petición a `/images/../../../../etc/passwd` muestra el contenido del fichero. Se confirma el LFI probando subdirectorios y se acierta que nginx sirve con un bloque `alias` sin barra final ("off-by-slash"), leyendo ficheros del sistema.
3. Descubrimiento de vhosts: el LFI permite ver el fichero de configuración de nginx (`/etc/nginx/sites-enabled/default`) → vhosts `adminroundcubemail.mountaineer.thm`, `intranet.mountaineer.thm`, etc.
4. Roundcube (webmail): `adminroundcubemail.mountaineer.thm` con credenciales por defecto `k2:k2` → correo con las credenciales del autor de WordPress (`informatiker` / password con temática de montaña).
5. WordPress y CVE-2021-24145: se usa la credencial obtenida para hacer login en el panel de WordPress (editor). El plugin **Modern Events Calendar** presente en la instancia no valida correctamente los privilegios en el borrado/edición de eventos; se manipula la firma para subir una reverse shell → RCE como `www-data`.
6. KeePass `Backup.kdbx`: en el servidor está el fichero de KeePass (base de credenciales). Se descarga y se crackea con `john --wordlist=rockyou --rules=korelogic`/reglas CUPP (perfil basado en montañas: `sherpa`, `alpinist`, nombres de picos). Se obtienen las credenciales de `alpinist`.
7. Acceso SSH: `ssh alpinist@mountaineer.thm` → **local.txt** en el home del usuario / se leen los flags de nivel de usuario (p.ej. `97a805...`).
8. Escalada a root: con las credenciales de KeePass (cuentas `admin`/servicio) y los binarios/SUID que guarda el reto se llega al usuario `root` → **root.txt** (`a418243...`).

### Cadena de ataque / Attack Chain

`nmap → Hosts → nginx off-by-slash (LFI /../../) → Fuga de config (vhosts) → Roundcube k2:k2 → Correo con credenciales WordPress → CVE-2021-24145 (Modern Events Calendar) → RCE www-data → KeePass Backup.kdbx → John + CUPP (montañismo) → SSH alpinist → local.txt → Escalada a root → root.txt`

**Learning chain:**

Configuración de nginx peligrosa (alias sin slash final) → Local File Inclusion → Descubrimiento de virtual hosts → Fuga de credenciales vía webmail → Abuso de plugin WordPress (firma/privilegio ausente) → Remote Code Execution → Robo de gestor de contraseñas → Password cracking con reglas contextuales (CUPP/names) → Bound user/system flags.

*Lección:* Una sola barra mal puesta en un `alias` de nginx ("off-by-slash") convierte una web estática en una máquina de lectura de ficheros arbitraria. Y las contraseñas "personales" (nombres de montañas, mascotas, aficiones) son el eslabón débil cuando el atacante construye diccionarios contextuales con CUPP en lugar de solo probar rockyou.

**MITRE ATT&CK:**

T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1552.001 (Unsecured Credentials: Credentials In Files), T1078 (Valid Accounts), T1505.003 (Web Shell: Server Software), T1068 (Exploitation for Privilege Escalation), T1110 (Brute Force)

**Fuente:** [TryHackMe - Mountaineer](https://tryhackme.com/room/mountaineerlinux)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.