# The CIA Triad [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `theciatriad`
* **Link:** https://tryhackme.com/room/theciatriad
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + ejercicio estático interactivo (secret-message/permisos) del propio room
* **Componentes:** Tríada CIA (Confidencialidad, Integridad, Disponibilidad) · Security Mindset · ejercicio estático "CIA_IS_ABOUT_BALANCE"
* **Impacto rol:** No explota ningún servicio real; es teoría de fundamentos de seguridad (Pre Security). Lección clave: la tríada no es una lista de definiciones, es una **mentalidad** para tomar decisiones de seguridad.

## Solucionario de Tareas / Task Solutions

> **ES:** La tríada CIA es el modelo de seguridad de la información que estructura prácticamente toda la ciberseguridad técnica y de proceso. **Confidencialidad** (nadie no autorizado lee los datos), **Integridad** (los datos no se modifican sin autorización y siguen siendo fiables) y **Disponibilidad** (los datos/servicios están accesibles cuando se necesitan). Entender qué pilar se ve afectado por cada incidente te permite priorizar mitigaciones. El ejercicio del room demuestra que algunos datos son más importantes en un pilar que en otro: revelar una contraseña daña la *confidencialidad*, pero la decisión "equilibrada" (¿qué es más importante proteger aquí?) requiere analizar el contexto y aceptar que **CIA se trata de balance**.
> **EN:** The CIA triad is the information-security model behind almost all technical and process security. **Confidentiality** (unauthorised parties can't read data), **Integrity** (data isn't altered without authorisation and remains trustworthy) and **Availability** (data/services are accessible when needed). Understanding which pillar an incident hits lets you prioritise mitigations. The room's exercise shows some data matters more for one pillar than another: leaking a password damages *confidentiality*, but the "balanced" decision (what matters most here?) requires context — the **CIA triad is about balance**.

### Task 1 — Introducción / Introduction

* **Check:** `I am ready to start!`
* **ES:** Apto para empezar desde cero; parte de la ruta *Pre Security*.
* **EN:** Beginner-friendly; part of the *Pre Security* path.

### Task 2 — Entendiendo la Tríada CIA / Understanding the CIA Triad

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which pillar of the CIA focuses on preventing **unauthorized modification** of data? | `Integrity` |
| Which pillar of the CIA focuses on preventing **unauthorized access** to data? | `Confidentiality` |
| Which CIA pillar ensures data is **available** to users when needed? | `Availability` |
| Which CIA pillar gets impacted if the data becomes **untrustworthy**? | `Integrity` |
| What is the term used **collectively** for all these pillars? | `CIA Triad` |

* **Confidencialidad / Confidentiality:** solo quien debe puede leer los datos (cifrado, controles de acceso, mínimo privilegio).
* **Integridad / Integrity:** los datos no cambian sin autorización; si un dato deja de ser fiable (modificado, corrupto, no verificable) quien sufre es la integridad.
* **Disponibilidad / Availability:** acceso en el momento en que se necesita (redundancia, backups, mitigación de DDoS).
* **Truco / Trick:** "se previene la modificación" → Integrity; "se previene el acceso" → Confidentiality; "cuando se necesite" → Availability.

### Task 3 — La Mentalidad de Seguridad / The Security Mindset

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag received after solving the exercise? | `THM{CIA_IS_ABOUT_BALANCE}` |
| CIA Triad is not just a set of definitions; it's a mindset. What type of mindset is it? | `Security mindset` |

* **Ejercicio estático / Static exercise:** el room carga un pequeño simulador (laboratorio estático, sin máquina) con escenarios donde debes elegir qué pilar priorizar; al resolverlo entrega `THM{CIA_IS_ABOUT_BALANCE}`.
* **Idea / Takeaway:** no memorizar las tres letras; usarlas como **mentalidad de seguridad**: ante cada decisión (acceso, cifrado, copia de seguridad, parche) preguntarte qué pilar proteges y qué sacrificas.

### Task 4 — Conclusión / Conclusion

* **Check:** `Complete this room.`
* **ES:** Cierra el fundamento; la tríada es la base de control de acceso, cifrado, backups y, en general, de toda arquitectura de seguridad.
* **EN:** Closes the foundation; the triad underpins access control, encryption, backups and security architecture in general.

## Metodología / Methodology

1. **Paso / Step:** Leer las definiciones de los tres pilares y asociar cada "síntoma" con su pilar (modificación→Integrity, acceso→Confidentiality, disponibilidad→Availability).
2. **Paso / Step:** Resolver el ejercicio estático del room modificando el escenario hasta satisfacer el objetivo → flag `THM{CIA_IS_ABOUT_BALANCE}`.
3. **Paso / Step:** Interiorizar la conclusión: *balance* entre pilares según el contexto (mentalidad), no purismos.

### Cadena de aprendizaje / Learning Chain

```
Tríada CIA (CIA Triad)
  -> Confidencialidad (Integrity: THM basa su defensa en los 3 pilares)
  -> mentalidad de seguridad (Security mindset)
  -> ejercicio interactivo -> THM{CIA_IS_ABOUT_BALANCE}
```

**Mapeo MITRE ATT&CK / relacionado:** los pilares se corresponden con las categorías de impacto: T1485 (Data Destruction, golpea disponibilidad/integridad) · T1489 (service stop, disponibilidad) · T1498/1499 (HA-availability attacks) · T1565 (Data Manipulation, integridad) · T1630 (exfiltration no técnico). El room en sí es teórico.

**Lección:** *CIA no es una lista; es una forma de pensar.* El mejor sistema no protege solo un pilar: equilibra los tres según el activo, el riesgo y el contexto de negocio.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.