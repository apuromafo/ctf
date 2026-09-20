# Threat Hunting Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `threathuntingintroduction` | [TryHackMe - Threat Hunting Introduction](https://tryhackme.com/room/threathuntingintroduction) | Threat Hunting | THM | IOC, Behavioral analysis, Hypothesis-driven, TTP, Static-site APT-Serpent | Threat hunting fundamentals |

---

**Contexto:** Introducción al Threat Hunting: definiciones, enfoques (intelligence-driven, indicator-driven), objetivos, técnicas (IOC-based, behavioral pattern analysis) y laboratorio práctico con el grupo APT-Serpent.

> **ES:** La sala introduce el threat hunting, sus enfoques (intelligence-driven, indicator-driven), objetivos, técnicas y un laboratorio práctico con el grupo APT-Serpent.
> **EN:** The room introduces threat hunting, its approaches (intelligence-driven, indicator-driven), objectives, techniques, and a practical lab with the APT-Serpent group.

## Solucionario

### Task 1: What Is Threat Hunting

**Explicación:** Definición de threat hunting: búsqueda proactiva de amenazas, basada en hipótesis, para detectar actividad maliciosa que evade defenses automáticas.

| Pregunta | Respuesta | Explicación ES |
|----------|-----------|----------------|
| Tiempo promedio que un atacante permanece indetectado | Dwell time | El dwell time promedio ronda los 200-300 días según informes de la industria |
| ¿El threat hunting es reactivo o proactivo? | Proactive | A diferencia del response reactivo, el hunting busca amenazas activamente antes de que generuen alertas |

### Task 2: Hunting Approaches

**Explicación:** Diferentes enfoques de hunting según la información disponible: orientado a inteligencia o a indicadores.

| Pregunta | Respuesta |
|----------|-----------|
| Enfoque cuando se recibe inteligencia sobre un APT que apunta a tu industria | Intelligence-Driven Hunting |
| Enfoque más eficiente con lista de hashes/IOCs de un feed de amenazas | Indicator-driven Hunting |

### Task 3: Hunting Targets

**Explicación:** Los objetivos del hunting incluyen lo que los atacantes dejan atrás, como residuos de ataques.

| Pregunta | Respuesta |
|----------|-----------|
| Categoría que representa artefactos dejados por atacantes | Attack Residues |

### Task 4: Hunting Techniques

**Explicación:** Técnicas de hunting: búsqueda por indicadores de compromiso y análisis de patrones de comportamiento.

| Pregunta | Respuesta |
|----------|-----------|
| Técnica que usa hashes, IPs, dominios para buscar artefactos específicos | Indicators of Compromise |
| Técnica representada por "Word.exe genera cmd.exe genera powershell.exe que conecta a IP externa" | Behavioral Pattern Analysis |

### Task 5: Practical (Static-site APT-Serpent)

**Explicación:** Laboratorio práctico consistente en una web estática sobre el grupo APT-Serpent: campañas, herramientas, vectores de acceso y técnica de C2.

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántas campañas conocidas ha llevado a cabo APT-Serpent desde 2021? | 4 |
| ¿En qué fase se deposita CustomBackdoor? | Execution & Persistence |
| ¿Cuál es el vector de acceso inicial principal de APT-Serpent? | Spear-phishing |
| ¿Cuál es el intervalo de los beacons C2 HTTPS de CustomBackdoor (segundos)? | 300 |
| Flag tras elegir el enfoque y objetivo correctos | THM-APT-SERPENT-INTEL |

### Tabla unificada de preguntas / Unified Q&A

| # | Pregunta / Question | Respuesta / Answer |
|---|---|---|
| 1 | Tiempo promedio que un atacante permanece indetectado | `Dwell time` |
| 2 | ¿El threat hunting es reactivo o proactivo? | `Proactive` |
| 3 | Enfoque cuando se recibe inteligencia sobre un APT que apunta a tu industria | `Intelligence-Driven Hunting` |
| 4 | Enfoque más eficiente con lista de hashes/IOCs de un feed de amenazas | `Indicator-driven Hunting` |
| 5 | Categoría que representa artefactos dejados por atacantes | `Attack Residues` |
| 6 | Técnica que usa hashes, IPs, dominios para buscar artefactos específicos | `Indicators of Compromise` |
| 7 | Técnica representada por "Word.exe genera cmd.exe genera powershell.exe que conecta a IP externa" | `Behavioral Pattern Analysis` |
| 8 | ¿Cuántas campañas conocidas ha llevado a cabo APT-Serpent desde 2021? | `4` |
| 9 | ¿En qué fase se deposita CustomBackdoor? | `Execution & Persistence` |
| 10 | ¿Cuál es el vector de acceso inicial principal de APT-Serpent? | `Spear-phishing` |
| 11 | ¿Cuál es el intervalo de los beacons C2 HTTPS de CustomBackdoor (segundos)? | `300` |
| 12 | Flag tras elegir el enfoque y objetivo correctos | `THM-APT-SERPENT-INTEL` |

---

**Metodología:** Se estudiaron los conceptos y enfoques del threat hunting (intelligence-driven e indicator-driven), las técnicas IOC-based y de behavioral pattern analysis, y se completó el laboratorio práctico sobre el grupo APT-Serpent revisando la web estática para identificar campañas, fases de depósito del backdoor, vector de acceso, intervalo de beacon y la flag final.

### Cadena de ataque / Attack Chain

1. Revisión de conceptos: dwell time y naturaleza proactiva del hunting.
2. Elección de enfoque: intelligence-driven frente a indicator-driven.
3. Identificación del objetivo de búsqueda (attack residues).
4. Aplicación de técnicas: IOC-based y behavioral pattern analysis.
5. Laboratorio APT-Serpent: recopilación de inteligencia y obtención de la flag.

**Learning chain:** Threat hunting concepts → hunting approaches → hunting targets → hunting techniques → APT-Serpent practical

**Lección:** *El threat hunting es un proceso proactivo que combina hipótesis e inteligencia con técnicas IOC-based y de patrones de comportamiento para detectar amenazas que las defensas automáticas no ven.*

**MITRE ATT&CK:** T1071.001 - Application Layer Protocol: Web Protocols, T1059.003 - Command and Scripting Interpreter: Windows Command Shell, T1566.001 - Phishing: Spearphishing Attachment

**Fuente:** [TryHackMe - Threat Hunting Introduction](https://tryhackme.com/room/threathuntingintroduction)

> **Fuente original / Original source:** https://simontaplin.net/2026/07/03/answers-for-the-tryhackme-threat-hunting-introduction-room/ | https://classroom.anir0y.in/post/thm-room-threat-hunting-introduction/

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.