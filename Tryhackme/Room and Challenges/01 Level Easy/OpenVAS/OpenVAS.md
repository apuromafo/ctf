# OpenVAS

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `openvas` | [TryHackMe](https://tryhackme.com/room/openvas) | `01 Level Easy` | THM | OpenVAS, escaneo de vulnerabilidades, MS17-010 | Reconocimiento y análisis de vulnerabilidades |

> **Objeto:** Aprender a utilizar OpenVAS para lanzar un escaneo de vulnerabilidades contra una máquina Windows y analizar el informe resultante, con especial atención a la detección de MS17-010 (EternalBlue).

---

**Contexto:** La sala enseña a instalar, configurar y ejecutar OpenVAS contra un objetivo Windows. El informe obtenido revela la detección de MS17-010 (EternalBlue), con sus fechas de escaneo, número de puertos abiertos, severidad, sistema afectado y el procedimiento para confirmar la vulnerabilidad.

> **ES:** La sala enseña a instalar, configurar y ejecutar OpenVAS contra un objetivo Windows. El informe obtenido revela la detección de MS17-010 (EternalBlue), con sus fechas de escaneo, número de puertos abiertos, severidad, sistema afectado y el procedimiento para confirmar la vulnerabilidad.

> **EN:** The room teaches how to install, configure and run OpenVAS against a Windows target. The resulting report reveals the detection of MS17-010 (EternalBlue), with its scan dates, number of open ports, severity, affected system and the procedure to confirm the vulnerability.

## Solucionario

### Task 1: OpenVAS / OpenVAS

**Explicación:** La tarea recorre el uso completo de OpenVAS: preparación del escáner, configuración del escaneo sobre el objetivo Windows y análisis del informe final. El contenido original, conservado íntegramente, es el siguiente:

1. No answer needed
2. No answer needed
3. No answer needed
4. No answer needed
5. No answer needed
6. No answer needed
7. 1. Feb 28, 00:04:46
   2. Feb 28, 00:21:02
   3. 3
   4. 5
   5. MS17-010
   6. Microsoft Windows 10 x32/x64 Edition
   7. Send the crafted SMB transaction request with fid = 0 and check the response to confirm the vulnerability.
8. No answer needed

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | No answer needed (paso 1) | `No answer needed` |
| 2 | No answer needed (paso 2) | `No answer needed` |
| 3 | No answer needed (paso 3) | `No answer needed` |
| 4 | No answer needed (paso 4) | `No answer needed` |
| 5 | No answer needed (paso 5) | `No answer needed` |
| 6 | No answer needed (paso 6) | `No answer needed` |
| 7.1 | Fecha y hora de inicio del escaneo | `Feb 28, 00:04:46` |
| 7.2 | Fecha y hora de finalización del escaneo | `Feb 28, 00:21:02` |
| 7.3 | Respuesta del apartado 7.3 | `3` |
| 7.4 | Respuesta del apartado 7.4 | `5` |
| 7.5 | Vulnerabilidad detectada (CVE/identificador) | `MS17-010` |
| 7.6 | Sistema operativo afectado | `Microsoft Windows 10 x32/x64 Edition` |
| 7.7 | Procedimiento para confirmar la vulnerabilidad | `Send the crafted SMB transaction request with fid = 0 and check the response to confirm the vulnerability.` |
| 8 | No answer needed (paso 8) | `No answer needed` |

---

**Metodología:** 1) Instalar y arrancar OpenVAS. 2) Configurar el escaneo contra el objetivo Windows. 3) Ejecutar el escaneo y esperar al informe. 4) Analizar el informe: fechas del escaneo (Feb 28, 00:04:46 → Feb 28, 00:21:02), puertos abiertos (`3`), severidad (`5`), vulnerabilidad MS17-010, sistema afectado (Microsoft Windows 10 x32/x64 Edition) y cómo confirmarla (enviar la solicitud SMB manipulada con fid = 0 y comprobar la respuesta). 5) Registrar los pasos sin respuesta requerida.

### Cadena de ataque / Attack Chain

1. Preparación del escáner OpenVAS.
2. Configuración y lanzamiento del escaneo contra el objetivo Windows.
3. Análisis del informe: fechas, puertos y severidad.
4. Detección de MS17-010 / EternalBlue en Windows 10.
5. Confirmación manual de la vulnerabilidad vía SMB (fid = 0).

**Learning chain:** OpenVAS setup → configuración del escaneo → vulnerability scan → MS17-010 / EternalBlue → análisis del informe

**Lección:** *Un escáner de vulnerabilidades automatiza el reconocimiento y estructura el informe (puertos, CVEs, severidades), pero la confirmación manual de la vulnerabilidad es lo que acredita su explotabilidad real.*

**MITRE ATT&CK:** T1595.002 - Active Scanning: Vulnerability Scanning, T1046 - Network Service Discovery, T1210 - Exploitation of Remote Services

**Fuente:** [TryHackMe - OpenVAS](https://tryhackme.com/room/openvas)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.