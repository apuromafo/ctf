# Sysmon

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (Blue Team / Windows) |
| **Slug** | `sysmon` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sysmon) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Sysmon / Event ID 1 (process creation) / Event ID 3 (network connection) / Event ID 5 (process terminated) / Event ID 6 (driver loaded) / Event ID 7 (image loaded) / Windows Event Logs / análisis de incidentes |
| **Impacto** | Sala que explica qué es Sysmon, cómo se despliega y configura, y enseña a leer sus eventos de proceso, red, terminación, controladores y librerías cargadas. La sección final plantea cuatro investigaciones donde se debe reconstruir una cadena de ataque completa: un dispositivo USB que invoca `svchost.exe`, una campaña de PowerShell oculta de Empire (malware "Turbo Tactics"), persistencia vía registro y tareas programadas, y acceso a credenciales vía `lsass.exe`. |

---

**Contexto:** Sysmon (System Monitor) es un driver y servicio de Windows que registra una gran variedad de eventos de sistema con Event IDs útiles para el Blue Team. La sala repasa los IDs principales: **1** (creación de procesos), **3** (conexiones de red), **5** (proceso terminado), **6** (controlador cargado) y **7** (imagen/iibrería cargada). Los datos del volcado incluyen el análisis de un log con 73.591 eventos de red (Event ID 3) cuyo primer evento tiene UTC time `2021-01-06 01:35:50.464`. La investigación final (20 respuestas) desmenuza el ataque "Badge/DFIR" de Empire y Rusty: la cadena empieza con un USB (registro `HKLM\System\CurrentControlSet\Enum\WpdBusEnumRoot\...\FriendlyName`), pasa por `rundll32.exe` descargando `update.hta`/`update.html` vía `mshta.exe`, establece C2 con `172.30.1.253` (Empire/empirec2) sobre el puerto 4443, persiste con `powershell -enc` desde `HKLM\SOFTWARE\Microsoft\Network\debug` y `schtasks`, y termina tocando `lsass.exe` y exfiltrando por el puerto 80.

## Solucionario

### Task 1: Introducción

**Explicación:** Presenta Sysmon y su papel como herramienta clave del Blue Team. La descripción del módulo dice: "System Monitor is a Windows service/driver and system monitoring tool which logs events of importance".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Despliegue y opciones de instalación

**Explicación:** Cubre las opciones de despliegue de Sysmon (instaladores, configs XML y monitoreo de tráfico DNS).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee las opciones de despliegue e instalación de Sysmon. | `No answer needed` |

### Task 3: Componentes y configuración

**Explicación:** Revisa los componentes de Sysmon (driver, servicio, proceso) y cómo se configura vía archivo XML con filtros y categorías de eventos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee los componentes y la configuración de Sysmon. | `No answer needed` |

### Task 4: Registro de eventos: leyendo los eventos

**Explicación:** Se cargan los archivos de log de Event Viewer para practicar la lectura de eventos. En el log analizado hay exactamente **73.591 eventos de red** (Event ID 3). El primer evento de red del log tiene como UTC time `2021-01-06 01:35:50.464` (se muestra en la pestaña "Details" del visor de eventos).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee los conceptos sobre el registro de eventos de Sysmon. | `No answer needed` |
| 2 | ¿Cuántos eventos con Event ID 3 hay en el log `Filtering.evtx`? | `73,591` |
| 3 | ¿Cuál es el UTC time del primer evento de red del mismo log? (El UTC time solo se muestra en la pestaña "Details"). | `2021-01-06 01:35:50.464` |

### Task 5: Event ID 1: Proceso creado

**Explicación:** El Event ID 1 registra la creación de procesos con utilidad de los clásicos "applicable to windows logging, to know you".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del Event ID 1 (process creation). | `No answer needed` |

### Task 6: Event ID 3: Conexión de red

**Explicación:** El Event ID 3 documenta conexiones de red (origen, destino, puerto, protocolo).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del Event ID 3 (network connections). | `No answer needed` |

### Task 7: Event ID 5: Proceso terminado

**Explicación:** El Event ID 5 señala cuándo un proceso ha terminado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del Event ID 5 (process terminated). | `No answer needed` |

### Task 8: Event ID 6: Controlador cargado

**Explicación:** El Event ID 6 registra cuándo se carga un controlador en el kernel.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del Event ID 6 (driver loaded). | `No answer needed` |

### Task 9: Event ID 7: Imagen cargada

**Explicación:** El Event ID 7 indica cuándo un proceso carga una librería/imagen (DLL).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del Event ID 7 (image loaded). | `No answer needed` |

### Task 10: Badge/Investigación Sysmon

