# The Cod Caper

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `thecodcaper` | [TryHackMe](https://tryhackme.com/room/thecodcaper) | 01 Level Easy | THM | Apache, SSH, PHP, MySQL, escalada de privilegios | Compromiso total (root) del sistema objetivo |

---

**Contexto:**

> **ES:** Sala de nivel fácil tipo walkthrough en la que se compromete un servidor web: escaneo de puertos, explotación de una vulnerabilidad web, acceso SSH y escalada de privilegios hasta obtener la bandera de root.
> **EN:** Easy walkthrough room in which a web server is compromised: port scanning, exploitation of a web vulnerability, SSH access and privilege escalation to obtain the root flag.

## Solucionario

### Task 1: Reconocimiento / Reconnaissance

**Explicación:**

Esta tarea cubre el reconocimiento inicial de la máquina objetivo. Se conserva de forma literal el contenido original:

1. No answer needed

2. 1. 2
   2. Apache2 Ubuntu Default Page: It works
   3. OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
   4. Apache/2.4.18

### Task 2: Explotación web / Web Exploitation

**Explicación:**

En esta tarea se explota la aplicación web para acceder al panel de administración y recuperar credenciales. Se conserva de forma literal el contenido original:

3. administrator.php

4. 1. pingudad
   2. secretpass
   3. 3

### Task 3: Acceso SSH / SSH Access

**Explicación:**

Con las credenciales obtenidas se accede al sistema por SSH y se localiza el archivo con la contraseña del usuario root. Se conserva de forma literal el contenido original:

5. 1. 3
   2. yes
   3. pinguapingu

6. /opt/secret/root

### Task 4: Escalada de privilegios / Privilege Escalation

**Explicación:**

La última fase consiste en escalar privilegios hasta root. Se conservan de forma literal las respuestas originales:

7. No answer needed
8. No answer needed
9. No answer needed
10. love2fish
11. No answer needed

### Tabla Unificada de Preguntas y Respuestas

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Inicio del reto (sin respuesta necesaria) | `No answer needed` |
| 2 | Task 1 | Número de puertos abiertos detectados | `2` |
| 3 | Task 1 | Página web por defecto detectada | `Apache2 Ubuntu Default Page: It works` |
| 4 | Task 1 | Banner del servicio SSH | `OpenSSH 7.2p2 Ubuntu 4ubuntu2.8` |
| 5 | Task 1 | Versión del servidor Apache | `Apache/2.4.18` |
| 6 | Task 2 | Nombre del panel de administración | `administrator.php` |
| 7 | Task 2 | Usuario de la base de datos | `pingudad` |
| 8 | Task 2 | Contraseña de la base de datos | `secretpass` |
| 9 | Task 2 | Valor devuelto por la consulta (índice de tabla) | `3` |
| 10 | Task 3 | Valor del primer dato | `3` |
| 11 | Task 3 | Confirmación de acceso | `yes` |
| 12 | Task 3 | Contraseña de la aplicación web | `pinguapingu` |
| 13 | Task 3 | Ruta del archivo que contiene la contraseña de root | `/opt/secret/root` |
| 14 | Task 4 | Respuesta 7 | `No answer needed` |
| 15 | Task 4 | Respuesta 8 | `No answer needed` |
| 16 | Task 4 | Respuesta 9 | `No answer needed` |
| 17 | Task 4 | Contraseña de root encontrada | `love2fish` |
| 18 | Task 4 | Respuesta 11 | `No answer needed` |

---

**Metodología:** 1) Escaneo de puertos (nmap) y enum de servicios; 2) Enumeración de aplicaciones web y panel de administración; 3) Explotación de la aplicación y obtención de credenciales; 4) Acceso SSH; 5) Enumeración de sistema y archivos de credenciales; 6) Escalada de privilegios a root.

### Cadena de ataque / Attack Chain

- Escaneo de puertos (Apache y SSH)
- Enumeración del directorio web (panel de administración)
- Explotación web → credenciales (pingudad/secretpass)
- Acceso SSH → shell de usuario
- Localización de la ruta de las contraseñas (pivoting a root)
- Escalada de privilegios → lectura de root flag

**Learning chain:** Reconocimiento → Enumeración web → Explotación → Acceso SSH → Escalada de privilegios → Captura de flag

**Lección:** *El movimiento lateral y la enumeración de archivos sensibles en un sistema comprometido son clave para escalar privilegios; la primera shell obtenida no suele ser el último paso.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1210 (Exploitation of Remote Services), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - The Cod Caper](https://tryhackme.com/room/thecodcaper)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.