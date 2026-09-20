# DevSecOps Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `devsecopsbasics` | https://tryhackme.com/room/devsecopsbasics | DevSecOps | TryHackMe | Agile, Waterfall, DevOps, CI/CD, IaC, Shift Left, Security Silos | DevSecOps fundamentals |

---

**Contexto:** Introducción a DevSecOps: metodologías de desarrollo (Waterfall, Agile, DevOps), el bucle infinito CI/CD, Shift Left, desafíos de DevSecOps y cultura organizacional. Incluye ejercicio interactivo con cómics.

> **ES:** Introducción a DevSecOps: metodologías (Waterfall, Agile, DevOps), CI/CD, IaC, monitoreo, Shift Left, desafíos (Security Silos, Lack of Visibility, Stringent Processes) y cultura organizacional.
> **EN:** DevSecOps introduction: methodologies (Waterfall, Agile, DevOps), CI/CD, IaC, monitoring, Shift Left, challenges (Security Silos, Lack of Visibility, Stringent Processes) and organizational culture.

## Solucionario

### Task 2: DevOps: una nueva era / DevOps: A New Era

**Explicación:** Se comparan las metodologías de desarrollo. Agile se apoya en equipos auto-organizados y colaboración constructiva; DevOps impulsa el cambio cultural mediante automatización e integración; Waterfall es el enfoque tradicional que generó desconfianza entre equipos. DevOps enfatiza el `Building Trust`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Metodología con equipos auto-organizados y colaboración constructiva | `Agile` |
| 2 | Metodología basada en automatización e integración para impulsar cambio cultural | `DevOps` |
| 3 | Enfoque tradicional que generó desconfianza entre equipos | `Waterfall` |
| 4 | ¿Qué enfatiza DevOps? | `Building Trust` |

### Task 3: El bucle infinito / The Infinite Loop

**Explicación:** El bucle infinito de DevOps incluye herramientas para automatizar el ciclo: CI/CD agrega tests automáticamente y maneja la fusión frecuente de cambios pequeños; Monitoring recolecta datos para analizar rendimiento y estabilidad; IaC provisiona infraestructura con código reutilizable y consistente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ayuda a agregar tests automáticamente y maneja la fusión frecuente de cambios pequeños | `CI/CD` |
| 2 | Proceso enfocado en recolectar datos para analizar rendimiento y estabilidad | `Monitoring` |
| 3 | Forma de provisionar infraestructura con código reutilizable y consistente | `IaC` |

### Task 4: Desplazamiento a la izquierda / Shifting Left

**Explicación:** Shifting Left consiste en contabilizar la seguridad desde las etapas más tempranas del desarrollo. Cuando la seguridad se introduce de inicio a fin del ciclo de vida se habla de DevSecOps.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Término para contabilizar seguridad desde las etapas más tempranas | `Shift Left` |
| 2 | Enfoque de desarrollo donde seguridad se introduce de inicio a fin | `DevSecOps` |

### Task 5: DevSecOps: la seguridad se desplaza a la izquierda / DevSecOps: Security Shifts Left

**Explicación:** Trasladar la seguridad hacia la izquierda trae desafíos organizativos: los equipos en silos generan una cultura de `Security Silos`; no priorizar los riesgos correctos provoca `Lack of Visibility`; y los procesos de seguridad innecesariamente complicados derivan en `Stringent Processes`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desafío DevSecOps que lleva a cultura siloed | `Security Silos` |
| 2 | Desafío que afecta al no priorizar los riesgos correctos | `Lack of Visibility` |
| 3 | Desafío que surge de procesos de seguridad innecesariamente complicados | `Stringent Processes` |

### Task 6: Cultura DevSecOps / DevSecOps Culture

**Explicación:** La cultura DevSecOps se construye con prácticas que escalan: `Promote Autonomy of Teams` hace la seguridad escalable en startups y grandes corporaciones; `Visibility and Transparency` ayuda a los equipos a entender el riesgo; y `Understanding and Empathy` son factores clave para instilar seguridad con flexibilidad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo hacer la seguridad escalable en startups o corporaciones grandes? | `Promote Autonomy of Teams` |
| 2 | ¿Cómo apoyar a los equipos a entender el riesgo? | `Visibility and Transparency` |
| 3 | Factores clave para instilar seguridad con flexibilidad | `Understanding and Empathy` |

### Task 7: Ejercicio: Fuel Trouble (Static-site) / Exercise: Fuel Trouble (Static-site)

