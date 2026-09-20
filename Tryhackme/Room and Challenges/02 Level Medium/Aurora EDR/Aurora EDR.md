# Aurora EDR

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | auroraedr |
| Link | https://tryhackme.com/room/auroraedr |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Aurora EDR, Windows Event Logs, Deteccion de Ransomware |
| Impacto | Alto |

---

**Contexto:** Sala dedicada al uso de Aurora EDR (Endpoint Detection and Response) para detectar y analizar amenazas en endpoints Windows. Se cubre la arquitectura de telemetria, la revision de eventos del sistema, la clasificacion de alertas y la respuesta a incidentes de ransomware. El participante aprende a utilizar EDR para rastrear actividad maliciosa y tomar decisiones de containment.

## Solucionario

### Task 1: Introduccion a Aurora EDR
**Explicación:** Introduccion al framework Aurora EDR y su arquitectura. Se presenta como el EDR recopila y analiza telemetria del sistema para detectar amenazas.

1. No answer needed

### Task 2: Conceptos Fundamentales
**Explicación:** Definicion y comprension de Endpoint Detection and Response como capacidad de seguridad.

2. Endpoint Detection and Response

### Task 3: Arquitectura de Telemetria
**Explicación:** Exploracion de los componentes de la arquitectura de telemetria de Aurora EDR, incluyendo proveedores, consumidores y canales de error.

3. 1. Providers
   2. Consumers
   3. Error
   4. System

### Task 4: Analisis de Eventos
**Explicación:** Analisis detallado de eventos del sistema, incluyendo clasificacion de procesos, relaciones padre-hijo y metricas de severidad.

4. 1. Intense
   2. Great grandparent
   3. 103

### Task 5: Deteccion de Amenazas
**Explicación:** Configuracion y uso de reglas de deteccion para identificar comportamientos maliciosos en el endpoint.

5. No answer needed

### Task 6: Respuesta a Incidentes
**Explicación:** Procedimientos de respuesta a incidentes detectados por Aurora EDR, incluyendo contencion y erradicacion.

6. No answer needed

### Task 7: Analisis de Ransomware
**Explicación:** Analisis especifico de actividad ransomware utilizando Aurora EDR. Se identifican indicadores de compromiso, tecnicas de ejecucion y se clasifican las alertas por severidad.

7. 1. Process Reconnaissance Via Wmic.EXE
   2. 221b251a-357a-49a9-920a-271802777cc0
   3. medium
   4. Suspicious Creation TXT File in User Desktop
   5. Ransomware

### Task 8: Conclusion
**Explicación:** Revision final y cierre de la actividad de analisis con Aurora EDR.

8. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | `No answer needed` |
| 2 | Task 2 | `Endpoint Detection and Response` |
| 3 | Task 3.1 | `Providers` |
| 3 | Task 3.2 | `Consumers` |
| 3 | Task 3.3 | `Error` |
| 3 | Task 3.4 | `System` |
| 4 | Task 4.1 | `Intense` |
| 4 | Task 4.2 | `Great grandparent` |
| 4 | Task 4.3 | `103` |
| 5 | Task 5 | `No answer needed` |
| 6 | Task 6 | `No answer needed` |
| 7 | Task 7.1 | `Process Reconnaissance Via Wmic.EXE` |
| 7 | Task 7.2 | `221b251a-357a-49a9-920a-271802777cc0` |
| 7 | Task 7.3 | `medium` |
| 7 | Task 7.4 | `Suspicious Creation TXT File in User Desktop` |
| 7 | Task 7.5 | `Ransomware` |
| 8 | Task 8 | `No answer needed` |

---

**Metodología:** Endpoint Detection and Response (EDR) con Aurora. Analisis de telemetria, deteccion de ransomware y respuesta a incidentes en endpoints Windows.

**Learning chain:** Arquitectura EDR -> Recopilacion de telemetria -> Analisis de eventos -> Deteccion de ransomware -> Respuesta a incidentes

**Lección:** _Un EDR efectivo permite rastrear la actividad completa de un adversario desde la ejecucion inicial hasta el impacto final._

**MITRE ATT&CK:** TA0002 (Execution), T1059.001 (PowerShell), T1047 (WMI), T1486 (Data Encrypted for Impact), TA0040 (Impact)

**Fuente:** [TryHackMe - Aurora EDR](https://tryhackme.com/room/auroraedr)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
