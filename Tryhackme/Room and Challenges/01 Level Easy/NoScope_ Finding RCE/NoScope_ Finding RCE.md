# NoScope: Finding RCE

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `noscoperce` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/noscoperce) |
| **Sección** | Web Exploitation |
| **Fuente** | THM |
| **Componentes** | Alf.io, Mozilla Rhino, sandbox escape, CVE-2026-35482 |
| **Impacto** | Crítico — ejecución remota de código (RCE) en servidor Alf.io mediante bypass de sandbox Rhino y escape completo al host |

---

**Contexto:** Este房间 explota una vulnerabilidad de ejecución remota de código en Alf.io, el software de venta de entradas open-source. El root cause es una referencia en vivo a `java.lang.Class` expuesta al scope de scripts, protegida únicamente por un deny-list que nunca modeló dicha referencia como vector de amenaza. Esto permite un sandbox escape completo en Mozilla Rhino, el motor de scripting JavaScript del lado servidor. La vulnerabilidad fue asignada CVE-2026-35482 y fue independientemente reproducida por el agente Challenger.

## Solucionario

### Task 1: Reconocimiento de Alf.io

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What sandboxing engine is in use? | `Mozilla Rhino` |
| 2 | Which agent independently reproduced the exploit? | `Challenger` |

### Task 2: Análisis del Vector de Ataque

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | On what event is the payload triggered? | `EVENT_STATUS_CHANGE` |
| 2 | CVE number (Alf.io RCE) | `CVE-2026-35482` |
| 3 | CVSS rating | `8.0 (High)` |
| 4 | CWE mapping | `CWE-470 (Unsafe Reflection)` |

### Task 3: Identificación del Software Objetivo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Target software & version | `Alf.io 2.0-M5-2509-1` |

### Task 4: Root Cause y Sandbox Escape

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Root cause in one line | `Una referencia en vivo a java.lang.Class (returnClass) expuesta al scope del script, protegida por un deny-list que nunca la modeló como vector de amenaza` |
| 2 | Key object that enables the sandbox escape | `returnClass` (a live java.lang.Class object; calling `returnClass.forName(...)` bypasses the deny-list) |

### Task 5: Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag | `Requiere explotación en vivo (máquina desplegada)` |

---

**Metodología:** Se identificó el motor de scripting (Mozilla Rhino) en Alf.io y se analizó el deny-list aplicado al scope de los scripts. Se descubrió que `returnClass` (una referencia en vivo a `java.lang.Class`) no estaba incluida en el deny-list. Mediante `EVENT_STATUS_CHANGE` se disparó un payload que invocó `returnClass.forName(...)` para cargar clases arbitrarias del JVM, logrando escape completo del sandbox y ejecución de comandos en el host. La vulnerabilidad se documentó como CVE-2026-35482 con CVSS 8.0.
**Learning chain:** Alf.io architecture → Mozilla Rhino sandbox → deny-list analysis → returnClass live reference → EVENT_STATUS_CHANGE trigger → returnClass.forName bypass → RCE via Java class loading → CVE-2026-35482
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006 (Command and Scripting Interpreter: Python/JavaScript), T1203 (Exploitation for Client Execution)
**Fuente:** [TryHackMe - NoScope: Finding RCE](https://tryhackme.com/r/room/noscoperce)
