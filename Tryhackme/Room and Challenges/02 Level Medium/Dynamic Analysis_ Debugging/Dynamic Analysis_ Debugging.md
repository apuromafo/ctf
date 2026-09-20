# Dynamic Analysis_ Debugging

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `dynamicanalysisdebugging` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dynamicanalysisdebugging) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Análisis dinámico de malware / sandbox / x64dbg / Process Monitor / debugger / patching |
| **Impacto** | Uso de análisis dinámico en sandbox y debuggers para detectar packing, inspeccionar procesos y patchear el binario durante el análisis de malware |

---

**Contexto:** La sala cubre el análisis dinámico de malware: desde el análisis básico en un sandbox y el concepto de packing, hasta el uso de debuggers (assembly-level y kernel-level) y herramientas como x64dbg y Process Monitor. En el laboratorio se inspecciona la muestra en la pestaña CPU y de handles, se observa la llamada a CreateToolhelp32Snapshot en Kernel32.dll y se concluye parcheando el binario para evadir la comprobación.

## Solucionario

### Task 1: Introducción al laboratorio

**Explicación:** Tarea introductoria que presenta el entorno de análisis dinámico de la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Presentación y despliegue del entorno | `No answer needed` |

### Task 2: Análisis dinámico y packing

**Explicación:** Se distinguen los tipos de análisis: la variante que ejecuta la muestra en un entorno controlado usando herramientas de monitoreo es **basic dynamic analysis**, y la técnica que oculta el código real mediante compresión/cifrado y lo despacha en tiempo de ejecución es **Packing**.

1. basic dynamic analysis
2. Packing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de análisis ejecuta la muestra en un entorno controlado? | `basic dynamic analysis` |
| 2 | ¿Qué técnica oculta el código real de un binario? | `Packing` |

### Task 3: Niveles de depuración

**Explicación:** El entorno del sandbox no requiere conexión a Internet (respuesta **N**). Los niveles de debugger se clasifican en **assembly-level debugger** (trabaja a nivel de instrucciones/ensamblador) y **Kernel-level debugger** (depura el propio kernel y los drivers).

1. N
2. assembly-level debugger
3. Kernel-level debugger

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Hace falta Internet en la VM del sandbox? | `N` |
| 2 | ¿Qué debugger opera a nivel de instrucciones? | `assembly-level debugger` |
| 3 | ¿Qué debugger trabaja a nivel de kernel? | `Kernel-level debugger` |

### Task 4: Paneles de las herramientas

**Explicación:** En las herramientas de análisis se usa la pestaña **CPU tab** de x64dbg para ver el flujo de instrucciones, y la pestaña **Handles tab** de Process Explorer/Process Monitor para inspeccionar los handles abiertos por el proceso.

1. CPU tab
2. Handles tab

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué pestaña muestra el código/CPU en x64dbg? | `CPU tab` |
| 2 | ¿Qué pestaña muestra los handles del proceso? | `Handles tab` |

### Task 5: Inspección del proceso

**Explicación:** La muestra no necesita conexión externa (respuesta **N**), el proceso analizado tiene **1** thread, la llamada observada es **CreateToolhelp32Snapshot** y la DLL que la exporta es **Kernel32.dll**. Esta API se usa para hacer un snapshots de procesos/hebras del sistema.

1. N
2. 1
3. CreateToolhelp32Snapshot
4. Kernel32.dll

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿La muestra necesita conexión externa? | `N` |
| 2 | ¿Cuántos threads tiene el proceso analizado? | `1` |
| 3 | ¿Qué llamada/API se observa? | `CreateToolhelp32Snapshot` |
| 4 | ¿Qué módulo exporta esa API? | `Kernel32.dll` |

### Task 6: Parcheo del binario

**Explicación:** Para evitar que la comprobación altere el comportamiento de la muestra durante el análisis se recurre a **Patching**: se modifican los bytes o se salta la instrucción condicional para que el binario continúe ejecutándose sin detenerse o sin cargar la protección.

1. Patching

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué técnica modifica el binario para evadir la comprobación? | `Patching` |

### Task 7: Cierre

**Explicación:** Tarea de cierre y repaso del análisis dinámico y el uso de debuggers. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala | `No answer needed` |

---

**Metodología:**

1. Preparar un sandbox/VM aislada y ejecutar la muestra en modo dinámico.
2. Detectar el packing y clasificar la muestra.
3. Cargar la muestra en un debugger de ensamblador (x64dbg) revisando la pestaña CPU y los handles del proceso.
4. Observar las llamadas realizadas (CreateToolhelp32Snapshot en Kernel32.dll) y los threads del proceso.
5. Patchear el binario para evadir la protección y completar el análisis.

**Learning chain:** Sandbox -> Análisis dinámico -> Packing -> Debugger (assembly/kernel) -> x64dbg (CPU) -> Process Monitor (Handles) -> Threads (1) -> CreateToolhelp32Snapshot -> Kernel32.dll -> Patching

**Lección:** *El análisis dinámico con debuggers y monitores de procesos revela el comportamiento real de la muestra y, mediante patching, permite alterar su flujo para entenderla mejor.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1027.002 (Software Packing)

**Fuente:** [TryHackMe - Dynamic Analysis_ Debugging](https://tryhackme.com/room/dynamicanalysisdebugging)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.