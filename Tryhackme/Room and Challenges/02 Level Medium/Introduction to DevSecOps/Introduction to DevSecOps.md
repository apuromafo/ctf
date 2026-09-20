# Introduction to DevSecOps

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `introductiontodevsecops` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introductiontodevsecops) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | DevSecOps / CI/CD / IaC / Shift Left / Metodologías (Waterfall, Agile, DevOps) / Cultura de equipo | **Impacto** | Explica la evolución de Waterfall → Agile → DevOps → DevSecOps, el porqué de la seguridad integrada y los tres pilares culturales para romper los silos de seguridad |

---

**Contexto:** Sala que explica qué es DevSecOps y por qué surge: la seguridad como parte integral del ciclo de vida del software y no como una fase final. Compare las metodologías Waterfall, Agile y DevOps, introduce los conceptos de CI/CD, Monitoring e IaC, promueve la estrategia "shift left", identifica los fallos del modelo tradicional (Security Silos, Lack of visibility, Stringent Processes) y define los tres pilares culturales necesarios (autonomía de equipos, visibilidad/transparencia y comprensión/empatía). Cierra con un reto de identificación de modelos y una flag `THM{ONE_TWO_THREE}`.

## Solucionario

### Task 1: Introducción a DevSecOps

**Explicación:** Conceptos de la sala: la necesidad de integrar seguridad en todo el ciclo de desarrollo. No se requiere respuesta:

1. No answer needed

### Task 2: Metodologías de Desarrollo

**Explicación:** Las metodologías y el factor cultural clave mencionados en la sala:

2. 1. agile
   2. DevOps
   3. waterfall
   4. building trust

### Task 3: Prácticas de DevOps / DevSecOps

**Explicación:** Las tres prácticas nucleares del movimiento DevOps:

3. 1. CI/CD
   2. Monitoring
   3. IaC

### Task 4: Security Shift Left

**Explicación:** La estrategia y la disciplina resultante cuando la seguridad se desplaza a las primeras etapas:

4. 1. shift left
   2. DevSecOps

### Task 5: Fallos del Modelo Tradicional de Seguridad

**Explicación:** Las debilidades del enfoque de seguridad tradicional que motivan el cambio:

5. 1. Security Silos
   2. Lack of visibility
   3. Stringent Processes

### Task 6: Los Tres Pilares de DevSecOps

**Explicación:** Los tres pilares culturales que habilitan una adopción exitosa:

6. 1. promote autonomy of teams
   2. Visibility and Transparency
   3. Understanding and Empathy

### Task 7: Reto de los Modelos

**Explicación:** Se identifican las etapas del desarrollo y se obtiene la flag:

7. 1. Waterfall
   2. Agile
   3. DevOps
   4. THM{ONE_TWO_THREE}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué metodología destaca por su desarrollo iterativo e incremental? | `agile` |
| 2 | ¿Qué práctica une a los equipos de desarrollo y operaciones? | `DevOps` |
| 3 | ¿Qué metodología clásica es secuencial y rígida? | `waterfall` |
| 4 | ¿Qué factor falta cuando los equipos no colaboran adecuadamente? | `building trust` |
| 5 | ¿Qué conjunto de prácticas automatiza la integración y el despliegue continuos? | `CI/CD` |
| 6 | ¿Qué práctica observa el rendimiento y los fallos en producción? | `Monitoring` |
| 7 | ¿Qué disciplina trata la infraestructura como código? | `IaC` |
| 8 | ¿Qué estrategia adelanta la seguridad al inicio del ciclo de vida? | `shift left` |
| 9 | ¿Cómo se llama la práctica de integrar la seguridad en el ciclo DevOps? | `DevSecOps` |
| 10 | Fallo 1 del modelo tradicional | `Security Silos` |
| 11 | Fallo 2 del modelo tradicional | `Lack of visibility` |
| 12 | Fallo 3 del modelo tradicional | `Stringent Processes` |
| 13 | Pilar 1 de DevSecOps | `promote autonomy of teams` |
| 14 | Pilar 2 de DevSecOps | `Visibility and Transparency` |
| 15 | Pilar 3 de DevSecOps | `Understanding and Empathy` |
| 16 | Primera etapa del reto de modelos | `Waterfall` |
| 17 | Segunda etapa del reto de modelos | `Agile` |
| 18 | Tercera etapa del reto de modelos | `DevOps` |
| 19 | Flag del reto | `THM{ONE_TWO_THREE}` |

---

**Metodología:**
1. Comparar Waterfall, Agile y DevOps.
2. Introducir CI/CD, Monitoring e IaC como prácticas nucleares.
3. Aplicar la estrategia shift left y definir DevSecOps.
4. Diagnosticar los fallos del modelo tradicional de seguridad.
5. Adoptar los tres pilares culturales de DevSecOps.
6. Resolver el reto de identificación de modelos y obtener la flag.

**Learning chain:** Waterfall → Agile → DevOps → CI/CD → Monitoring → IaC → shift left → DevSecOps → Security Silos → Lack of visibility → Stringent Processes → autonomía → visibilidad → empatía → reto → `THM{ONE_TWO_THREE}`

**Lección:** *La seguridad no puede ser una fase final ni un silo: solo cuando se desplaza a la izquierda (shift left) y se apoya en una cultura de confianza, visibilidad y empatía, el pipeline DevSecOps produce software seguro a la velocidad del negocio.*

**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter (ejecución en pipelines CI/CD); T1078 - Valid Accounts (gestión de accesos en CI/CD); T1505.002 - Server Software Component: Web Shell (postura defensiva IaC); la sala es de cultura/proceso DevSecOps más que de TTPs ofensivos

**Fuente:** [TryHackMe - Introduction to DevSecOps](https://tryhackme.com/room/introductiontodevsecops)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.