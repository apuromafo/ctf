# AI Threat Modelling Assessment
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `ai-threat-modelling-assessment` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ai-threat-modelling-assessment) |
| **Sección** | Secure AI Systems (Section 2 of 5) |
| **Fuente** | [vanshksingh/TryHackMe-AI-Security-Path](https://github.com/vanshksingh/TryHackMe-AI-Security-Path) — `ai-threat-modelling-assessment\Readme.md` |
| **Componentes** | Evaluación: IA/ML offensivo+defensivo, threat modelling (STRIDE-AI, MITRE ATLAS, OWASP LLM Top 10), enumeración de superficies de ataque de IA, explotación |
| **Impacto** | Evaluación final del AI Security Path: analizar una aplicación habilitada con IA, identificar sus superficies de ataque, aplicar threat modelling de IA, enumerar componentes relacionados y explotar debilidades para recuperar las flags. |
---
**Contexto:** Esta evaluación combina conceptos de módulos anteriores que cubren fundamentos de IA y Machine Learning, superficies de ataque de IA, threat modelling de IA, vulnerabilidades de IA del mundo real y metodologías de evaluación de seguridad. El objetivo es aplicar conocimiento de seguridad de IA tanto ofensivo como defensivo para identificar vulnerabilidades y recuperar flags de la aplicación objetivo. Es la culminación práctica de las rooms de teoría anteriores (AI Models & Data, Prompt Engineering, AI Threat Modelling, AI System Reconnaissance) y prepara el terreno para las rooms de explotación (UnIndexed, Payload, Checkpoint, Lockdown, LLMborghini, ContAInment).
*EN: This assessment combines concepts from previous modules (AI/ML fundamentals, AI attack surfaces, AI threat modelling, real-world AI vulnerabilities and security assessment methodologies). The goal is to apply both offensive and defensive AI security knowledge to identify vulnerabilities and retrieve flags from the target application.*
## Solucionario
### Task 1 — Evaluación / Assessment
**Explicación:** Evaluación final. Objetivos: analizar la aplicación habilitada con IA, identificar funcionalidad expuesta y superficies de ataque, aplicar conceptos de threat modelling de IA, enumerar componentes y comportamientos relacionados con IA y explotar debilidades para recuperar flags. La primera flag se obtiene en una fase temprana del ejercicio y la segunda al completar la explotación final.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the first flag? | `THM{threat_m0d3l_re4d1_}` |
| 2 | What's the second flag? | `THM{AI_thr3at_m0dell3d}` |
---
**Metodología:** Análisis de la aplicación IA → identificación de superficies de ataque → threat modelling de IA (STRIDE-AI / ATLAS / OWASP LLM) → enumeración de componentes IA → explotación de debilidades → flags.
**Learning chain:** aplicar threat modelling a una app real → enumerar componentes IA y superficie de ataque → explotar vulnerabilidades específicas de IA → recuperar flags.
**MITRE ATT&CK / ATLAS:** T1190 (Exploit Public-Facing Application), AML.T0051 (LLM Prompt Injection), AML.T0024 (Model Extraction), AML.T0010 (ML Supply Chain Compromise), T1083 (File and Directory Discovery).
**Fuente:** [TryHackMe - AI Threat Modelling Assessment](https://tryhackme.com/room/ai-threat-modelling-assessment)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
