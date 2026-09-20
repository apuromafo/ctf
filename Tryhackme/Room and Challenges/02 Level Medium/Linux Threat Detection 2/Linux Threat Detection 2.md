# Linux Threat Detection 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Premium (requiere suscripción) | linuxthreatdetection2 | https://tryhackme.com/room/linuxthreatdetection2 | Linux / Threat Detection | Writeup de thmrevenant (GitHub) / simontaplin.net | auditd, Bash history, procesos, systemd-detect-virt, Elastic agent, debug.sh, brute-force SSH, cryptominer (kernupd/Dota3) | Detección de ataque completo hasta cryptominer |

> **Objeto:** Detectar un atacante en una máquina Linux mediante logs (auditd, Bash) y análisis de procesos: descargas maliciosas, brute-force SSH, descubrimiento y despliegue de un cryptominer.

---

**Contexto:** La sala **Linux Threat Detection 2** es la segunda entrega de la serie de detección de amenazas en Linux (Premium). Se sigue el vector de ataque completo sobre una máquina Linux: identificación del entorno virtualizado (nube `amazon`) y del antimalware presente, descubrimiento interno vía el script `/home/itsupport/debug.sh`, descargas de agentes (Elastic) y scripts (helper.sh), fuerza bruta SSH desde `45.9.148.125`, y finalmente el despliegue de un cryptominer (`kernupd`, Dota3). Todo se reconstruye a partir de logs de auditd, historial de Bash y el árbol de procesos.

## Solucionario

> Segunda sala de la serie de detección de amenazas en Linux. Se analiza el vector de ataque desde el descubrimiento hasta la ejecución de un cryptominer (Dota3).
> Second room of the Linux threat-detection series. Attack vector analyzed from discovery to cryptominer execution (Dota3).

### Task 1: Environment & Persistence
**Explicación:**

Se detecta la nube del sistema con `systemd-detect-virt` y se buscan procesos EDR o antivirus con `ps aux` para localizar el binario antimalware y la ruta del agente de persistencia.

**Ejecuta `systemd-detect-virt` para detectar la nube del sistema. ¿Cuál es la salida del comando? / Run `systemd-detect-virt` to detect the system's cloud. What is the command's output you discovered?**
`amazon`

**Ahora ejecuta `ps aux` y busca procesos EDR o antivirus. ¿Cuál es la ruta completa del binario antimalware detectado? / Now run `ps aux` and look for EDR or antivirus processes. What is the full path to the detected antimalware binary?**
`/var/lib/ultrasec/malscan`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Task 2: Internal Discovery
**Explicación:**

Se identifica el script que lanzó el comando `hostname`, el último comando de discovery ejecutado por el script y el email de su autor, reconstruyendo el movimiento interno del atacante.

**¿Cuál es la ruta del script que inició el comando "hostname"? / What is the path of the script that initiated the "hostname" command?**
`/home/itsupport/debug.sh`

**¿Cuál fue el último comando de Discovery lanzado por el script? / What was the last Discovery command launched by the script?**
`ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu`

**Mirando el contenido del script, ¿cuál es el email del autor? / Looking at the script content, what's the email of the script author?**
`greg@tryhackme.thm`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Task 2: Downloads (Elastic / helper script)
**Explicación:**

Se analizan las descargas realizadas en el host: el dominio del agente Elastic, la ruta completa del script helper.sh y la determinación de cuál descarga (curl o wget) es más sospechosa.

**¿De qué dominio se descargó el agente Elastic? / From which domain was the Elastic agent downloaded?**
`artifacts.elastic.co`

**¿Cuál es la ruta completa del script "helper.sh" descargado? / What is the full path to the downloaded "helper.sh" script?**
`/var/tmp/helper.sh`

**¿Cuál de los archivos descargados es más probable que sea malicioso: el descargado con curl o con wget? / Which of the downloaded files is more likely to be malicious: the one downloaded with curl or wget?**
`curl`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Task 3: SSH Brute-Force
**Explicación:**

Se investiga la fuerza bruta sobre el servicio SSH expuesto: la IP que consiguió autenticarse, el comando de descubrimiento de usuarios (`last`) y la búsqueda de procesos EDR con `egrep`.

**¿Qué dirección IP consiguió hacer fuerza bruta al SSH expuesto? / Which IP address managed to brute-force the exposed SSH?**
`45.9.148.125`

