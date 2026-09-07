# Agent Design

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `agentdesign` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/agentdesign) |
| **Sección** | AI Agents |
| **Fuente** | THM |
| **Componentes** | Agent design lifecycle, Role/Scope, Tool boundary, Context/State/Memory, Human oversight |
| **Impacto** | Diseño de agentes IA seguros |

---

**Contexto:** Room del AI Security Path de TryHackMe centrado en la fase de *design* del ciclo de vida de un agente IA. Antes de implementar cualquier agente, hay que definirlo: qué rol cumple, cuál es su alcance, qué herramientas puede (y no puede) usar, cómo gestiona contexto, estado y memoria, y cuándo debe detenerse y escalar a supervisión humana. Una mala decisión de diseño en estas fases se traduce en riesgo directo durante la operación.

## Solucionario

### Task 2: From Discovery to Design

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What defines agent behaviour before implementation? | `agent design` |
| 2 | What do these questions reduce before implementation begins? | `ambiguity` |
| 3 | What can a vague agent design create? | `risk` |

### Task 3: Define the Agent Role and Scope

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What describes what the agent is responsible for? | `role` |
| 2 | What should happen to a design choice if it allows the agent to act beyond investigation support? | `rejected` |

### Task 4: Design the Tool Boundary

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What extends agent capability? | `tools` |
| 2 | Should the agent be able to modify systems (yea/nay)? | `nay` |

### Task 5: Design Context, State, and Memory

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tracks workflow progress? | `state` |
| 2 | What information is available to the model during a specific run? | `context` |

### Task 6: Human Oversight and Stop Conditions

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who owns the final decision? | `the engineer` |
| 2 | Should agents retry forever (yea/nay)? | `nay` |
| 3 | What should missing evidence trigger? | `human review` |

### Task 7: Design the Structured Output

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What must the agent use when evidence does not support a priority recommendation? | `undetermined` |
| 2 | What should not replace supporting evidence? | `confidence` |

### Task 8: Agent Spec Builder

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag revealed? | `THM{agent_design_ready}` |

---

**Metodología:** Recorrer el lifecycle de diseño de un agente IA definiendo primero el rol y alcance, luego acotar el boundary de herramientas (denegando acciones que alteren sistemas), diseñar contexto/estado/memoria, fijar condiciones de parada y supervisión humana, definir la salida estructurada, y finalmente consolidarlo en una especificación del agente.

**Learning chain:** Discovery → Design del rol/scope → Tool boundary → Context/State/Memory → Human oversight & stop conditions → Structured output → Agent Spec

**MITRE ATT&CK:** N/A (Room de diseño/defensa de agentes IA)

**Fuente:** [TryHackMe - Agent Design](https://tryhackme.com/r/room/agentdesign)
