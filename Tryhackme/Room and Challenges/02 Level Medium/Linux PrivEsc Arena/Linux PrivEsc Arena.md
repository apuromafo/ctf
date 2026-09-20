# Linux PrivEsc Arena

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Arena | linuxprivescarena | https://tryhackme.com/room/linuxprivescarena | Linux / Privilege Escalation | TryHackMe | sudo, /etc/shadow, MySQL, SUID, nginx (CVE-2016-1247), service command, id_rsa | Escalada de privilegios a root |

---

**Contexto:** La sala **Linux PrivEsc Arena** es un laboratorio-práctica de escalada de privilegios en Linux donde se aplican los vectores clásicos sobre una máquina: credenciales y usuarios de bases de datos (MySQL), configuración errónea de archivos y claves SSH (id_rsa), binarios con vectores vulnerables (nginx / CVE-2016-1247), el comando `service` para escalar a root y la manipulación del PATH para ejecutar binarios maliciosos.

## Solucionario

### Task 1
**Explicación:**

Acceso inicial al sistema con el usuario del laboratorio.

`No answer needed`

### Task 2
**Explicación:**

Enumeración básica del sistema antes de escalar.

`No answer needed`

### Task 3
**Explicación:**

Enumeración de servicios, procesos y permisos del sistema.

`No answer needed`

### Task 4
**Explicación:**

Se obtienen credenciales en texto plano durante la enumeración de servicios con permisos de sudo.

1. `password321`
2. `user`

### Task 5
**Explicación:**

Se identifican las credenciales de la base de datos MySQL del sistema.

1. `mysql`
2. `root`
3. `password123`

### Task 6
**Explicación:**

Se examinan los permisos del share expuesto (montaje/lectura) en el sistema.

`-rw-rw-r--`

### Task 7
**Explicación:**

Dentro del share expuesto se localiza la clave privada SSH.

`/backups/supersecretkeys/id_rsa`

### Task 8
**Explicación:**

Conexión SSH con la clave privada robada al usuario destino.

`No answer needed`

### Task 9
**Explicación:**

Enumeración del usuario SSH al que se ha accedido.

`No answer needed`

### Task 10
**Explicación:**

Se listan los procesos que se ejecutan con privilegios de root.

`No answer needed`

### Task 11
**Explicación:**

Se verifica la versión del servicio web vulnerable (nginx) instalado.

`No answer needed`

### Task 12
**Explicación:**

Identificación del vector CVE del servicio y del mecanismo de elevación abusado.

1. `CVE-2016-1247`
2. `sudo`

### Task 13
**Explicación:**

Comando exacto que se ejecuta para lanzar la escalada vía el servicio.

`service apache2 start`

### Task 14
**Explicación:**

Ruta completa del comando ejecutado por el servicio desde el entorno sudo.

`/usr/sbin/service apache2 start`

### Task 15
**Explicación:**

Se obtiene la shell con privilegios tras la explotación del vector de servicio.

`No answer needed`

### Task 16
**Explicación:**

Uso de la shell de root para leer la flag final.

`No answer needed`

### Task 17
**Explicación:**

Limpieza y comprobación del acceso root obtenido.

`No answer needed`

### Task 18
**Explicación:**

Cierre de la arena con la verificación de todos los vectores explotados.

`No answer needed`

### Task 19
**Explicación:**

Cuestionario final de consolidación de la práctica.

`No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 - Respuesta | `No answer needed` |
| 2 | Task 2 - Respuesta | `No answer needed` |
| 3 | Task 3 - Respuesta | `No answer needed` |
| 4.1 | Task 4 - Respuesta 1 | `password321` |
| 4.2 | Task 4 - Respuesta 2 | `user` |
| 5.1 | Task 5 - Respuesta 1 | `mysql` |
| 5.2 | Task 5 - Respuesta 2 | `root` |
| 5.3 | Task 5 - Respuesta 3 | `password123` |
| 6 | Task 6 - Respuesta | `-rw-rw-r--` |
| 7 | Task 7 - Respuesta | `/backups/supersecretkeys/id_rsa` |
| 8 | Task 8 - Respuesta | `No answer needed` |
| 9 | Task 9 - Respuesta | `No answer needed` |
| 10 | Task 10 - Respuesta | `No answer needed` |
| 11 | Task 11 - Respuesta | `No answer needed` |
| 12.1 | Task 12 - Respuesta 1 | `CVE-2016-1247` |
| 12.2 | Task 12 - Respuesta 2 | `sudo` |
| 13 | Task 13 - Respuesta | `service apache2 start` |
| 14 | Task 14 - Respuesta | `/usr/sbin/service apache2 start` |
| 15 | Task 15 - Respuesta | `No answer needed` |
| 16 | Task 16 - Respuesta | `No answer needed` |
| 17 | Task 17 - Respuesta | `No answer needed` |
| 18 | Task 18 - Respuesta | `No answer needed` |
| 19 | Task 19 - Respuesta | `No answer needed` |

---

**Metodología:** Enumeración de permisos y servicios → robo de credenciales en texto plano (MySQL) → abuso de share con claves SSH (id_rsa) → identificación del CVE del servicio (nginx CVE-2016-1247) → elevación vía `service apache2 start` para lanzar binario malicioso como root.

**Learning chain:** Acceso inicial → credenciales débiles → claves ssh en share con permisos laxos → CVE-2016-1247 + sudo → `service apache2 start` → root.

**Lección:** *Las credenciales en texto plano, las claves privadas accesibles en shares con permisos laxos y los binarios con vectores de servicio conocidos (CVE) convierten la enumeración perezosa en una escalada a root; el control de permisos sobre archivos y procesos críticos es la defensa principal.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1552.001 Unsecured Credentials: Credentials in Files · T1552.004 Unsecured Credentials: Private Keys · T1068 Exploitation for Privilege Escalation · T1543.003 Create or Modify System Process: Windows Service.

**Fuente:** [TryHackMe - Linux PrivEsc Arena](https://tryhackme.com/room/linuxprivescarena)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.