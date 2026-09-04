# Linux Logs Investigations [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `linuxlogsinvestigations`
* **Link:** https://tryhackme.com/room/linuxlogsinvestigations
* **Sección / Section:** Forensics / Logs
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Investigación forense de logs en Linux, cubriendo tipos de logs del sistema, configuración de journald, análisis de autenticación y trazas de una aplicación web comprometida.
> **EN:** Linux log forensics investigation covering system log types, journald configuration, authentication analysis, and traces of a compromised web application.

---

### Task 1 — Fundamentos de Logs en Linux

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

---

### Task 2 — Análisis de Logs de Autenticación y Servicios

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What command can be used to search logs related to a session opened for a user? | `sudo grep -i "session opened" /var/log/auth.log` |
| Which folder contains Apache2 logs? | `/var/log/apache2` |

---

### Task 3 — Investigación de Incidente Web

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the IP address from which the application was exploited? | `10.10.190.69` |
| What file contains the reverse shell? | `cmd.php` |
| At which port was the reverse shell running? | `5000` |
| What is the file name that was being executed with sudo privileges? | `tests.sh` |
| What is the name of the user created using the service? | `attacker` |
| Was the new account ever logged in to? y/n | `n` |

---

## Metodología / Methodology

1. **Paso / Step:** Comprender los tipos de logs del sistema Linux (kernel, syslog, auth) y sus niveles de severidad / Understand Linux system log types (kernel, syslog, auth) and their severity levels.
2. **Paso / Step:** Identificar el almacenamiento de mensajes del kernel (ring buffer) y la configuración de persistencia de journald / Identify kernel message storage (ring buffer) and journald persistence configuration.
3. **Paso / Step:** Localizar logs específicos de autenticación (btmp, auth.log) y buscar sesiones de usuario con grep / Locate specific authentication logs (btmp, auth.log) and search for user sessions with grep.
4. **Paso / Step:** Explorar logs de servicios web (Apache2) para identificar tráfico malicioso / Examine web service logs (Apache2) to identify malicious traffic.
5. **Paso / Step:** Correlar la IP atacante con archivos subidos (web shell), reverse shell y puertos de escucha / Correlate attacker IP with uploaded files (web shell), reverse shell, and listening ports.
6. **Paso / Step:** Investigar persistencia: ejecución con sudo, creación de usuarios y intentos de login / Investigate persistence: sudo execution, user creation, and login attempts.

### Cadena de ataque / Attack Chain

```
Explotación de aplicación web desde 10.10.190.69
  -> Subida de web shell (cmd.php)
    -> Reverse shell en puerto 5000
      -> Escalada de privilegios con tests.sh (sudo)
        -> Creación de usuario "attacker"
          -> Verificación: el usuario nunca inició sesión
```

**Lección:** Los logs de Linux son una herramienta fundamental para la investigación forense. La correlación entre auth.log, logs de Apache y la configuración de journald permite reconstruir la cadena de ataque completa incluso cuando no hay persistencia exitosa.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
