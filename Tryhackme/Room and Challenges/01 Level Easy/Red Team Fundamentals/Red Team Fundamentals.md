# Red Team Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `redteamfundamentals` | https://tryhackme.com/room/redteamfundamentals | 01 Level Easy | TryHackMe | Red Team / APT / crown jewels / TTPs / Red Cell / White Cell / fases de ataque | Introducción a los fundamentos del Red Team: adversarios avanzados, TTPs, células de ejercicio y fases de un ataque simulado. |

---

**Contexto:** Sala introductoria de los conceptos base del Red Team. Explica qué es un grupo de amenaza avanzada y persistente (APT), los términos clave como "crown jewels" y TTPs (Tactics, Techniques and Procedures), y cómo se organiza un ejercicio con las células Red Cell y White Cell. También repasa los pasos de una operación, desde la fase inicial (Installation) hasta la explotación (Exploitation), y cierra con una bandera.

> **ES:** "Red Team Fundamentals" — fundamentos del Red Team: APTs, TTPs, células de ejercicio (Red/White Cell) y fases de ataque.
> **EN:** "Red Team Fundamentals" — Red Team basics: APTs, TTPs, exercise cells (Red/White Cell) and attack phases.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de los conceptos que se van a abordar (adversarios, TTPs, células y fases de ataque). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |

### Task 2: Conceptos fundamentales / Core Concepts

**Explicación:** La sala plantea dos preguntas conceptuales tipo yay/nay sobre los límites y el rol del Red Team (ambas se responden `Nay`) y pregunta por el término que define a los grupos de ciberatacantes persistentes, organizados y con recursos (a menudo respaldados por estados): `Advanced Persistent Threats`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta conceptual sobre el alcance del Red Team. (yay/nay) / Conceptual question about Red Team scope. (yay/nay) | `Nay` |
| 2 | Pregunta conceptual sobre el rol del Red Team. (yay/nay) / Conceptual question about the Red Team role. (yay/nay) | `Nay` |
| 3 | ¿Cómo se denomina a los grupos de ciberatacantes persistentes y con grandes recursos? / What are the persistent, well-resourced cybercriminal groups called? | `Advanced Persistent Threats` |

### Task 3: Conoce a tu adversario / Know Your Adversary

**Explicación:** Se repasa el conocimiento del adversario: los activos más valiosos que busca proteger o comprometer se llaman `crown jewels`, y los métodos, técnicas y procesos que utiliza un adversario se conocen como `Tactics, techniques and procedures` (TTPs). La pregunta conceptual tipo yay/nay sobre este apartado se responde `Nay`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llaman los activos más valiosos que un adversario quiere proteger o comprometer? / What are the most valuable assets an adversary wants to protect or compromise called? | `crown jewels` |
| 2 | ¿Qué término describe los métodos y procesos que utiliza un adversario? / What term describes the methods and processes used by an adversary? | `Tactics, techniques and procedures` |
| 3 | Pregunta conceptual sobre el conocimiento del adversario. (yay/nay) / Conceptual question about knowing your adversary. (yay/nay) | `Nay` |

### Task 4: Equipos del ejercicio / Exercise Cells

**Explicación:** En un ejercicio de Red Team intervienen varias células: el equipo que simula al adversario y ejecuta los ataques es la `Red Cell`, mientras que el equipo que controla, facilita y arbitra el ejercicio es la `White Cell`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la célula que simula al adversario en un ejercicio? / What is the cell that simulates the adversary in an exercise called? | `Red Cell` |
| 2 | ¿Cómo se llama la célula que controla y facilita el ejercicio? / What is the cell that controls and facilitates the exercise called? | `White Cell` |

### Task 5: Fases del ataque / Attack Stages

**Explicación:** Las fases del ataque dentro del ejercicio: la fase en la que el malware o la herramienta se instalan en la máquina objetivo es `Installation`, y la fase en la que se aprovecha una vulnerabilidad para obtener acceso es `Exploitation`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué fase se instala el malware o la herramienta en el sistema objetivo? / In which phase is malware or a tool installed on the target system? | `Installation` |
| 2 | ¿En qué fase se explota una vulnerabilidad para obtener acceso? / In which phase is a vulnerability exploited to gain access? | `Exploitation` |

### Task 6: Flag / Flag

**Explicación:** Tras completar el contenido teórico de la sala se obtiene la bandera final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la sala? / What is the room flag? | `THM{RED_TEAM_ROCKS}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen de los fundamentos del Red Team. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |
| 2 | Pregunta conceptual sobre el alcance del Red Team. (yay/nay) / Conceptual question about Red Team scope. (yay/nay) | `Nay` |
| 3 | Pregunta conceptual sobre el rol del Red Team. (yay/nay) / Conceptual question about the Red Team role. (yay/nay) | `Nay` |
| 4 | ¿Cómo se denomina a los grupos de ciberatacantes persistentes y con grandes recursos? / What are the persistent, well-resourced cybercriminal groups called? | `Advanced Persistent Threats` |
| 5 | ¿Cómo se llaman los activos más valiosos que un adversario quiere proteger o comprometer? / What are the most valuable assets an adversary wants to protect or compromise called? | `crown jewels` |
| 6 | ¿Qué término describe los métodos y procesos que utiliza un adversario? / What term describes the methods and processes used by an adversary? | `Tactics, techniques and procedures` |
| 7 | Pregunta conceptual sobre el conocimiento del adversario. (yay/nay) / Conceptual question about knowing your adversary. (yay/nay) | `Nay` |
| 8 | ¿Cómo se llama la célula que simula al adversario en un ejercicio? / What is the cell that simulates the adversary in an exercise called? | `Red Cell` |
| 9 | ¿Cómo se llama la célula que controla y facilita el ejercicio? / What is the cell that controls and facilitates the exercise called? | `White Cell` |
| 10 | ¿En qué fase se instala el malware o la herramienta en el sistema objetivo? / In which phase is malware or a tool installed on the target system? | `Installation` |
| 11 | ¿En qué fase se explota una vulnerabilidad para obtener acceso? / In which phase is a vulnerability exploited to gain access? | `Exploitation` |
| 12 | ¿Cuál es la flag de la sala? / What is the room flag? | `THM{RED_TEAM_ROCKS}` |
| 13 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

**Metodología:** Leer los fundamentos teóricos del Red Team (APT, crown jewels, TTPs), identificar las células del ejercicio (Red Cell atacante, White Cell de control) y repasar las fases de una operación (Installation y Exploitation), para terminar reclamando la flag final de la sala.

### Cadena de ataque / Attack Chain

```text
Comprender el adversario (APT, TTPs, crown jewels) -> Organizar el ejercicio (Red Cell / White Cell) -> Ejecutar las fases (Installation / Exploitation) -> Obtener la flag
```

**Learning chain:** Fundamentos -> Conocer al adversario -> Células del ejercicio -> Fases de ataque -> Flag final.

**Lección:** *El Red Team no es solo "atacar": entender al adversario (TTPs, crown jewels) y estructurar el ejercicio con células claras (Red/White Cell) es lo que separa un simulacro de una operación realista.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1587 (Develop Capabilities), T1595 (Active Scanning)

**Fuente:** [TryHackMe - Red Team Fundamentals](https://tryhackme.com/room/redteamfundamentals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.