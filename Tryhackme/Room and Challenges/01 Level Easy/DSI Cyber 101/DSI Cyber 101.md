# DSI Cyber 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `dsicyber1013n3` | [TryHackMe](https://tryhackme.com/room/dsicyber1013n3) | SOC | THM | Simulador SOC, bloqueo de cuenta, reporte de incidentes | Fundamentos SOC |

> **Objeto:** Ejercitar el flujo completo de un analista SOC dentro de un simulador interactivo: detectar un incidente, contenerlo bloqueando la cuenta comprometida, investigar al atacante y emitir el reporte de incidentes final.

---

**Contexto:** Simulador SOC interactivo que guía a un analista a través de un incidente completo en 4 fases: ataque inicial, contención, investigación del atacante y reporte final. Las tasks T2–T5 son simuladores cuyos flags se generan en vivo.

> **ES:** Room de nivel Easy centrada en SOC. El simulador reproduce un incidente en 4 fases: triaje de la alerta "Suspicious Login" (usuario comprometido), contención bloqueando la cuenta de dave.saunders, investigación del atacante y actualización de los sistemas FakeBank, y por último el reporte con identificador SOC-2026-XXX. Las respuestas de T2–T5 dependen del flag que genera el simulador en vivo.
> **EN:** An Easy SOC-focused room. The simulator reproduces an incident in 4 phases: triage of the "Suspicious Login" alert (compromised user), containment by blocking dave.saunders' account, attacker investigation and FakeBank patching, and finally the report with the SOC-2026-XXX identifier. The T2–T5 answers depend on the flag generated live by the simulator.

## Solucionario

### T1 - Introducción / Introduction
**Explicación:** Tarea introductoria que sitúa al analista en el rol SOC y pregunta por el acrónimo que da nombre al equipo de seguridad: Security Operations Center.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa la sigla "SOC"? / What does the acronym "SOC" stand for? | `Security Operations Center` |

### T2 - Fase 1: Comienza un ataque / Phase 1: An Attack Begins
**Explicación:** Se abre la primera alerta del simulador ("Suspicious Login") y se hace triaje: hay que identificar qué usuario de la entidad bancaria está siendo comprometido. El resultado exacto depende del simulador estático en vivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisar la alerta "Suspicious Login" - ¿Qué usuario está en uso? / Review the "Suspicious Login" alert - which user is in use? | `*(Requiere resolución en el simulador estático en vivo)*` |

### T3 - Fase 2: Detener el ataque / Phase 2: Stopping the Attack
**Explicación:** Se contiene el incidente bloqueando la cuenta del usuario identificado en la fase anterior (dave.saunders) para detener el acceso del atacante. El flag que otorga el simulador aparece al completar la acción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bloquear la cuenta dave.saunders - ¿Qué flag apareció? / Block the dave.saunders account - what flag appeared? | `*(Requiere resolución en el simulador estático en vivo)*` |

### T4 - Fase 3: Investigar al atacante / Phase 3: Investigating the Attacker
**Explicación:** Se investiga al atacante y se refuerza la postura de los sistemas de la entidad, actualizando los sistemas FakeBank para cerrar la brecha. El flag generado por el simulador responde la cuestión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Actualizar sistemas FakeBank - ¿Qué flag apareció? / Update FakeBank systems - what flag appeared? | `*(Requiere resolución en el simulador estático en vivo)*` |

### T5 - Fase 4: Enviar tu reporte / Phase 4: Submitting Your Report
**Explicación:** Se cierra el ciclo con la documentación del incidente: el reporte de incidentes con su identificador (tipo SOC-2026-XXX). El valor final lo produce el simulador en vivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identificador del reporte de incidente (SOC-2026-XXX) / Incident report identifier (SOC-2026-XXX) | `*(Requiere resolución en el simulador estático en vivo)*` |

> **Nota:** Las tasks T2–T5 son simuladores SOC interactivos cuyos flags no están documentados en walkthroughs públicos. Se recomienda resolverlos directamente en la plataforma siguiendo las pistas del simulador.

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa la sigla "SOC"? / What does the acronym "SOC" stand for? | `Security Operations Center` |
| 2 | Revisar la alerta "Suspicious Login" - ¿Qué usuario está en uso? | `*(Requiere resolución en el simulador estático en vivo)*` |
| 3 | Bloquear la cuenta dave.saunders - ¿Qué flag apareció? | `*(Requiere resolución en el simulador estático en vivo)*` |
| 4 | Actualizar sistemas FakeBank - ¿Qué flag apareció? | `*(Requiere resolución en el simulador estático en vivo)*` |
| 5 | Identificador del reporte de incidente (SOC-2026-XXX) | `*(Requiere resolución en el simulador estático en vivo)*` |

---

**Metodología:** Conducir el incidente en el orden del simulador: detectar → contener → investigar → reportar, anotando cada flag generado.

### Cadena de ataque / Attack Chain

```text
Alerta "Suspicious Login" -> triaje (usuario comprometido) -> bloqueo de dave.saunders -> investigación del atacante + actualización FakeBank -> reporte de incidente SOC-2026-XXX
```

**Learning chain:** Triaje de alertas → bloqueo de cuenta comprometida → investigación del atacante → emisión de reporte de incidente.

**Lección:** *Un analista SOC debe seguir un ciclo ordenado ante un incidente: triaje y detección, contención inmediata del acceso (bloqueo de cuenta), investigación de la causa raíz y documentación del reporte; cada fase genera evidencia propia.*

**MITRE ATT&CK:** TA0001 Initial Access, TA0002 Execution.

**Fuente:** [TryHackMe - DSI Cyber 101](https://tryhackme.com/room/dsicyber1013n3)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.