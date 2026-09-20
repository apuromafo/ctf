# Nmap Post Port Scans

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | nmappostportscans | https://tryhackme.com/room/nmappostportscans | 02 Level Medium | TryHackMe | Nmap, service detection (-sV), OS detection (-O), NSE Scripts, ssh2-enum-algos, guardado de resultados (-oN/-oA/-oG) | Aprender las técnicas de post-escaneo de Nmap: detección de la versión de los servicios, detección del sistema operativo, uso del Nmap Scripting Engine (NSE) y guardado de los resultados en distintos formatos. |

---

**Contexto:** La sala **Nmap Post Port Scans** cierra la serie Nmap de TryHackMe (junto a Nmap Live Host Discovery, Nmap Basic Port Scans y Nmap Advanced Port Scans). Se centra en los pasos posteriores al escaneo de puertos: detectar la versión de los servicios abiertos con `-sV --version-light`, detectar el sistema operativo con `-O`, ejecutar scripts del NSE (por nombre o por defecto) y guardar los resultados en formato normal, grepable y XML. Los ejercicios prácticos se resuelven desde la AttackBox contra la máquina desplegada en cada tarea, y en la última se analizan los logs de escaneo descargados del objetivo.

> **ES:** Aprende a aprovechar Nmap para la detección de servicios y sistemas operativos, utiliza el Nmap Scripting Engine (NSE) y guarda los resultados de tus escaneos.
> **EN:** Learn how to leverage Nmap for service and OS detection, use Nmap Scripting Engine (NSE), and save the results.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la room: se repasan los pasos de un escaneo Nmap completo (enumerar objetivos, descubrir hosts vivos, resolución DNS inversa y escaneo de puertos). Se indica que hay que lanzar la AttackBox y contar con una comprensión sólida del flujo de escaneo antes de continuar con los ejercicios de las siguientes tareas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ensure you have a solid understanding of how the Nmap scan progresses and its stages (no answer required). | `No answer needed` |

### Task 2: Detección de Servicios / Service Detection
**Explicación:** Con `nmap -sV --version-light <IP>` se detecta la versión de los servicios priorizando la velocidad sobre la exhaustividad: Nmap conecta con el puerto abierto para capturar el banner y cualquier información de versión disponible. En el puerto 143 se identifica **Dovecot imapd**, mientras que el servicio **rpcbind** no revela su versión con esta variante ligera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run nmap -sV --version-light MACHINE_IP via the AttackBox. What is the detected version for port 143? | `Dovecot imapd` |
| 2 | Which service did not have a version detected with --version-light? | `rpcbind` |

