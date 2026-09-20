# Red Team Threat Intel

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room / Inteligencia de amenazas | redteamthreatintel | https://tryhackme.com/room/redteamthreatintel | 02 Level Medium | TryHackMe | Threat Intelligence, Cyber Kill Chain, TTPs, ATT&CK, herramientas de acceso | Priorización de operaciones y alineación con TTPs reales |

> **Objeto:** Aplicar el proceso de inteligencia de amenazas a operaciones de red team: mapear las fases de la Cyber Kill Chain, identificar los TTPs y las herramientas empleadas en una cadena de ataque real y traducirlos a criterios operativos para planificar y emular el comportamiento del adversario.

---

**Contexto:** La sala **Red Team Threat Intel** muestra cómo el red team utiliza la inteligencia de amenazas (Threat Intelligence) para modelar al adversario y planificar sus propias operaciones. El laboratorio recorre la cadena de ataque de una intrusión real: identificación de fases y TTPs (como el uso de `Rundll32` para ejecución y las `Valid Accounts` para persistencia), herramientas de transferencia y carga (`certutil`, `ASPXSpy`) y el mecanismo de canal C2 (`MESSAGETAP`). Varias preguntas son de carácter teórico (sin respuesta), mientras que otras piden datos concretos de la cadena modelada.

## Solucionario

### Task 1: Introducción al Threat Intel / Threat Intel introduction
**Explicación:**

Pregunta teórica de introducción: lectura del concepto y del enfoque de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Task 2: Modelado del adversario / Adversary modelling
**Explicación:**

Pregunta teórica sobre el enfoque de modelado, sin respuesta obligatoria.

1. `No answer needed`

### Task 3: Fuentes de inteligencia / Intelligence sources
**Explicación:**

Pregunta teórica sobre las fuentes de inteligencia, sin respuesta obligatoria.

1. `No answer needed`

### Task 4: Integración en la operación / Operational integration
**Explicación:**

Pregunta teórica sobre la integración de la inteligencia en la operación, sin respuesta obligatoria.

1. `No answer needed`

### Task 5: Kill Chain / Cyber Kill Chain
**Explicación:**

Mapeo de la cadena de ataque: la primera pregunta no requiere respuesta, seguida del número de la fase de la cadena correspondiente, la herramienta de ejecución utilizada (`Rundll32`) y la técnica de acceso empleada (`Valid Accounts`).

1. `No answer needed`
2. `2`
3. `Rundll32`
4. `Valid Accounts`

### Task 6: Emulación de TTPs / TTP emulation
**Explicación:**

Pregunta teórica sobre la emulación de TTPs derivados de la inteligencia, sin respuesta obligatoria.

1. `No answer needed`

### Task 7: Componentes de la intrusión / Intrusion components
**Explicación:**

Componentes concretos de la intrusión modelada: la flag de la inteligencia de la cadena, el webshell desplegado (`ASPXSpy`), la herramienta de transferencia usada (`certutil`) y el canal de exfiltración/C2 (`MESSAGETAP`).

1. `THM{7HR347_1N73L_12 __4w35om}`
2. `ASPXSpy`
3. `certutil`
4. `MESSAGETAP`

### Task 8: Cierre / Wrap-up
**Explicación:**

Última pregunta de confirmación de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2 | Modelado del adversario | `No answer needed` |
| 3 | Fuentes de inteligencia | `No answer needed` |
| 4 | Integración en la operación | `No answer needed` |
| 5 | Kill Chain (preparación) | `No answer needed` |
| 6 | Kill Chain (número de fase) | `2` |
| 7 | Herramienta de ejecución | `Rundll32` |
| 8 | Técnica de acceso | `Valid Accounts` |
| 9 | Emulación de TTPs | `No answer needed` |
| 10 | Flag de la cadena | `THM{7HR347_1N73L_12 __4w35om}` |
| 11 | Webshell desplegado | `ASPXSpy` |
| 12 | Herramienta de transferencia | `certutil` |
| 13 | Canal C2 / exfiltración | `MESSAGETAP` |
| 14 | Cierre | `No answer needed` |

---

**Metodología:** Estudio del proceso de inteligencia de amenazas, mapeo de la Cyber Kill Chain de una intrusión real, identificación de TTPs y herramientas (Rundll32, Valid Accounts, ASPXSpy, certutil, MESSAGETAP) y traducción de la inteligencia a la planificación operativa del red team.

**Learning chain:** Fundamentos de Threat Intel → modelado del adversario → mapeo de la Kill Chain → identificación de TTPs y herramientas → emulación operativa.

**Lección:** *La inteligencia de amenazas convierte informes de intrusión en planes operativos: cada herramienta y técnica documentada es un candidato directo a emular en las operaciones del red team.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1078 Valid Accounts · T1105 Ingress Tool Transfer · T1021 Remote Services · T1041 Exfiltration Over C2 Channel.

**Fuente:** [TryHackMe - Red Team Threat Intel](https://tryhackme.com/room/redteamthreatintel)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.