# Agent Discovery

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `agentdiscovery` | https://tryhackme.com/room/agentdiscovery | AI Agents | THM | Workflows, Assistants, Agents, Discovery canvas | Identificación de flujo agentico |

---

**Contexto:** Room del AI Security Path de TryHackMe que enseña a distinguir entre *workflows* (tradicionales y con IA), *assistants* y *agents*, y a descubrir qué tipo de sistema resuelve mejor cada problema. Se usa un caso práctico (NorthStar, una empresa con un solo ingeniero de seguridad) para mapear el flujo real de investigación de alertas mediante un *Agent Discovery Canvas*.

> **ES:** Clasificar workflows (tradicional/IA), assistants y agents, y usar el Agent Discovery Canvas para mapear el flujo real de investigación de NorthStar.
> **EN:** Classify workflows (traditional/AI), assistants and agents, and use the Agent Discovery Canvas to map NorthStar's real investigation workflow.

## Solucionario

### Task 1: Workflows, asistentes y agentes / Workflows, Assistants, and Agents

**Explicación:** Se diferencian los cuatro tipos de sistema: *traditional workflow* (código y reglas fijas, sin LLM), *ai workflow* (un LLM dentro de una secuencia controlada por código), *ai assistant* (responde a preguntas dirigidas por el ingeniero) y *ai agent* (elige dinámicamente el siguiente paso aprobado). La clave es quién tiene el control de los pasos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which approach uses fixed code and rules without an LLM? | `traditional workflow` |
| 2 | Which approach uses an LLM inside a code-controlled sequence? | `ai workflow` |
| 3 | Which approach responds to engineer-led questions and requests? | `ai assistant` |
| 4 | Which approach dynamically chooses the next approved step? | `ai agent` |

### Task 2: Por qué importa el discovery / Why Agent Discovery Matters

**Explicación:** Se practica la clasificación con ejemplos concretos: extraer IPs y ordenar timestamps con reglas fijas encaja en *traditional workflow*; que el ingeniero pida comparar incidentes y el sistema siga pasos programados es *ai workflow*; y si la primera tool devuelve evidencia débil y el modelo elige otra tool aprobada, eso ya es un *ai agent*.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Extracts IPs, sorts timestamps, follows fixed rules -> fits which approach? | `traditional workflow` |
| 2 | Engineer asks for incident comparison but picks next step -> which system? | `ai workflow` |
| 3 | First tool returns weak evidence, model selects another approved tool -> which type? | `ai agent` |

### Task 3: Entender el problema de negocio / Understanding the Business Problem

**Explicación:** NorthStar tiene un solo ingeniero que revisa ~50 alertas de seguridad al día; todo lo demás (infraestructura y código) también depende de esa única persona (`1` ingeniero en total). Ese volumen y escasez de recursos condicionan qué tiene sentido automatizar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Approx how many security alerts does NorthStar's engineer review each day? | `50` |
| 2 | How many total engineers handle security, infrastructure, and code? | `1` |

### Task 4: Mapear el workflow / Mapping the Workflow

**Explicación:** Se traza la investigación real de una alerta: si incluye una IP externa, el primer paso es comprobar la reputación de la IP (*check ip reputation*). Ante un login desde ubicación inusual seguido de una regla de reenvío de correo externo, lo siguiente es buscar alertas relacionadas (*related alerts*).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Alert contains external source IP -> which investigation step? | `check ip reputation` |
| 2 | Unusual-location login then external mail-forwarding rule -> search what? | `related alerts` |

### Task 5: Canvas de descubrimiento de agentes / Agent Discovery Canvas

**Explicación:** Se completa el Agent Discovery Canvas con todos los datos del flujo mapeado (entradas, pasos, decisiones y tools). Completarlo correctamente entrega la flag del reto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{NoRtHSt4r_Ag3nt}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which approach uses fixed code and rules without an LLM? | `traditional workflow` |
| 2 | Which approach uses an LLM inside a code-controlled sequence? | `ai workflow` |
| 3 | Which approach responds to engineer-led questions and requests? | `ai assistant` |
| 4 | Which approach dynamically chooses the next approved step? | `ai agent` |
| 5 | Extracts IPs, sorts timestamps, follows fixed rules -> fits which approach? | `traditional workflow` |
| 6 | Engineer asks for incident comparison but picks next step -> which system? | `ai workflow` |
| 7 | First tool returns weak evidence, model selects another approved tool -> which type? | `ai agent` |
| 8 | Approx how many security alerts does NorthStar's engineer review each day? | `50` |
| 9 | How many total engineers handle security, infrastructure, and code? | `1` |
| 10 | Alert contains external source IP -> which investigation step? | `check ip reputation` |
| 11 | Unusual-location login then external mail-forwarding rule -> search what? | `related alerts` |
| 12 | What's the flag? | `THM{NoRtHSt4r_Ag3nt}` |

---

**Metodología:** Clasificar el tipo de sistema (workflow tradicional / workflow IA / assistant / agent) según quién toma las decisiones y qué tan dinámicos son los pasos; luego entender el problema de negocio (carga de alertas, personal) y mapear verazmente el flujo de investigación real antes de decidir qué automatizar.

### Cadena de ataque / Attack Chain

```text
Clasificar approach (tradicional/IA/assistant/agent) -> entender el negocio (50 alertas, 1 ingeniero) -> mapear pasos (IP rep, related alerts) -> completar Agent Discovery Canvas -> flag
```

**Learning chain:** Clasificar approaches → Entender por qué importa el discovery → Analizar el problema de negocio → Mapear el workflow real → Completar el Discovery Canvas

**Lección:** *Antes de construir un agente hay que descubrir el flujo real: si los pasos son fijos es un workflow, si un modelo elige el siguiente paso aprobado es un agente.*

**MITRE ATT&CK:** N/A (Room de diseño/identificación de flujos agenticos)

**Fuente:** [TryHackMe - Agent Discovery](https://tryhackme.com/room/agentdiscovery)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.