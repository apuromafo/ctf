# Advent 2025 SideQuest

| **Dificultad** | N/A | **Tipo** | Guía/Índice (Evento Advent of Cyber 2025 - Side Quests) | **Slug** | `readme` | | **Link** | [TryHackMe](https://tryhackme.com/room/readme) | | **Seccion** | Advent of Cyber Tryhackme / SideQuest | | **Fuente** | texto oficial THM + walkthroughs propios (Hopper's Origins, The Great Disappearing Act, Scheme Catcher, Carrotbane of My Existence, BreachBlocker Unlocker) | | **Componentes** | side quests / passwords / egg decode / guías / índice | | **Impacto** | Documento índice de los Side Quests de AoC 2025: cada side quest necesita una contraseña para empezar; aquí se listan las guías para obtenerlas |

---

![Advent of Cyber 2025 Side Quests](https://tryhackme.com/images/pngs/aoc25/sidequest/cosy-cabin.webp)

**Contexto:** Página índice del evento **Advent of Cyber 2025 Side Quests**. Contiene las respuestas y pasos necesarios para llegar a los side quests; cada uno necesita una *password* para empezarlo. Esta room solo cubre los pasos para obtener estas contraseñas; el contenido de cada side quest se cubre en sus respectivas guías (Sidequest 0-4).

> **Note (EN mirror):** Index page for the AoC 2025 Side Quests event. Each side quest requires a password to start; this page only covers how to obtain those passwords. The actual side quests are documented in their own guides.

**Tabla de contenidos / Table of contents**

- Sidequest 0 [Hopper's Origin](#hopper-s-origin)
- Sidequest 1 [The Great Disappearing Act](#the-great-disappearing-act)
- Sidequest 2 [Scheme Catcher](#scheme-catcher)
- Sidequest 3 [Carrotbane of My Existence](#carrotbane-of-my-existence)
- Sidequest 4 [BreachBlocker Unlocker](#breachblocker-unlocker)

## Solucionario

### Task 1: Hopper's Origin (Sidequest 0)

**Explicación:** El side quest 0 es el reto de **AD / Active Directory** de la saga. Para empezarlo hace falta el **Invite Code** que se obtiene al completar el Sidequest 1 (escape de HopSec Asylum): el endpoint `/cgi-bin/escape_check.sh` validado con las 3 flags de ese reto devuelve `{"ok": true, "invite_url": "https://static-labs.tryhackme.cloud/apps/hoppers-invitation/", "invite_code": "THM{There.is.no.EASTmas.without.Hopper}"}`. Con ese invite code se desbloquea la página de invitación y se llega a la room oficial. La guía completa (CORS abuse, hopper-origins.txt, descifrado PBKDF2, compromiso de AI.VANCHAT.LOC / TBFC.LOC / VANCHAT.LOC y los 4 servidores con 17 flags) se documenta en `SideQuest/Sidequest0/Sidequest0.md` y en los tutorials `Hoppers-Origin-id-root` y `Tutorial drouxinol`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Invite Code para desbloquear Hopper's Origin | `THM{There.is.no.EASTmas.without.Hopper}` |

### Task 2: The Great Disappearing Act (Sidequest 1)

**Explicación:** El side quest 1 es el plan de **escape de HopSec Asylum** en 5 pasos (desbloquear celda, lobby, keypad del Psych Ward, Main Corridor y escape final). Empieza con un **egg decode** cuya password desbloquea el firewall. La guía completa (nmap, ffuf, cgi-bin, hydra con combinator, JWT + HTTP Parameter Pollution en el video portal, SCADA en localhost:9001, unlock code y SUID `diag_shell` + docker) se documenta en `SideQuest/Sidequest1/Sidequest1.md` y en el tutorial `tutorial jaxafed`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Egg Decode Password para desbloquear el reto | `now_you_see_me` |

### Task 3: Scheme Catcher (Sidequest 2)

**Explicación:** El side quest 2 es un reto **INSANE** de pwn/heap exploitation ("Payload Storage Malhare's"). Empieza con un **egg decode**. La guía completa (nmap, fuzzing, folder `/dev`, análisis de `beacon.bin` con Enter key `EastMass`, strings y heap exploitation para las 4 flags) se documenta en `SideQuest/Sidequest2/Sidequest2.md`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Egg Decode Password para desbloquear el reto | `tit_for_tat` |

### Task 4: Carrotbane of My Existence (Sidequest 3)

**Explicación:** El side quest 3 es la investigación para detener el levantamiento liderado por Hopper. Empieza con un **egg decode**. La guía completa (enumeración, explotación, escalada de privilegios e investigación para las 4 flags) se documenta en `SideQuest/Sidequest3/Sidequest3.md`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Egg Decode Password para desbloquear el reto | `one_hopper_army` |

### Task 5: BreachBlocker Unlocker (Sidequest 4)

**Explicación:** El side quest 4 es un reto de **reverse engineering** del código fuente del BreachBlocker para encontrar la flag oculta. Empieza con un **egg decode**. La guía completa (web fuzzing, source code exposure, timing attack / side channel, SMTP y email parsing) se documenta en `SideQuest/Sidequest4/Sidequest4.md`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Egg Decode Password para desbloquear el reto | `hrone123*r` |

---

**Metodología:**

1. Localizar la contraseña de cada side quest (Hoppers Origin, Great Disappearing Act, Scheme Catcher, Carrotbane of My Existence, BreachBlocker Unlocker)
2. Usar cada password para desbloquear el side quest correspondiente
3. Documentar los pasos en las guías específicas de cada side quest

**Learning chain:** SideQuest Readme -> contraseñas -> Sidequest 0 Hopper's Origin -> Sidequest 1 The Great Disappearing Act -> Sidequest 2 Scheme Catcher -> Sidequest 3 Carrotbane of My Existence -> Sidequest 4 BreachBlocker Unlocker

Cadena de ataque / Attack Chain:
```text
AoC 2025 Side Quests -> passwords -> SQ0 Hopper's Origin -> SQ1 The Great Disappearing Act
-> SQ2 Scheme Catcher -> SQ3 Carrotbane of My Existence -> SQ4 BreachBlocker Unlocker
```

**Lección:** *Los side quests son una mecánica de desbloqueo en cadena: cada reto entrega la contraseña que abre el siguiente, premiando la documentación ordenada de cada fase.*

**MITRE ATT&CK:**

- T1110 - Brute Force
- T1190 - Exploit Public-Facing Application
- T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Advent 2025 SideQuest](https://tryhackme.com/room/readme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.