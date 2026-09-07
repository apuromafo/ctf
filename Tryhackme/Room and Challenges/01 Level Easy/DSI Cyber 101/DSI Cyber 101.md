# DSI Cyber 101

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `dsicyber1013n3` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/dsicyber1013n3) |
| **Sección** | SOC |
| **Fuente** | THM |
| **Componentes** | Simulador SOC, bloqueo de cuenta, reporte de incidentes |
| **Impacto** | Fundamentos SOC |

---

**Contexto:** Simulador SOC interactivo que guía a un analista a través de un incidente completo en 4 fases: ataque inicial, contención, investigación del atacante y reporte final. Las tasks T2–T5 son simuladores cuyos flags se generan en vivo.

## Solucionario

### T1 - Introduction

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué significa la sigla "SOC"? | Security Operations Center |

### T2 - Phase 1: An Attack Begins

| Pregunta | Respuesta |
|----------|-----------|
| Revisar la alerta "Suspicious Login" - ¿Qué usuario está en uso? | *(Requiere resolución en el simulador estático en vivo)* |

### T3 - Phase 2: Stopping the Attack

| Pregunta | Respuesta |
|----------|-----------|
| Bloquear la cuenta dave.saunders - ¿Qué flag apareció? | *(Requiere resolución en el simulador estático en vivo)* |

### T4 - Phase 3: Investigating the Attacker

| Pregunta | Respuesta |
|----------|-----------|
| Actualizar sistemas FakeBank - ¿Qué flag apareció? | *(Requiere resolución en el simulador estático en vivo)* |

### T5 - Phase 4: Submitting Your Report

| Pregunta | Respuesta |
|----------|-----------|
| Identificador del reporte de incidente (SOC-2026-XXX) | *(Requiere resolución en el simulador estático en vivo)* |

> **Nota:** Las tasks T2–T5 son simuladores SOC interactivos cuyos flags no están documentados en walkthroughs públicos. Se recomienda resolverlos directamente en la plataforma siguiendo las pistas del simulador.

---

**Metodología:** Conducir el incidente en el orden del simulador: detectar → contener → investigar → reportar, anotando cada flag generado.

**Learning chain:** Triaje de alertas → bloqueo de cuenta comprometida → investigación del atacante → emisión de reporte de incidente.

**MITRE ATT&CK:** TA0001 Initial Access, TA0002 Execution.

**Fuente:** https://tryhackme.com/room/dsicyber1013n3