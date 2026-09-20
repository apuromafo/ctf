# Linux Logs Investigations

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough (Premium) | linuxlogsinvestigations | https://tryhackme.com/room/linuxlogsinvestigations | Forensics / Logs | Writeup de thmrevenant (GitHub) | Kernel logs, kernel ring buffer, syslog, journald, auth.log, btmp, auditd (ausearch), Apache2 logs | Reconstrucción forense completa del incidente y del acceso no autorizado |

---

**Contexto:** La sala **Linux Logs Investigations** es una investigación forense basada en logs (Premium) que cubre los tipos de logs del sistema Linux, los niveles de severidad y el almacenamiento del kernel (ring buffer), la configuración de persistencia de journald, la búsqueda de sesiones en auth.log y, finalmente, la reconstrucción de un incidente contra una aplicación web: desde la IP de explotación hasta el reverse shell, la escalada con sudo y la creación de una cuenta de usuario. La correlación entre logs de distinto origen permite reconstruir toda la cadena de ataque.

## Solucionario

> **ES:** Investigación forense de logs en Linux, cubriendo tipos de logs del sistema, configuración de journald, análisis de autenticación y trazas de una aplicación web comprometida.
> **EN:** Linux log forensics investigation covering system log types, journald configuration, authentication analysis, and traces of a compromised web application.

### Task 1: Fundamentos de Logs en Linux
**Explicación:**

Se repasan los tipos de logs del sistema (kernel, syslog, btmp), los niveles de severidad por defecto y los keywords de syslog, los códigos de facility (cron), la configuración de persistencia de journald y la utilidad para buscar logs de auditd.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which type of logs provide messages related to hardware events and system errors? | `Kernel` |
| What is the memory space used to store system messages? | `Kernel ring buffer` |
| What is the default log level used to inform about non-imminent errors? | `WARNING` |
| Which log file can be used to record failed login attempts only? | `btmp` |
| What severity level keyword is used to indicate immediate action is needed in a syslog message? | `alert` |
| What facility code is used for cron jobs? | `9` |
| To configure the persistence of journal logs, which parameter has to be modified within the journald configuration file? | `Storage` |
| Which utility is used to search for auditd logs? | `ausearch` |

### Task 2: Análisis de Logs de Autenticación y Servicios
**Explicación:**

Se busca en el log de autenticación la apertura de sesiones de usuario con grep y se localiza la carpeta que contiene los logs de Apache2.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What command can be used to search logs related to a session opened for a user? | `sudo grep -i "session opened" /var/log/auth.log` |
| Which folder contains Apache2 logs? | `/var/log/apache2` |

### Task 3: Investigación de Incidente Web
**Explicación:**

Se reconstruye el incidente de la aplicación web: la IP desde la que se explotó la app, el archivo de web shell subido, el puerto del reverse shell, el archivo ejecutado con privilegios sudo, el usuario creado mediante el servicio y si esa cuenta llegó a iniciar sesión.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the IP address from which the application was exploited? | `10.10.190.69` |
| What file contains the reverse shell? | `cmd.php` |
| At which port was the reverse shell running? | `5000` |
| What is the file name that was being executed with sudo privileges? | `tests.sh` |
| What is the name of the user created using the service? | `attacker` |
| Was the new account ever logged in to? y/n | `n` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Which type of logs provide messages related to hardware events and system errors? | `Kernel` |
| 1.2 | What is the memory space used to store system messages? | `Kernel ring buffer` |
| 1.3 | What is the default log level used to inform about non-imminent errors? | `WARNING` |
| 1.4 | Which log file can be used to record failed login attempts only? | `btmp` |
| 1.5 | What severity level keyword is used to indicate immediate action is needed in a syslog message? | `alert` |
| 1.6 | What facility code is used for cron jobs? | `9` |
| 1.7 | To configure the persistence of journal logs, which parameter has to be modified within the journald configuration file? | `Storage` |
| 1.8 | Which utility is used to search for auditd logs? | `ausearch` |
| 2.1 | What command can be used to search logs related to a session opened for a user? | `sudo grep -i "session opened" /var/log/auth.log` |
| 2.2 | Which folder contains Apache2 logs? | `/var/log/apache2` |
| 3.1 | What is the IP address from which the application was exploited? | `10.10.190.69` |
| 3.2 | What file contains the reverse shell? | `cmd.php` |
| 3.3 | At which port was the reverse shell running? | `5000` |
| 3.4 | What is the file name that was being executed with sudo privileges? | `tests.sh` |
| 3.5 | What is the name of the user created using the service? | `attacker` |
| 3.6 | Was the new account ever logged in to? y/n | `n` |

---

**Metodología:** 1. Comprender los tipos de logs del sistema Linux (kernel, syslog, auth) y sus niveles de severidad / Understand Linux system log types (kernel, syslog, auth) and their severity levels. 2. Identificar el almacenamiento de mensajes del kernel (ring buffer) y la configuración de persistencia de journald / Identify kernel message storage (ring buffer) and journald persistence configuration. 3. Localizar logs específicos de autenticación (btmp, auth.log) y buscar sesiones de usuario con grep / Locate specific authentication logs (btmp, auth.log) and search for user sessions with grep. 4. Explorar logs de servicios web (Apache2) para identificar tráfico malicioso / Examine web service logs (Apache2) to identify malicious traffic. 5. Correlar la IP atacante con archivos subidos (web shell), reverse shell y puertos de escucha / Correlate attacker IP with uploaded files (web shell), reverse shell, and listening ports. 6. Investigar persistencia: ejecución con sudo, creación de usuarios y intentos de login / Investigate persistence: sudo execution, user creation, and login attempts.

Cadena de ataque / Attack Chain:

```
Explotación de aplicación web desde 10.10.190.69
  -> Subida de web shell (cmd.php)
    -> Reverse shell en puerto 5000
      -> Escalada de privilegios con tests.sh (sudo)
        -> Creación de usuario "attacker"
          -> Verificación: el usuario nunca inició sesión
```

**Learning chain:** Tipos de logs y severidad → ring buffer y journald → logs de autenticación → logs Apache → correlación IP/web shell/reverse shell → persistencia (sudo + cuentas).

**Lección:** *Los logs de Linux son una herramienta fundamental para la investigación forense. La correlación entre auth.log, logs de Apache y la configuración de journald permite reconstruir la cadena de ataque completa incluso cuando no hay persistencia exitosa.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1505.003 Web Shell · T1071.001 Application Layer Protocol · T1548.002 Sudo and Sudo Caching · T1098 Account Manipulation.

**Fuente:** [TryHackMe - Linux Logs Investigations](https://tryhackme.com/room/linuxlogsinvestigations)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.