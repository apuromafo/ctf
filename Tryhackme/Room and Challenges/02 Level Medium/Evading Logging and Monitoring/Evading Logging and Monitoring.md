# Evading Logging and Monitoring

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Red Team / Evasión de Logs (ETW) | evadingloggingandmonitoring | https://tryhackme.com/room/evadingloggingandmonitoring | 02 Level Medium | TryHackMe | ETW, PowerShell, Group Policy, técnicas de evasión | Evasión de telemetría y registros de Windows (ETW event logs) |

---

**Contexto:** **Evading Logging and Monitoring** es una sala de la rama *Red Teaming - Host Evasion* que enseña a atacar el sistema de rastreo de eventos de Windows (**ETW**, Event Tracing for Windows). Se cubren los tres componentes de ETW (controllers, providers y consumers), los event IDs clave de seguridad (como 4726 y 104), y cuatro técnicas: modificación por reflexión del proveedor `PSEtwLogProvider`, parcheo en memoria de `EtwEventWrite` (`ret 14h`), toma de control de la GPO de PowerShell (`EnableScriptBlockLogging`/`EnableScriptBlockInvocationLogging`) y abuso del pipeline de módulos. Termina con un escenario real donde se desactivan los logs, se borran los eventos 4103/4104 y se ejecuta un binario de forma silenciosa para obtener la flag.

## Solucionario

### Task 1: Introduction
**Explicación:**

El registro (logging) crea un registro físico de actividad que puede ser analizado. El objetivo del atacante es controlar qué logs quedan en el host. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 2: Event Tracing / Event IDs
**Explicación:**

ETW se divide en tres componentes. El **Controller** es el que construye y configura las sesiones de trazado. Entre los event IDs de seguridad destacados en la sala, **4726** corresponde a "A user account was deleted".

Respuestas del lab (contenido original):

```
1. Controllers
2. 4726
```

### Task 3: Approaches to Log Evasion
**Explicación:**

Se evalúa el "log smashing" como vía de evasión. La sala lista **3** event IDs capaces de monitorizar la destrucción de logs (1102, 104 y 1100). De ellos, el event ID **104** registra el momento en que se limpia un archivo de log.

Respuestas del lab (contenido original):

```
1. 3
2. 104
```

### Task 4: Tracing Instrumentation
**Explicación:**

Pregunta de comprensión sobre la instrumentación de ETW y cómo cada componente (provider, controller, consumer) participa en el flujo de eventos. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 5: Reflection for Fun and Silence
**Explicación:**

Dentro de PowerShell los proveedores ETW se cargan desde el ensamblado .NET **`PSEtwLogProvider`**. Mediante reflexión, un atacante obtiene la clase, accede al campo `etwProvider` y establece el campo `m_enabled` a `$null` (0), silenciando los eventos del proveedor para esa sesión.

Respuestas del lab (contenido original):

```
1. PSEtwLogProvider
2. m_enabled
```

### Task 6: Patching Tracing Functions
**Explicación:**

ETW se carga desde la CLR de cada proceso nuevo. Observando el desensamblado de `EtwEventWrite`, en la dirección **`779f245b`** se encuentra la instrucción `call ntdll!_security_check_cookie`. Para neutralizar la función se escriben en memoria los bytes del opcode `ret 14h`, es decir **`c21400`**, haciendo que la función retorne antes de generar eventos.

Respuestas del lab (contenido original):

```
1. 779f245b
2. c21400
```

### Task 7: Providers via Policy (Script Block Logging)
**Explicación:**

El script block logging, introducido en PowerShell v4/v5, reporta **2** event IDs distintos: 4103 (command invocation) y 4104 (script block execution). El event ID **4104** es el más relevante para un atacante porque expone los scripts que ejecuta.

Respuestas del lab (contenido original):

```
1. 2
2. 4104
```

### Task 8: Group Policy Takeover
**Explicación:**

Los dos proveedores de PowerShell (script block y module logging) se habilitan por GPO. Para desactivarlos, se usa reflexión para obtener la caché `cachedGroupPolicySettings` y se ponen a `0` las claves. Los event IDs implicados son **4103, 4104**, y la clave que controla los eventos 4104 es **`EnableScriptBlockLogging`**.

