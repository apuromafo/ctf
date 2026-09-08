# SOAR

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `soar` |
| **Link** | [TryHackMe](https://tryhackme.com/room/soar) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | SOAR / SOC evolution / alert fatigue / orchestration / playbooks / automation |
| **Impacto** | Entender cómo SOAR automatiza operaciones de seguridad y por qué el análisis manual sigue siendo vital |

---

**Contexto:** Sala enfocada en la automatización de operaciones de seguridad: explica la evolución de los SOC, el problema de la fatiga de alertas y los conceptos fundamentales de SOAR (Security Orchestration, Automation and Response) — orquestación, playbooks y automatización — cerrando con un ejercicio práctico con flag.

## Solucionario

### Task 1: Evolución del SOC y Fatiga de Alertas / SOC Evolution and Alert Fatigue

**Explicación:**

Los **SIEM** surgieron en la **segunda** generación de SOC. La sobrecarga de eventos de seguridad disparados dentro de un SOC se describe como **Alert Fatigue** (fatiga de alertas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Under which SOC generation did SIEM tools emerge? | `Second` |
| 2 | How would you describe the experience of having an overload of security events being triggered within a SOC? | `Alert Fatigue` |

### Task 2: Orquestación y Playbooks / Orchestration and Playbooks

**Explicación:**

Conectar e integrar herramientas y sistemas de seguridad en flujos de trabajo sin fisuras se conoce como **Security Orchestration**. Una lista predefinida de acciones para manejar un incidente es un **Playbook**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The act of connecting and integrating security tools and systems into seamless workflows is known as? | `Security Orchestration` |
| 2 | What do we call a predefined list of actions to handle an incident? | `Playbook` |

### Task 3: Trabajo Manual y Flag Final / Manual Work and Final Flag

**Explicación:**

Los análisis manuales siguen siendo **vitales** dentro de un flujo SOAR (respuesta: `yay`). La flag de la sala es `THM{AUT0M@T1N6_S3CUR1T¥}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are manual analyses vital within a SOAR workflow? yay or nay? | `yay` |
| 2 | What is the flag received? | `THM{AUT0M@T1N6_S3CUR1T¥}` |

---

**Metodología:**

1. Revisión de la evolución de los SOC: la segunda generación fue la que introdujo los SIEM para centralizar la correlación de eventos.
2. Comprender el problema operativo que SOAR resuelve: el exceso de eventos genera "alert fatigue", por lo que se necesita orquestación para integrar herramientas y playbooks para estandarizar la respuesta.
3. Aplicar los conceptos y confirmar que el análisis manual sigue siendo vital dentro del flujo SOAR, obteniendo la flag de la sala.

**Learning chain:** SOC 1G (manual) -> SOC 2G (SIEM) -> alert fatigue -> SOAR 3G/4G: Orchestration + Automation + Response (Playbooks) -> análisis manual sigue siendo vital -> flag

**Lección:** *La tecnología automatiza procesos repetitivos, pero el análisis manual y el criterio humano siguen siendo vitales en un flujo SOAR; la fatiga de alertas es el problema central que SOAR busca mitigar.*

**MITRE ATT&CK:** T1005 (Data from Local System) · T1485 (Data Destruction) · CWE-201 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - SOAR](https://tryhackme.com/room/soar)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
