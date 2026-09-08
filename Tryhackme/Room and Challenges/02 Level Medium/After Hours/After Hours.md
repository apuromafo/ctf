# After Hours
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `hh-afterhours-b090d1f0` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-afterhours-b090d1f0) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=hh-afterhours-b090d1f0` + websearch de walkthroughs) |
| **Componentes** | Windows, DFIR, triage EVTX/reg, análisis de ejecución (procesos/servicios/tareas/WMI event subscriptions), persistencia maliciosa, backdoor |
| **Impacto** | Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en forense Windows/malware: desde un triage se identifica una ejecución "after hours" correspondiente a una persistencia maliciosa que abre un backdoor y deja la flag documentada. |
---
**Contexto:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en **forense Windows / malware**: a partir de un triage se analiza una ejecución posterior al horario laboral ("after hours") que corresponde a un proceso/persistencia maliciosa (servicio de Windows, tarea o suscripción WMI); el malware abre un backdoor y la flag está en el artefacto/registro que lo documenta.
*EN: Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty centered on **Windows forensics / malware**: from a triage an "after hours" execution is analyzed that corresponds to malicious persistence (Windows service, scheduled task or WMI subscription); the malware opens a backdoor and the flag lives in the artifact/registry that documents it.*
## Solucionario
### Task 1 - After Hours
**Explicación:** Se investiga un host Windows donde se detectó actividad fuera del horario laboral. Revisando los artefactos de ejecución (eventos, servicios, tareas programadas o suscripciones WMI) aparece un proceso inusual llamado "Patch" que se ejecuta de madrugada y persiste para abrir un backdoor. La flag está documentada en el artefacto que registra la ejecución/persistencia maliciosa. 1 pregunta.
*EN: A Windows host with activity detected outside business hours is investigated. Reviewing the execution artifacts (events, services, scheduled tasks or WMI subscriptions) an unusual process named "Patch" appears, running early in the morning and persisting to open a backdoor. The flag is documented in the artifact that records the malicious execution/persistence. 1 question.*

```
triage EVTX / registry (host Windows)
  -> actividad "after hours" -> proceso inusual "Patch" de madrugada
  -> persistencia (servicio / tarea / WMI event subscription)
  -> malware abre backdoor
  -> artefacto/registro documenta la instalacion -> THM{P4tch_op3ned_th3_BacKd00r}
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{P4tch_op3ned_th3_BacKd00r}` |
---
**Metodología:** Triage de evidencias (EVTX, registry y artefactos) → filtrado de actividad por línea de tiempo → búsqueda de ejecución fuera de horario (proceso "Patch" de madrugada) → localización de la persistencia (servicio/tarea/suscripción WMI) → análisis del backdoor → flag en el artefacto documental.
**Learning chain:** DFIR Windows → correlación de ejecución temporal fuera de jornada → identificación de persistencia sigilosa (WMI event subscriptions) → backdoor y extracción de la flag.
**MITRE ATT&CK:** T1053.005 (Scheduled Task), T1543.003 (Windows Service), T1546.003 (WMI Event Subscription), T1133 (External Remote Services)/persistencia, T1572 (Protocol Tunneling)/backdoor.
**Fuente:** [TryHackMe - After Hours](https://tryhackme.com/room/hh-afterhours-b090d1f0)