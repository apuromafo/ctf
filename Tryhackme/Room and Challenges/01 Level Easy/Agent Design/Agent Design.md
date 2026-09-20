# Agent Design

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `agentdesign` | https://tryhackme.com/room/agentdesign | AI Agents | THM | Agent design lifecycle, Role/Scope, Tool boundary, Context/State/Memory, Human oversight | Diseño de agentes IA seguros |

---

**Contexto:** Room del AI Security Path de TryHackMe centrado en la fase de *design* del ciclo de vida de un agente IA. Antes de implementar cualquier agente, hay que definirlo: qué rol cumple, cuál es su alcance, qué herramientas puede (y no puede) usar, cómo gestiona contexto, estado y memoria, y cuándo debe detenerse y escalar a supervisión humana. Una mala decisión de diseño en estas fases se traduce en riesgo directo durante la operación.

> **ES:** Recorrer el ciclo de vida del diseño de un agente IA: rol, alcance, límites de herramientas, contexto/estado/memoria, supervisión humana, salida estructurada y especificación final.
> **EN:** Walk the agent design lifecycle: role, scope, tool boundary, context/state/memory, human oversight, structured output and the final agent spec.

## Solucionario

### Task 2: Del descubrimiento al diseño / From Discovery to Design

**Explicación:** Antes de implementar el agente hay que definirlo explícitamente: es el **agent design** lo que define su comportamiento previo a la implementación. Hacer las preguntas de diseño correctas (qué tarea, qué datos, qué entorno) reduce la **ambiguity**, y si el diseño es vago se acaba generando **risk** para la organización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What defines agent behaviour before implementation? | `agent design` |
| 2 | What do these questions reduce before implementation begins? | `ambiguity` |
| 3 | What can a vague agent design create? | `risk` |

### Task 3: Definir el rol y alcance del agente / Define the Agent Role and Scope

**Explicación:** El agente necesita un **role** que describa de qué es responsable. Cualquier decisión de diseño que permita al agente actuar más allá del soporte de investigación (por ejemplo, modificar sistemas) debe ser **rejected** para mantener el alcance acotado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What describes what the agent is responsible for? | `role` |
| 2 | What should happen to a design choice if it allows the agent to act beyond investigation support? | `rejected` |

### Task 4: Diseñar el límite de herramientas / Design the Tool Boundary

**Explicación:** Las **tools** extienden la capacidad del agente, pero cada una amplía superficie de riesgo. El diseño debe impedir que el agente modifique sistemas ni realice acciones destructivas: no debe poder modificar sistemas (respuesta **nay**).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What extends agent capability? | `tools` |
| 2 | Should the agent be able to modify systems (yea/nay)? | `nay` |

### Task 5: Diseñar contexto, estado y memoria / Design Context, State, and Memory

**Explicación:** El **state** da seguimiento al progreso del workflow (en qué paso va la investigación). El **context** es la información disponible para el modelo durante una ejecución concreta. Separar ambos evita que el agente pierda el hilo entre pasos y sobrecargue la ventana del modelo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tracks workflow progress? | `state` |
| 2 | What information is available to the model during a specific run? | `context` |

### Task 6: Supervisión humana y condiciones de parada / Human Oversight and Stop Conditions

**Explicación:** El responsable de la decisión final es **the engineer** (el humano), no el agente. El agente no debe reintentar indefinidamente (**nay**); ante evidencia faltante debe detenerse y escalar, disparando una **human review** para que el humano complete el análisis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who owns the final decision? | `the engineer` |
| 2 | Should agents retry forever (yea/nay)? | `nay` |
| 3 | What should missing evidence trigger? | `human review` |

### Task 7: Diseñar la salida estructurada / Design the Structured Output

**Explicación:** La salida estructurada obliga al agente a declarar **undetermined** cuando la evidencia no respalda una recomendación prioritaria. Además, la **confidence** (confianza) del modelo nunca debe sustituir a la evidencia de apoyo: un nivel de confianza alto no convierte una conjetura en un hallazgo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What must the agent use when evidence does not support a priority recommendation? | `undetermined` |
| 2 | What should not replace supporting evidence? | `confidence` |

### Task 8: Constructor de especificaciones del agente / Agent Spec Builder

**Explicación:** Se consolida todo lo diseñado en una especificación del agente mediante el builder de la room. Al completar la especificación atendiendo a rol, tools, contexto/estado, supervisión y salida, se revela la flag del reto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag revealed? | `THM{agent_design_ready}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What defines agent behaviour before implementation? | `agent design` |
| 2 | What do these questions reduce before implementation begins? | `ambiguity` |
| 3 | What can a vague agent design create? | `risk` |
| 4 | What describes what the agent is responsible for? | `role` |
| 5 | What should happen to a design choice if it allows the agent to act beyond investigation support? | `rejected` |
| 6 | What extends agent capability? | `tools` |
| 7 | Should the agent be able to modify systems (yea/nay)? | `nay` |
| 8 | What tracks workflow progress? | `state` |
| 9 | What information is available to the model during a specific run? | `context` |
| 10 | Who owns the final decision? | `the engineer` |
| 11 | Should agents retry forever (yea/nay)? | `nay` |
| 12 | What should missing evidence trigger? | `human review` |
| 13 | What must the agent use when evidence does not support a priority recommendation? | `undetermined` |
| 14 | What should not replace supporting evidence? | `confidence` |
| 15 | What is the flag revealed? | `THM{agent_design_ready}` |

---

**Metodología:** Recorrer el lifecycle de diseño de un agente IA definiendo primero el rol y alcance, luego acotar el boundary de herramientas (denegando acciones que alteren sistemas), diseñar contexto/estado/memoria, fijar condiciones de parada y supervisión humana, definir la salida estructurada, y finalmente consolidarlo en una especificación del agente.

### Cadena de ataque / Attack Chain

```text
Discovery -> definir rol/scope -> acotar tool boundary (sin modificar sistemas) -> contexto/estado/memoria -> stop conditions + human oversight -> salida estructurada (undetermined/confidence) -> Agent Spec Builder -> flag
```

**Learning chain:** Discovery → Design del rol/scope → Tool boundary → Context/State/Memory → Human oversight & stop conditions → Structured output → Agent Spec

**Lección:** *Diseñar primero (rol, herramientas, estado y paradas humanas) evita que el agente actúe fuera de su alcance; el agente propone, el ingeniero decide.*

**MITRE ATT&CK:** N/A (Room de diseño/defensa de agentes IA)

**Fuente:** [TryHackMe - Agent Design](https://tryhackme.com/room/agentdesign)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.