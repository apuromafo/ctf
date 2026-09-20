# Vectara

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `vectara` | [TryHackMe](https://tryhackme.com/r/room/vectara) | AI Security Path | THM | RAG, prompt injection, HHEM, model registry | Medio |

---

**Contexto:** Sala challenge del AI Security Path que simula un escenario de RAG (Retrieval-Augmented Generation) con múltiples amenazas de IA. Vectara despliega una plataforma con los módulos Choir, Badge y Exabrian — un stack RAG completo. El participante explora prompt injection en plantillas de origen, data poisoning en supply chains logísticas, manipulación de model registry, y worms de agentes XSS médicos. Cada task presenta un escenario ficticio con flags propias.

> **ES:** Sala challenge del AI Security Path sobre un stack RAG completo (Vectara): prompt injection, data poisoning, manipulación del model registry y worms de agentes XSS médicos, con flags propias por escenario.
> **EN:** AI Security Path challenge room over a full RAG stack (Vectara): prompt injection, data poisoning, model registry manipulation and medical agent XSS worms, each scenario with its own flags.

## Solucionario

### Task 1: Transmission Zero

**Explicación:** Primer escenario del ecosistema Vectara RAG: encontrar el mensaje y la flag correspondiente.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Find the message. Find the flag. | `THM{0racl3_9_1s_c0ming}` |

### Task 2: In a Pickle

**Explicación:** Escenario de prompt injection en plantillas de origen: se identifica la directiva inyectada en la plantilla fuente y se obtiene la flag.

| # | Pregunta | Respuesta |
|---|---|---|
| 2 | What is the name of the directive injected into the source template? | `OVERRIDE_9` |
| 3 | What is the flag? | `THM{p01s0n3d_fr0m_th3_s0urc3}` |

### Task 3: Ghost Ship

**Explicación:** Escenario de manipulación del model registry: se identifica el ID de la entrada del registry del modelo bajo revisión y se recupera la flag.

| # | Pregunta | Respuesta |
|---|---|---|
| 4 | What is the registry entry ID of the model under review? | `XR-7-491` |
| 5 | What is the flag? | `THM{gh0st_1n_th3_r3g1stry}` |

### Task 4: Dead Freight

**Explicación:** Escenario de data poisoning en la supply chain logística: se localiza el código de carga clasificada oculto en los registros de HaulMind.

| # | Pregunta | Respuesta |
|---|---|---|
| 6 | What is the classified cargo code hidden in HaulMind's records? | `THM{m4n1f3st_unl0ck3d}` |

### Task 5: Glitched Transit

**Explicación:** Escenario de manipulación de manifiestos: se identifica la bodega con manifiesto falsificado, el nombre completo de la fuente de filing falsa y la flag oculta en el manifiesto forjado.

| # | Pregunta | Respuesta |
|---|---|---|
| 7 | Which cargo hold has a falsified manifest? | `D` |
| 8 | What is the full name of the fake filing source? | `TryHaulMe Central Logistics Bureau` |
| 9 | What is the flag hidden in the forged manifest? | `THM{GH0ST_FR31GHT}` |

### Task 6: GhostQuery

**Explicación:** Escenario independiente dentro del ecosistema Vectara: se obtiene la flag correspondiente.

| # | Pregunta | Respuesta |
|---|---|---|
| 10 | What is the flag? | `THM{b84bc0f023bc0bc0fdbb85eae75b26c4}` |

### Task 7: Protocol Drift

**Explicación:** Escenario de worms de agentes XSS en contextos médicos: se obtiene la flag final.

| # | Pregunta | Respuesta |
|---|---|---|
| 11 | What is the flag? | `THM{med1c4l_xss_ag3nt_w0rm}` |

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1 | Find the message. Find the flag. | `THM{0racl3_9_1s_c0ming}` |
| 2 | What is the name of the directive injected into the source template? | `OVERRIDE_9` |
| 2 | What is the flag? | `THM{p01s0n3d_fr0m_th3_s0urc3}` |
| 3 | What is the registry entry ID of the model under review? | `XR-7-491` |
| 3 | What is the flag? | `THM{gh0st_1n_th3_r3g1stry}` |
| 4 | What is the classified cargo code hidden in HaulMind's records? | `THM{m4n1f3st_unl0ck3d}` |
| 5 | Which cargo hold has a falsified manifest? | `D` |
| 5 | What is the full name of the fake filing source? | `TryHaulMe Central Logistics Bureau` |
| 5 | What is the flag hidden in the forged manifest? | `THM{GH0ST_FR31GHT}` |
| 6 | What is the flag? | `THM{b84bc0f023bc0bc0fdbb85eae75b26c4}` |
| 7 | What is the flag? | `THM{med1c4l_xss_ag3nt_w0rm}` |

---

**Metodología:** Cada task corresponde a un escenario independiente dentro del ecosistema Vectara RAG. Se exploraron: inyección de directivas en plantillas de origen (In a Pickle), manipulación de model registry (Ghost Ship), data poisoning en supply chains logísticos (Dead Freight / Glitched Transit), y worms de agentes XSS en contextos médicos (Protocol Drift). Los flags se obtuvieron mediante análisis forense de los componentes RAG comprometidos.

### Cadena de ataque / Attack Chain

Reconocimiento del stack RAG (Choir, Badge, Exabrian) → análisis de plantillas de origen → prompt injection en templates (OVERRIDE_9) → manipulación del model registry (XR-7-491) → data poisoning en registros logísticos (HaulMind) → manifiestos forjados (TryHaulMe Central Logistics Bureau) → GhostQuery → worm XSS médico (Protocol Drift)

**Learning chain:** RAG Architecture → Prompt Injection → Data Poisoning → Model Registry Manipulation → Supply Chain Tampering → Agent XSS Worms → HHEM

**Lección:** *En los sistemas RAG la cadena de confianza completa es atacable: desde la plantilla de origen y el registry de modelos hasta los manifiestos de la supply chain y los agentes, cada componente conectado puede ser envenenado o manipulado para desviar el comportamiento del sistema de IA.*

**MITRE ATT&CK:** N/A — Challenge defensivo/AI adversarial focus

**Fuente:** [TryHackMe - Vectara](https://tryhackme.com/room/vectara)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.