# Carrotbane of My Existence

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `sq3-aoc2025-bk3vvbcgiT` | [TryHackMe](https://tryhackme.com/r/room/sq3-aoc2025-bk3vvbcgiT) | Advent of Cyber 2025 (Side Quest 3) | THM | AI email assistant, DNS MX/SMTP, Ollama, tickets | Medio — explotación de asistente AI desplegado localmente para obtener acceso y levantar tickets fraudulentos |

---

**Contexto:** El Side Quest 3 presenta un escenario donde un asistente de IA para gestión de emails (basado en Ollama con el modelo sir-carrotbane) ha sido desplegado en un entorno Docker. El jugador debe enumerar la infraestructura DNS/SMTP, descubrir credenciales débiles, acceder al modelo de lenguaje, y explotar el sistema de tickets para obtener las flags. Se requiere resolución en vivo para algunas flags.

> **ES:** Desafío de Advent of Cyber 2025 (Side Quest 3): enumerar DNS/SMTP, descubrir credenciales débiles, interactuar con el modelo Ollama `sir-carrotbane` mediante prompt injection y explotar el sistema de tickets para obtener las flags. Algunas flags requieren resolución en vivo.

> **EN:** Advent of Cyber 2025 (Side Quest 3) challenge: enumerate DNS/SMTP, find weak credentials, interact with the local Ollama model `sir-carrotbane` via prompt injection and abuse the ticket system to retrieve the flags. Some flags require live solving.

## Solucionario

### Task 1: Unlock / Desbloqueo

**Explicación:** La primera tarea pide la clave de desbloqueo (Unlock key) del Día 17. Depende de la resolución en vivo del Side Quest; el valor no es fijo.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Unlock key (Day 17) | *Requiere resolverse en vivo* |

### Task 2: Challenges / Desafíos

**Explicación:** Se explotan el asistente de IA local y el sistema de tickets para recuperar las 4 flags del desafío. Parte de ellas están redactadas en los walkthroughs públicos por requerir resolución en vivo con la infraestructura desplegada.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the value of flag 1? | `THM{9cd687b330554bd807a717e62910e3d0}` |
| 2 | What is the value of flag 2? | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 3 | What is the value of flag 3? | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 4 | What is the value of flag 4? | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Session Intel conocido:**

- Admin password: `v3rys3cur3p@ssw0rd!`
- Modelo Ollama: `sir-carrotbane`
- Host Ollama: `172.17.0.1:11434`

---

**Metodología:** Enumeración DNS MX/SMTP del dominio → descubrimiento de host Ollama → conexión a la API del modelo `sir-carrotbane` → inyección de prompts para obtener credenciales → acceso a panel de tickets → generación de tickets fraudulentos → obtención de flags.

**Learning chain:** DNS enumeration → SMTP recon → Ollama API interaction → prompt injection → ticket fraud → flag extraction

### Cadena de ataque / Attack Chain

Enumeración DNS/SMTP → descubrimiento del host Ollama (172.17.0.1:11434) → interacción con el modelo `sir-carrotbane` → prompt injection para extraer credenciales → acceso al panel de tickets → generación de tickets fraudulentos → obtención de las flags.

**Lección:** *Un asistente de IA desplegado localmente con credenciales débiles y expuesto en la red es un vector real: la prompt injection sobre un modelo accesible vía API puede convertir un reto de gestión de emails en el compromiso completo del sistema de tickets.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.007 (JavaScript — LLM interaction), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Carrotbane of My Existence](https://tryhackme.com/room/sq3-aoc2025-bk3vvbcgiT)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.