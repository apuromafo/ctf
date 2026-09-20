# Internal

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `internal` | [TryHackMe](https://tryhackme.com/room/internal) | 03 Level Hard | TryHackMe | WordPress / CVE-2013-4547 (Nginx) / CMS password reset / Shell | Acceso completo a un servidor WordPress vulnerable, obteniendo una shell del sistema y la flag raíz mediante abuso del panel de administración y directorios ocultos. |

---

**Contexto:**

> **ES:** La sala **Internal** es un CTF de dificultad Hard. Se parte de un servidor web WordPress (Nginx) que en un directorio oculto (`/blog/wp-admin`) expone el panel de administración sin protección de autenticación. El proceso comienza con enumeración de directorios, identificación de la versión vulnerable de WordPress, acceso admin por la CVE conocida de Nginx (CVE-2013-4547), carga de un plugin/webshell, escalada al usuario `www-data` y finalmente pivote a root mediante una tarea de cron o binario SUID hasta leer la flag final. La flag de la máquina interna confirma el compromiso total del host.
> **EN:** The **Internal** room is a Hard-difficulty CTF. It starts from a WordPress (Nginx) web server that exposes the admin panel (`/blog/wp-admin`) in a hidden directory without authentication protection. The flow begins with directory enumeration, identifying the vulnerable WordPress version, gaining admin access via the known Nginx CVE (CVE-2013-4547), uploading a plugin/webshell, escalating to the `www-data` user and finally pivoting to root through a cron job or SUID binary until reading the final flag. The internal machine flag confirms total host compromise.

---

## Solucionario

### Task 1: Internal / Room

**Explicación:**
Sala basada en la explotación de un WordPress dentro de un contenedor Nginx. El usuario instruye la descomposición del CTF: enumerar el host, localizar el panel de WordPress, explotar la vulnerabilidad de Nginx para evitar el filtro de acceso y obtener una webshell, luego escalar privilegios hasta leer la flag raíz.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta informativa inicial | `No answer needed` |

### Task 2: Flags

**Explicación:**
Se obtienen las dos flags del CTF tras completar la cadena de explotación: una flag correspondiente al acceso inicial a la máquina y la flag de root final tras la escalada de privilegios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de acceso inicial / internal flag | `THM{int3rna1_fl4g_1}` |
| 2 | Flag final / root flag | `THM{d0ck3r_d3str0y3r}` |

---

**Metodología:**

1. Enumeración de puertos y servicios con `nmap` para identificar el servidor Nginx y el sitio WordPress.
2. Fuzzing de directorios (`gobuster`/`wfuzz`) para localizar `wp-admin`, `wp-login.php` y rutas ocultas del CMS.
3. Identificación de la versión de WordPress y verificación de la CVE de Nginx con la ruta falsificada (`/wp-login.php?`).
4. Acceso al panel de administración sin pasar por el filtro (CVE-2013-4547) para cargar un plugin malicioso o themes.
5. Ejecución de una webshell como `www-data`, enumeración del sistema y escalada de privilegios.
6. Lectura de las flags de usuario y root para finalizar la resolución.

### Cadena de ataque / Attack Chain

`Reconocimiento (nmap) → Enumeración de directorios (gobuster) → Identificación de versión WordPress → Bypass de acceso admin (CVE-2013-4547 Nginx) → Carga de webshell → Shell como www-data → Escalada a root → Lectura de flags THM`

**Learning chain:**

Enumeración de CMS → Vulnerabilidades de servidor web (Nginx path traversal/CRLF) → Abuso del panel admin de WordPress → Web shells → Escalada de privilegios en Linux → Persistencia y flags.

*Lección:* La enumeración exhaustiva de directorios y versiones es clave; explotar el motor de servidor (Nginx) con una ruta truncada permite esquivar autenticación y lograr RCE en WordPress sin esfuerzos de cracking previos.

**MITRE ATT&CK:**

T1046 (Service Scanning), T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell: Server Software), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Internal](https://tryhackme.com/room/internal)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.