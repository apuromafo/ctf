# NoScope: Finding RCE

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `noscoperce` | https://tryhackme.com/room/noscoperce | Web Exploitation | TryHackMe | Alf.io, Mozilla Rhino, sandbox escape, CVE-2026-35482 | Crítico — ejecución remota de código (RCE) en servidor Alf.io mediante bypass de sandbox Rhino y escape completo al host |

---

**Contexto:** Este房间 explota una vulnerabilidad de ejecución remota de código en Alf.io, el software de venta de entradas open-source. El root cause es una referencia en vivo a `java.lang.Class` expuesta al scope de scripts, protegida únicamente por un deny-list que nunca modeló dicha referencia como vector de amenaza. Esto permite un sandbox escape completo en Mozilla Rhino, el motor de scripting JavaScript del lado servidor. La vulnerabilidad fue asignada CVE-2026-35482 y fue independientemente reproducida por el agente Challenger.

> **ES:** Explotación de una vulnerabilidad de ejecución remota de código (RCE) en Alf.io: una referencia viva a `java.lang.Class` (`returnClass`) expuesta al scope de scripts permite, mediante `returnClass.forName(...)`, escapar por completo del sandbox de Mozilla Rhino y ejecutar comandos en el host (CVE-2026-35482, CVSS 8.0).
> **EN:** Exploitation of a remote code execution (RCE) vulnerability in Alf.io: a live reference to `java.lang.Class` (`returnClass`) exposed to the script scope allows a full escape from the Mozilla Rhino sandbox via `returnClass.forName(...)`, achieving host command execution (CVE-2026-35482, CVSS 8.0).

## Solucionario

### Task 1: Reconocimiento de Alf.io

**Explicación:** Se identifica el motor de sandboxing en uso por el servidor Alf.io (Mozilla Rhino) y el agente que reprodujo el exploit de forma independiente (Challenger).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What sandboxing engine is in use? | `Mozilla Rhino` |
| 2 | Which agent independently reproduced the exploit? | `Challenger` |

### Task 2: Análisis del Vector de Ataque

**Explicación:** Se determina en qué evento se dispara el payload (`EVENT_STATUS_CHANGE`), el código de la vulnerabilidad (CVE-2026-35482), su rating CVSS 8.0 (High) y el mapeo CWE-470 (Unsafe Reflection).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | On what event is the payload triggered? | `EVENT_STATUS_CHANGE` |
| 2 | CVE number (Alf.io RCE) | `CVE-2026-35482` |
| 3 | CVSS rating | `8.0 (High)` |
| 4 | CWE mapping | `CWE-470 (Unsafe Reflection)` |

### Task 3: Identificación del Software Objetivo

**Explicación:** Se concreta el software objetivo del laboratorio y su versión exacta: Alf.io 2.0-M5-2509-1.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Target software & version | `Alf.io 2.0-M5-2509-1` |

### Task 4: Root Cause y Sandbox Escape

**Explicación:** Análisis del root cause: la referencia en vivo `returnClass` a `java.lang.Class` expuesta al scope del script y protegida por un deny-list que nunca la modeló como vector de amenaza; invocando `returnClass.forName(...)` se sortea el deny-list.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Root cause in one line | `Una referencia en vivo a java.lang.Class (returnClass) expuesta al scope del script, protegida por un deny-list que nunca la modeló como vector de amenaza` |
| 2 | Key object that enables the sandbox escape | `returnClass` (a live java.lang.Class object; calling `returnClass.forName(...)` bypasses the deny-list) |

### Task 5: Flag

**Explicación:** La flag requiere explotación en vivo contra la máquina desplegada del laboratorio, lanzando el payload de sandbox escape contra Alf.io.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag | `Requiere explotación en vivo (máquina desplegada)` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What sandboxing engine is in use? | `Mozilla Rhino` |
| 2 | Which agent independently reproduced the exploit? | `Challenger` |
| 3 | On what event is the payload triggered? | `EVENT_STATUS_CHANGE` |
| 4 | CVE number (Alf.io RCE) | `CVE-2026-35482` |
| 5 | CVSS rating | `8.0 (High)` |
| 6 | CWE mapping | `CWE-470 (Unsafe Reflection)` |
| 7 | Target software & version | `Alf.io 2.0-M5-2509-1` |
| 8 | Root cause in one line | `Una referencia en vivo a java.lang.Class (returnClass) expuesta al scope del script, protegida por un deny-list que nunca la modeló como vector de amenaza` |
| 9 | Key object that enables the sandbox escape | `returnClass` (a live java.lang.Class object; calling `returnClass.forName(...)` bypasses the deny-list) |
| 10 | Flag | `Requiere explotación en vivo (máquina desplegada)` |

---

**Metodología:** Se identificó el motor de scripting (Mozilla Rhino) en Alf.io y se analizó el deny-list aplicado al scope de los scripts. Se descubrió que `returnClass` (una referencia en vivo a `java.lang.Class`) no estaba incluida en el deny-list. Mediante `EVENT_STATUS_CHANGE` se disparó un payload que invocó `returnClass.forName(...)` para cargar clases arbitrarias del JVM, logrando escape completo del sandbox y ejecución de comandos en el host. La vulnerabilidad se documentó como CVE-2026-35482 con CVSS 8.0.

### Cadena de ataque / Attack Chain

```text
Despliegue de Alf.io -> revisión del scope de Mozilla Rhino -> análisis del deny-list -> returnClass (referencia viva a java.lang.Class) -> disparo vía EVENT_STATUS_CHANGE -> returnClass.forName(...) -> carga de clases arbitarias del JVM -> sandbox escape -> RCE en el host (CVE-2026-35482)
```

**Learning chain:** Alf.io architecture → Mozilla Rhino sandbox → deny-list analysis → returnClass live reference → EVENT_STATUS_CHANGE trigger → returnClass.forName bypass → RCE via Java class loading → CVE-2026-35482

**Lección:** *Un deny-list que no modela los objetos vivos del runtime (como una referencia a `java.lang.Class`) deja un hueco explotable: la seguridad por listas negativas falla cuando no se contemplan todos los vectores reales del lenguaje.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006 (Command and Scripting Interpreter: Python/JavaScript), T1203 (Exploitation for Client Execution)

**Fuente:** [TryHackMe - NoScope: Finding RCE](https://tryhackme.com/room/noscoperce)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.