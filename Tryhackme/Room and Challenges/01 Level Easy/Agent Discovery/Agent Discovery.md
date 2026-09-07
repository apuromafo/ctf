# Agent Discovery

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `agentdiscovery` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/agentdiscovery) |
| **Sección** | AI Agents |
| **Fuente** | THM |
| **Componentes** | Workflows, Assistants, Agents, Discovery canvas |
| **Impacto** | Identificación de flujo agentico |

---

**Contexto:** Room del AI Security Path de TryHackMe que enseña a distinguir entre *workflows* (tradicionales y con IA), *assistants* y *agents*, y a descubrir qué tipo de sistema resuelve mejor cada problema. Se usa un caso práctico (NorthStar, una empresa con un solo ingeniero de seguridad) para mapear el flujo real de investigación de alertas mediante un *Agent Discovery Canvas*.

## Solucionario

### Task 1: Workflows, Assistants, and Agents

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which approach uses fixed code and rules without an LLM? | `traditional workflow` |
| 2 | Which approach uses an LLM inside a code-controlled sequence? | `ai workflow` |
| 3 | Which approach responds to engineer-led questions and requests? | `ai assistant` |
| 4 | Which approach dynamically chooses the next approved step? | `ai agent` |

### Task 2: Why Agent Discovery Matters

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Extracts IPs, sorts timestamps, follows fixed rules -> fits which approach? | `traditional workflow` |
| 2 | Engineer asks for incident comparison but picks next step -> which system? | `ai workflow` |
| 3 | First tool returns weak evidence, model selects another approved tool -> which type? | `ai agent` |

### Task 3: Understanding the Business Problem

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Approx how many security alerts does NorthStar's engineer review each day? | `50` |
| 2 | How many total engineers handle security, infrastructure, and code? | `1` |

### Task 4: Mapping the Workflow

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Alert contains external source IP -> which investigation step? | `check ip reputation` |
| 2 | Unusual-location login then external mail-forwarding rule -> search what? | `related alerts` |

### Task 5: Agent Discovery Canvas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{NoRtHSt4r_Ag3nt}` |

---

**Metodología:** Clasificar el tipo de sistema (workflow tradicional / workflow IA / assistant / agent) según quién toma las decisiones y qué tan dinámicos son los pasos; luego entender el problema de negocio (carga de alertas, personal) y mapear verazmente el flujo de investigación real antes de decidir qué automatizar.

**Learning chain:** Clasificar approaches → Entender por qué importa el discovery → Analizar el problema de negocio → Mapear el workflow real → Completar el Discovery Canvas

**MITRE ATT&CK:** N/A (Room de diseño/identificación de flujos agenticos)

**Fuente:** [TryHackMe - Agent Discovery](https://tryhackme.com/r/room/agentdiscovery)
