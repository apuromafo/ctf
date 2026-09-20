# Alfred

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `alfred` |
| **Link** | [TryHackMe](https://tryhackme.com/room/alfred) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Jenkins, credenciales por defecto `admin:admin`, Metasploit, enumeración de privilegios, token impersonation |
| **Impacto** | Ejecución remota de código en Jenkins y escalada de privilegios hasta `NT AUTHORITY\SYSTEM` |

---

**Contexto:** El room explota una instancia de Jenkins accesible con las credenciales por defecto (`admin:admin`). El panel de administración permite ejecutar comandos, lo que se aprovecha para obtener una shell y, tras pasar a Metasploit y enumerar los privilegios del sistema, escalar hasta la cuenta `NT AUTHORITY\SYSTEM`. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Acceso inicial / Initial Access

**Explicación:** Se identifican los servicios del host objetivo, se accede al panel de administración de Jenkins con las credenciales `admin:admin` y se consigue ejecución de comandos. Se obtiene la primera flag del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `3` |
| 2 | *(Pregunta 2 no especificada en el original)* | `admin:admin` |
| 3 | *(Pregunta 3 no especificada en el original)* | `No answer needed` |
| 4 | *(Pregunta 4 no especificada en el original)* | `79007a09481963edf2e1321abd9ae2a0` |

### Task 2: Shell en Metasploit / Metasploit Shell

**Explicación:** Se traslada el acceso obtenido a una sesión de Metasploit para disponer de un control más cómodo y estable sobre la shell comprometida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `73802` |

### Task 3: Escalada de privilegios / Privilege Escalation

**Explicación:** Se enumeran las tareas y privilegios del sistema, se identifica la capacidad de impersonar tokens de proceso y se escala hasta ejecutar como `NT AUTHORITY\SYSTEM`, obteniendo la flag final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |
| 3 | *(Pregunta 3 no especificada en el original)* | `NT AUTHORITY\SYSTEM` |
| 4 | *(Pregunta 4 no especificada en el original)* | `No answer needed` |
| 5 | *(Pregunta 5 no especificada en el original)* | `dff0f748678f280250f25a45b8046b4a` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `3` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `admin:admin` |
| 3 | *(Task 1, Pregunta 3 no especificada en el original)* | `No answer needed` |
| 4 | *(Task 1, Pregunta 4 no especificada en el original)* | `79007a09481963edf2e1321abd9ae2a0` |
| 5 | *(Task 2, Pregunta 1 no especificada en el original)* | `73802` |
| 6 | *(Task 3, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 7 | *(Task 3, Pregunta 2 no especificada en el original)* | `No answer needed` |
| 8 | *(Task 3, Pregunta 3 no especificada en el original)* | `NT AUTHORITY\SYSTEM` |
| 9 | *(Task 3, Pregunta 4 no especificada en el original)* | `No answer needed` |
| 10 | *(Task 3, Pregunta 5 no especificada en el original)* | `dff0f748678f280250f25a45b8046b4a` |

---

**Metodología:** Acceso a Jenkins con credenciales por defecto → ejecución de comandos / reverse shell → migración a Metasploit → enumeración de privilegios → escalada a `NT AUTHORITY\SYSTEM` mediante abuso de tokens → recogida de flags.

**Learning chain:** Enumeración de servicios → credenciales por defecto → RCE en Jenkins → foothold → escalada a SYSTEM → obtención de banderas

**Lección:** *Las credenciales por defecto en paneles de administración con capacidad de ejecución de comandos (como la Script Console de Jenkins) son una puerta directa al control total del sistema.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1134.001 (Token Impersonation/Theft), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Alfred](https://tryhackme.com/room/alfred)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.