# Ice

| **Dificultad** | Easy |
| **Tipo** | Explotación de Windows (laboratorio) |
| **Slug** | `ice` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ice) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Icecast / Metasploit / Meterpreter / Migración de procesos / Bypass de UAC / Mimikatz (kiwi) |
| **Impacto** | Laboratorio guiado de explotación de una máquina Windows vulnerable: enumeración del servicio Icecast abierto en el puerto alto, explotación con Metasploit, obtención de sesión Meterpreter, migración a un proceso de sistema, escalada con bypass de UAC, volcado de credenciales con kiwi y uso de comandos de post-explotación (pantalla, micrófono, timestomp y golden ticket). |

---

**Contexto:** La sala empieza con la enumeración de una máquina Windows a través de Nmap (puerto 3389, un puerto alto y nombre DARK-PC). Tras identificar el servicio Icecast vulnerable, se lanza el exploit de Metasploit `icecast_header` desde una sesión Meterpreter. Para estabilizar la sesión se migra del proceso Icecast (Dark) a `spoolsv.exe`, se comprueba la arquitectura x64 y el build 7601, y se escala a SYSTEM con el exploit local `bypassuac_eventvwr`. Finalmente se extraen las credenciales con `creds_all` y se prueban comandos de reconocimiento como `hashdump`, `screenshare`, `record_mic`, `timestomp` y `golden_ticket_create`.

## Solucionario

### Task 1: Despliegue del laboratorio

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y espera a que esté lista. | `No answer needed` |
| 2 | Verifica la conectividad con la máquina. | `No answer needed` |
| 3 | Arranca el escáner de Nmap. | `No answer needed` |
| 4 | Analiza los resultados del escaneo. | `No answer needed` |

### Task 2: Enumeración

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta un escaneo de puertos a la máquina objetivo. | `No answer needed` |
| 2 | Revisa los puertos abiertos y los servicios. | `No answer needed` |
| 3 | ¿Qué puerto usa el servicio de escritorio remoto? | `3389` |
| 4 | ¿Qué servicio se anuncia en el banner del puerto alto? | `Icecast` |
| 5 | ¿Cuál es el nombre NetBIOS de la máquina? | `DARK-PC` |

### Task 3: Explotación del servicio

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la puntuación CVSS de la vulnerabilidad de Icecast? | `6.4` |
| 2 | ¿Cuál es el identificador CVE de la vulnerabilidad? | `CVE-2004-1561` |
| 3 | Inicia la consola de Metasploit (msfconsole). | `No answer needed` |
| 4 | ¿Qué módulo de Metasploit aprovecha la vulnerabilidad de Icecast? | `exploit/windows/http/icecast_header` |
| 5 | Configura las opciones del módulo. | `No answer needed` |
| 6 | ¿Qué opción debe contener la IP de la máquina víctima? | `rhosts` |
| 7 | Ejecuta el exploit y comprueba si obtienes una sesión. | `No answer needed` |

### Task 4: Escalada de privilegios

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de shell obtuviste tras ejecutar el exploit? | `meterpreter` |
| 2 | ¿Cuál es el nombre del proceso que se está ejecutando (el servicio Icecast)? | `Dark` |
| 3 | ¿Cuál es el número de build del sistema Windows? | `7601` |
| 4 | ¿Qué arquitectura tiene el sistema, de 32 o de 64 bits? | `x64` |
| 5 | Migra la sesión a un proceso más estable. | `No answer needed` |
| 6 | ¿Qué módulo local de Metasploit se utiliza para escalar privilegios (bypass de UAC)? | `exploit/windows/local/bypassuac_eventvwr` |
| 7 | Configura el módulo con la sesión migrada. | `No answer needed` |
| 8 | Ejecuta el exploit local. | `No answer needed` |
| 9 | Comprueba los privilegios de la nueva sesión. | `No answer needed` |
| 10 | ¿Qué opción del exploit local debe contener tu IP de atacante? | `LHOST` |
| 11 | Ejecuta el exploit con la nueva configuración. | `No answer needed` |
| 12 | Confirma el nuevo nivel de privilegios. | `No answer needed` |
| 13 | Sigue las indicaciones para estabilizar la sesión. | `No answer needed` |
| 14 | ¿Qué privilegio de Windows permite hacerse dueño de archivos y procesos? | `SeTakeOwnershipPrivilege` |

### Task 5: Post-explotación

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Carga el módulo kiwi en la sesión de Meterpreter. | `No answer needed` |
| 2 | ¿En qué proceso se ejecuta la nueva sesión de nivel SYSTEM? | `spoolsv.exe` |
| 3 | Consulta la ayuda de kiwi. | `No answer needed` |
| 4 | ¿Con qué cuenta se está ejecutando la sesión? | `NT AUTHORITY\SYSTEM` |
| 5 | Visualiza las credenciales disponibles. | `No answer needed` |
| 6 | Revisa la ayuda de los comandos de credenciales. | `No answer needed` |
| 7 | ¿Qué comando de kiwi recupera todas las credenciales almacenadas? | `creds_all` |
| 8 | ¿Cuál es la contraseña de la cuenta Dark? | `Password01` |

### Task 6: Reconocimiento y otras herramientas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora los comandos disponibles en Meterpreter. | `No answer needed` |
| 2 | ¿Qué comando extrae los hashes de las contraseñas del sistema? | `hashdump` |
| 3 | ¿Qué comando permite ver en vivo la pantalla de la víctima? | `screenshare` |
| 4 | ¿Qué comando graba el audio del micrófono de la víctima? | `record_mic` |
| 5 | ¿Qué comando modifica las marcas de tiempo (timestamps) de los archivos? | `timestomp` |
| 6 | ¿Qué comando permite crear un golden ticket? | `golden_ticket_create` |
| 7 | Prueba los comandos de la lista en la sesión. | `No answer needed` |

### Task 7: Resumen

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa las técnicas aprendidas durante el laboratorio. | `No answer needed` |

---

**Metodología:** Se enumera la máquina con Nmap y se identifica el servicio Icecast en el puerto alto, vulnerable a CVE-2004-1561 (CVSS 6.4). Con Metasploit se selecciona `exploit/windows/http/icecast_header`, se fija `rhosts` a la víctima y se obtiene una sesión Meterpreter. Para trabajar de forma estable se migra el proceso al servicio `spoolsv.exe` (build 7601, x64) de SYSTEM. Se escala con el exploit local `bypassuac_eventvwr` y el privilegio `SeTakeOwnershipPrivilege`, y se aprovecha la sesión de SYSTEM para volcar credenciales con kiwi (`creds_all`, contraseña `Password01`). Finalmente se practican comandos de post-explotación que van desde el volcado de hashes hasta el espionaje de pantalla/micrófono, la alteración de timestamps y la creación de golden tickets.

**Learning chain:** enumeración → explotación de Icecast → sesión Meterpreter → migración de procesos → bypass de UAC → volcado de credenciales → comandos de post-explotación.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1548.002 (Abuse Elevation Control Mechanism: Bypass User Account Control), T1003.001 (OS Credential Dumping: LSASS Memory), T1070.006 (Indicator Removal: Timestomp), T1558.001 (Steal or Forge Kerberos Tickets: Golden Ticket)

**Fuente:** [TryHackMe - Ice](https://tryhackme.com/room/ice)