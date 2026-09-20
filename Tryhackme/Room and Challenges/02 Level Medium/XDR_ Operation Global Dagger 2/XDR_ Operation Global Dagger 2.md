# XDR_ Operation Global Dagger 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | xdroperationglobaldagger2 | https://tryhackme.com/room/xdroperationglobaldagger2 | 02 Level Medium | TryHackMe | Microsoft 365 Defender, XDR, KQL | Segunda parte de la operación Global Dagger: registro de servicios maliciosos, modificaciones de registro y deshabilitación de Defender con WMIC |

---

**Contexto:** La sala **XDR: Operation Global Dagger 2** continúa la investigación del incidente en Microsoft 365 Defender. Esta vez el análisis se centra en los artefactos de persistencia y sabotaje: el registro de un servicio sospechoso, la modificación de claves de registro (RegistryModification), la deshabilitación de la monitorización en tiempo real de Windows Defender mediante `DisableRealtimeMonitoring`, el uso de WMIC para ejecución de comandos y el encadenado de las tácticas de Discovery y Execution. El solucionario concluye con la flag de la sala.

## Solucionario

### Task 1: Introducción al incidente

**Explicación:**

La sala presenta la segunda parte de la operación Global Dagger y el objetivo de seguir la pista de la persistencia y el sabotaje del atacante.

Respuesta: `No answer needed`

### Task 2: Preparación de la investigación

**Explicación:**

Se accede a las nuevas alertas del incidente y se prepara el análisis de los artefactos de persistencia.

Respuesta: `No answer needed`

### Task 3: Análisis de los artefactos de persistencia y antivirus

**Explicación:**

Se analizan las alertas de la segunda fase: el nombre de la alerta de registro de servicio sospechoso (`Suspicious service registration`), el nivel de severidad (`3`), el tipo de evento (`RegistryModification`), el hash SHA256 de la muestra, la clave que deshabilita la protección en tiempo real (`DisableRealtimeMonitoring`), el comando `reg add` exacto ejecutado, la herramienta de administración utilizada (`WMIC.exe`), las técnicas encadenadas (Discovery, Execution) y la flag de la sala.

Nota de referencia: el comando exacto proviene del writeup de la sala disponible en Medium (https://medium.com/@Sle3pyHead/xdr-operation-global-dagger-2-ctf-notes-tryhackme-e85eaa8daab3).

1. `Suspicious service registration`
2. `3`
3. `RegistryModification`
4. `cdb58d0bcabe76afc60428f364834463`
5. `DisableRealtimeMonitoring`
6. `reg  add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f `
7. `WMIC.exe`
8. `Discovery, Execution`
9. `THM{PZ874JC89DR5NZ1DAF6MS2KH}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción al incidente | `No answer needed` |
| 2 | Preparación de la investigación | `No answer needed` |
| 3.1 | Nombre de la alerta | `Suspicious service registration` |
| 3.2 | Severidad de la alerta | `3` |
| 3.3 | Tipo de evento | `RegistryModification` |
| 3.4 | Hash de la muestra | `cdb58d0bcabe76afc60428f364834463` |
| 3.5 | Clave de deshabilitación | `DisableRealtimeMonitoring` |
| 3.6 | Comando reg add ejecutado | `reg  add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f ` |
| 3.7 | Herramienta de administración | `WMIC.exe` |
| 3.8 | Técnicas encadenadas | `Discovery, Execution` |
| 3.9 | Flag de la sala | `THM{PZ874JC89DR5NZ1DAF6MS2KH}` |

---

**Metodología:** Investigación de la segunda fase del incidente en Microsoft 365 Defender: análisis de la alerta de registro de servicio sospechoso, revisión de la modificación del registro para deshabilitar Defender, reconstrucción del comando `reg add`, identificación de WMIC y vinculación de las tácticas Discovery y Execution.

**Learning chain:** Incidente → alerta de servicio → registro → clave de Defender → comando reg add → WMIC → tácticas → flag.

**Lección:** *La persistencia y el sabotaje del antivirus viajan juntos: deshabilitar la monitorización real-time y registrar servicios son dos caras de la misma cadena de ataque.*

**MITRE ATT&CK:** T1543.003 Create or Modify System Process · T1112 Modify Registry · T1562.001 Impair Defenses (Disable or Modify Tools) · T1047 Windows Management Instrumentation.

**Fuente:** [TryHackMe - XDR_ Operation Global Dagger 2](https://tryhackme.com/room/xdroperationglobaldagger2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.