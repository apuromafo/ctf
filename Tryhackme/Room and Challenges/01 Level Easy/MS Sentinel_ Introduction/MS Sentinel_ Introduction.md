# MS Sentinel_ Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (Microsoft Sentinel) | `mssentinelintroduction` | https://tryhackme.com/room/mssentinelintroduction | 01 Level Easy | TryHackMe | Microsoft Sentinel / SIEM / SOAR / data connectors / Log Analytics workspaces / dashboards / playbooks / incidents | Introducción a Microsoft Sentinel: rol del SOC, componentes del SIEM/SOAR y flujo de trabajo del analista. |

---

**Contexto:** Sala introductoria de Microsoft Sentinel. Se sitúa a Sentinel dentro del flujo del Security Operations Center (el analista de nivel 2 hace triage), se repasa la relación SIEM/SOAR (con `4` componentes/capas), se recorren los componentes de Sentinel (data connectors, log analytics workspaces, dashboards, playbooks, incidents y el concepto de alert fatigue) y se describe su naturaleza de monitorización cloud-native. Cierra con una tarea de lectura sin respuesta.

> **ES:** Microsoft Sentinel en el SOC: conceptos SIEM/SOAR, componentes y flujo del analista de nivel 2.
> **EN:** Microsoft Sentinel in the SOC: SIEM/SOAR concepts, components and the Level 2 analyst workflow.

## Solucionario

### Task 1: El SOC y el analista / The SOC and the analyst

**Explicación:** Se presenta la estructura del equipo de seguridad: el equipo es el `Security Operations Center`, el perfil que realiza el triage de los eventos es el `SOC Level 2 Analyst`, y la palabra clave del proceso de revisión inicial es `triage`.

Contenido original de la tarea / Original task content:

```text
1. 1. Security Operations Center
   2. SOC Level 2 Analyst
   3. triage
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del equipo de seguridad / Security team name | `Security Operations Center` |
| 2 | Rol que hace triage / Role that does triage | `SOC Level 2 Analyst` |
| 3 | Proceso de revisión inicial / Initial review process | `triage` |

### Task 2: Conceptos SIEM/SOAR / SIEM & SOAR concepts

**Explicación:** Microsoft Sentinel combina capacidades de orquestación y respuesta (`SOAR`) con las de correlación y análisis de eventos (`SIEM`), y la arquitectura introductoria se compone de `4` partes.

Contenido original de la tarea / Original task content:

```text
2. 1. SOAR
   2. SIEM
   3. 4
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Capacidad de orquestación y respuesta / Orchestration and response capability | `SOAR` |
| 2 | Capacidad de correlación/análisis / Correlation/analysis capability | `SIEM` |
| 3 | Número de partes de la arquitectura / Number of architecture parts | `4` |

### Task 3: Componentes de Microsoft Sentinel / Microsoft Sentinel components

**Explicación:** Se recorren los componentes de la plataforma: los `data connectors` traen los datos, que se almacenan en `log analytics workspaces`; la visualización se hace con `dashboards`, la sobrecarga de alertas se conoce como `alert fatigue`, la automatización de respuesta se define con `playbooks` y el análisis de eventos se organiza en `Incidents`.

Contenido original de la tarea / Original task content:

```text
3. 1. data connectors
   2. log analytics workspaces
   3. dashboards
   4. alert fatigue
   5. playbooks
   6. Incidents
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conectores de datos / Data connectors | `data connectors` |
| 2 | Almacenamiento de logs / Log storage | `log analytics workspaces` |
| 3 | Paneles de visualización / Visualization dashboards | `dashboards` |
| 4 | Sobrecarga de alertas / Alert overload | `alert fatigue` |
| 5 | Automatización de respuesta / Response automation | `playbooks` |
| 6 | Incidentes de seguridad / Security incidents | `Incidents` |

### Task 4: Qué hace Sentinel / What does Sentinel do?

**Explicación:** Microsoft Sentinel es una solución de `monitor`ización continua de seguridad y, por su diseño en Azure, es `cloud-native`.

Contenido original de la tarea / Original task content:

```text
4. 1. monitor
   2. cloud-native
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Función principal / Main function | `monitor` |
| 2 | Naturaleza de la plataforma / Platform nature | `cloud-native` |

### Task 5: Conclusión / Conclusion

**Explicación:** Cierre de la sala recapitulando el papel de Microsoft Sentinel en el SOC. Tarea de lectura sin respuesta.

Contenido original de la tarea / Original task content:

```text
5. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del equipo de seguridad / Security team name | `Security Operations Center` |
| 2 | Rol que hace triage / Role that does triage | `SOC Level 2 Analyst` |
| 3 | Proceso de revisión inicial / Initial review process | `triage` |
| 4 | Capacidad de orquestación y respuesta / Orchestration and response capability | `SOAR` |
| 5 | Capacidad de correlación/análisis / Correlation/analysis capability | `SIEM` |
| 6 | Número de partes de la arquitectura / Number of architecture parts | `4` |
| 7 | Conectores de datos / Data connectors | `data connectors` |
| 8 | Almacenamiento de logs / Log storage | `log analytics workspaces` |
| 9 | Paneles de visualización / Visualization dashboards | `dashboards` |
| 10 | Sobrecarga de alertas / Alert overload | `alert fatigue` |
| 11 | Automatización de respuesta / Response automation | `playbooks` |
| 12 | Incidentes de seguridad / Security incidents | `Incidents` |
| 13 | Función principal / Main function | `monitor` |
| 14 | Naturaleza de la plataforma / Platform nature | `cloud-native` |

---

**Metodología:** Leer la sección de contexto del SOC (equipo, analista nivel 2, triage), estudiar la relación SIEM/SOAR, repasar los componentes de Sentinel (connectors, workspaces, dashboards, playbooks, incidents, alert fatigue) y describir su arquitectura cloud-native antes de cerrar con la conclusión.

### Cadena de ataque / Attack Chain

```text
SOC (Security Operations Center) -> SOC Level 2 Analyst (triage) -> SIEM/SOAR (4 componentes) -> data connectors -> log analytics workspaces -> dashboards -> playbooks -> Incidents (alert fatigue) -> monitorización cloud-native
```

**Learning chain:** SOC y triage -> SIEM vs SOAR -> componentes de Sentinel -> alert fatigue/playbooks -> cloud-native.

**Lección:** *Microsoft Sentinel articula el flujo SIEM/SOAR en el SOC: los datos entran por conectores, se analizan en workspaces y se responde con playbooks; entender estos componentes es la base del trabajo diario del analista.* 

**MITRE ATT&CK:** N/A (sala introductoria de una plataforma de defensa/SOC; no hay técnica ofensiva concreta)

**Fuente:** [TryHackMe - MS Sentinel_ Introduction](https://tryhackme.com/room/mssentinelintroduction)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.