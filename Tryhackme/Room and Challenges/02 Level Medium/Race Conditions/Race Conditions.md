# Race Conditions

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Explotación / CTF | raceconditions | https://tryhackme.com/room/raceconditions | 02 Level Medium | TryHackMe | Condiciones de carrera, Concurrencia, Procesos/Hilos | Ejecución no determinista / corrupción de estado |

> **Objeto:** Entender qué es una condición de carrera (race condition), distinguir los conceptos de program, process y thread, identificar cuál de los hilos entra en liza y contar cuántos hilos participan en el escenario descrito.

---

**Contexto:**

La sala **Race Conditions** introduce las condiciones de carrera: situaciones donde dos o más hilos o procesos compiten por un recurso compartido sin sincronización, de modo que el resultado depende del orden de ejecución (quién llega primero). Se estudian los conceptos de programa, proceso e hilo, se razona sobre el estado de espera de un proceso, se identifican los hilos implicados y se contabilizan correctamente antes de validar la explotación obteniendo las flags finales.

> **ES:** La sala trata sobre condiciones de carrera: cuándo múltiples hilos compiten por un recurso compartido sin sincronización y el resultado depende de quién llega primero.

> **EN:** This room covers race conditions: when multiple threads compete for a shared resource without synchronization, and the outcome depends on who gets there first.

## Solucionario

### Task 1: Introducción
**Explicación:**

Pregunta introductoria de la sala; no se requiere respuesta concreta.

1. `No answer needed`

### Task 2: Conceptos de ejecución
**Explicación:**

Se distingue entre programa, proceso e hilo, y se razona sobre el estado en el que queda un proceso al ponerse en marcha (estado de espera / waiting).

1. `Program`
2. `Waiting`

### Task 3: Identificación de hilos
**Explicación:**

Se confirma (o niega) la premisa planteada sobre la condición de carrera y se identifica el hilo concreto que interviene en el escenario.

1. `Nay`
2. `Thread-1`

### Task 4: Conteo de hilos
**Explicación:**

Se contabilizan los hilos que entran en liza en cada uno de los escenarios planteados.

1. `2`
2. `3`
3. `5`

### Task 5: Flag de usuario
**Explicación:**

Se recupera la primera flag tras explotar la condición de carrera sobre el entorno de ficheros/recursos compartidos.

1. `THM{PHONE-RACE}`

### Task 6: Verificación intermedia
**Explicación:**

Pregunta de verificación intermedia sin respuesta concreta; sólo hay que continuar con el flujo de resolución.

1. `No answer needed`

### Task 7: Flag final
**Explicación:**

Se obtiene la flag final al validar la explotación de la condición de carrera sobre el entorno bancario.

1. `THM{BANK-RED-FLAG}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta introductoria | `No answer needed` |
| 2.1 | Concepto identificado | `Program` |
| 2.2 | Estado del proceso | `Waiting` |
| 3.1 | Confirmación de la condición | `Nay` |
| 3.2 | Hilo identificado | `Thread-1` |
| 4.1 | Conteo de hilos (parte 1) | `2` |
| 4.2 | Conteo de hilos (parte 2) | `3` |
| 4.3 | Conteo de hilos (parte 3) | `5` |
| 5 | Flag de usuario | `THM{PHONE-RACE}` |
| 6 | Verificación intermedia | `No answer needed` |
| 7 | Flag final | `THM{BANK-RED-FLAG}` |

---

**Metodología:**

Revisión conceptual de programación concurrente: distinguir programa/proceso/hilo, razonar sobre el orden de ejecución en condiciones de carrera y contabilizar los hilos implicados; finalmente se valida la explotación obteniendo las flags.

**Learning chain:** Program → Process → Thread → recursos compartidos → sincronización → condición de carrera → explotación → flags.

**Lección:** *Una condición de carrera convierte un recurso compartido no sincronizado en un punto de competición donde el resultado depende de "quién llega primero".*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1499 Endpoint Denial of Service · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Race Conditions](https://tryhackme.com/room/raceconditions)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
