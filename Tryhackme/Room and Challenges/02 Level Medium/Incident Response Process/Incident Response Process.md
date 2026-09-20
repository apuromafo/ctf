# Incident Response Process

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | IR / DFIR / Windows | incidentresponseprocess | https://tryhackme.com/room/incidentresponseprocess | 02 Level Medium | TryHackMe | NIST 800-61, Windows, VBA Macro, certutil, netstat | Compromiso por minero de criptomonedas |

---

**Contexto:** Un usuario reporta que su estación Windows está extremadamente lenta. TI confirma un uso anómalo de CPU, el SOC observa conexiones salientes repetitivas desde el equipo hacia una única IP externa y el caso se escala al equipo de respuesta a incidentes. El análisis revela el proceso `32th4ckm3.exe` consumiendo CPU y contactando con su C2 (`45.33.32.156:42424`). El vector inicial es un documento Word con macros (`invoice n. 65748224.docm`) cuyo macro `AutoOpen` usa `certutil` (LOLBin) para descargar y ejecutar el minero y establecer persistencia en el registro. La sala recorre el framework de **NIST SP 800-61**, haciendo hincapié en la fase de *Detection and Analysis* y la contención/erradicación en una VM de laboratorio.

## Solucionario

### Task 1: Introducción
**Explicación:**

Se presenta el framework de respuesta a incidentes de NIST y el alcance de la sala: un caso práctico de minero de criptomonedas en una máquina Windows.

Respuesta: `No answer needed`

### Task 2: Fases del framework
**Explicación:**

Se identifica la fase del framework NIST en la que los responders suelen ser llamados a la acción, cuando el incidente ya fue detectado y requiere análisis.

Respuesta: `Detection and Analysis`

### Task 3: Detección y análisis
**Explicación:**

En la VM se abre el Administrador de tareas (vista *More details*): el proceso `32th4ckm3.exe` (PID 4668) consume unos 50% de CPU. Con su PID, `netstat -aofn | find "{PID}"` revela la conexión saliente al C2. El historial del navegador muestra la descarga del documento `invoice n. 65748224.docm` desde una URL basada en IP. Al analizar el macro `AutoOpen` (Ver → Macros → Edit) se observa que usa `certutil` para descargar el minero de forma sigilosa y ejecutarlo en ventana oculta.

1. Proceso sospechoso de minería: `32th4ckm3.exe`
2. IP:puerto del C2 del malware: `45.33.32.156:42424`
3. Documento con el macro malicioso: `invoice n. 65748224.docm`
4. Sitio desde el que se descargó el minero: `http://172.233.61.246/`
5. Utilidad usada por el macro para descargar el malware: `certutil`

### Task 4: Contención, erradicación y recuperación
**Explicación:**

Para actuar sobre los IOCs: se abre Properties del proceso en el Administrador de tareas para localizar la carpeta del ejecutable malicioso (en Temp) y se usa `regedit` para inspeccionar la clave `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, donde se encuentra el valor de persistencia añadido por el minero.

1. Carpeta del proceso malicioso (ruta completa): `C:\Users\TryCleanUser\AppData\Local\Temp\2`
2. Valor de la clave Run añadido para persistencia: `DefaultApp`

### Task 5: Desarrollo del plan
**Explicación:**

El objetivo de una fase de preparación eficaz es tener documentado y ensayado el plan de gestión del incidente antes de que ocurra.

Respuesta: `Incident Response Plan`

### Task 6: Cierre
**Explicación:**

Se consolidan los aprendizajes del caso práctico (detección, análisis, contención, erradicación y recuperación) y las lecciones sobre macros maliciosas y LOLBins.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Fase del framework en la que actúan los responders | `Detection and Analysis` |
| 3.1 | Proceso sospechoso de minería | `32th4ckm3.exe` |
| 3.2 | IP:puerto del C2 | `45.33.32.156:42424` |
| 3.3 | Documento con el macro malicioso | `invoice n. 65748224.docm` |
| 3.4 | Sitio de descarga del minero | `http://172.233.61.246/` |
| 3.5 | Utilidad usada por el macro | `certutil` |
| 4.1 | Carpeta del proceso malicioso (ruta completa) | `C:\Users\TryCleanUser\AppData\Local\Temp\2` |
| 4.2 | Valor de la clave Run para persistencia | `DefaultApp` |
| 5 | Meta de la fase de preparación | `Incident Response Plan` |

---

**Metodología:** IR basado en NIST SP 800-61: triage de rendimiento en la VM (Administrador de tareas), confirmación de C2 con `netstat -aofn | find "{PID}"`, revisión de historial del navegador, análisis del macro VBA `AutoOpen` en el .docm, recopilación de IOCs, contención (bloqueo red, finalización de proceso) y erradicación (borrado del binario en Temp, restauración de la clave Run y limpieza del historial).

**Learning chain:** Fase del framework → detección del proceso anómalo → C2 → origen (docm) → LOLBin (certutil) → persistencia (Run) → contención → erradicación → plan de respuesta.

**Lección:** *Los LOLBins como certutil permiten descargar malware sin disparar alertas: en IR, los indicadores de red (conexiones C2) y las claves de persistencia (Run) son las pistas que confirman una infección de la que no hay alerta de EDR.*

**MITRE ATT&CK:** T1566.001 Phishing: Spearphishing Attachment · T1204.002 User Execution: Malicious File · T1059.005 Command and Scripting Interpreter: Visual Basic · T1105 Ingress Tool Transfer · T1071.001 Application Layer Protocol: Web Protocols · T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder · T1027 Obfuscated Files or Information.

**Fuente:** [TryHackMe - Incident Response Process](https://tryhackme.com/room/incidentresponseprocess)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.