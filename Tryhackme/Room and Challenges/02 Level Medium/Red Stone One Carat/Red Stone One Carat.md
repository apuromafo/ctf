# Red Stone One Carat

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Desafío guiado | redstoneonecarat | https://tryhackme.com/room/redstoneonecarat | 02 Level Medium | TryHackMe | Desafío de lógica y captura de flags | Compromiso del objetivo con la captura de las dos flags finales |

> **Objeto:** Resolver el desafío guiado de Red Stone One Carat avanzando por las tres fases del laboratorio: identificar el dato requerido, ejecutar la acción que entrega las dos flags del objetivo y cerrar la sala sin respuesta adicional.

---

**Contexto:** La sala **Red Stone One Carat** es un desafío guiado en el que el jugador debe identificar un valor concreto (de palabra clave), completar la acción que da acceso a las flags del objetivo y cerrar el laboratorio. El flujo de respuestas es corto: una fase sin respuesta esperada, una fase con el valor y las dos flags, y una última fase de cierre sin respuesta obligatoria.

## Solucionario

### Task 1: Fase inicial / Initial phase
**Explicación:**

Primera fase del laboratorio: solo requiere leer la indicación y avanzar, sin responder ninguna pregunta.

1. `No answer needed`

### Task 2: Valor y flags / Value and flags
**Explicación:**

Se identifica el valor requerido por la sala para continuar y se obtienen las dos flags que acreditan el avance y la resolución del objetivo.

1. `cheeseburger`
2. `THM{3a106092635945849a0fbf7bac92409d}`
3. `THM{58e53d1324eef6265fdb97b08ed9aadf}`

### Task 3: Cierre / Wrap-up
**Explicación:**

Última pregunta de confirmación del laboratorio, sin respuesta obligatoria.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fase inicial | `No answer needed` |
| 2 | Valor requerido | `cheeseburger` |
| 3 | Flag 1 del objetivo | `THM{3a106092635945849a0fbf7bac92409d}` |
| 4 | Flag 2 del objetivo | `THM{58e53d1324eef6265fdb97b08ed9aadf}` |
| 5 | Cierre | `No answer needed` |

---

**Metodología:** Lectura de las indicaciones del laboratorio, identificación del valor requerido, ejecución de la acción que entrega las flags y cierre de la sala.

**Learning chain:** Fase inicial → identificación del valor → captura de flags → cierre.

**Lección:** *En los desafíos guiados, identificar correctamente el dato de entrada es el paso crítico que habilita el resto del flujo.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1003 OS Credential Dumping.

**Fuente:** [TryHackMe - Red Stone One Carat](https://tryhackme.com/room/redstoneonecarat)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.