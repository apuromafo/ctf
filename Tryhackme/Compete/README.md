# King of the Hill (KoTH) — Juego competitivo [INFO]

> **ES/EN** — Guía del modo competitivo King of the Hill de TryHackMe.
> Guide to TryHackMe's competitive King of the Hill mode.

Referencia oficial / Official reference: https://tryhackme.com/games/koth
Guía oficial / Official guide: https://tryhackme.com/resources/blog/guide-to-king-of-the-hill

## ¿Qué es? / What is it?

King of the Hill (KoTH) es un juego competitivo de hacking donde juegas contra **hasta 9 hackers más** (lobbies de máximo 10 jugadores) para **comprometer una máquina y luego parchear sus vulnerabilidades** e impedir que otros jugadores te quiten el acceso. **Mientras más tiempo mantengas tu acceso, más puntos ganas.**

A diferencia de las rooms normales (donde basta con comprometer), aquí la gracia está en **mantener acceso y endurecer (hardening)**: la parte que casi nunca se practica.

## ¿Cómo se juega? / How to play

- La plataforma crea grupos en forma de **lobby**: máximo 10 jugadores participantes + **espectadores**.
- Puedes jugar **1v1**, armar un lobby con amigos o unirte a **lobbies públicos diarios** que crea TryHackMe.
- Como suscriptor puedes **elegir qué máquina usa tu lobby** e invitar espectadores (menú Settings, arriba a la derecha).
- Definido el tiempo de inicio, el juego dura el tiempo configurado compitiendo todos contra todos.

## Reglas (anti-trampa) / Rules

- **Prohibido DoS** contra la máquina o contra otros usuarios.
- **No tocar el servicio del puerto 9999** (ni atacarlo, modificarlo o detenerlo).
- **No modificar ni eliminar flags.**
- No dejar la máquina inutilizable: nada de apagarla, cortar toda comunicación con firewall, terminar todos los servicios o "botchearla".
- Solo detén un servicio si no hay otra forma de parchearlo; los servicios deben seguir funcionando.
- **Prohibidos scripts que hackeen o endurezcan automáticamente.** Lobbies moderados.

## Rooms KoTH documentadas en este repo

- `Room and Challenges/01 Level Easy/KoTH Food CTF`
- `Room and Challenges/02 Level Medium/KoTH Hackers`

## Puntaje / Scoring

Posesión = puntos por tiempo. Gana quien acumula más tiempo como rey de la colina. Los puntos cuentan para ranking/leaderboards según la política vigente de puntos de la plataforma.

---

 fecha:21.09.2026

---

**Fuente / Source:** [KoTH Overview](https://help.tryhackme.com/en/articles/6498315-king-of-the-hill-overview) · [KoTH Guide (blog)](https://tryhackme.com/resources/blog/guide-to-king-of-the-hill) · [Leaderboards](https://tryhackme.com/leaderboards)
**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-21
