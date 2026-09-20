# The Case: Seven Minutes on the Seine

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `thecasesevenminutesontheseine` | [TryHackMe](https://tryhackme.com/r/room/thecasesevenminutesontheseine) | CTF / Forensics | THM | VM, investigación detective | Investigación forense de un caso |

---

**Contexto:**

> **ES:** Desafío de investigación forense ambientado en París. El usuario asume el rol de detective investigando un robo en el Museo del Louvre en la ribera del Sena. Se analizan evidencias digitales para resolver el caso.
> **EN:** Forensic investigation challenge set in Paris. The user takes the role of a detective investigating a robbery at the Louvre Museum on the banks of the Seine. Digital evidence is analyzed to solve the case.

## Solucionario

### Task 1: Seine Incident

**Explicación:**

El primer paso del caso se centra en investigar el incidente ocurrido en el Sena y analizar las evidencias iniciales disponibles. Las respuestas del room se conservan de forma literal:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del flag? | `THM{n1c3_h31st_r3s34rch}` |

### Task 2: Louvre Protocol

**Explicación:**

En esta fase se examinan las grabaciones de CCTV y las auditorías del protocolo de seguridad del Museo del Louvre para avanzar en la investigación. Las respuestas del room se conservan de forma literal:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del flag? | `THM{cctv_4ud1ts_4r3_fun}` |

### Tabla Unificada de Preguntas y Respuestas

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 - Seine Incident | ¿Cuál es el valor del flag? | `THM{n1c3_h31st_r3s34rch}` |
| 2 | Task 2 - Louvre Protocol | ¿Cuál es el valor del flag? | `THM{cctv_4ud1ts_4r3_fun}` |

---

**Metodología:** 1) Seine Incident - investigar el incidente en el Sena, analizar evidencias iniciales; 2) Louvre Protocol - examinar CCTV y auditorías del protocolo de seguridad del Louvre.

### Cadena de ataque / Attack Chain

- Investigación de la escena del incidente en el Sena
- Recolección y análisis de evidencias digitales
- Correlación de grabaciones CCTV y auditorías
- Resolución del caso

**Learning chain:** Análisis de escena del crimen → Recolección de evidencias digitales → Correlación de CCTV → Resolución del caso

**Lección:** *La investigación forense es un proceso metódico: las pequeñas pistas digitales, como las grabaciones de CCTV o las auditorías, se encadenan para reconstruir la escena y resolver el caso.*

**MITRE ATT&CK:** N/A (Challenge de forensics/CTF)

**Fuente:** [TryHackMe - The Case: Seven Minutes on the Seine](https://tryhackme.com/r/room/thecasesevenminutesontheseine)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.