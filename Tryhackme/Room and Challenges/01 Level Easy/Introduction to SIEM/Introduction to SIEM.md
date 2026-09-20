# Introduction to SIEM

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontosiem` | [TryHackMe](https://tryhackme.com/room/introductiontosiem) | 01 Level Easy | TryHackMe | SIEM, Elastic Stack, recolección de logs, análisis de eventos, dashboards, correlación | Comprender qué es un SIEM, cómo se ingieren y analizan los logs y cómo responder ante detecciones y falsos positivos. |

---

**Contexto:** Sala introductoria a los SIEM (Security Information and Event Management). Explica qué es un sistema de gestión de información y eventos de seguridad, los modelos de datos host-centric y network-centric, cómo se recogen los registros de distintas fuentes y se presentan en dashboards. Incluye un laboratorio con Elastic (Kibana) donde el alumno analiza logs reales, distingue verdaderos positivos y falsos positivos e investiga un incidente de minería de criptomoneda. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Definir SIEM, distinguir los enfoques host-centric y network-centric, localizar los logs de Apache, interpretar en el dashboard los eventos y resolver el incidente de cryptomining hasta obtener la flag.
> **EN:** Define SIEM, distinguish host-centric and network-centric approaches, locate the Apache logs, read the events on the dashboard and solve the cryptomining incident until the flag is recovered.

## Solucionario

### Task 1: ¿Qué es un SIEM? / What is a SIEM?
**Explicación:** Se define el concepto de SIEM como Security Information and Event Management system y el valor de centralizar los eventos de seguridad.

1. Security Information and Event Management system

### Task 2: Modelos de datos / Data Models
**Explicación:** Se distinguen los dos enfoques principales de captura de datos: centrado en el host y centrado en la red.

1. host-centric
2. network-centric

### Task 3: Recolección de logs / Log Collection
**Explicación:** Se practica con las fuentes de registro, localizando a modo de ejemplo los logs del servidor web Apache.

1. /var/log/httpd

### Task 4: Laboratorio SIEM / SIEM Lab
**Explicación:** Se explora el entorno de laboratorio con Elastic y los dashboards disponibles.

1. No answer needed

### Task 5: Análisis de eventos / Event Analysis
**Explicación:** Se interpretan los eventos mostrados en el dashboard, identificando un evento concreto y clasificando la alerta como falso positivo.

1. 104
2. False Alarm

### Task 6: Investigación del incidente / Incident Investigation
**Explicación:** Se investiga un incidente de cryptomining siguiendo el proceso de ejecución del malware: el binario malicioso, las cuentas implicadas, el grupo, la clasificación de la detección y la flag.

1. cudominer.exe
2. chris.fort
3. HR_02
4. miner
5. True-Positive
6. THM{000_SIEM_INTRO}

### Task 7: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre el flujo completo de trabajo con un SIEM.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa SIEM? / What does SIEM stand for? | `Security Information and Event Management system` |
| 2 | Modelo centrado en el host / Host-centric data model | `host-centric` |
| 3 | Modelo centrado en la red / Network-centric data model | `network-centric` |
| 4 | Logs del servidor web Apache / Apache web server logs | `/var/log/httpd` |
| 5 | (Pregunta 5 no especificada en el original) | `No answer needed` |
| 6 | ID del evento analizado / ID of the analysed event | `104` |
| 7 | Clasificación de la alerta / Alert classification | `False Alarm` |
| 8 | Binario malicioso / Malicious binary | `cudominer.exe` |
| 9 | Cuenta implicada / Involved account | `chris.fort` |
| 10 | Equipo afectado / Affected team | `HR_02` |
| 11 | Grupo del proceso / Process group | `miner` |
| 12 | Tipo de detección / Detection type | `True-Positive` |
| 13 | Flag del incidente / Incident flag | `THM{000_SIEM_INTRO}` |
| 14 | (Pregunta 14 no especificada en el original) | `No answer needed` |

---

**Metodología:** Estudiar el concepto de SIEM y los modelos de datos, identificar las rutas de logs habituales, explorar el dashboard de Kibana, revisar cada evento de forma posicional, clasificar la alerta y reconstruir el incidente de cryptomining para obtener la flag.

### Cadena de ataque / Attack Chain

```text
definición de SIEM -> modelos host/network-centric -> recolección de logs (/var/log/httpd) -> dashboard Kibana -> análisis de eventos (104) -> falso positivo -> incidente cryptomining -> flag THM{000_SIEM_INTRO}
```

**Learning chain:** SIEM -> Elastic Stack -> ingesta de logs -> dashboards -> análisis de eventos -> verdaderos/falsos positivos -> investigación de incidentes.

**Lección:** *Un SIEM no es solo un almacén de logs: la capacidad de correlacionar eventos, clasificar alertas como verdaderos o falsos positivos y reconstruir la cadena completa de un incidente es lo que convierte los datos en respuesta.*

**MITRE ATT&CK:** T1496 (Resource Hijacking), T1036 (Masquerading), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1562 (Impair Defenses)

**Fuente:** [TryHackMe - Introduction to SIEM](https://tryhackme.com/room/introductiontosiem)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.