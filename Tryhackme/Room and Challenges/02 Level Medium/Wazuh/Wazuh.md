# Wazuh

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `wazuhct` |
| **Link** | [TryHackMe](https://tryhackme.com/room/wazuhct) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Wazuh / SIEM / XDR / agent / manager / rules / API / auditd |
| **Impacto** | Conocer la arquitectura de Wazuh (manager/agent), reglas, fuente de eventos y la API REST para operar un SIEM |

---

**Contexto:** Sala CTF sobre Wazuh SIEM/XDR: arquitectura (manager, agent), instalación, políticas de registro, reglas, Sysmon/Event Viewer como fuentes y la API de Wazuh para interactuar con el servicio.

## Solucionario

### Task 1: (Arquitectura / Architecture)

**Explicación:**

Arquitectura de Wazuh: el año de creación de OSSEC (proyecto origen) es `2015`; los componentes principales son el `Agent` y el `Manager`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Year) | `1. 2015` |
| 2 | (Component 1) | `2. Agent` |
| 3 | (Component 2) | `3. Manager` |

### Task 2: (Despliegue / Deployment)

**Explicación:**

Despliegue/instalación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Deploy) | `No answer needed` |

### Task 3: (Agente / Agent)

**Explicación:**

Agente: se muestran los estados del agente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Agent - 1) | `1. No answer needed` |
| 2 | (Agent - 2) | `2. No answer needed` |
| 3 | (Status value) | `3. 2` |
| 4 | (Status text) | `4. Disconnected` |

### Task 4: (Políticas / Policies)

**Explicación:**

Políticas de registro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Policy - 1) | `1. No answer needed` |
| 2 | (Policy - 2) | `2. No answer needed` |
| 3 | (Policy - 3) | `3. No answer needed` |
| 4 | (Events count) | `4. 196` |

### Task 5: (Reglas / Rules)

**Explicación:**

Reglas de correlación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Rule - 1) | `1. No answer needed` |
| 2 | (Rule - 2) | `2. No answer needed` |

### Task 6: (Reglas / Rules 2)

**Explicación:**

Reglas (definición de reglas personalizadas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Rule 2 - 1) | `1. No answer needed` |
| 2 | (Rule 2 - 2) | `2. No answer needed` |

### Task 7: (Fuente de eventos / Event Source)

**Explicación:**

La fuente de eventos de Windows que registra la actividad detallada es `Sysmon` y la herramienta para ver los logs en Windows es `Event Viewer`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Event source) | `1. Sysmon` |
| 2 | (Viewer) | `2. Event Viewer` |

### Task 8: (Reglas por defecto / Default rules)

**Explicación:**

Las reglas por defecto de Wazuh se almacenan en `/var/ossec/ruleset/rules`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Rules path) | `1. /var/ossec/ruleset/rules` |

### Task 9: (auditd / Linux audit)

**Explicación:**

La herramienta de auditoría de Linux es `auditd` y su configuración se encuentra en `/etc/audit/rules.d/audit.rules`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Tool) | `1. auditd` |
| 2 | (Config path) | `2. /etc/audit/rules.d/audit.rules` |

### Task 10: (API)

**Explicación:**

La API de Wazuh: el comando de prueba es `curl`; los métodos HTTP usados son `GET` y `PUT`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Tool) | `1. curl` |
| 2 | (GET) | `2. GET` |
| 3 | (PUT) | `3. PUT` |
| 4 | (API - 4) | `4. No answer needed` |
| 5 | (Version) | `5. v4.2.5` |

### Task 11: (API - operaciones / API operations)

**Explicación:**

Operaciones de la API.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (API op - 1) | `1. No answer needed` |
| 2 | (API op - 2) | `2. No answer needed` |
| 3 | (Agent name) | `3. agent-001` |

### Task 12: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión - 1) | `1. No answer needed` |
| 2 | (Conclusión - 2) | `2. No answer needed` |

---

**Metodología:**

1. Comprender la arquitectura manager/agent de Wazuh (proyecto heredero de OSSEC, 2015).
2. Desplegar el agente, verificar su estado (Disconnected) y las políticas de registro (196 eventos).
3. Configurar y ubicar reglas (`/var/ossec/ruleset/rules`) y fuentes de eventos (Sysmon, Event Viewer).
4. Configurar auditd Linux (`/etc/audit/rules.d/audit.rules`).
5. Interactuar con la API de Wazuh vía `curl` (GET/PUT; v4.2.5) y operaciones sobre agentes.

**Learning chain:** OSSEC 2015 -> Agent/Manager -> deploy -> status Disconnected -> policies 196 -> rules path -> Sysmon/Event Viewer -> auditd rules -> API curl GET/PUT v4.2.5 -> agent-001

**Lección:** *Wazuh combina un manager central con agentes ligeros para recoger eventos (Sysmon/auditd), correlacionarlos con reglas en `/var/ossec/ruleset/rules` y exponer una API REST para operar de forma programática.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter) · T1005 (Data from Local System) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Wazuh](https://tryhackme.com/room/wazuhct)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