**Explicación:** En el ejercicio interactivo con cómics se identifican los modelos de desarrollo de cada equipo: el cómic 1 usa `Waterfall`, el cómic 2 `Agile` y el cómic 3 `DevOps`. Al completar el ejercicio se obtiene la flag `THM{ONE_TWO_THREE}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Modelo de desarrollo del equipo en Cómic 1 | `Waterfall` |
| 2 | Modelo del equipo en Cómic 2 | `Agile` |
| 3 | Modelo del equipo en Cómic 3 | `DevOps` |
| 4 | Flag | `THM{ONE_TWO_THREE}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Metodología con equipos auto-organizados y colaboración constructiva | `Agile` |
| 2 | Metodología basada en automatización e integración para impulsar cambio cultural | `DevOps` |
| 3 | Enfoque tradicional que generó desconfianza entre equipos | `Waterfall` |
| 4 | ¿Qué enfatiza DevOps? | `Building Trust` |
| 5 | Ayuda a agregar tests automáticamente y maneja la fusión frecuente de cambios pequeños | `CI/CD` |
| 6 | Proceso enfocado en recolectar datos para analizar rendimiento y estabilidad | `Monitoring` |
| 7 | Forma de provisionar infraestructura con código reutilizable y consistente | `IaC` |
| 8 | Término para contabilizar seguridad desde las etapas más tempranas | `Shift Left` |
| 9 | Enfoque de desarrollo donde seguridad se introduce de inicio a fin | `DevSecOps` |
| 10 | Desafío DevSecOps que lleva a cultura siloed | `Security Silos` |
| 11 | Desafío que afecta al no priorizar los riesgos correctos | `Lack of Visibility` |
| 12 | Desafío que surge de procesos de seguridad innecesariamente complicados | `Stringent Processes` |
| 13 | ¿Cómo hacer la seguridad escalable en startups o corporaciones grandes? | `Promote Autonomy of Teams` |
| 14 | ¿Cómo apoyar a los equipos a entender el riesgo? | `Visibility and Transparency` |
| 15 | Factores clave para instilar seguridad con flexibilidad | `Understanding and Empathy` |
| 16 | Modelo de desarrollo del equipo en Cómic 1 | `Waterfall` |
| 17 | Modelo del equipo en Cómic 2 | `Agile` |
| 18 | Modelo del equipo en Cómic 3 | `DevOps` |
| 19 | Flag | `THM{ONE_TWO_THREE}` |

---

**Metodología:** El room repasa primero las metodologías de desarrollo (Waterfall, Agile, DevOps) y sus diferencias culturales. Se recorre el bucle infinito de DevOps (CI/CD, Monitoring, IaC) y el concepto de Shift Left para integrar seguridad de manera temprana. Después se analizan los desafíos de DevSecOps (Security Silos, Lack of Visibility, Stringent Processes) y la cultura organizacional necesaria (autonomía, visibilidad, transparencia y empatía). El ejercicio interactivo con cómics consolida la identificación de cada modelo de desarrollo y desbloquea la flag.

### Cadena de ataque / Attack Chain

```text
Waterfall (tradicional, desconfianza) -> Agile (auto-organización) -> DevOps + CI/CD (automatización e integración) -> Shift Left (seguridad temprana) -> DevSecOps (seguridad de inicio a fin) -> superar desafíos (silos, visibilidad, procesos) -> cultura DevSecOps -> ejercicio Fuel Trouble (THM{ONE_TWO_THREE})
```

**Learning chain:** Waterfall → Agile → DevOps → CI/CD → IaC → Shift Left → DevSecOps → Security Silos/Lack of Visibility/Stringent Processes → Cultura DevSecOps.

**Lección:** *La seguridad no es una fase final sino parte del ciclo de desarrollo: aplicar Shift Left mediante DevSecOps requiere superar los silos organizativos y construir una cultura de autonomía, visibilidad y empatía.*

**MITRE ATT&CK:** No aplica directamente (room formativo de metodologías y cultura); se alinea conceptualmente con el Secure Development Lifecycle (SDLC).

**Fuente:** [TryHackMe - DevSecOps Basics](https://tryhackme.com/room/devsecopsbasics)

> **Fuente original / Original source:** https://simontaplin.net/2026/05/22/answers-for-the-tryhackme-devsecops-basics-room/
> **Fuente original / Original source:** https://sreeragpramod.hashnode.dev/devsecops-basic-tryhackme-walthrough

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.