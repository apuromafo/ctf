# SOAR [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `soar`
* **Link:** https://tryhackme.com/room/soar
* **Sección / Section:** SOC / SOAR
* **Fuente / Source:** (thmrevenant)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala enfocada en la automatización de operaciones de seguridad: explica la evolución de los SOC, el problema de la fatiga de alertas y los conceptos fundamentales de SOAR (Security Orchestration, Automation and Response) como la orquestación, los playbooks y la automatización, cerrando con un ejercicio práctico con flag.
> **EN:** Room focused on security operations automation: it explains the evolution of SOCs, the alert fatigue problem and the fundamental SOAR (Security Orchestration, Automation and Response) concepts such as orchestration, playbooks and automation, ending with a practical flag challenge.

---

### Task 1 — Evolución del SOC y Fatiga de Alertas / SOC Evolution and Alert Fatigue

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Under which SOC generation did SIEM tools emerge? | `Second` |
| How would you describe the experience of having an overload of security events being triggered within a SOC? | `Alert Fatigue` |

---

### Task 2 — Orquestación y Playbooks / Orchestration and Playbooks

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| The act of connecting and integrating security tools and systems into seamless workflows is known as? | `Security Orchestration` |
| What do we call a predefined list of actions to handle an incident? | `Playbook` |

---

### Task 3 — Trabajo Manual y Flag Final / Manual Work and Final Flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Are manual analyses vital within a SOAR workflow? yay or nay? | `yay` |
| What is the flag received? | `THM{AUT0M@T1N6_S3CUR1T¥}` |

---

## Metodología / Methodology

1. **Paso / Step:** Revisión de la evolución de los SOC: la segunda generación fue la que introdujo los SIEM para centralizar la correlación de eventos. / Review of SOC evolution: the second generation was the one that introduced SIEMs to centralize event correlation.
2. **Paso / Step:** Comprender el problema operativo que SOAR resuelve: el exceso de eventos genera "alert fatigue", por lo que se necesita orquestación para integrar herramientas y playbooks para estandarizar la respuesta. / Understand the operational problem SOAR solves: an excess of events generates "alert fatigue", so orchestration is needed to integrate tools and playbooks to standardize response.
3. **Paso / Step:** Aplicar los conceptos y confirmar que el análisis manual sigue siendo vital dentro del flujo SOAR, obteniendo la flag de la sala. / Apply the concepts and confirm that manual analysis remains vital within the SOAR workflow, obtaining the room flag.

### Cadena de ataque / Attack Chain

```
SOC 1G (manual) -> SOC 2G (SIEM) -> alert fatigue -> SOAR 3G/4G:
Orchestration + Automation + Response (Playbooks)
-> Análisis manual sigue siendo vital (juicio humano)
-> Flag: THM{AUT0M@T1N6_S3CUR1T¥}
```

**Lección:** La tecnología automatiza procesos repetitivos, pero el análisis manual y el criterio humano siguen siendo vitales en un flujo SOAR; la fatiga de alertas es el problema central que SOAR busca mitigar.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.