Respuestas del lab (contenido original):

```
1. 4103, 4104
2. EnableScriptBlockLogging
```

### Task 9: Abusing Log Pipeline
**Explicación:**

Cada módulo PowerShell tiene la propiedad `LogPipelineExecutionDetails`. Estableciéndola a `$false` se desactiva el **module logging** para esa sesión. En el ejemplo de la sala, el módulo objetivo que se modifica es **`Microsoft.PowerShell.Utility`** (junto con el snap-in `Microsoft.PowerShell.Core`).

Respuestas del lab (contenido original):

```
1. Module logging
2. Microsoft.PowerShell.Utility
```

### Task 10: Real World Scenario (flag)
**Explicación:**

En el escenario final se desactivan las GPO de PowerShell, se eliminan los logs 4103/4104 (no hay forwarding) y se ejecuta el binario `agent.exe` de forma silenciosa. Si la implementación es correcta se obtiene la flag en el escritorio.

**Respuesta:** `THM{51l3n7_l1k3_4_5n4k3}`

### Task 11: Conclusion
**Explicación:**

Cierre de la sala resumiendo la caja de herramientas de evasión sobre ETW. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 (Introduction) | `No answer needed` |
| 2 | ¿Qué componente de ETW construye y configura las sesiones? | `Controllers` |
| 3 | ¿Qué event ID registra la eliminación de una cuenta de usuario? | `4726` |
| 4 | ¿Cuántos event IDs monitorizan el log smashing? | `3` |
| 5 | ¿Qué event ID registra cuando se limpia un archivo de log? | `104` |
| 6 | ¿Entiendes cómo se instrumenta ETW? | `No answer needed` |
| 7 | ¿Desde qué ensamblado .NET se cargan los proveedores ETW en PowerShell? | `PSEtwLogProvider` |
| 8 | ¿Qué campo se establece a $null en la técnica de reflexión? | `m_enabled` |
| 9 | Dirección del `call ntdll!_security_check_cookie` en el desensamblado | `779f245b` |
| 10 | Opcode `ret 14h` escrito en memoria | `c21400` |
| 11 | ¿Cuántos event IDs reporta el script block logging? | `2` |
| 12 | ¿Qué event ID registra la ejecución de script blocks? | `4104` |
| 13 | ¿Qué event IDs registran command invocation y script block execution? | `4103, 4104` |
| 14 | ¿Qué ajuste GPO controla los eventos 4104? | `EnableScriptBlockLogging` |
| 15 | ¿Qué proveedor registra módulos y su actividad? | `Module logging` |
| 16 | ¿Qué módulo se usa en el ejemplo para desactivar el logging? | `Microsoft.PowerShell.Utility` |
| 17 | Flag del escenario real (agent.exe) | `THM{51l3n7_l1k3_4_5n4k3}` |
| 18 | Conclusion | `No answer needed` |

---

**Metodología:** Análisis de ETW y sus componentes, revisión de event IDs de Windows, modificación por reflexión de ensamblados .NET, parcheo de `EtwEventWrite` con opcodes en memoria, modificación de la caché de GPO y desactivación del logging de módulos para ejecutar un binario sin telemetría.

**Learning chain:** Introducción al logging → ETW → Approaches to Log Evasion → Instrumentación del trazado → Reflexión → Parcheo de funciones → Providers vía GPO → Group Policy Takeover → Abuso del pipeline → Escenario real.

**Lección:** *Los movimientos ofensivos dejan telemetría en ETW y PowerShell; conocer los event IDs (4103/4104/4726/104) y las técnicas de reflexión y parcheo permite borrar la huella conservando la integridad del entorno.*

**MITRE ATT&CK:** T1562.001 Impair Defenses: Disable or Modify Tools · T1562.002 Impair Defenses: Disable Windows Event Logging · T1070.001 Indicator Removal on Host: Clear Windows Event Logs · T1059.001 PowerShell.

**Fuente:** [TryHackMe - Evading Logging and Monitoring](https://tryhackme.com/room/evadingloggingandmonitoring)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.