# Poster

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `poster` | [TryHackMe](https://tryhackme.com/room/poster) | 01 Level Easy | THM | NMAP, PostgreSQL, Metasploit, Fuerza bruta, Consultas SQL, Hashdump, Lectura de archivos, RCE | CTF de PostgreSQL mal configurado |

---

**Contexto:** CTF de nivel fácil centrado en una base de datos PostgreSQL expuesta. El flujo incluye escaneo de puertos, detección del servicio PostgreSQL, fuerza bruta de credenciales (postgres:password), ejecución de consultas SQL, volcado de hashes de usuarios, lectura de archivos del sistema y explotación de una vulnerabilidad que permite la ejecución de comandos para obtener las banderas de usuario y root.

> **ES:** Máquina CTF que explota una PostgreSQL mal configurada: fuerza bruta de login, consultas SQL, volcado de hashes, lectura de archivos y RCE hasta obtener las flags.
> **EN:** CTF machine exploiting a misconfigured PostgreSQL: login brute force, SQL queries, hash dumping, file read and RCE to grab the flags.

## Solucionario

### Task 1: Explotación de PostgreSQL / PostgreSQL Exploitation

**Explicación:** Recorre el compromiso completo de la máquina mediante el servicio PostgreSQL: escaneo de puertos y detección de la base de datos, fuerza bruta del login, consultas SQL para enumerar versiones y usuarios, volcado de hashes, lectura de archivos con los privilegios de la base de datos y explotación de la función copy-from-program para ejecutar comandos del sistema y leer las banderas.

1. 1. postgresql
   2. 5432
   3. No answer needed
   4. auxiliary/scanner/postgres/postgres_login
   5. postgres:password
   6. auxiliary/admin/postgres/postgres_sql
   7. 9.5.21
   8. auxiliary/scanner/postgres/postgres_hashdump
   9. 6
   10. auxiliary/admin/postgres/postgres_readfile
   11. exploit/multi/postgres/postgres_copy_from_program_cmd_exec
   12. THM{postgresql_fa1l_conf1gurat1on}
   13. THM{c0ngrats_for_read_the_f1le_w1th_credent1als}

| Pregunta | Respuesta |
|---|---|
| ¿Qué tipo de base de datos se detecta en el escaneo? | `postgresql` |
| ¿En qué puerto corre el servicio de base de datos? | `5432` |
| Paso del escaneo sin respuesta | `No answer needed` |
| ¿Qué módulo de Metasploit fuerza el login de PostgreSQL? | `auxiliary/scanner/postgres/postgres_login` |
| ¿Cuáles son las credenciales de acceso a la base de datos? | `postgres:password` |
| ¿Qué módulo permite ejecutar consultas SQL? | `auxiliary/admin/postgres/postgres_sql` |
| ¿Qué versión de PostgreSQL corre en el servidor? | `9.5.21` |
| ¿Qué módulo permite volcar los hashes de contraseñas? | `auxiliary/scanner/postgres/postgres_hashdump` |
| ¿Cuántos usuarios PostgreSQL existen? | `6` |
| ¿Qué módulo permite leer archivos del sistema? | `auxiliary/admin/postgres/postgres_readfile` |
| ¿Qué módulo explota la vulnerabilidad para ejecutar comandos del sistema? | `exploit/multi/postgres/postgres_copy_from_program_cmd_exec` |
| ¿Cuál es la bandera de usuario? | `THM{postgresql_fa1l_conf1gurat1on}` |
| ¿Cuál es la bandera de root? | `THM{c0ngrats_for_read_the_f1le_w1th_credent1als}` |

---

**Metodología:** Escaneo de puertos con NMAP, enumeración del servicio PostgreSQL, fuerza bruta de credenciales con Metasploit, reconocimiento de la base de datos mediante consultas SQL, volcado de hashes, abuso de los privilegios de PostgreSQL para leer archivos y explotación de la función COPY ... FROM PROGRAM para obtener ejecución de comandos.

### Cadena de ataque / Attack Chain
Escaneo NMAP -> Detección de PostgreSQL en el puerto 5432 -> Fuerza bruta del login (postgres:password) -> Consultas SQL para enumerar versión (9.5.21) y usuarios -> Volcado de hashes (6 usuarios) -> Lectura de archivos con postgres_readfile -> Explotación de COPY FROM PROGRAM para RCE -> Lectura de las banderas de usuario y root.

**Learning chain:** Escaneo de puertos, fuerza bruta de servicios de base de datos, Metasploit (módulos de PostgreSQL), enumeración SQL y RCE mediante funcionalidades propias de PostgreSQL.

**Lección:** *Una base de datos expuesta con credenciales débiles y privilegios amplios (superuser) permite pasar de leer datos a ejecutar comandos en el sistema: el principio de mínimo privilegio es crítico en PostgreSQL.*

**MITRE ATT&CK:** T1110.001 Brute Force (Password Guessing), T1213.003 Data from Information Repositories (Code Repositories/DB), T1003.008 OS Credential Dumping (/etc/passwd y hashes), T1005 Data from Local System, T1059 Command and Scripting Interpreter, T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Poster](https://tryhackme.com/room/poster)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.