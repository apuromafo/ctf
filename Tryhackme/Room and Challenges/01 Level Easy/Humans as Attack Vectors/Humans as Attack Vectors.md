# Humans as Attack Vectors

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `humansasattackvectors` | https://tryhackme.com/room/humansasattackvectors | 01 Level Easy | TryHackMe | Factor humano / ingeniería social / suplantación / concienciación en seguridad | Comprender cómo el factor humano es un vector de ataque y cómo mitigarlo con formación. |

---

**Contexto:** Sala centrada en el factor humano como vector de ataque: las personas y su acceso a los sistemas son el eslabón más débil. Se estudian la ingeniería social, la suplantación (impersonation), las mitigaciones y la concienciación en seguridad, con una parte práctica que entrega flags.

> **ES:** Aprende por qué las personas son el mayor vector de ataque, las técnicas de ingeniería social y suplantación, y las formas de mitigarlo con concienciación.
> **EN:** Learn why humans are the biggest attack vector, the social engineering and impersonation techniques, and how security awareness mitigates them.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala sobre el factor humano como vector de ataque; tarea de lectura sin respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: El factor humano / Humans

**Explicación:** Los humanos son el mayor vector de ataque: los atacantes buscan obtener acceso a los sistemas a través de las personas.

1. 1. Humans
   2. Access

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el mayor vector de ataque? / What is the biggest attack vector? | `Humans` |
| 2 | ¿Qué es lo que los atacantes buscan obtener a través de las personas? / What do attackers seek through humans? | `Access` |

### Task 3: Técnicas de ataque / Attack Techniques

**Explicación:** La ingeniería social manipula a las personas para que realicen acciones, y la suplantación consiste en hacerse pasar por otra persona o entidad.

1. 1. Social Engineering
   2. Impersonation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué técnica manipula a las personas para que actúen? / What technique manipulates people into acting? | `Social Engineering` |
| 2 | ¿Cómo se llama cuando el atacante se hace pasar por otra persona? / What is it called when an attacker pretends to be someone else? | `Impersonation` |

### Task 4: Mitigación / Mitigation

**Explicación:** La mitigación del riesgo del factor humano pasa por aplicar controles y, sobre todo, por la concienciación y la formación en seguridad.

1. 1. Mitigation
   2. Security Awareness Training

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué se aplica para reducir el riesgo sobre el factor humano? / What is applied to reduce human risk? | `Mitigation` |
| 2 | ¿Qué formación se recomienda en las organizaciones? / What training is recommended in organisations? | `Security Awareness Training` |

### Task 5: Práctica / Practice

**Explicación:** En la parte práctica se responde a las preguntas de la plataforma y se obtienen las flags del reto.

1. 1. THM{anyone_else_at_risk?}
   2. THM{human_protection_expert!}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{anyone_else_at_risk?}` |
| 2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{human_protection_expert!}` |

### Task 6: Cierre / Wrap-up

**Explicación:** Resumen final de la sala; no requiere respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el resumen final. | `No answer needed` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | 1 | ¿Cuál es el mayor vector de ataque? / What is the biggest attack vector? | `Humans` |
| 2 | 2 | ¿Qué es lo que los atacantes buscan obtener a través de las personas? / What do attackers seek through humans? | `Access` |
| 3 | 1 | ¿Qué técnica manipula a las personas para que actúen? / What technique manipulates people into acting? | `Social Engineering` |
| 3 | 2 | ¿Cómo se llama cuando el atacante se hace pasar por otra persona? / What is it called when an attacker pretends to be someone else? | `Impersonation` |
| 4 | 1 | ¿Qué se aplica para reducir el riesgo sobre el factor humano? / What is applied to reduce human risk? | `Mitigation` |
| 4 | 2 | ¿Qué formación se recomienda en las organizaciones? / What training is recommended in organisations? | `Security Awareness Training` |
| 5 | 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{anyone_else_at_risk?}` |
| 5 | 2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{human_protection_expert!}` |
| 6 | 1 | Revisa el resumen final. | `No answer needed` |

---

**Metodología:** Lectura del material sobre el factor humano, identificación del acceso como objetivo, estudio de la ingeniería social y la suplantación, aplicación de mitigaciones y concienciación, y resolución de la práctica para obtener las flags.

### Cadena de ataque / Attack Chain

```text
leer material -> identificar el factor humano -> ingeniería social -> suplantación -> mitigación/concienciación -> flags
```

**Learning chain:** Factor Humano -> Social Engineering -> Impersonation -> Mitigation -> Security Awareness -> flags.

**Lección:** *Las personas son el eslabón más débil de la cadena de seguridad; la concienciación y la formación reducen el éxito de la ingeniería social y de la suplantación, protegiendo el acceso a los sistemas.*

**MITRE ATT&CK:** T1598 (Phishing for Information), T1656 (Impersonation)

**Fuente:** [TryHackMe - Humans as Attack Vectors](https://tryhackme.com/room/humansasattackvectors)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
