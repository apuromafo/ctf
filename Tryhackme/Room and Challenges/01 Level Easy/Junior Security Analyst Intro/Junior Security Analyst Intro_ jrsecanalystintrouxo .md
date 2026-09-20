# Junior Security Analyst Intro

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `jrsecanalystintrouxo` | https://tryhackme.com/room/jrsecanalystintrouxo | 01 Level Easy | TryHackMe | SOC / Triage Specialist / análisis de alertas / Cyber Kill Chain / phishing | Simular un día en la vida de un analista de seguridad junior: clasificar incidentes (triage), analizar alertas de phishing y responder como un SOC. |

---

**Contexto:** Sala introductoria de la carrera de SOC Analyst de TryHackMe. Simula un día en la vida de un Security Analyst: se desempeñan las tareas cotidianas de clasificación y respuesta a incidentes. La sala presenta dos versiones de recorrido (2025 y 2026) con las mismas preguntas y respuestas equivalentes.

> **ES:** "Play through a day in the life of a Security Analyst and experience their everyday duties." Sala de simulación del trabajo diario de un analista de seguridad.
> **EN:** Junior Security Analyst Intro. Play through a day in the life of a Security Analyst and experience their everyday duties.

## Solucionario

### Task 1: El rol del analista / The Analyst Role

**Explicación:** La primera pregunta plantea qué rol desempeña el analista dentro del SOC. En la versión 2025 la respuesta es **Triage Specialist**; en la versión 2026 la respuesta es **SOC**.

2025:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué rol desempeña el analista? / What role does the analyst play? | `Triage Specialist` |

2026:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué rol desempeña el analista? / What role does the analyst play? | `SOC` |

### Task 2: Rutinas del analista / Analyst Routines

**Explicación:** Tarea de lectura sobre las tareas cotidianas del analista. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 3: Análisis de alertas / Alert Analysis

**Explicación:** Se analiza una alerta de phishing: no requiere respuesta el primer paso; el correo malicioso proviene de la IP `221.181.185.159`, el analista que lo crea se llama **Will Griffin** y al resolver el caso se obtiene la flag `THM{UNTIL-WE-MEET-AGAIN}` (versión 2025) o `THM{until-we-meet-again}` (versión 2026).

2025:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso previo del análisis. / Previous step of the analysis. | `No answer needed` |
| 2 | ¿Cuál es la dirección IP del remitente? / What is the sender's IP address? | `221.181.185.159` |
| 3 | ¿Cómo se llama el analista que crea la alerta? / What is the name of the analyst who creates the alert? | `Will Griffin` |
| 4 | ¿Cuál es la flag del caso? / What is the flag of the case? | `THM{UNTIL-WE-MEET-AGAIN}` |

2026:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso previo del análisis. / Previous step of the analysis. | `No answer needed` |
| 2 | ¿Cuál es la dirección IP del remitente? / What is the sender's IP address? | `221.181.185.159` |
| 3 | ¿Cómo se llama el analista que crea la alerta? / What is the name of the analyst who creates the alert? | `Will Griffin` |
| 4 | ¿Cuál es la flag del caso? / What is the flag of the case? | `THM{until-we-meet-again}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué rol desempeña el analista (2025)? / What role does the analyst play (2025)? | `Triage Specialist` |
| 2 | Lee el contenido de la tarea. | `No answer needed` |
| 3 | Paso previo del análisis (2025). | `No answer needed` |
| 4 | ¿Cuál es la dirección IP del remitente (2025)? | `221.181.185.159` |
| 5 | ¿Cómo se llama el analista que crea la alerta (2025)? | `Will Griffin` |
| 6 | ¿Cuál es la flag del caso (2025)? | `THM{UNTIL-WE-MEET-AGAIN}` |
| 7 | ¿Qué rol desempeña el analista (2026)? / What role does the analyst play (2026)? | `SOC` |
| 8 | Lee el contenido de la tarea. | `No answer needed` |
| 9 | Paso previo del análisis (2026). | `No answer needed` |
| 10 | ¿Cuál es la dirección IP del remitente (2026)? | `221.181.185.159` |
| 11 | ¿Cómo se llama el analista que crea la alerta (2026)? | `Will Griffin` |
| 12 | ¿Cuál es la flag del caso (2026)? | `THM{until-we-meet-again}` |

---

**Metodología:** Seguir el día simulado del analista: identificar el rol (triage/SOC), leer las rutinas del puesto y analizar la alerta de phishing (IP del remitente, analista responsable y flag del caso), recordando que las versiones 2025 y 2026 comparten estructura con flags distintas.

### Cadena de ataque / Attack Chain

```text
Recepción de alerta -> triage/clasificación -> análisis de la alerta de phishing (IP/origen) -> reportero del caso -> resolución -> flag
```

**Learning chain:** rol del analista -> duties -> alerta phishing -> IP -> Will Griffin -> flag.

**Lección:** *Un analista junior empieza entendiendo el flujo del SOC: recibir, clasificar (triage), investigar la alerta (origen y responsable) y cerrar el caso con la resolución correcta.*

**MITRE ATT&CK:** T1566 (Phishing), N/A (room de simulación SOC)

**Fuente:** [TryHackMe - Junior Security Analyst Intro](https://tryhackme.com/room/jrsecanalystintrouxo)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.