**¿Qué comando usó el atacante para listar los últimos usuarios con sesión iniciada? / Which command did the attacker use to list the last logged-in users?**
`last`

**¿Qué tres procesos EDR buscó el atacante con "egrep"? (formato: separados por coma, en orden alfabético) / Which three EDR processes did the attacker look for with "egrep"?**
`ds_agent,falcon,sentinel`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Task 4: Cryptominer
**Explicación:**

Se reconstruye la fase final: el archivo malicioso transferido vía SCP, la línea de comando completa del lanzamiento del cryptominer y el rango de IPs escaneado en busca de un SSH expuesto.

**¿Cuál es el nombre del archivo malicioso transferido vía SCP? / What is the name of the malicious archive that was transferred via SCP?**
`kernupd.tar.gz`

**¿Cuál fue la línea de comando completa del lanzamiento del cryptominer? / What was the full command line of the cryptominer launch?**
`nohup /tmp/.apt/kernupd/kernupd`

**¿Qué rango de direcciones IP escaneó el atacante para buscar un SSH expuesto? / Which IP address range did the attacker scan for an exposed SSH?**
`10.10.12.1-10.10.12.10`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/*

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | ¿Cuál es la salida del comando `systemd-detect-virt`? | `amazon` |
| 1.2 | ¿Cuál es la ruta completa del binario antimalware detectado? | `/var/lib/ultrasec/malscan` |
| 2.1 | ¿Cuál es la ruta del script que inició el comando "hostname"? | `/home/itsupport/debug.sh` |
| 2.2 | ¿Cuál fue el último comando de Discovery lanzado por el script? | `ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu` |
| 2.3 | ¿Cuál es el email del autor del script? | `greg@tryhackme.thm` |
| 2.4 | ¿De qué dominio se descargó el agente Elastic? | `artifacts.elastic.co` |
| 2.5 | ¿Cuál es la ruta completa del script "helper.sh" descargado? | `/var/tmp/helper.sh` |
| 2.6 | ¿Cuál de los archivos descargados es más probable que sea malicioso: curl o wget? | `curl` |
| 3.1 | ¿Qué dirección IP consiguió hacer fuerza bruta al SSH expuesto? | `45.9.148.125` |
| 3.2 | ¿Qué comando usó el atacante para listar los últimos usuarios con sesión iniciada? | `last` |
| 3.3 | ¿Qué tres procesos EDR buscó el atacante con "egrep"? | `ds_agent,falcon,sentinel` |
| 4.1 | ¿Cuál es el nombre del archivo malicioso transferido vía SCP? | `kernupd.tar.gz` |
| 4.2 | ¿Cuál fue la línea de comando completa del lanzamiento del cryptominer? | `nohup /tmp/.apt/kernupd/kernupd` |
| 4.3 | ¿Qué rango de direcciones IP escaneó el atacante para buscar un SSH expuesto? | `10.10.12.1-10.10.12.10` |

---

**Metodología:** 1. Environment & persistence: `systemd-detect-virt` + `ps aux` para localizar el antimalware y el agente persistente. 2. Internal discovery: reconstrucción del script `debug.sh` (hostname, últimos comandos de discovery, email del autor). 3. Downloads: correlación de las descargas (dominio Elastic, helper.sh, curl vs wget). 4. SSH brute-force: IP autenticada, comando `last` y búsqueda de EDR con `egrep`. 5. Cryptominer: transferencia SCP, línea de lanzamiento y escaneo del rango de IPs.

**Learning chain:** Cloud/EDR (amazon, malscan) → discovery interno (debug.sh) → descargas (Elastic + helper.sh) → SSH brute-force (45.9.148.125, last, EDR check) → cryptominer (kernupd.tar.gz → nohup kernupd; escaneo 10.10.12.1-10).

**Lección:** *La detección de amenazas Linux es una cadena: cada fase del atacante (entorno, discovery, descargas, credential access, cryptominer) deja una huella en logs auditd, history de Bash y procesos; correlacionar esas huellas reconstruye el vector completo sin necesidad de ver el ataque en vivo.*

**MITRE ATT&CK:** T1110 Brute Force · T1033 System Owner/User Discovery · T1046 Network Service Discovery · T1105 Ingress Tool Transfer · T1496 Resource Hijacking · T1036.005 Masquerading: Match Legitimate Name or Location · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Linux Threat Detection 2](https://tryhackme.com/room/linuxthreatdetection2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.