# After Hours [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-afterhours-b090d1f0`
* **Link:** https://tryhackme.com/room/hh-afterhours-b090d1f0
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-afterhours-b090d1f0` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en **forense Windows / malware**: a partir de un triage se analiza una ejecución posterior al horario laboral ("after hours") que corresponde a un proceso/persistencia maliciosa (servicio de Windows, tarea o suscripción WMI); el malware abre un backdoor y la flag está en el artefacto/registro que lo documenta.
> **EN:** Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty centered on **Windows forensics / malware**: from a triage an "after hours" execution is analyzed that corresponds to malicious persistence (Windows service, scheduled task or WMI subscription); the malware opens a backdoor and the flag lives in the artifact/registry that documents it.

### Task 1 - After Hours

> **ES:** Se investiga un host Windows donde se detectó actividad fuera del horario laboral. Revisando los artefactos de ejecución (eventos, servicios, tareas programadas o suscripciones WMI) aparece un proceso inusual llamado "Patch" que se ejecuta de madrugada y persiste para abrir un backdoor. La flag está documentada en el artefacto que registra la ejecución/persistencia maliciosa. 1 pregunta.
> **EN:** A Windows host with activity detected outside business hours is investigated. Reviewing the execution artifacts (events, services, scheduled tasks or WMI subscriptions) an unusual process named "Patch" appears, running early in the morning and persisting to open a backdoor. The flag is documented in the artifact that records the malicious execution/persistence. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{P4tch_op3ned_th3_BacKd00r}` |

## Metodología / Methodology

1. **Paso / Step - Triage de evidencias:** Se importa/procesa el triage del host (EVTX, registry y artefactos del sistema) y se filtra la actividad según la línea de tiempo.
2. **Paso / Step - Búsqueda de ejecución fuera de horario:** Se cruzan los registros de proceso con el horario posterior al cierre del hotel; destaca un proceso "Patch" ejecutándose de madrugada.
3. **Paso / Step - Persistencia sigilosa:** Se localiza el mecanismo de persistencia (servicio de Windows, tarea programada o suscripción WMI event) creado para relanzar el proceso y mantener el acceso.
4. **Paso / Step - Backdoor:** El análisis del binario/script muestra que abre un backdoor; la flag aparece en el artefacto o registro que documenta la instalación → `THM{P4tch_op3ned_th3_BacKd00r}`.

### Cadena de ataque / Attack Chain

```
triage EVTX / registry (host Windows)
  -> actividad "after hours" -> proceso inusual "Patch" de madrugada
  -> persistencia (servicio / tarea / WMI event subscription)
  -> malware abre backdoor
  -> artefacto/registro documenta la instalación -> THM{P4tch_op3ned_th3_BacKd00r}
```

**Lección:** Los adversarios aprovechan los horarios de descanso y la persistencia sigilosa (tipo WMI event subscriptions) para pasar desapercibidos; el forense debe mirar también el "quiénes" (procesos y potenciales backdoors) fuera de la jornada laboral.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.