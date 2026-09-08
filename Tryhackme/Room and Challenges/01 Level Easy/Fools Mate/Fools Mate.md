# Fools Mate

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `foolsmate` |
| **Link** | [TryHackMe](https://tryhackme.com/room/foolsmate) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=foolsmate` + websearch de walkthroughs) |
| **Componentes** | Web app / JavaScript / validación client-side / API / fetch / ajedrez (FEN) / EndgameTrainer |
| **Impacto** | Demuestra que la validación que vive solo en el cliente nunca es seguridad: se salta el frontend de una app de ajedrez para completar el mate vía API y obtener la flag. |

---

**Contexto:** Sala Easy de web app basada en ajedrez ("Fool's Mate", el mate en 2 jugadas). La lección central es que toda la validación vive en el cliente (JavaScript): el servidor acepta cualquier movimiento válido cuando se le habla directo vía API, por lo que basta con saltarse el frontend para completar el mate y obtener la flag.

## Solucionario

### Task 1: play

**Explicación:** Se despliega una app web con una VM (http://MACHINE_IP). Es un tablero de ajedrez llamado "EndgameTrainer" que pide resolver un mate en 1 con la posición FEN `6k1/5ppp/8/8/8/8/5PPP/R5K1`: solo hay que mover la torre de a1 a a8 (`Ra8`) para dar mate. Al mover la pieza, un popup bloquea la partida ("I'll shut down your PC..."), pero leyendo `/js/app.js` se descubre que `preMoveCheck()` simplemente clona el tablero y bloquea el movimiento en el cliente mientras que los movimientos legales se envían por `fetch POST /api/move` con `{from, to, promotion}`. Hablando directamente con la API y mandando `{"from":"a1","to":"a8"}` se obtiene `{"ok":true,"move":"a1a8","status":"checkmate","winner":"white","flag":"THM{...}"}` con la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{cl13nt_s1d3_ch3ckm4t3}` |

---

**Metodología:**
1. **Reconocimiento:** se abre `http://MACHINE_IP` y se identifica la app "EndgameTrainer", un entrenador de finales de ajedrez que pide resolver un mate en 1.
2. **Identificar el objetivo:** el FEN `6k1/5ppp/8/8/8/8/5PPP/R5K1` indica que es un mate en 1 moviendo la torre de a1 a a8 (`Ra8`).
3. **Fallo del cliente:** al hacer el movimiento, un popup bloquea la partida ("I'll shut down your PC..."); el cliente no deja completar el movimiento.
4. **Enumeración del frontend:** se lee `/js/app.js`; `preMoveCheck()` clona el tablero y bloquea el movimiento en el cliente, pero los movimientos legales se envían por `fetch POST /api/move` con `{from, to, promotion}`.
5. **Bypass de la validación:** se habla directo con la API: `POST /api/move` con cuerpo `{"from":"a1","to":"a8"}`.
6. **Flag:** el servidor responde `{"ok":true,"move":"a1a8","status":"checkmate","winner":"white","flag":"THM{cl13nt_s1d3_ch3ckm4t3}"}`.

**Learning chain:** http://MACHINE_IP (EndgameTrainer) → leer /js/app.js → preMoveCheck() valida SOLO en el cliente (bloquea Ra8) → POST /api/move directo con {"from":"a1","to":"a8"} → response: checkmate / winner:white / flag.

**Lección:** La validación que vive solo en el cliente nunca es seguridad: el servidor debe validar por sí mismo cualquier entrada, porque el frontend siempre puede saltarse.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.007 (Command and Scripting Interpreter: JavaScript), T1071.001 (Application Layer Protocol: Web Protocols).

**Fuente:** [TryHackMe - Fools Mate](https://tryhackme.com/room/foolsmate)