**Explicación:** Cuatro investigaciones sobre los logs de una víctima. En la **Investigación 1**, la cadena empieza cuando un dispositivo USB (SanDisk U3 Cruzer Micro) conectado como volumen invoca a `svchost.exe`; la clave de registro completa es `HKLM\System\CurrentControlSet\Enum\WpdBusEnumRoot\...\FriendlyName` y el dispositivo es leído como `\Device\HarddiskVolume3`. En la **Investigación 2**, `svchost.exe` lanza `rundll32.exe` que descarga `update.hta` (carpeta Internet Explorer) y `update.html` (Downloads), ejecutados por `mshta.exe`; el tráfico C2 apunta a `10.0.2.18:4443` y al servidor Empire `172.30.1.253` (nombre de agente `empirec2`, host `DESKTOP-O153T4R`). En la **Investigación 3**, el payload se persiste en `HKLM\SOFTWARE\Microsoft\Network\debug` y se ejecuta con `powershell -enc`; la descarga usa `172.168.103.188` y el búfer ADS `c:\users\q\AppData:blah.txt`, con persistencia vía `schtasks /Create`. En la **Investigación 4**, el atacante accede a `lsass.exe`, conecta al C2 `172.30.1.253` por el puerto `80` y el framework usado es **Empire**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la clave de registro completa del dispositivo USB que llama a svchost.exe en la Investigación 1? | `HKLM\System\CurrentControlSet\Enum\WpdBusEnumRoot\UMB\2&37c186b&0&STORAGE#VOLUME#_??_USBSTOR#DISK&VEN_SANDISK&PROD_U3_CRUZER_MICRO&REV_8.01#4054910EF19005B3&0#\FriendlyName` |
| 2 | ¿Cuál es el nombre del dispositivo cuando es llamado por RawAccessRead en la Investigación 1? | `\Device\HarddiskVolume3` |
| 3 | ¿Qué proceso hijo crea svchost.exe en la Investigación 2? | `rundll32.exe` |
| 4 | ¿Cuál es la ruta completa del archivo `update.hta` descargado? | `C:\Users\IEUser\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\S97WTYG7\update.hta` |
| 5 | ¿Cuál es la ruta completa del archivo `update.html` descargado? | `C:\Users\IEUser\Downloads\update.html` |
| 6 | ¿Qué proceso ejecuta el archivo descargado (HTA/HTML)? | `C:\Windows\System32\mshta.exe` |
| 7 | ¿Cuál es el IP de origen de la descarga del payload? | `10.0.2.18` |
| 8 | ¿Qué puerto utiliza la conexión de red del payload? | `4443` |
| 9 | ¿Cuál es el IP del servidor Empire (C2)? | `172.30.1.253` |
| 10 | ¿Cuál es el nombre del equipo comprometido (destino del C2)? | `DESKTOP-O153T4R` |
| 11 | ¿Cuál es el nombre del agente/unidad de carga de Empire? | `empirec2` |
| 12 | ¿En qué clave de registro se persiste el payload en la Investigación 3.1? | `HKLM\SOFTWARE\Microsoft\Network\debug` |
| 13 | ¿Cuál es la línea de comandos usada para ejecutar el payload (PowerShell) en la Investigación 3? | `"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -c "$x=$((gp HKLM:Software\Microsoft\Network debug).debug);start -Win Hidden -A \"-enc $x\" powershell";exit;` |
| 14 | ¿Cuál es el IP del servidor que sirve el payload en la Investigación 3.2? | `172.168.103.188` |
| 15 | ¿Cuál es la ruta del archivo al que se accede (ADS) para leer el payload? | `c:\users\q\AppData:blah.txt` |
| 16 | ¿Qué comando crea la tarea programada para la persistencia? | `"C:\WINDOWS\system32\schtasks.exe" /Create /F /SC DAILY /ST 09:00 /TN Updater /TR "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -c \"IEX ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String($(cmd /c ''more < c:\users\q\AppData:blah.txt'''))))\""` |
| 17 | ¿Qué proceso es atacado para obtener credenciales (LSASS) en la Investigación 4? | `lsass.exe` |
| 18 | ¿A qué IP conecta la red de exfiltración en la Investigación 4? | `172.30.1.253` |
| 19 | ¿Qué puerto usa esa conexión de red? | `80` |
| 20 | ¿Qué framework de C2 se utilizó en la cadena completa? | `Empire` |

---

**Metodología:** Instalación/lectura de la config de Sysmon → lectura de event logs en Event Viewer → conteo y filtrado de eventos (Event ID 3) → correlación de la cadena USB → rundll32/mshta (descarga) → C2 Empire (red) → persistencia (registro + schtasks) → credential access (lsass) → exfiltración.
**Learning chain:** qué es Sysmon y cómo se configura → lectura de Event IDs 1/3/5/6/7 → análisis del log de eventos de red → reconstrucción de una intrusión completa (USB → descarga → C2 → persistencia → credenciales → salida).
**MITRE ATT&CK:** T1200 (Hardware Additions), T1218.011 (Rundll32), T1218.005 (Mshta), T1059.001 (PowerShell), T1053.005 (Scheduled Task), T1003.001 (LSASS Memory), T1071.001 (Application Layer Protocol: Web)
**Fuente:** [TryHackMe - Sysmon](https://tryhackme.com/room/sysmon)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
