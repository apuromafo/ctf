# Incident Handling With Splunk

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | SOC / SIEM / IR | incidenthandlingwithsplunk | https://tryhackme.com/room/incidenthandlingwithsplunk | 02 Level Medium | TryHackMe | Splunk, Suricata, Sysmon, Fortigate, OSINT | Defacement de servidor web / compromiso de CMS |

---

**Contexto:** Eres analista del SOC de Wayne Enterprises durante una investigación de incidente tras el defacement del sitio web corporativo `www.imreallynotbatman.com`. Se dispone de una instancia **Splunk** con logs ingeridos de múltiples orígenes: firewall Fortinet, IDS **Suricata**, **Sysmon**, IIS y tráfico HTTP (`stream:http`). El reto consiste en reconstruir la actividad del atacante sobre el servidor (192.168.250.70) siguiendo la **Cyber Kill Chain**: reconocimiento (escáner Acunetix, CVE-2014-6271/Shellshock), explotación (brute force al panel de Joomla), instalación (upload y ejecución de `3791.exe`), C2 (dominio `prankglassinebracket.jumpingcrab.com`), y acciones sobre el objetivo (defacement con `poisonivy-is-coming-for-you-batman.jpeg`). Se cierran los huecos con OSINT (VirusTotal, ThreatMiner, Robtex).

## Solucionario

### Task 1: Información del entorno
**Explicación:**

Se explora el índice `botsv1` y la pestaña *Data summary* de Splunk para conocer las fuentes de logs disponibles (suricata, XmlWinEventLog, fortigate_utm, stream:http, etc.) antes de iniciar la investigación.

Respuesta: `No answer needed`

### Task 2: Cyber Kill Chain
**Explicación:**

Se contextualiza la investigación dentro de las fases de la Cyber Kill Chain de Lockheed Martin, desde el reconocimiento hasta las acciones sobre el objetivo.

Respuesta: `No answer needed`

### Task 3: Fase de Reconocimiento
**Explicación:**

Se filtra el tráfico hacia el servidor (`index=botsv1 imreallynotbatman.com sourcetype=stream:http`) y se observan dos `src_ip`: `40.80.148.42` (mayor volumen y origen del escaneo) y `23.22.63.114`. Con `src=40.80.148.42 sourcetype=suricata` se revela en `alert.signature` el intento de explotación de **Shellshock**.

1. CVE asociado al intento de ataque: `CVE-2014-6271`
2. CMS del servidor web (visible en los campos `uri`, `uri_path`, `http_referrer`, `src_content`): `joomla`
3. Escáner web usado (campo `http_user_agent`): `acunetix`
4. IP del servidor `imreallynotbatman.com` (campo `dest_ip`): `192.168.250.70`

### Task 4: Fase de Explotación
**Explicación:**

Se buscan los POST al portal de administración de Joomla (`uri="/joomla/administrator/index.php" http_method=POST`) y se extrae `form_data`. El campo `username` es siempre `admin` y `passwd` varía: un usuario-agente `Python-urllib/2.7` desde la IP `23.22.63.114` automatiza el brute force, mientras un único intento con `Mozilla/5.0` desde `40.80.148.42` es el login exitoso. Con `rex field=form_data "passwd=(?<creds>\w+)"` y `| dedup creds` se cuenta el número de contraseñas únicas.

1. URI con múltiples intentos de brute force: `/joomla/administrator/index.php`
2. Usuario objetivo del brute force: `admin`
3. Contraseña correcta del panel de administración: `batman`
4. Contraseñas únicas intentadas: `412`
5. IP que intenta el brute force: `23.22.63.114`
6. IP usada para el login exitoso: `40.80.148.42`

### Task 5: Fase de Instalación
**Explicación:**

Se busca el archivo subido tras el acceso: `sourcetype=stream:http dest_ip="192.168.250.70" "*.exe"` revela en `part_filename{}` el binario malicioso `3791.exe` (y un `agent.php`) subidos desde la IP del atacante. En Sysmon (`sourcetype="XmlWinLogEvent" EventCode=1`) se ve la creación de proceso: la ejecución la realiza el usuario del pool de IIS. La comprobación del hash en VirusTotal muestra el segundo nombre asociado al binario.

1. MD5 HASH del programa `3791.exe`: `AAE3F5A29935E6ABCC2C2754D12A9AF0`
2. Usuario que ejecutó `3791.exe` en el servidor: `NT AUTHORITY\IUSR`
3. Otro nombre asociado a `3791.exe` (VirusTotal): `ab.exe`

### Task 6: Acciones sobre el objetivo
**Explicación:**

El servidor comprometido genera tráfico saliente hacia la infraestructura del atacante. Se filtra `src=192.168.250.70 sourcetype=suricata dest_ip=23.22.63.114` y se observa la descarga de una imagen desde el host del atacante. La imagen se sirve desde `/poisonivy-is-coming-for-you-batman.jpeg`. Por otro lado, el firewall `fortigate_utm` registra un intento de inyección SQL procedente de `40.80.148.42`.

