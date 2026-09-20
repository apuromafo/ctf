# Linux PrivEsc

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | linuxprivesc | https://tryhackme.com/room/linuxprivesc | Linux / Privilege Escalation | TryHackMe | /etc/shadow, sudo, SUID, cron, NFS, PATH, hash cracking (sha512crypt) | Escalada de privilegios a root |

---

**Contexto:** La sala **Linux PrivEsc** es el laboratorio clásico de escalada de privilegios en Linux: se parte de la enumeración de la máquina (usuario, grupos, kernel, sudo) y se recorren los vectores más comunes — credenciales en `/etc/shadow` y crackeo de hashes, permisos de sudo, binarios SUID, tareas cron, misconfiguraciones de NFS (no_root_squash), scripts con PATH manipulable y credenciales en archivos de configuración. Cada vector se explota hasta conseguir una shell como root.

## Solucionario

### Task 1
**Explicación:**

Acceso inicial a la máquina con el usuario del laboratorio; el objetivo es enumerar el sistema antes de escalar.

1. `No answer needed`
2. `uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)`

### Task 2
**Explicación:**

Enumeración de servicios de escucha y del usuario activo; no requiere respuesta numérica.

`No answer needed`

### Task 3
**Explicación:**

Se examina el archivo `/etc/shadow` del equipo, se extrae el hash del usuario `user`, se identifica el algoritmo de cifrado y se crackea la contraseña.

1. `$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0`
2. `sha512crypt`
3. `password123`

### Task 4
**Explicación:**

Uso de las credenciales obtenidas para cambiar de usuario; sin respuesta numérica.

`No answer needed`

### Task 5
**Explicación:**

Se comprueba la identidad del nuevo usuario tras el cambio: root.

`uid=0(root) gid=0(root) groups=0(root)`

### Task 6
**Explicación:**

Enumeración de procesos y servicios en ejecución en el sistema.

1. `11`
2. `apache2`
3. `No answer needed`

### Task 7
**Explicación:**

Se examina el PATH del sistema y los scripts ejecutables con permisos anómalos.

`No answer needed`

### Task 8
**Explicación:**

Cron jobs del sistema: se listan las tareas programadas y los scripts invocados.

`No answer needed`

### Task 9
**Explicación:**

Se obtiene el PATH completo del usuario, visible en las variables de entorno del sistema.

`/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin`

### Task 10
**Explicación:**

Cuestionario teórico sobre binarios con permiso SUID en el sistema.

`No answer needed`

### Task 11
**Explicación:**

Análisis del binario SUID vulnerable localizado en el sistema.

`No answer needed`

### Task 12
**Explicación:**

Explotación del binario SUID para obtener una shell como root.

`No answer needed`

### Task 13
**Explicación:**

Aplicación de los permisos SUID aprendidos a otro binario y verificación del resultado.

`No answer needed`

### Task 14
**Explicación:**

Revisión de los permisos del archivo de flags y de la configuración sudo del usuario actual.

`No answer needed`

### Task 15
**Explicación:**

Se identifican los permisos sudo del usuario actual sobre los binarios del sistema.

`No answer needed`

### Task 16
**Explicación:**

Se aprovechan las credenciales en texto plano encontradas en los archivos de configuración para conectarse a una base de datos remota.

`mysql -h somehost.local -uroot -ppassword123`

### Task 17
**Explicación:**

Conexión a la base de datos: se examina el contenido de la base y se encuentra el archivo de credenciales del servicio VPN en el sistema.

`/etc/openvpn/auth.txt`

### Task 18
**Explicación:**

Se explota el acceso a la base de datos para conseguir acceso como root en el sistema.

`No answer needed`

### Task 19
**Explicación:**

Análisis de la configuración de NFS del servidor: export sin `root_squash`, que permite mapear volúmenes como root.

`no_root_squash`

### Task 20
**Explicación:**

Montaje del volumen NFS de la máquina víctima desde Kali y creación del binario SUID en el share.

`No answer needed`

### Task 21
**Explicación:**

Ejecución remota del binario SUID montado por NFS para obtener una shell como root.

`No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Task 1 - Respuesta 1 | `No answer needed` |
| 1.2 | Task 1 - Respuesta 2 | `uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)` |
| 2 | Task 2 - Respuesta | `No answer needed` |
| 3.1 | Task 3 - Respuesta 1 | `$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0` |
| 3.2 | Task 3 - Respuesta 2 | `sha512crypt` |
| 3.3 | Task 3 - Respuesta 3 | `password123` |
| 4 | Task 4 - Respuesta | `No answer needed` |
| 5 | Task 5 - Respuesta | `uid=0(root) gid=0(root) groups=0(root)` |
| 6.1 | Task 6 - Respuesta 1 | `11` |
| 6.2 | Task 6 - Respuesta 2 | `apache2` |
| 6.3 | Task 6 - Respuesta 3 | `No answer needed` |
| 7 | Task 7 - Respuesta | `No answer needed` |
| 8 | Task 8 - Respuesta | `No answer needed` |
| 9 | Task 9 - Respuesta | `/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin` |
| 10 | Task 10 - Respuesta | `No answer needed` |
| 11 | Task 11 - Respuesta | `No answer needed` |
| 12 | Task 12 - Respuesta | `No answer needed` |
| 13 | Task 13 - Respuesta | `No answer needed` |
| 14 | Task 14 - Respuesta | `No answer needed` |
| 15 | Task 15 - Respuesta | `No answer needed` |
| 16 | Task 16 - Respuesta | `mysql -h somehost.local -uroot -ppassword123` |
| 17 | Task 17 - Respuesta | `/etc/openvpn/auth.txt` |
| 18 | Task 18 - Respuesta | `No answer needed` |
| 19 | Task 19 - Respuesta | `no_root_squash` |
| 20 | Task 20 - Respuesta | `No answer needed` |
| 21 | Task 21 - Respuesta | `No answer needed` |

---

**Metodología:** Enumeración del sistema (usuario, grupos, kernel, proceso, PATH, cron, SUID) → extracción y crackeo de hashes de `/etc/shadow` → explotación de sudo, binarios SUID y scripts con PATH vulnerable → abuso de credenciales en archivos de configuración (MySQL) → escalada vía NFS con `no_root_squash`.

**Learning chain:** Enumeración → /etc/shadow + crackeo → sudo/SUID → cron y PATH → credenciales en texto plano (MySQL) → NFS (no_root_squash) → root.

**Lección:** *La escalada de privilegios en Linux se reduce a enumerar de forma exhaustiva: cuentas, permisos, procesos, cron, SUID, PATH, NFS y credenciales olvidadas. Un solo descriptor mal configurado (como no_root_squash o un binario SUID vulnerable) convierte al usuario estándar en root.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1003.008 OS Credential Dumping: /etc/passwd and /etc/shadow · T1548.002 Abuse Elevation Control Mechanism: Sudo and Sudo Caching · T1548.001 Setuid and Setgid · T1053.003 Scheduled Task/Job: Cron · T1574.007 Hijack Execution Flow: Path Interception by PATH Environment Variable · T1611 Escape to Host.

**Fuente:** [TryHackMe - Linux PrivEsc](https://tryhackme.com/room/linuxprivesc)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.