### Task 3: Detección de SO y Traceroute / OS Detection and Traceroute
**Explicación:** La detección de sistema operativo usa el fingerprinting TCP/IP habilitado con la opción `-O`. Contra la máquina del lab, Nmap analiza las señales del stack de red del objetivo y detecta el sistema operativo **Linux** (la detección de SO requiere privilegios de root, por lo que se ejecuta con `sudo nmap -O`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run nmap with -O option against MACHINE_IP. What OS did Nmap detect? | `Linux` |

### Task 4: Motor de Scripts NSE / Nmap Scripting Engine (NSE)
**Explicación:** El NSE permite extender Nmap con scripts almacenados en `/usr/share/nmap/scripts/`. El script `http-robots.txt` comprueba si el servidor web expone en el `robots.txt` entradas desautorizadas (`disallowed entries`). Para la vulnerabilidad de ejecución remota de código MS15-034 (CVE-2015-1635) existe el script `http-vuln-cve2015-1635` (se localiza con `grep -R 'MS15-034' /usr/share/nmap/scripts/`). Ejecutando el escaneo con los scripts por defecto (`nmap -n -sC`) sobre el puerto 53 se obtiene la versión completa del servicio DNS (`9.18.28-1~deb12u2-Debian`), y con `ssh2-enum-algos` se extraen los algoritmos SSH soportados, entre ellos el algoritmo de clave pública `rsa-sha2-512`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Knowing that Nmap scripts are saved in /usr/share/nmap/scripts on the AttackBox. What does the script http-robots.txt check for? | `disallowed entries` |
| 2 | Can you figure out the name for the script that checks for the remote code execution vulnerability MS15-034 (CVE-2015-1635)? | `http-vuln-cve2015-1635` |
| 3 | Run Nmap with the default scripts (-sC) against MACHINE_IP. What is the full version value of the service listening on port 53? | `9.18.28-1~deb12u2-Debian` |
| 4 | Based on the ssh2-enum-algos script, what is the name of the public-key (host key) algorithm that relies on SHA-2 supported by MACHINE_IP? | `rsa-sha2-512` |

### Task 5: Guardar la Salida / Saving the Output
**Explicación:** Se descargan los informes de Nmap de la máquina objetivo con `scp pentester@MACHINE_IP:/home/pentester/* .` (usuario `pentester`, contraseña `THM17577`). Los archivos `scan_172_17_network.gnmap`/`.nmap` contienen el escaneo en formato grepable y normal. Grepeando los logs se cuentan los sistemas con el puerto HTTPS abierto (`cat scan_172_17_network.gnmap | grep https` → 3) y se localiza la IP del sistema que escucha en el puerto 8089.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Check the attached Nmap logs. How many systems are listening on the HTTPS port? | `3` |
| 2 | What is the IP address of the system listening on port 8089? | `172.17.20.147` |

### Task 6: Resumen / Summary
**Explicación:** Cierre de la sala: se repasan las opciones de post-escaneo cubiertas (detección de servicios y de sistema operativo, traceroute, scripts NSE y guardado de resultados en formato normal, grepable y XML).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ensure you have taken note of all the post-scan options covered in this room (no answer required). | `No answer needed` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Engagement/requisitos de la sala. | `No answer needed` |
| 2 | (Task 2) What is the detected version for port 143? | `Dovecot imapd` |
| 3 | (Task 2) Which service did not have a version detected with --version-light? | `rpcbind` |
| 4 | (Task 3) What OS did Nmap detect? | `Linux` |
| 5 | (Task 4) What does the script http-robots.txt check for? | `disallowed entries` |
| 6 | (Task 4) Name of the script that checks for MS15-034 (CVE-2015-1635). | `http-vuln-cve2015-1635` |
| 7 | (Task 4) Full version value of the service listening on port 53. | `9.18.28-1~deb12u2-Debian` |
| 8 | (Task 4) Public-key (host key) algorithm based on SHA-2 supported by MACHINE_IP. | `rsa-sha2-512` |
| 9 | (Task 5) How many systems are listening on the HTTPS port? | `3` |
| 10 | (Task 5) IP address of the system listening on port 8089. | `172.17.20.147` |
| 11 | (Task 6) Resumen de opciones de post-escaneo. | `No answer needed` |

---

**Metodología:** Escaneo de puertos → detección de servicios con `-sV --version-light` → detección de SO con `-O` → NSE con scripts específicos (`http-robots.txt`, `http-vuln-cve2015-1635`, `ssh2-enum-algos`) y por defecto (`-sC`) → descarga y análisis de logs de escaneo guardados en formato grepable.

**Learning chain:** detección de versión de servicios → identificación de servicios sin versión → fingerprinting de SO → scripts NSE y correlación con CVEs → guardado de resultados y análisis posterior de logs.

**Lección:** *El escaneo no termina cuando se encuentran los puertos abiertos: la detección de versiones, el sistema operativo y los scripts NSE convierten el hallazgo de puertos en un inventario explotable de servicios, versiones y vulnerabilidades.*

**MITRE ATT&CK:** T1046 (Network Service Discovery) · T1595.001 (Active Scanning: Scanning IP Blocks) · T1595.002 (Active Scanning: Vulnerability Scanning).

**Fuente:** [TryHackMe - Nmap Post Port Scans](https://tryhackme.com/room/nmappostportscans)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.