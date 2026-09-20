# Prompt Injection - Sched-yule conflict

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `promptinjection-aoc2025-sxUMnCkvLO` | https://tryhackme.com/room/promptinjection-aoc2025-sxUMnCkvLO | Advent of Cyber 2025 | THM | prompt injection, LLM, calendar app | Manipulating LLM-powered apps to restore deleted calendar entries |

---

**Contexto:** Un adversario ha borrado los eventos de SOC-mas de la aplicación de calendario impulsada por un LLM. Mediante inyección de prompts, debemos convencer al asistente de restaurar los eventos eliminados y recuperar el acceso al calendario de Navidad.

> **ES:** Un adversario ha borrado los eventos de SOC-mas de la aplicación de calendario impulsada por un LLM. Mediante inyección de prompts, debemos convencer al asistente de restaurar los eventos eliminados y recuperar el acceso al calendario de Navidad.
> **EN:** An adversary has deleted the SOC-mas events from the LLM-powered calendar application. Through prompt injection, we must convince the assistant to restore the deleted events and regain access to the Christmas calendar.

## Solucionario

### Task 1: Restaurando SOC-mas / Restoring SOC-mas

**Explicación:** Se analiza la aplicación de calendario impulsada por un LLM y se identifica el campo de interacción con el asistente. Mediante un prompt injection cuidadosamente formulado se logra hacer overriding de las instrucciones de nivel de sistema del asistente, convenciéndolo de restaurar los eventos de SOC-mas que el adversario eliminó.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag provided when SOC-mas is restored in the calendar? | `THM{XMAS_IS_COMING__BACK}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag provided when SOC-mas is restored in the calendar? | `THM{XMAS_IS_COMING__BACK}` |

---

**Metodología:** Se exploró la interfaz del calendario y se identificó el campo de interacción con el LLM. Se formuló un prompt injection para manipular al asistente y restaurar los eventos eliminados de SOC-mas, obteniendo el flag como confirmación.

### Cadena de ataque / Attack Chain

```text
Interactuar con la app de calendario LLM → analizar el comportamiento del asistente → formular prompt injection → overriding de instrucciones del sistema → restaurar eventos de SOC-mas → extraer flag
```

**Learning chain:** LLM-powered app analysis → prompt crafting → instruction override → calendar event restoration → flag extraction

**Lección:** *Un prompt de usuario mal redactado puede sobreescribir las instrucciones de sistema de un LLM: la inyección de prompts explota la ausencia de una jerarquía de instrucciones robusta y la confianza ciega del modelo en el contenido que se le presenta.*

**MITRE ATT&CK:** N/A (defensive walkthrough)

**Fuente:** [TryHackMe - Prompt Injection - Sched-yule conflict](https://tryhackme.com/room/promptinjection-aoc2025-sxUMnCkvLO)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.