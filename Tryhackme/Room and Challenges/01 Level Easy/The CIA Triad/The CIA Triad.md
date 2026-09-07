# The CIA Triad

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `theciatriad` |
| **Link** | [TryHackMe](https://tryhackme.com/room/theciatriad) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + ejercicio estático interactivo (secret-message/permisos) del propio room |
| **Componentes** | Tríada CIA (Confidencialidad, Integridad, Disponibilidad) / Security Mindset / ejercicio estático "CIA_IS_ABOUT_BALANCE" |
| **Impacto** | Teoría de fundamentos de seguridad (Pre Security): la tríada no es una lista de definiciones, es una mentalidad para tomar decisiones |

---

**Contexto:** La tríada CIA es el modelo de seguridad de la información que estructura prácticamente toda la ciberseguridad técnica y de proceso. **Confidencialidad** (nadie no autorizado lee los datos), **Integridad** (los datos no se modifican sin autorización y siguen siendo fiables) y **Disponibilidad** (los datos/servicios están accesibles cuando se necesitan). Entender qué pilar se ve afectado por cada incidente te permite priorizar mitigaciones. El ejercicio del room demuestra que algunos datos son más importantes en un pilar que en otro: revelar una contraseña daña la *confidencialidad*, pero la decisión "equilibrada" (¿qué es más importante proteger aquí?) requiere analizar el contexto y aceptar que **CIA se trata de balance**.

## Solucionario

### Task 1: Introducción / Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to start! | `No answer needed` |

### Task 2: Entendiendo la Tríada CIA / Understanding the CIA Triad

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which pillar of the CIA focuses on preventing **unauthorized modification** of data? | `Integrity` |
| 2 | Which pillar of the CIA focuses on preventing **unauthorized access** to data? | `Confidentiality` |
| 3 | Which CIA pillar ensures data is **available** to users when needed? | `Availability` |
| 4 | Which CIA pillar gets impacted if the data becomes **untrustworthy**? | `Integrity` |
| 5 | What is the term used **collectively** for all these pillars? | `CIA Triad` |

### Task 3: La Mentalidad de Seguridad / The Security Mindset

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag received after solving the exercise? | `THM{CIA_IS_ABOUT_BALANCE}` |
| 2 | CIA Triad is not just a set of definitions; it's a mindset. What type of mindset is it? | `Security mindset` |

### Task 4: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete this room. | `No answer needed` |

---

**Metodología:**
1. **Pilares:** **Confidencialidad** = solo quien debe puede leer los datos (cifrado, controles de acceso, mínimo privilegio); **Integridad** = los datos no cambian sin autorización y, si un dato deja de ser fiable (modificado, corrupto, no verificable), quien sufre es la integridad; **Disponibilidad** = acceso en el momento en que se necesita (redundancia, backups, mitigación de DDoS). Truco: "se previene la modificación" → Integrity; "se previene el acceso" → Confidentiality; "cuando se necesite" → Availability.
2. **Ejercicio estático:** el room carga un pequeño simulador (laboratorio estático, sin máquina) con escenarios donde debes elegir qué pilar priorizar; al resolverlo entrega `THM{CIA_IS_ABOUT_BALANCE}`.
3. **Mentalidad de seguridad:** el takeaway no es memorizar las tres letras, sino usarlas como **Security mindset**: ante cada decisión (acceso, cifrado, copia de seguridad, parche) preguntarte qué pilar proteges y qué sacrificas, equilibrando según el activo, el riesgo y el contexto de negocio.

**Learning chain:** Tríada CIA (CIA Triad) → Confidencialidad / Integridad / Disponibilidad → mentalidad de seguridad (Security mindset) → ejercicio interactivo → THM{CIA_IS_ABOUT_BALANCE}

**MITRE ATT&CK:** T1485 (Data Destruction), T1489 (Service Stop), T1565 (Data Manipulation), T1498 (Network Denial of Service)

**Fuente:** [TryHackMe - The CIA Triad](https://tryhackme.com/room/theciatriad)