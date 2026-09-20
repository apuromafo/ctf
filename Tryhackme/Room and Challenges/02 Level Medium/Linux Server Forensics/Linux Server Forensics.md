# Linux Server Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Forensics | linuxserverforensics | https://tryhackme.com/room/linuxserverforensics | Forensics / Linux Server | TryHackMe | Logs de servidor, /etc/passwd, contact.php, web shell, reverse shell, tcpdump (nmap), comandos shell | Compromiso del servidor Linux y acceso root |

---

**Contexto:** La sala **Linux Server Forensics** investiga un servidor Linux comprometido: se analizan los logs del servidor para reconstruir el ataque, se identifica el archivo de la web (contact.php) que permitió la explotación, la IP del atacante, el usuario local, la reverse shell lanzada con `sh -i`, el puerto de redis, los datos de tcpdump, la conexión SSH como `kali@kali` y la manipulación de `/etc/passwd` con nano para obtener accesso root.

## Solucionario

### Task 1
**Explicación:**

Acceso inicial al servidor comprometido y preparación del entorno forense.

`No answer needed`

### Task 2
**Explicación:**

Análisis de los logs del servidor: se recogen indicadores del escaneo inicial y de las rutas atacadas.

1. `No answer needed`
2. `2`
3. `/nmaplowercheck1618912425`

### Task 3
**Explicación:**

Reconstrucción de la explotación web: se identifica el archivo vulnerable, la IP del atacante y el usuario explotado.

1. `contact.php`
2. `192.168.56.24`
3. `Fred`

### Task 4
**Explicación:**

Se identifica el comando de la reverse shell lanzado por el atacante.

`sh -i`

### Task 5
**Explicación:**

Se localiza el nombre del usuario del sistema que participó en el incidente.

`mrcake`

### Task 6
**Explicación:**

Revisión de conexiones y procesos del servidor durante el incidente.

`No answer needed`

### Task 7
**Explicación:**

Análisis de las trazas de red (tcpdump): identificador del paquete y timestamp capturado.

1. `GXWR`
2. `13:30:15`

### Task 8
**Explicación:**

Autenticación por SSH registrada en los logs de acceso al servidor.

`kali@kali`

### Task 9
**Explicación:**

Comando utilizado por el atacante para modificar el archivo `/etc/passwd` y crear/escalar la cuenta.

`nano /etc/passwd`

### Task 10
**Explicación:**

Comprobación del acceso root conseguido mediante la edición de `/etc/passwd`.

`No answer needed`

### Task 11
**Explicación:**

Flag final de la sala obtenida tras la investigación completa.

`[gh0st_1n_the_machine]`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 - Respuesta | `No answer needed` |
| 2.1 | Task 2 - Respuesta 1 | `No answer needed` |
| 2.2 | Task 2 - Respuesta 2 | `2` |
| 2.3 | Task 2 - Respuesta 3 | `/nmaplowercheck1618912425` |
| 3.1 | Task 3 - Respuesta 1 | `contact.php` |
| 3.2 | Task 3 - Respuesta 2 | `192.168.56.24` |
| 3.3 | Task 3 - Respuesta 3 | `Fred` |
| 4 | Task 4 - Respuesta | `sh -i` |
| 5 | Task 5 - Respuesta | `mrcake` |
| 6 | Task 6 - Respuesta | `No answer needed` |
| 7.1 | Task 7 - Respuesta 1 | `GXWR` |
| 7.2 | Task 7 - Respuesta 2 | `13:30:15` |
| 8 | Task 8 - Respuesta | `kali@kali` |
| 9 | Task 9 - Respuesta | `nano /etc/passwd` |
| 10 | Task 10 - Respuesta | `No answer needed` |
| 11 | Task 11 - Respuesta | `[gh0st_1n_the_machine]` |

---

**Metodología:** Análisis de logs del servidor web y de autenticación → reconstrucción de la explotación (contact.php, IP atacante, reverse shell `sh -i`) → revisión de trazas de red y conexiones SSH → rastreo de la manipulación de `/etc/passwd` para conseguir root → lectura de la flag final.

**Learning chain:** Logs del servidor → web shell (contact.php) → reverse shell `sh -i` → usuario mrcake → tcpdump y SSH (kali@kali) → `/etc/passwd` con nano → root.

**Lección:** *La forensia de servidor arranca en los logs: un solo archivo web vulnerable (contact.php) encadena el acceso inicial, la reverse shell y la manipulación de cuentas. Documentar comandos exactos, IPs y timestamps permite reconstruir el ataque paso a paso.*

**MITRE ATT&CK:** T1505.003 Server Software Component: Web Shell · T1059.004 Command and Scripting Interpreter: Unix Shell · T1071.001 Application Layer Protocol · T1098.001 Account Manipulation: Additional Cloud Credentials · T1136.001 Create Account: Local Account · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Linux Server Forensics](https://tryhackme.com/room/linuxserverforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.