1. Archivo que deface el sitio: `poisonivy-is-coming-for-you-batman.jpeg`
2. Regla disparada por el intento de SQL injection (Fortigate): `HTTP.URI.SQL.Injection`

### Task 7: Dominio de C2
**Explicación:**

El ataque usó **DNS dinámico** para resolver a la IP maliciosa. Se consulta el campo `url` en `fortigate_utm` y `stream:http` (`index=botsv1 sourcetype=stream:http dest_ip=23.22.63.114 "poisonivy-is-coming-for-you-batman.jpeg" src_ip=192.168.250.70`) para obtener el FQDN completo del C2.

Respuesta: `prankglassinebracket.jumpingcrab.com`

### Task 8: Atribución y asociación del malware
**Explicación:**

Con OSINT se correlacionan los indicadores: la IP `23.22.63.114` está vinculada por ThreatMiner/VirusTotal a los dominios pre-escalonados del grupo **P01s0n1vy** y a la cuenta de correo de contacto, además del malware `MirandaTateScreensaver.scr.exe` (`c99131e0169171935c5ac32615ed6261`) relacionado con la infraestructura Poison Ivy.

1. IP ligada a `P01s0n1vy` y sus dominios pre-stage: `23.22.63.114`
2. Correo asociado al grupo APT: `lillian.rose@po1s0n1vy.com`
3. Hash del malware asociado al grupo: `c99131e0169171935c5ac32615ed6261`
4. Nombre del malware de la infraestructura Poison Ivy: `MirandaTateScreensaver.scr.exe`

### Task 9: Fase de cierre
**Explicación:**

Se consolidan los hallazgos de todas las fases de la Kill Chain para emitir recomendaciones de detección, bloqueo y remediación.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3.1 | CVE asociado al intento de ataque | `CVE-2014-6271` |
| 3.2 | CMS del servidor web | `joomla` |
| 3.3 | Escáner web del atacante | `acunetix` |
| 3.4 | IP del servidor imreallynotbatman.com | `192.168.250.70` |
| 4.1 | URI con múltiples intentos de brute force | `/joomla/administrator/index.php` |
| 4.2 | Usuario objetivo del brute force | `admin` |
| 4.3 | Contraseña correcta del CMS | `batman` |
| 4.4 | Contraseñas únicas intentadas | `412` |
| 4.5 | IP que intenta el brute force | `23.22.63.114` |
| 4.6 | IP del login exitoso al panel | `40.80.148.42` |
| 5.1 | MD5 HASH de 3791.exe | `AAE3F5A29935E6ABCC2C2754D12A9AF0` |
| 5.2 | Usuario que ejecutó 3791.exe | `NT AUTHORITY\IUSR` |
| 5.3 | Otro nombre asociado a 3791.exe | `ab.exe` |
| 6.1 | Archivo que deface el sitio | `poisonivy-is-coming-for-you-batman.jpeg` |
| 6.2 | Regla de SQL injection (Fortigate) | `HTTP.URI.SQL.Injection` |
| 7 | FQDN del C2 (DNS dinámico) | `prankglassinebracket.jumpingcrab.com` |
| 8.1 | IP ligada a P01s0n1vy | `23.22.63.114` |
| 8.2 | Correo asociado al grupo APT | `lillian.rose@po1s0n1vy.com` |
| 8.3 | Hash del malware asociado al grupo | `c99131e0169171935c5ac32615ed6261` |
| 8.4 | Malware de la infraestructura Poison Ivy | `MirandaTateScreensaver.scr.exe` |

---

**Metodología:** Análisis SIEM con Splunk sobre el índice `botsv1` (Suricata, Sysmon/XmlWinLogEvent, fortigate_utm, stream:http): correlación de src/dest IP, extracción de credenciales con `rex`, conteo con `stats/dedup`, seguimiento del upload con `part_filename{}`, reconciliación con OSINT (VirusTotal, ThreatMiner, Robtex) y reconstrucción completa de la Cyber Kill Chain.

**Learning chain:** Data summary → reconocimiento (CVE/CMS/escáner) → explotación (brute force/credenciales) → instalación (upload y ejecución) → defacement → C2 por DNS dinámico → atribución OSINT → malware asociado.

**Lección:** *Splunk convierte logs dispares en una historia única: pivoteando de una IP a un campo y de un campo a un evento se reconstruye la cadena de ataque completa sin depender de una única fuente de verdad.*

**MITRE ATT&CK:** T1595.002 Active Scanning: Vulnerability Scanning · T1190 Exploit Public-Facing Application · T1110.001 Brute Force: Password Guessing · T1505.003 Web Shell · T1059.003 Command and Scripting Interpreter: Windows Command Shell · T1071.001 Application Layer Protocol: Web Protocols · T1491.001 Defacement: Internal Defacement · T1105 Ingress Tool Transfer.

**Fuente:** [TryHackMe - Incident Handling With Splunk](https://tryhackme.com/room/incidenthandlingwithsplunk)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.