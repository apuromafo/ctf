# Enumeration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `enumeration` | [TryHackMe](https://tryhackme.com/room/enumeration) | 01 Level Easy | TryHackMe | PowerShell / SSH / Linux / Windows Server / DNS / SMB / SNMP / PsLoggedOn | Aprender a enumerar manualmente máquinas Linux y Windows para recopilar información del sistema. |

> **Objeto:** Realizar enumeración manual y sistemática de una máquina Linux (Ubuntu) y una máquina Windows Server 2019 para extraer información de sistema, servicios y protocolos (SSH, DNS, SMB, SNMP): distribución y versión, usuarios, puertos en escucha, scripts en ejecución, zone transfer, shares SMB, información SNMP y utilidades como PsLoggedOn.

---

**Contexto:** La enumeración es la base de todo pentest: conocer el sistema operativo, usuarios, versiones, puertos en escucha, tareas programadas y servicios disponibles permite decidir el vector de ataque. La room ofrece dos laboratorios (Linux y Windows) para practicar la recopilación de información con los comandos correctos en cada plataforma, además de servicios de la red local (DNS, SMB, SNMP).

> **ES:** Se introducen las bases de la enumeración manual. Tras recordar cómo arrancar la consola de PowerShell (powershell.exe) y qué clave necesita el cliente en la autenticación SSH (private key), se enumeran los dos laboratorios: en Linux se saca la distribución (Ubuntu), la versión (20.04.6), el último usuario conectado (randa), el puerto TCP más alto en escucha (6667) con su servicio (inspircd) y un script en segundo plano (THM-24765.sh); en Windows se obtiene el tipo de sistema, la versión del SO, los hotfixes instalados, el puerto TCP más bajo en escucha (22) y su programa (sshd.exe). Cierran la room el DNS/SMB/SNMP de red local (flags THM{DNS_ZONE}, THM{829738} y THM{SNMP_SERVICE}), la herramienta PsLoggedOn y la conclusión.
> **EN:** Fundamentals of manual enumeration. After recalling how to start the PowerShell console (powershell.exe) and which key the client needs for SSH authentication (private key), both labs are enumerated: on Linux the distribution (Ubuntu), version (20.04.6), last logged-in user (randa), highest listening TCP port (6667) with its service (inspircd) and a background script (THM-24765.sh) are found; on Windows the OS type, OS version, installed hotfixes, lowest listening TCP port (22) and its program (sshd.exe) are obtained. The room ends with the local-network DNS/SMB/SNMP (THM{DNS_ZONE}, THM{829738}, THM{SNMP_SERVICE}), the PsLoggedOn tool and a conclusion.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presenta el propósito de la room: aprender a enumerar de forma manual. Se recuerda el comando para abrir la consola interactiva de PowerShell.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command would you use to start the PowerShell interactive command line? / ¿Qué comando usarías para iniciar la consola interactiva de PowerShell? | `powershell.exe` |

### Task 2: Propósito de la enumeración / Purpose
**Explicación:** Explica por qué es importante enumerar antes de atacar. Aprovecha la autenticación SSH por clave para recordar los conceptos: en la autenticación por clave asimétrica el cliente necesita guardar y presentar su clave privada (private key).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In SSH key-based authentication, which key does the client need? / En la autenticación SSH por clave, ¿qué clave necesita el cliente? | `private key` |

### Task 3: Enumeración - Linux / Enumerating Linux
**Explicación:** Con el laboratorio Linux desplegado se enumeran datos del sistema: la distribución (Ubuntu), el número de versión (20.04.6), el nombre del último usuario que inició sesión (randa), el puerto TCP en escucha más alto (6667) y el programa que lo atiende (inspircd), además de un script en segundo plano cuyo nombre empieza por THM (THM-24765.sh).

```bash
cat /etc/os-release                    # distribución y versión
last -a                                # últimos usuarios conectados
ss -tlnp                               # puertos en escucha
ps aux | grep THM                      # scripts en segundo plano
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Linux distribution used in the VM? / ¿Qué distribución de Linux se usa en la VM? | `Ubuntu` |
| 2 | What is its version number? / ¿Cuál es su número de versión? | `20.04.6` |
| 3 | What is the name of the user who last logged in to the system? / ¿Cuál es el nombre del último usuario que inició sesión en el sistema? | `randa` |
| 4 | What is the highest listening TCP port number? / ¿Cuál es el número de puerto TCP más alto en escucha? | `6667` |
| 5 | What is the program name of the service listening on it? / ¿Cuál es el nombre del programa del servicio que escucha en ese puerto? | `inspircd` |
| 6 | There is a script running in the background. Its name starts with THM. What is the name of the script? / Hay un script ejecutándose en segundo plano cuyo nombre empieza por THM. ¿Cómo se llama? | `THM-24765.sh` |

### Task 4: Enumeración - Windows / Enumerating Windows
**Explicación:** Con el laboratorio Windows Server desplegado se enumeran datos del sistema: el tipo de sistema/OS (Microsoft Windows Server 2019 Datacenter), la versión del SO (10.0.17763), el número de hotfixes instalados (30), el puerto TCP más bajo en escucha (22) y el programa que atiende ese puerto (sshd.exe).

```powershell
systeminfo                 # tipo de sistema, versión del SO y hotfixes
Get-Service | Where-Object {$_.Status -eq 'Running'}
netstat -ano | List-Observing &          # puertos en escucha
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full OS Name? / ¿Cuál es el nombre completo del sistema operativo? | `Microsoft Windows Server 2019 Datacenter` |
| 2 | What is the OS Version? / ¿Cuál es la versión del SO? | `10.0.17763` |
| 3 | How many hotfixes are installed on this MS Windows Server? / ¿Cuántos hotfixes hay instalados en este MS Windows Server? | `30` |
| 4 | What is the lowest TCP port number listening on the system? / ¿Cuál es el puerto TCP más bajo en escucha en el sistema? | `22` |
| 5 | What is the name of the program listening on that port? / ¿Cuál es el nombre del programa que escucha en ese puerto? | `sshd.exe` |

