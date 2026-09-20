# Boiler CTF
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `boilerctf` |
| **Link** | [TryHackMe](https://tryhackme.com/room/boilerctf) |
| **Sección** | CTF / Enumeration |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Port scanning, service enumeration, web exploitation, file discovery |
| **Impacto** | Enseña técnicas de reconocimiento y enumeración de servicios (FTP, SSH, Webmin, Joomla) para identificar vulnerabilidades y extraer flags. |
---
**Contexto:** Boiler CTF es una sala de TryHackMe estilo Capture The Flag que requiere enumerar múltiples servicios expuestos en la máquina objetivo. El participante debe identificar servicios activos, encontrar archivos de backup ocultos y explotar configuraciones débiles para obtener las flags de cada task.
*EN: Boiler CTF is a TryHackMe Capture The Flag room requiring enumeration of multiple exposed services on the target machine. The participant must identify active services, find hidden backup files, and exploit weak configurations to obtain the flags for each task.*
## Solucionario
### Task 1 — Service Enumeration
**Explicación:** Se realiza un escaneo de puertos y enumeración de servicios para identificar los servicios activos en la máquina. Se descubre FTP (archivos de texto), SSH, Webmin y un servidor web con Joomla. También se localiza un archivo de log relevante.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What service is running on port 21? | `txt` |
| 2 | What service is running on port 22? | `ssh` |
| 3 | What service is running on port 10000? | `webmin` |
| 4 | What is the name of the hidden directory? | `nay` |
| 5 | What CMS is running on the web server? | `joomla` |
| 6 | What is the flag for the FTP service? | `No answer needed` |
| 7 | What is the name of the log file? | `log.txt` |
### Task 2 — Exploitation
**Explicación:** Se accede al directorio oculto y se localiza un archivo de backup que contiene una bandera de progreso. Usando las credenciales obtenidas se completa el reto y se obtienen las flags finales.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the backup file? | `backup` |
| 2 | What is the flag for the backup? | `You made it till here, well done.` |
| 3 | What command was used to find the file? | `find` |
| 4 | What is the final flag? | `It wasn't that hard, was it?` |
---
**Metodología:** Nmap (-sV -sC) → enumeración de servicios (FTP, SSH, Webmin, Joomla) → directorios ocultos (GoBuster) → inspección de archivos (log.txt, backup) → obtención de flags.
**Learning chain:** escaneo → servicios activos → directorios ocultos → archivos de backup → flags.
**Lección:** *La enumeración sistemática de servicios y directorios ocultos revela superficies de ataque que una inspección superficial pasa por alto.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1592.002 (Gather Victim Host Information: Software), T1083 (File and Directory Discovery).
**Fuente:** [TryHackMe - Boiler CTF](https://tryhackme.com/room/boilerctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
