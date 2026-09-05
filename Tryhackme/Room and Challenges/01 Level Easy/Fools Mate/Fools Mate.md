# Fools Mate [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF
* **Slug:** `foolsmate`
* **Link:** https://tryhackme.com/room/foolsmate
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=foolsmate` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala Easy de web app basada en ajedrez ("Fool's Mate", el mate en 2 jugadas). La lección central es que toda la validación vive en el cliente (JavaScript): el servidor acepta cualquier movimiento válido cuando se le habla directo vía API, por lo que basta con saltarse el frontend para completar el mate y obtener la flag.
> **EN:** Easy room about a chess-based web app ("Fool's Mate", the two-move checkmate). The core lesson is that all validation lives client-side (JavaScript): the server accepts any legal move when spoken to directly via the API, so bypassing the frontend is enough to deliver the checkmate and get the flag.

### Task 1 - play

> **ES:** Se despliega una app web con una VM (http://MACHINE_IP). Es un tablero de ajedrez llamado "EndgameTrainer" que pide resolver un mate en 1 con la posición FEN `6k1/5ppp/8/8/8/8/5PPP/R5K1`: solo hay que mover la torre de a1 a a8 (`Ra8`) para dar mate. Al mover la pieza, un popup bloquea la partida ("I'll shut down your PC..."), pero leyendo `/js/app.js` se descubre que `preMoveCheck()` simplemente clona el tablero y bloquea el movimiento en el cliente mientras que los movimientos legales se envían por `fetch POST /api/move` con `{from, to, promotion}`. Hablando directamente con la API y mandando `{"from":"a1","to":"a8"}` se obtiene `{"ok":true,"move":"a1a8","status":"checkmate","winner":"white","flag":"THM{...}"}` con la flag.
> **EN:** A web app is deployed on a VM (http://MACHINE_IP). It is a chess board called "EndgameTrainer" asking for a mate-in-1 on the FEN position `6k1/5ppp/8/8/8/8/5PPP/R5K1`: you only need to move the rook from a1 to a8 (`Ra8`) to deliver checkmate. Moving the piece triggers a popup that blocks the game ("I'll shut down your PC..."), but reading `/js/app.js` reveals that `preMoveCheck()` merely clones the board and blocks the move client-side, while legal moves are submitted via `fetch POST /api/move` with `{from, to, promotion}`. Talking to the API directly and posting `{"from":"a1","to":"a8"}` returns `{"ok":true,"move":"a1a8","status":"checkmate","winner":"white","flag":"THM{...}"}` with the flag.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{cl13nt_s1d3_ch3ckm4t3}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Se abre `http://MACHINE_IP` y se identifica la app "EndgameTrainer", un entrenador de finales de ajedrez que pide un mate en 1.
2. **Paso / Step - Identificar el objetivo:** El FEN `6k1/5ppp/8/8/8/8/5PPP/R5K1` indica que es un mate en 1 moviendo la torre de a1 a a8 (`Ra8`).
3. **Paso / Step - Fallo del cliente:** Al hacer el movimiento, un popup bloquea la partida ("I'll shut down your PC..."); el cliente no deja completar el movimiento.
4. **Paso / Step - Enumeración del frontend:** Se lee `/js/app.js`; `preMoveCheck()` clona el tablero y bloquea el movimiento, pero los movimientos legales se envían por `fetch POST /api/move` con `{from,to,promotion}`.
5. **Paso / Step - Bypass de la validación:** Se habla directo con la API: `POST /api/move` con cuerpo `{"from":"a1","to":"a8"}`.
6. **Paso / Step - Flag:** El servidor responde `{"ok":true,"move":"a1a8","status":"checkmate","winner":"white","flag":"THM{cl13nt_s1d3_ch3ckm4t3}"}`.

### Cadena de ataque / Attack Chain

```
http://MACHINE_IP (EndgameTrainer)
  -> leer /js/app.js
  -> preMoveCheck() valida SOLO en el cliente (bloquea Ra8)
  -> POST /api/move directo con {"from":"a1","to":"a8"}
  -> response: checkmate / winner:white / flag
  -> THM{cl13nt_s1d3_ch3ckm4t3}
```

**Lección:** La validación que vive solo en el cliente nunca es seguridad: el servidor debe validar por sí mismo cualquier entrada, porque el frontend siempre puede saltarse.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
