# Linux File System Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | linuxfilesystemanalysis | [TryHackMe](https://tryhackme.com/room/linuxfilesystemanalysis) | 01 Level Easy | THM | ls -la, file, stat, find, /etc/passwd, UID, SUID, pstree, /etc/sudoers, crontab, /var/tmp | Análisis forense del sistema de archivos Linux para detectar backdoors, usuarios ocultos con UID 0, binarios SUID y scripts maliciosos |

---

**Contexto:** Sala orientada al análisis del sistema de archivos en un Linux comprometido. Se localizan archivos sospechosos, se determina su tipo y metadatos temporales con `file` y `stat`, se audita `/etc/passwd` en busca de cuentas ocultas con UID 0 y grupos comprometidos, se identifican binarios SUID como `/usr/bin/pstree`, se revisa `/etc/sudoers` y se detecta un script malicioso (`/var/tmp/findme.sh`) respaldado por una tarea programada.

> **EN:**
> 1. No answer needed
> 2. THM{5514ec4f1ce82f63867806d3cd95dbd8}
> 3. 1. THM{0b1313afd2136ca0faafb2daa2b430f3}
>    2. application/octet-stream
>    3. 2020-10-26 21:10:44.000000000 +0000
> 4. 1. b4ckd00r3d
>    2. plugdev
>    3. /usr/bin/pstree
> 5. 1. THM{f38279ab9c6af1215815e5f7bbad891b}
>    2. THM{6ed90e00e4fb7945bead8cd59e9fcd7f}
>    3. 2024-02-13 00:34:16.005897449 +0000
> 6. 1. /etc/sudoers
>    2. 7063c3930affe123baecd3b340f1ad2c
> 7. 1. /var/tmp/findme.sh
>    2. Warning
> 8. No answer needed

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta el escenario: una máquina Linux comprometida que debe inspeccionarse a través del sistema de archivos para identificar actividad maliciosa y recopilar evidencias.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Reconocimiento inicial / Initial reconnaissance

**Explicación:** Se explora el sistema de archivos con `ls -la` en busca de archivos y directorios ocultos o sospechosos. La flag confirma la identificación del primer artefacto comprometido.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué flag se encontró durante la exploración? / What flag was found during the exploration? | `THM{5514ec4f1ce82f63867806d3cd95dbd8}` |

### Task 3: Tipo de archivo y metadatos / File type and metadata

**Explicación:** Se emplea `file` para determinar la naturaleza de un binario sospechoso y `stat` para extraer su línea de tiempo, estableciendo cuándo fue modificado. Una flag se oculta dentro del propio artefacto.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué flag está oculta en el archivo sospechoso? / What flag is hidden in the suspicious file? | `THM{0b1313afd2136ca0faafb2daa2b430f3}` |
| 2 | ¿Qué tipo de archivo es? / What file type is it? | `application/octet-stream` |
| 3 | ¿Cuándo se modificó por última vez? / When was it last modified? | `2020-10-26 21:10:44.000000000 +0000` |

### Task 4: Cuentas, grupos y binarios SUID / Accounts, groups and SUID binaries

**Explicación:** Auditar `/etc/passwd` revela una cuenta oculta adicional con UID 0 (`b4ckd00r3d`), un vector típico de persistencia. Se identifica su grupo (`plugdev`) y, buscando binarios con el bit SUID, aparece `/usr/bin/pstree`.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué usuario, además de root, tiene UID 0? / Which user besides root has UID 0? | `b4ckd00r3d` |
| 2 | ¿A qué grupo pertenece ese usuario? / Which group does that user belong to? | `plugdev` |
| 3 | ¿Qué binario tiene activo el bit SUID? / Which binary has the SUID bit set? | `/usr/bin/pstree` |

### Task 5: Flags y marcas de tiempo / Flags and timestamps

**Explicación:** Se profundiza en directorios comprometidos extrayendo dos flags adicionales y registrando la marca de tiempo exacta de un artefacto con el comando `stat` para construir la línea de tiempo del incidente.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Primera flag encontrada en el artefacto / First flag found in the artifact | `THM{f38279ab9c6af1215815e5f7bbad891b}` |
| 2 | Segunda flag encontrada en el artefacto / Second flag found in the artifact | `THM{6ed90e00e4fb7945bead8cd59e9fcd7f}` |
| 3 | ¿Cuál es la marca de tiempo del artefacto? / What is the artifact's timestamp? | `2024-02-13 00:34:16.005897449 +0000` |

### Task 6: Permisos sudo / sudo permissions

**Explicación:** Se inspecciona la configuración de privilegios. `/etc/sudoers` es el archivo de control de sudo, y se identifica un hash comprometido presente en el sistema.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué archivo controla los permisos de sudo? / Which file controls sudo permissions? | `/etc/sudoers` |
| 2 | ¿Qué hash comprometido se identifica? / Which compromised hash is identified? | `7063c3930affe123baecd3b340f1ad2c` |

### Task 7: Script malicioso / Malicious script

**Explicación:** Se localiza un script malicioso en `/var/tmp/findme.sh`, un directorio de escritura compartida frecuentemente usado para persistencia. El sistema clasifica la alerta con severidad `Warning`.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Dónde reside el script malicioso? / Where does the malicious script reside? | `/var/tmp/findme.sh` |
| 2 | ¿Qué severidad recibe la alerta? / What severity does the alert receive? | `Warning` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre de la sala: se reúnen las evidencias recolectadas (backdoors, usuarios con UID 0, binarios SUID y scripts maliciosos) para confirmar el compromiso del sistema.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Comenzar con `ls -la` para enumerar archivos ocultos y sospechosos. Determinar tipo y metadatos de cada artefacto con `file` y `stat`, registrando timestamps exactos. Auditar `/etc/passwd` para detectar cuentas con UID 0 (`b4ckd00r3d`) y anotar sus grupos. Buscar binarios con el bit SUID con `find / -perm -u=s -type f` e identificar `/usr/bin/pstree`. Revisar `/etc/sudoers` y los hashes presentes. Por último, inspeccionar directorios de escritura compartida (`/var/tmp`) y tareas programadas, encontrando el script malicioso `findme.sh` clasificado como `Warning`.

### Cadena de ataque / Attack Chain

Enumeración con `ls -la` → `file`/`stat` y extracción de flags → auditoría de `/etc/passwd` (UID 0) → grupos → binarios SUID (`pstree`) → `/etc/sudoers` y hashes → script malicioso en `/var/tmp/findme.sh`

**Learning chain:** ls -la → file → stat → /etc/passwd → UID 0 → SUID → pstree → /etc/sudoers → hash → /var/tmp → findme.sh → Warning

**Lección:** *Los indicadores de compromiso no siempre viven en procesos o conexiones de red: los atacantes esconden backdoors en el sistema de archivos mediante usuarios con UID 0, binarios SUID y scripts en directorios de escritura compartida como `/var/tmp`, a menudo respaldados por tareas cron.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1548.001 (Setuid and Setgid), T1053.003 (Scheduled Task/Job: Cron), T1083 (File and Directory Discovery), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Linux File System Analysis](https://tryhackme.com/room/linuxfilesystemanalysis)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.