# Linux Threat Detection 2 [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `linuxthreatdetection2`
* **Link:** https://tryhackme.com/room/linuxthreatdetection2
* **Objeto:** Detectar un atacante en una máquina Linux mediante logs (auditd, Bash) y análisis de procesos: descargas maliciosas, brute-force SSH, descubrimiento y despliegue de un cryptominer.

---

## Solucionario de Tareas / Task Solutions

> Segunda sala de la serie de detección de amenazas en Linux. Se analiza el vector de ataque desde el descubrimiento hasta la ejecución de un cryptominer (Dota3).
> Second room of the Linux threat-detection series. Attack vector analyzed from discovery to cryptominer execution (Dota3).

### Tarea 1 / Task 1 — Environment & Persistence

**Ejecuta `systemd-detect-virt` para detectar la nube del sistema. ¿Cuál es la salida del comando? / Run `systemd-detect-virt` to detect the system's cloud. What is the command's output you discovered?**
`amazon`

**Ahora ejecuta `ps aux` y busca procesos EDR o antivirus. ¿Cuál es la ruta completa del binario antimalware detectado? / Now run `ps aux` and look for EDR or antivirus processes. What is the full path to the detected antimalware binary?**
`/var/lib/ultrasec/malscan`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Tarea 2 / Task 2 — Internal Discovery

**¿Cuál es la ruta del script que inició el comando "hostname"? / What is the path of the script that initiated the "hostname" command?**
`/home/itsupport/debug.sh`

**¿Cuál fue el último comando de Discovery lanzado por el script? / What was the last Discovery command launched by the script?**
`ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu`

**Mirando el contenido del script, ¿cuál es el email del autor? / Looking at the script content, what's the email of the script author?**
`greg@tryhackme.thm`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Tarea 2 / Task 2 — Downloads (Elastic / helper script)

**¿De qué dominio se descargó el agente Elastic? / From which domain was the Elastic agent downloaded?**
`artifacts.elastic.co`

**¿Cuál es la ruta completa del script "helper.sh" descargado? / What is the full path to the downloaded "helper.sh" script?**
`/var/tmp/helper.sh`

**¿Cuál de los archivos descargados es más probable que sea malicioso: el descargado con curl o con wget? / Which of the downloaded files is more likely to be malicious: the one downloaded with curl or wget?**
`curl`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Tarea 3 / Task 3 — SSH Brute-Force

**¿Qué dirección IP consiguió hacer fuerza bruta al SSH expuesto? / Which IP address managed to brute-force the exposed SSH?**
`45.9.148.125`

**¿Qué comando usó el atacante para listar los últimos usuarios con sesión iniciada? / Which command did the attacker use to list the last logged-in users?**
`last`

**¿Qué tres procesos EDR buscó el atacante con "egrep"? (formato: separados por coma, en orden alfabético) / Which three EDR processes did the attacker look for with "egrep"?**
`ds_agent,falcon,sentinel`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

### Tarea 4 / Task 4 — Cryptominer

**¿Cuál es el nombre del archivo malicioso transferido vía SCP? / What is the name of the malicious archive that was transferred via SCP?**
`kernupd.tar.gz`

**¿Cuál fue la línea de comando completa del lanzamiento del cryptominer? / What was the full command line of the cryptominer launch?**
`nohup /tmp/.apt/kernupd/kernupd`

**¿Qué rango de direcciones IP escaneó el atacante para buscar un SSH expuesto? / Which IP address range did the attacker scan for an exposed SSH?**
`10.10.12.1-10.10.12.10`

Fuente / Source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/

---

*Documentación para propósitos educativos y registro de CTF.*
*Fuente de respuestas / Answer source: https://simontaplin.net/2025/10/12/answers-for-the-tryhackme-linux-threat-detection-2-room/*
