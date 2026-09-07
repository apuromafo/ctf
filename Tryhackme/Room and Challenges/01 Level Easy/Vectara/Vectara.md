# Vectara

| **Dificultad** | Easy |
| **Tipo** | challenge |
| **Slug** | `vectara` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/vectara) |
| **Sección** | AI Security Path |
| **Fuente** | THM |
| **Componentes** | RAG, prompt injection, HHEM, model registry |
| **Impacto** | Medio |

---

**Contexto:** Sala challenge del AI Security Path que simula un escenario de RAG (Retrieval-Augmented Generation) con múltiples amenazas de IA. Vectara despliega una plataforma con los módulos Choir, Badge y Exabrian — un stack RAG completo. El participante explora prompt injection en plantillas de origen, data poisoning en supply chains logísticas, manipulación de model registry, y worms de agentes XSS médicos. Cada task presenta un escenario ficticio con flags propias.

## Solucionario

### Task 1: Transmission Zero

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the message. Find the flag. | `THM{0racl3_9_1s_c0ming}` |

### Task 2: In a Pickle

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | What is the name of the directive injected into the source template? | `OVERRIDE_9` |
| 3 | What is the flag? | `THM{p01s0n3d_fr0m_th3_s0urc3}` |

### Task 3: Ghost Ship

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | What is the registry entry ID of the model under review? | `XR-7-491` |
| 5 | What is the flag? | `THM{gh0st_1n_th3_r3g1stry}` |

### Task 4: Dead Freight

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | What is the classified cargo code hidden in HaulMind's records? | `THM{m4n1f3st_unl0ck3d}` |

### Task 5: Glitched Transit

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | Which cargo hold has a falsified manifest? | `D` |
| 8 | What is the full name of the fake filing source? | `TryHaulMe Central Logistics Bureau` |
| 9 | What is the flag hidden in the forged manifest? | `THM{GH0ST_FR31GHT}` |

### Task 6: GhostQuery

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 10 | What is the flag? | `THM{b84bc0f023bc0bc0fdbb85eae75b26c4}` |

### Task 7: Protocol Drift

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 11 | What is the flag? | `THM{med1c4l_xss_ag3nt_w0rm}` |

---

**Metodología:** Cada task corresponde a un escenario independiente dentro del ecosistema Vectara RAG. Se exploraron: inyección de directivas en plantillas de origen (In a Pickle), manipulación de model registry (Ghost Ship), data poisoning en supply chains logísticos (Dead Freight / Glitched Transit), y worms de agentes XSS en contextos médicos (Protocol Drift). Los flags se obtuvieron mediante análisis forense de los componentes RAG comprometidos.

**Learning chain:** RAG Architecture → Prompt Injection → Data Poisoning → Model Registry Manipulation → Supply Chain Tampering → Agent XSS Worms → HHEM

**MITRE ATT&CK:** N/A — Challenge defensivo/AI adversarial focus

**Fuente:** [TryHackMe - Vectara](https://tryhackme.com/r/room/vectara)
