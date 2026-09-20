# Linux Live Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough (Premium) | linuxliveanalysis | https://tryhackme.com/room/linuxliveanalysis | Forensics / Linux | Writeup de thmrevenant (GitHub) | Procesos, memoria, archivos abiertos (lsof), directorio /tmp, puertos en escucha, binarios ocultos, paquetes, servicios (netcat), cron | Compromiso total del host Linux con persistencia y exfiltración de datos |

---

**Contexto:** La sala **Linux Live Analysis** es un laboratorio forense en vivo (Premium) sobre un sistema Linux comprometido. El analista debe reconstruir el incidente examinando la máquina en caliente: identificación del host (hostname, Machine ID, arquitectura), procesos ejecutándose desde directorios inusuales y desde memoria, archivos abiertos asociados a keyloggers, puertos en escucha, binarios ocultos en el directorio raíz, paquetes maliciosos instalados y persistencia vía servicio (netcat) y cron. La clave es correlacionar múltiples fuentes del sistema para pintar el panorama completo del compromiso.

## Solucionario

> **ES:** Análisis forense en tiempo real de un sistema Linux comprometido, investigando procesos sospechosos, archivos abiertos, servicios maliciosos y paquetes instalados.
> **EN:** Live forensics analysis of a compromised Linux system, investigating suspicious processes, open files, malicious services, and installed packages.

### Task 1: Reconocimiento y Análisis del Sistema
**Explicación:**

Se identifica el host comprometido consultando el hostname devuelto por la query, el Machine ID y la arquitectura de la máquina investigada; también se comprueba, en la web oficial, cuántas tablas se listan para Linux OS.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What hostname is returned after running the following query? | `attacker.thm` |
| On the official website, how many tables are listed for Linux OS? | `154` |
| What is the Machine ID of the machine we are investigating? | `dc7c8ac5c09a4bbfaf3d09d399f10d96` |
| What is the architecture of the host we are investigating? | `x86_64` |

### Task 2: Procesos y Actividad Sospechosa
**Explicación:**

Se enumeran los procesos en ejecución y se aíslan los que corren desde el directorio `tmp` y desde el directorio de usuario, además del proceso oculto en memoria. Se verifica el estado del puerto local 80, se investigan los archivos abiertos asociados al proceso sospechoso (keylogger) y se localiza el binario oculto del directorio raíz.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the process running from the tmp directory? (Note: Not Hidden one) | `sshdd` |
| What is the name of the suspicious process running in the memory of the infected host? | `.systm_updater` |
| What is the name of the process running from the user directory? | `rdp_updater` |
| What is the state of the local port that is listening on port 80? | `ESTABLISHED` |
| Investigate the opened files. What is the opened file associated with the suspicious process running on the system? | `keylogger.log` |
| What is the name of the process that is associated with the suspicious file found in the above question? | `sshdd` |
| What is the name of the hidden binary found in the root directory? | `.systmd` |

### Task 3: Paquetes y Persistencia
**Explicación:**

Se analizan los paquetes instalados en busca del paquete sospechoso y su código secreto oculto en la descripción; se identifica el servicio malicioso instalado vía netcat y la ruta completa del proceso encontrado en la tabla cron (persistencia).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the suspicious package installed on the host? | `datacollector` |
| The suspicious package contains a secret code. What is the code hidden in the description? | `{NOT_SO_BENIGN_Package}` |
| Which suspicious service was observed to be installed on this infected machine using netcat? | `systm.service` |
| What is the full path of the process found in the cron table? | `/home/badactor/storage/.secret_docs/rdp_updater` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | What hostname is returned after running the following query? | `attacker.thm` |
| 1.2 | On the official website, how many tables are listed for Linux OS? | `154` |
| 1.3 | What is the Machine ID of the machine we are investigating? | `dc7c8ac5c09a4bbfaf3d09d399f10d96` |
| 1.4 | What is the architecture of the host we are investigating? | `x86_64` |
| 2.1 | What is the name of the process running from the tmp directory? (Note: Not Hidden one) | `sshdd` |
| 2.2 | What is the name of the suspicious process running in the memory of the infected host? | `.systm_updater` |
| 2.3 | What is the name of the process running from the user directory? | `rdp_updater` |
| 2.4 | What is the state of the local port that is listening on port 80? | `ESTABLISHED` |
| 2.5 | Investigate the opened files. What is the opened file associated with the suspicious process running on the system? | `keylogger.log` |
| 2.6 | What is the name of the process that is associated with the suspicious file found in the above question? | `sshdd` |
| 2.7 | What is the name of the hidden binary found in the root directory? | `.systmd` |
| 3.1 | What is the name of the suspicious package installed on the host? | `datacollector` |
| 3.2 | The suspicious package contains a secret code. What is the code hidden in the description? | `{NOT_SO_BENIGN_Package}` |
| 3.3 | Which suspicious service was observed to be installed on this infected machine using netcat? | `systm.service` |
| 3.4 | What is the full path of the process found in the cron table? | `/home/badactor/storage/.secret_docs/rdp_updater` |

---

**Metodología:** 1. Verificar hostname y arquitectura del sistema con queries del sistema / Verify hostname and system architecture using system queries. 2. Obtener Machine ID del sistema para identificar el host / Retrieve the Machine ID to identify the host. 3. Listar procesos en ejecución e identificar los que provienen de directorios inusuales (/tmp, directorio de usuario) / List running processes and identify those from unusual directories (/tmp, user directory). 4. Examinar procesos ocultos en memoria y verificar puertos abiertos en escucha / Examine hidden processes in memory and verify open listening ports. 5. Revisar archivos abiertos asociados a procesos sospechosos para encontrar artefactos como keyloggers / Review open files associated with suspicious processes to find artifacts like keyloggers. 6. Buscar binarios ocultos en el directorio raíz y paquetes sospechosos instalados / Search for hidden binaries in the root directory and suspicious installed packages. 7. Investigar servicios instalados mediante netcat y cron jobs para identificar persistencia / Investigate services installed via netcat and cron jobs to identify persistence.

Cadena de ataque / Attack Chain:

```
Reconocimiento del host (hostname, Machine ID, arquitectura)
  -> Identificación de procesos sospechosos (sshdd en /tmp, .systm_updater en memoria)
    -> Correlación de archivos abiertos (keylogger.log asociado a sshdd)
      -> Descubrimiento de binarios ocultos (.systmd en root)
        -> Análisis de paquetes maliciosos (datacollector con código oculto)
          -> Persistencia mediante servicio (systm.service) y cron job (rdp_updater)
```

**Learning chain:** Hostname + Machine ID + arquitectura → procesos en /tmp y memoria → archivos abiertos (keylogger) → binarios ocultos en root → paquetes maliciosos → servicio netcat + cron job (persistencia).

**Lección:** *El análisis forense en vivo requiere cruzar múltiples fuentes de información (procesos, archivos abiertos, servicios, cron) para construir un panorama completo del compromiso. Los atacantes ocultan artefactos en directorios no convencionales y utilizan nombres similares a servicios legítimos.*

**MITRE ATT&CK:** T1036 Masquerading · T1071.001 Application Layer Protocol · T1543.002 Systemd Service · T1053.003 Cron · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Linux Live Analysis](https://tryhackme.com/room/linuxliveanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.