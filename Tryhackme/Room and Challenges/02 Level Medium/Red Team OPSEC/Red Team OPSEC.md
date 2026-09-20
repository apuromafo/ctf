# Red Team OPSEC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room / Operaciones Red Team | redteamopsec | https://tryhackme.com/room/redteamopsec | 02 Level Medium | TryHackMe | OPSEC, TTPs, buenas prácticas de red team, gestión de la huella | Reducción de la detección y éxito de las operaciones ofensivas |

> **Objeto:** Comprender y aplicar los principios de OPSEC (Operational Security) en operaciones de red team, evaluando decisiones de seguridad, identificando información crítica y validando los criterios que reducen la visibilidad y mejoran el éxito de las operaciones.

---

**Contexto:** La sala **Red Team OPSEC** es una sala teórico-práctica sobre seguridad operativa aplicada a operaciones de red team. OPSEC es el proceso de identificar información crítica y analizar las acciones propias frente a las capacidades del adversario para reducir la probabilidad de detección. El laboratorio combina preguntas de evaluación (Sí/No) sobre distintas decisiones operativas con la captura de dos flags relacionadas con el manejo de la información crítica y la disciplina OPSEC.

## Solucionario

### Task 1: Premisas de la operación / Operation premises
**Explicación:**

Primera pregunta: lectura del planteamiento general de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Task 2: Información crítica / Critical information
**Explicación:**

Se identifica la información crítica cuya exposición compromete la operación y se obtiene la flag correspondiente.

1. `THM{OPSEC_CRITICAL_INFO}`

### Task 3: Evaluación inicial / Initial assessment
**Explicación:**

Pregunta de reflexión inicial sobre las premisas operativas, sin respuesta obligatoria.

1. `No answer needed`

### Task 4: Decisiones de OPSEC / OPSEC decisions (Sí/No)
**Explicación:**

Evaluación de cinco decisiones o planteamientos operativos. Cada pregunta se responde con `Y` (Yes / Sí) o `N` (No) según el criterio OPSEC correcto:

1. `Y`
2. `N`
3. `Y`
4. `Y`
5. `N`

### Task 5: Criterio final / Final criterion
**Explicación:**

Valoración final de un último planteamiento operativo, respondida afirmativamente.

1. `Y`

### Task 6: Aplicación práctica / Practical application
**Explicación:**

Fase de aplicación práctica de los conceptos de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Task 7: Flag de OPSEC / OPSEC flag
**Explicación:**

Tras completar la parte práctica se obtiene la flag final que acredita la resolución de la sala.

1. `THM{OPSEC-RED-TEAM}`

### Task 8: Cierre / Wrap-up
**Explicación:**

Última pregunta de confirmación de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Premisas de la operación | `No answer needed` |
| 2 | Flag de información crítica | `THM{OPSEC_CRITICAL_INFO}` |
| 3 | Evaluación inicial | `No answer needed` |
| 4 | Decisión OPSEC 1 | `Y` |
| 5 | Decisión OPSEC 2 | `N` |
| 6 | Decisión OPSEC 3 | `Y` |
| 7 | Decisión OPSEC 4 | `Y` |
| 8 | Decisión OPSEC 5 | `N` |
| 9 | Criterio final | `Y` |
| 10 | Aplicación práctica | `No answer needed` |
| 11 | Flag final OPSEC | `THM{OPSEC-RED-TEAM}` |
| 12 | Cierre | `No answer needed` |

---

**Metodología:** Estudio de los principios OPSEC, identificación de la información crítica, evaluación de decisiones operativas frente a las capacidades del adversario y validación práctica con las flags de la sala.

**Learning chain:** Fundamentos OPSEC → identificación de información crítica → evaluación de decisiones (Sí/No) → aplicación práctica → flag final.

**Lección:** *En red team, la seguridad operativa importa más que la herramienta: cada acción monitorizable añade superficie de detección y debe evaluarse frente a la capacidad del adversario.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1070 Indicator Removal on Host · TA0005 Defense Evasion.

**Fuente:** [TryHackMe - Red Team OPSEC](https://tryhackme.com/room/redteamopsec)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.