### Task 5: DNS, SMB y SNMP / DNS, SMB and SNMP
**Explicación:** Con la dirección IP del Windows Server (10.10.217.54, dominio redteam.thm) se practican tres protocolos de servicio: una transferencia de zona DNS con dig (la flag aparece en los registros obtenidos), el listado de un share SMB disponible (cuyo nombre comienza por THM y otorga una flag al montarlo) y una consulta SNMP con snmpcheck usando el community string público, que revela la location y da la tercera flag.

```bash
dig axfr @10.10.217.54 redteam.thm        # DNS zone transfer flag THM{DNS_ZONE}
smbclient -L \\\\10.10.217.54             # listar shares SMB (THM-...)
snmpcheck -t 10.10.217.54                 # obtener info SNMP (location flag)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag from the DNS zone transfer? / ¿Cuál es la flag de la transferencia de zona DNS? | `THM{DNS_ZONE}` |
| 2 | What is the flag of the SMB share named THM...? / ¿Cuál es la flag del share SMB llamado THM...? | `THM{829738}` |
| 3 | Knowing that the community string of the SNMP service is public, what is the location specified? / Sabiendo que el community string del servicio SNMP es public, ¿cuál es la location especificada? | `THM{SNMP_SERVICE}` |

### Task 6: Más herramientas para Windows / More Tools for Windows
**Explicación:** Introduce utilidades de Sysinternals para la enumeración de Windows; la que muestra los usuarios con sesión iniciada es PsLoggedOn.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What utility from Sysinternals Suite shows the logged-in users? / ¿Qué utilidad de Sysinternals Suite muestra los usuarios conectados? | `PsLoggedOn` |

### Task 7: Conclusión / Conclusion
**Explicación:** Resumen de la importancia de la enumeración en todas las fases del pentest.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above / Lee el contenido de la tarea. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command would you use to start the PowerShell interactive command line? | `powershell.exe` |
| 2 | In SSH key-based authentication, which key does the client need? | `private key` |
| 3 | What is the Linux distribution used in the VM? | `Ubuntu` |
| 4 | What is its version number? | `20.04.6` |
| 5 | What is the name of the user who last logged in to the system? | `randa` |
| 6 | What is the highest listening TCP port number? | `6667` |
| 7 | What is the program name of the service listening on it? | `inspircd` |
| 8 | There is a script running in the background. Its name starts with THM. What is the name of the script? | `THM-24765.sh` |
| 9 | What is the full OS Name? | `Microsoft Windows Server 2019 Datacenter` |
| 10 | What is the OS Version? | `10.0.17763` |
| 11 | How many hotfixes are installed on this MS Windows Server? | `30` |
| 12 | What is the lowest TCP port number listening on the system? | `22` |
| 13 | What is the name of the program listening on that port? | `sshd.exe` |
| 14 | What is the flag from the DNS zone transfer? | `THM{DNS_ZONE}` |
| 15 | What is the flag of the SMB share named THM...? | `THM{829738}` |
| 16 | Knowing that the community string of the SNMP service is public, what is the location specified? | `THM{SNMP_SERVICE}` |
| 17 | What utility from Sysinternals Suite shows the logged-in users? | `PsLoggedOn` |

---

**Metodología:** Se repasan las bases de la enumeración manual y el arranque de PowerShell. Sobre el laboratorio Linux se ejecutan comandos de enumeración (os-release, last, ss, ps). Sobre el Windows Server se usa systeminfo y análisis de puertos en escucha. Después se explotan protocolos de red local: transferencia de zona DNS (dig axfr), shares SMB (smbclient) y SNMP (snmpcheck), y se completa con Sysinternals (PsLoggedOn) para cerrar la recopilación de información.

### Cadena de ataque / Attack Chain

```text
Introducción (PowerShell / SSH keys) -> Linux: os-release, last, ss, ps -> Ubuntu 20.04.6, randa, 6667/inspircd, THM-24765.sh -> Windows: systeminfo, netstat -> Win 2019 17763, 30 hotfixes, 22/sshd.exe -> DNS zone transfer (THM{DNS_ZONE}) -> SMB share (THM{829738}) -> SNMP snmpcheck (THM{SNMP_SERVICE}) -> PsLoggedOn -> conclusión
```

**Learning chain:** Introduction → Purpose → Enumerating Linux → Enumerating Windows → DNS, SMB and SNMP → More Tools for Windows (PsLoggedOn) → Conclusion.

**Lección:** *La enumeración correcta y ordenada (SO, versiones, usuarios, puertos en escucha, servicios y protocolos de red) es lo que convierte una caja "desconocida" en un conjunto de vectores de ataque: casi todas las rutas de compromiso comienzan con los datos que se recopilan aquí.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1082 (System Information Discovery), T1033 (System Owner/User Discovery), T1016 (System Network Configuration Discovery)

**Fuente:** [TryHackMe - Enumeration](https://tryhackme.com/room/enumeration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.