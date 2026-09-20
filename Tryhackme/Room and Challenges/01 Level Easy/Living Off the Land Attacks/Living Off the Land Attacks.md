# Living Off the Land Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | livingoffthelandattacks | [TryHackMe](https://tryhackme.com/room/livingoffthelandattacks) | 01 Level Easy | THM | GTFOBins, Sysinternals, WMI, T1546.003, IEX, SMB | Ataques living off the land: uso de binarios y herramientas legítimas del sistema para evadir detecciones |

---

**Contexto:** Sala sobre ataques "living off the land" (LotL), donde el atacante abusa de binarios y herramientas legítimas del sistema. Se cubren GTFOBins (Linux) y Sysinternals (Windows), técnicas MITRE como `T1546.003` (WMI Event Subscription), el uso de SMB para movimiento lateral y la ejecución de payloads en memoria con `IEX`.

> **EN:**
> 1. No answer needed
> 2. 1. GTFOBins
>    2. Sysinternals
> 3. 1. T1546.003
>    2. SMB
> 4. 1. IEX
>    2. create
> 5. THM{LOL-but-not-that-lol-you-finishit}
> 6. No answer needed

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta el concepto de ataques living off the land: utilizar programas que ya existen en el sistema víctima para operar sin desplegar malware.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Herramientas abusables / Abusable tools

**Explicación:** Se recopilan las bases de datos y conjuntos de herramientas que documentan binarios legítimos abusables: `GTFOBins` para binarios Unix y `Sysinternals` para utilidades de Windows.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué proyecto documenta binarios Unix abusables? / Which project documents abusable Unix binaries? | `GTFOBins` |
| 2 | ¿Qué conjunto de herramientas de Windows es abusable? / Which Windows toolset is abusable? | `Sysinternals` |

### Task 3: Técnica y transporte / Technique and transport

**Explicación:** Se identifica la técnica MITRE empleada (`T1546.003`, suscripciones WMI que activan eventos) y el protocolo usado para el desplazamiento lateral o la distribución de archivos (`SMB`).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué técnica MITRE se emplea? / Which MITRE technique is used? | `T1546.003` |
| 2 | ¿Qué protocolo se usa para transferir/ejecutar? / Which protocol is used to transfer/execute? | `SMB` |

### Task 4: Ejecución en memoria / In-memory execution

**Explicación:** Se práctica el típico flujo LotL en Windows: cargar y ejecutar un script en memoria con `IEX` (Invoke-Expression) y persistir creando el artefacto con el parámetro `create`.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué cmdlet de PowerShell ejecuta código cargado en memoria? / Which PowerShell cmdlet executes code loaded in memory? | `IEX` |
| 2 | ¿Qué acción confirma la creación del artefacto? / Which action confirms the creation of the artifact? | `create` |

### Task 5: Flag de finalización / Completion flag

**Explicación:** La flag confirma la finalización de la sala tras completar todos los ejercicios de abuso de binarios legítimos.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuál es la flag de finalización? / What is the completion flag? | `THM{LOL-but-not-that-lol-you-finishit}` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la sala repasando que la defensa contra LotL requiere visibilidad sobre el uso normal de binarios del sistema.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Identificar binarios legítimos abusables consultando `GTFOBins` y `Sysinternals`. Mapear la técnica contra MITRE (`T1546.003`, activación mediante suscripciones WMI) y transportar los artefactos por `SMB`. En el host Windows, cargar el payload en memoria con `IEX` y crear la persistencia con el parámetro `create`, evitando escribir malware en disco. Completar el ejercicio de laboratorio confirma la flag final.

### Cadena de ataque / Attack Chain

Fuentes de binarios abusables → GTFOBins/Sysinternals → técnica T1546.003 (WMI) → transporte por SMB → ejecución con IEX → creación del artefacto → flag final

**Learning chain:** GTFOBins → Sysinternals → T1546.003 → WMI → SMB → IEX → create → THM{LOL-but-not-that-lol-you-finishit}

**Lección:** *Los ataques living off the land son difíciles de detectar porque no introducen código nuevo en disco: abusar de binarios legítimos (documentados en GTFOBins y Sysinternals) y ejecutar payloads en memoria con `IEX` exige monitorizar el comportamiento de los procesos, no solo los archivos.*

**MITRE ATT&CK:** T1546.003 (Event Triggered Execution: WMI Event Subscription), T1218 (System Binary Proxy Execution), T1047 (Windows Management Instrumentation), T1572 (Protocol Tunneling), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Living Off the Land Attacks](https://tryhackme.com/room/livingoffthelandattacks)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.