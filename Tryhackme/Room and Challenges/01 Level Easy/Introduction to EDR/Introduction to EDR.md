# Introduction to EDR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontoedr` | [TryHackMe](https://tryhackme.com/room/introductiontoedr) | 01 Level Easy | TryHackMe | EDR, Visibility, Telemetry, Agent, Sensor, IOC Matching, Triage | Fundamentos de Endpoint Detection and Response: visibilidad, telemetría, componentes, detección por IOC y triage de alertas |

> **Objeto:** Comprender cómo funciona un EDR (Endpoint Detection and Response): qué lo diferencia de un antivirus, qué visibilidad ofrece, qué telemetría recopila (procesos, conexiones, registro), cómo se despliega (agente y sensor), cómo detecta mediante IOC Matching y cómo investigar una alerta de triage en la consola.

---

**Contexto:** Sala del path SOC Level 1 que explica el EDR: qué es y qué añade frente al antivirus tradicional (visibilidad y contexto completo de las detecciones), la analogía del aeropuerto (immigration check = AV, EDR = equipo de seguridad), la telemetría que se recopila de los endpoints (procesos como cmd.exe o svchost.exe, conexiones de red, registro), los componentes de despliegue (agente y sensor), la detección por coincidencia de indicadores (IOC Matching) y un ejercicio final investigando una alerta real en la consola EDR: cadena WINWORD.EXE -> CMD.EXE -> CURL.EXE en DESKTOP-HR01, la descarga a C:\Users\Public\install.exe, el binario sospechoso syncsvc.exe de WIN-ENG-LAPTOP03, una exfiltración a WeTransfer y el veredicto final de la herramienta interna conocida.

> **ES:** Sala de introducción a EDR: visibilidad, telemetría, agente/sensor, detección por IOC Matching y triage de una alerta real en la consola.
> **EN:** Introduction to EDR room: visibility, telemetry, agent/sensor, IOC Matching detection and triage of a real alert in the console.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: qué es el EDR, por qué es esencial como analista de SOC y qué aspectos se van a cubrir (detección, telemetría y triage).

No answer needed

### Task 2: ¿Qué es un EDR? / What is an EDR?
**Explicación:** Se aprende qué es un EDR: la característica que proporciona contexto completo de todas las detecciones (visibility) y se identifica el proceso del escenario (cmd.exe).

1. Visibility
2. cmd.exe

### Task 3: Más allá del antivirus / Beyond the Antivirus
**Explicación:** Mediante la analogía del aeropuerto se entiende la diferencia con el AV: qué representa el AV en la analogía (immigration check), qué proceso legítimo fue secuestrado en el escenario (svchost.exe) y la solución de seguridad tradicional del endpoint (Antivirus).

1. immigration check
2. svchost.exe
3. Antivirus

### Task 4: ¿Cómo funciona el EDR? / How Does EDR Work?
**Explicación:** Se explican los componentes de despliegue del EDR: el agente instalado en el endpoint y el sensor que recopila los datos de telemetría.

1. Agent
2. sensor

### Task 5: Datos de telemetría / Telemetry Data
**Explicación:** Se repasan los tipos de datos que recopila el EDR: las conexiones de red (Network Connections) y el registro del sistema (registry).

1. Network Connections
2. registry

### Task 6: Detección / Detection
**Explicación:** Se aprende cómo detecta el EDR mediante la coincidencia de indicadores de compromiso conocidos (IOC Matching).

IOC Matching

### Task 7: Investiga una alerta en el EDR / Investigate an Alert on EDR
**Explicación:** Ejercicio de triage sobre la alerta: en DESKTOP-HR01 la cadena WINWORD.EXE -> CMD.EXE -> CURL.EXE descarga el payload a C:\Users\Public\install.exe; en WIN-ENG-LAPTOP03 el binario sospechoso syncsvc.exe se lanza desde la carpeta Temp, intenta volcar lsass y exfiltra el dump a WeTransfer; el veredicto del último evento es la herramienta interna de TI conocida.

1. CURL.exe
2. C:\Users\Public\install.exe
3. C:\Users\haris.khan\AppData\Local\Temp\syncsvc.exe
4. https://files-wetransfer.com/upload/session/ab12cd34ef56/dump_2025.dmp
5. Known internal IT utility tool

### Task 8: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2.1 | ¿Qué característica del EDR proporciona un contexto completo de todas las detecciones? | `Visibility` |
| 2.2 | ¿Qué proceso lanzó sc.exe en el escenario? | `cmd.exe` |
| 3.1 | En la analogía dada, ¿qué representa un AV? | `immigration check` |
| 3.2 | ¿Qué proceso legítimo fue secuestrado por el atacante en el escenario? | `svchost.exe` |
| 3.3 | Solución de seguridad tradicional del endpoint | `Antivirus` |
| 4.1 | Componente instalado en el endpoint | `Agent` |
| 4.2 | Componente que recopila los datos | `sensor` |
| 5.1 | Tipo de telemetría que registra las conexiones de red | `Network Connections` |
| 5.2 | Tipo de telemetría que registra los cambios del registro | `registry` |
| 6 | Técnica de detección mediante indicadores conocidos | `IOC Matching` |
| 7.1 | ¿Qué herramienta lanzó CMD.exe para descargar el payload en DESKTOP-HR01? | `CURL.exe` |
| 7.2 | Ruta absoluta del malware descargado en DESKTOP-HR01 | `C:\Users\Public\install.exe` |
| 7.3 | Ruta absoluta del sospechoso syncsvc.exe en WIN-ENG-LAPTOP03 | `C:\Users\haris.khan\AppData\Local\Temp\syncsvc.exe` |
| 7.4 | URL del intento de exfiltración en WIN-ENG-LAPTOP03 | `https://files-wetransfer.com/upload/session/ab12cd34ef56/dump_2025.dmp` |
| 7.5 | Veredicto del evento final | `Known internal IT utility tool` |
| 8 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Estudio conceptual del EDR y su diferencia con el antivirus (visibilidad y contexto), análisis de la telemetría recopilada en el endpoint (procesos, conexiones y registro), revisión de los componentes (agente y sensor), comprensión de la detección por IOC Matching y triage práctico de una alerta real en la consola EDR siguiendo la cadena de procesos, los paths de los artefactos, la URL de exfiltración y el veredicto del evento.

### Cadena de ataque / Attack Chain

Documento macro (invoice.docm) -> WINWORD.EXE -> CMD.EXE -> CURL.EXE -> descarga a C:\Users\Public\install.exe -> syncsvc.exe desde Temp -> acceso a lsass (credential dumping) -> exfiltración a WeTransfer -> veredicto (Known internal IT utility tool)

**Learning chain:** EDR -> visibility -> antivirus analogy -> telemetry -> agent/sensor -> IOC Matching -> alert triage -> process chain

**Lección:** *Un EDR aporta la visibilidad y el contexto que el antivirus no ofrece; dominar la telemetría y la cadena de procesos permite convertir una alerta aislada en el relato completo de un compromiso.*

**MITRE ATT&CK:** T1003.001 (OS Credential Dumping: LSASS Memory) / T1041 (Exfiltration Over C2 Channel).

**Fuente:** [TryHackMe - Introduction to EDR](https://tryhackme.com/room/introductiontoedr)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.