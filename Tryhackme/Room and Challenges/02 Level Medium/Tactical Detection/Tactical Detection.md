# Tactical Detection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Defensivo / Detection | tacticaldetection | https://tryhackme.com/room/tacticaldetection | 02 Level Medium | TryHackMe | Sigma, Elastic/ELK, Winlogbeat, Sysmon, Follina CVE-2022-30190 | Detección de intrusión mediante reglas Sigma y analítica de endpoints |

---

**Contexto:** La sala **Tactical Detection** es un ejercicio defensivo donde el alumno detecta una intrusión empresarial paso a paso usando el stack **Elastic** (Winlogbeat) y reglas **Sigma**: se analiza el binario malicioso descargado (`bad3xe69.exe`) y su puerto de comunicación, se construye el job de ingesta en Kibana/Logstash con su index pattern (`winlogbeat-*`), se revisan los eventos de acceso a objetos frente a Sysmon (eventos 4656/4658), se diagnostica el fallo documentando un **Follina** (CVE-2022-30190) y se prioriza el hallazgo como ejercicio de **Purple Team**.

## Solucionario

### Task 1: Preparación
**Explicación:**

Se prepara el entorno de detección y se confirma el acceso a los paneles analíticos sin respuesta requerida.

Respuesta: `No answer needed`

### Task 2: Análisis del binario malicioso
**Explicación:**

Con el binario bajo investigación se responde qué formato de reglas se usará (Sigma), y se documenta el canal de comunicación (dominio), la ruta del ejecutable descargado y el método de salida identificado.

1. `Sigma`
2. `bad3xe69connection.io`
3. `C:\Downloads\bad3xe69.exe`
4. `proxy`

### Task 3: Configuración de la ingesta (beats)
**Explicación:**

Se define la ingesta de datos en Elastic: el patrón de índices a filtrar, el nivel de log, el tipo de configuración aplicado al pipeline, el número de configuración y la ventana temporal de búsqueda, además del canal de eventos a vigilar.

1. `winlogbeat-*`
2. `debug`
3. `filter`
4. `3`
5. `-60m@m`
6. `WinEventLog:Security`

### Task 4: Eventos de acceso a objetos (Sysmon)
**Explicación:**

Analizando los eventos de acceso a objetos se identifica el permiso utilizado (ReadData/ListDirectory), el identificador del evento de apertura de objeto, el del cierre de handle y el campo que enlaza ambos eventos.

1. `ReadData (or ListDirectory)`
2. `4656`
3. `4658`
4. `Handle ID`

### Task 5: Diagnóstico del fallo documentado
**Explicación:**

Se clasifica el ejercicio como pertinente a Purple Team, se relaciona el incidente con la vulnerabilidad de documento conocida CVE-2022-30190 y se deja la descripción final sin respuesta adicional.

1. `Purple Team`
2. `CVE-2022-30190`
3. `No answer needed`

### Task 6: Cierre
**Explicación:**

Finaliza el ejercicio de detección táctica sin requerir respuesta adicional.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bienvenida / preparación | `No answer needed` |
| 2.1 | Formato de reglas usado | `Sigma` |
| 2.2 | Dominio de comunicación | `bad3xe69connection.io` |
| 2.3 | Ruta del binario | `C:\Downloads\bad3xe69.exe` |
| 2.4 | Método de salida | `proxy` |
| 3.1 | Patrón de índices | `winlogbeat-*` |
| 3.2 | Nivel de log | `debug` |
| 3.3 | Tipo de configuración | `filter` |
| 3.4 | Número de configuración | `3` |
| 3.5 | Ventana temporal | `-60m@m` |
| 3.6 | Canal de eventos | `WinEventLog:Security` |
| 4.1 | Permiso usado | `ReadData (or ListDirectory)` |
| 4.2 | Evento de apertura de objeto | `4656` |
| 4.3 | Evento de cierre de handle | `4658` |
| 4.4 | Campo de correlación | `Handle ID` |
| 5.1 | Tipo de ejercicio | `Purple Team` |
| 5.2 | CVE del fallo documentado | `CVE-2022-30190` |
| 5.3 | Descripción del hallazgo | `No answer needed` |
| 6 | Tarea de cierre | `No answer needed` |

---

**Metodología:** Monitorización de endpoints con Elastic (Winlogbeat), escritura de reglas Sigma sobre la telemetría, correlación de eventos de acceso a objetos con Sysmon y diagnóstico del CVE-2022-30190 (Follina) dentro de un ejercicio Purple Team.

**Learning chain:** Reconocimiento del binario → ingesta y filtrado → analítica de eventos de objeto → correlación de handles → diagnóstico de vulnerabilidad → priorización Purple Team.

**Lección:** *Un buen SOC no busca firmas, correlaciona telemetría: los eventos 4656/4658 y una regla Sigma bien escrita detectan el mismo binario que el AV quizá ya perdonó.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1105 Ingress Tool Transfer · T1566 Phishing · T1203 Exploitation for Client Execution (Follina).

**Fuente:** [TryHackMe - Tactical Detection](https://tryhackme.com/room/tacticaldetection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.