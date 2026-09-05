# Love Letter Locker [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e2`
* **Link:** https://tryhackme.com/room/lafb2026e2
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e2` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es una **casilla de cartas de amor privadas**: cada carta se referencia por un identificador secuencial en la URL sin ningún control de autorización por objeto. Enumerando ese `id` se leen cartas de otros usuarios y entre ellas aparece la flag (IDOR/BOLA).
> **EN:** Event room (Love at First Breach 2026) of Easy difficulty. The theme is a **private love-letter locker**: each letter is referenced by a sequential identifier in the URL with no per-object authorization check. Enumerating that `id` reads other users' letters, and the flag is among them (IDOR/BOLA).

### Task 1 - Private Love Letters

> **ES:** La app lista y abre cartas mediante `GET /letter?id=<N>`. El renglón `/letter?id=1` (o similar) muestra una carta legítima del usuario actual. Probando `?id=N-1` y `?id=N+1` se obtienen cartas de otros usuarios: el servidor consulta la base de datos por `id` directamente, sin verificar a qué usuario pertenece la carta (ausencia de ACL a nivel de objeto = **BOLA/IDOR**, OWASP API4:2023). Entre las cartas ajenas se encuentra la que contiene la flag. 1 pregunta.
> **EN:** The app lists and opens letters via `GET /letter?id=<N>`. The row `/letter?id=1` (or similar) shows a legitimate letter from the current user. Trying `?id=N-1` and `?id=N+1` returns other users' letters: the server queries the database by `id` directly, never checking which user owns the letter (missing object-level ACL = **BOLA/IDOR**, OWASP API4:2023). Among someone else's letters you find the one containing the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Web de cartas de amor con listado de los mensajes del usuario autenticado. Cada carta se abre con `GET /letter?id=<N>`.
2. **Paso / Step - Detección del patrón:** Se observa que el `id` es secuencial y que la respuesta contiene el contenido completo de la carta, sin indicar el propietario.
3. **Paso / Step - BOLA/IDOR:** Con `curl / Burp Repeater` se pide `?id=N±1`. El servidor devuelve cartas de otros usuarios: no valida que el recurso pertenezca a la sesión.
4. **Paso / Step - Flag:** Enumerando unos pocos ids se alcanza la carta con la flag: `THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}`.

### Cadena de ataque / Attack Chain

```
web de cartas de amor -> sesión autenticada
  -> GET /letter?id=1    -> carta propia (baseline)
  -> GET /letter?id=2..N -> sin ACL por objeto
  -> BOLA/IDOR -> carta de otro usuario leída
  -> THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}
```

**Lección:** Un `id` enumerable sin control de autorización por objeto es BOLA/IDOR (OWASP API4): toda consulta a un recurso debe verificar la pertenencia antes de devolver datos.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.