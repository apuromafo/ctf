# SSDLC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teórico / Formativo | ssdlc | https://tryhackme.com/room/ssdlc | 02 Level Medium | TryHackMe | SSDLC, Fases del ciclo de vida, Threat Modelling, DREAD/STRIDE/PASTA, SAST/DAST, SAMM/BSIMM | Cultura de desarrollo seguro y reducción de vulnerabilidades en el SDLC |

---

**Contexto:** La sala **SSDLC** introduce el ciclo de vida de desarrollo seguro de software (*Secure Software Development Life Cycle*): sus fases, la gestión de riesgos, los modelos de amenazas (DREAD, STRIDE, PASTA), las técnicas de análisis estático y dinámico (SAST/DAST), las pruebas de seguridad y los frameworks maduros del sector (Microsoft SDL, SAMM, BSIMM). Cada pregunta fija los conceptos clave y el recorrido concluye con una flag que resume la sala.

## Solucionario

### Task 1: Bienvenida
**Explicación:**

Se aterriza en el entorno de la sala y se confirma el acceso antes de comenzar con los contenidos del SSDLC.

Respuesta: `No answer needed`

### Task 2: Número de fases del SSDLC
**Explicación:**

El ciclo de desarrollo seguro descrito en la sala se compone de un total de fases que deben recorrerse de forma iterativa durante todo el ciclo de vida del software.

Respuesta: `15`

### Task 3: Orden inicial de las fases
**Explicación:**

Las primeras fases del SSDLC se ordenan empezando por la postura de seguridad de la organización y la planificación de requisitos, para desembocar en el modelado de amenazas.

1. `Security Posture`
2. `Planning and Requirements`
3. `Threat Modelling`

### Task 4: Evaluación de riesgos
**Explicación:**

El riesgo se calcula combinando la severidad con la probabilidad de ocurrencia, y el enfoque que asigna valores numéricos a los activos es la evaluación cuantitativa de riesgos.

1. `Severity x Likelihood`
2. `Quantitative Risk Assessment`

### Task 5: Modelos de amenazas
**Explicación:**

Se identifican las metodologías de modelado de amenazas propuestas en la sala: DREAD, STRIDE y PASTA.

1. `DREAD`
2. `STRIDE`
3. `PASTA`

### Task 6: Análisis de código
**Explicación:**

Se valida la afirmación sobre las herramientas de análisis y se distinguen las pruebas dinámicas (ejecutando la aplicación) de las estáticas (analizando el código fuente).

1. `y`
2. `DAST`
3. `SAST`

### Task 7: Pruebas y operación
**Explicación:**

Tras el desarrollo, la seguridad se verifica mediante la evaluación de vulnerabilidades y el pentesting, y el ciclo se mantiene con las operaciones y el mantenimiento.

1. `Vulnerability Assessment`
2. `Penetration Testing`
3. `Operations & Maintenance`

### Task 8: Frameworks y buenas prácticas
**Explicación:**

Se listan los marcos de referencia del sector para implantar un SSDLC maduro: Microsoft SDL, SAMM y BSIMM.

1. `Microsoft SDL`
2. `SAMM`
3. `BSIMM`

### Task 9: Flag final
**Explicación:**

Completados los conceptos del ciclo de vida de desarrollo seguro, se obtiene la flag de cierre de la sala.

Respuesta: `THM{D0-A-Barr3l-R011}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bienvenida / tarea inicial | `No answer needed` |
| 2 | ¿Cuántas fases tiene el SSDLC descrito? | `15` |
| 3.1 | Primera fase del ciclo | `Security Posture` |
| 3.2 | Segunda fase del ciclo | `Planning and Requirements` |
| 3.3 | Tercera fase del ciclo | `Threat Modelling` |
| 4.1 | Fórmula del riesgo | `Severity x Likelihood` |
| 4.2 | Enfoque de evaluación de riesgos solicitado | `Quantitative Risk Assessment` |
| 5.1 | Modelo de amenazas 1 | `DREAD` |
| 5.2 | Modelo de amenazas 2 | `STRIDE` |
| 5.3 | Modelo de amenazas 3 | `PASTA` |
| 6.1 | ¿Afirmación correcta? | `y` |
| 6.2 | Tipo de análisis dinámico | `DAST` |
| 6.3 | Tipo de análisis estático | `SAST` |
| 7.1 | Fase de evaluación de vulnerabilidades | `Vulnerability Assessment` |
| 7.2 | Fase de pruebas de penetración | `Penetration Testing` |
| 7.3 | Fase final del ciclo | `Operations & Maintenance` |
| 8.1 | Framework 1 | `Microsoft SDL` |
| 8.2 | Framework 2 | `SAMM` |
| 8.3 | Framework 3 | `BSIMM` |
| 9 | Flag final | `THM{D0-A-Barr3l-R011}` |

---

**Metodología:** Estudio del ciclo de vida de desarrollo seguro, identificación de fases, modelado de amenazas (DREAD/STRIDE/PASTA), análisis de riesgo, herramientas SAST/DAST y frameworks de referencia del sector.

**Learning chain:** Fases del SDLC → postura y requisitos → threat modelling → riesgo y métricas → análisis y pruebas → operación → frameworks maduros → flag.

**Lección:** *La seguridad no es una fase final: se planifica, modela, verifica y opera a lo largo de todo el ciclo de vida del software.*

**MITRE ATT&CK:** T1592 Gather Victim Host Information · T1190 Exploit Public-Facing Application (mitigado por SAST/DAST).

**Fuente:** [TryHackMe - SSDLC](https://tryhackme.com/room/ssdlc)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.