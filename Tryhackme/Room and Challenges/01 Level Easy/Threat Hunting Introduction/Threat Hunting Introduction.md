# Threat Hunting Introduction

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `threathuntingintroduction` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/threathuntingintroduction) |
| **Sección** | Threat Hunting |
| **Fuente** | THM |
| **Componentes** | IOC, Behavioral analysis, Hypothesis-driven, TTP, Static-site APT-Serpent |
| **Impacto** | Threat hunting fundamentals |

---

**Contexto:** Introducción al Threat Hunting: definiciones, enfoques (intelligence-driven, indicator-driven), objetivos, técnicas (IOC-based, behavioral pattern analysis) y laboratorio práctico con el grupo APT-Serpent.

## Solucionario

### T2 - What Is Threat Hunting

| Pregunta | Respuesta | Explicación ES |
|----------|-----------|----------------|
| Tiempo promedio que un atacante permanece indetectado | Dwell time | El dwell time promedio ronda los 200-300 días según informes de la industria |
| ¿El threat hunting es reactivo o proactivo? | Proactive | A diferencia del response reactivo, el hunting busca amenazas activamente antes de que generuen alertas |

### T3 - Hunting Approaches

| Pregunta | Respuesta |
|----------|-----------|
| Enfoque cuando se recibe inteligencia sobre un APT que apunta a tu industria | Intelligence-Driven Hunting |
| Enfoque más eficiente con lista de hashes/IOCs de un feed de amenazas | Indicator-driven Hunting |

### T4 - Hunting Targets

| Pregunta | Respuesta |
|----------|-----------|
| Categoría que representa artefactos dejados por atacantes | Attack Residues |

### T5 - Hunting Techniques

| Pregunta | Respuesta |
|----------|-----------|
| Técnica que usa hashes, IPs, dominios para buscar artefactos específicos | Indicators of Compromise |
| Técnica representada por "Word.exe genera cmd.exe genera powershell.exe que conecta a IP externa" | Behavioral Pattern Analysis |

### T6 - Practical (Static-site APT-Serpent)

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántas campañas conocidas ha llevado a cabo APT-Serpent desde 2021? | 4 |
| ¿En qué fase se deposita CustomBackdoor? | Execution & Persistence |
| ¿Cuál es el vector de acceso inicial principal de APT-Serpent? | Spear-phishing |
| ¿Cuál es el intervalo de los beacons C2 HTTPS de CustomBackdoor (segundos)? | 300 |
| Flag tras elegir el enfoque y objetivo correctos | THM-APT-SERPENT-INTEL |

---

**Fuentes:** https://simontaplin.net/2026/07/03/answers-for-the-tryhackme-threat-hunting-introduction-room/ | https://classroom.anir0y.in/post/thm-room-threat-hunting-introduction/
