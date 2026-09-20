# Crocc Crew

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `crocccrew` | [TryHackMe](https://tryhackme.com/room/crocccrew) | 04 Level Insane | TryHackMe | ctf / web / compromiso progresivo | Seguimiento de la banda Crocc Crew: de la entrada como invitado hasta el compromiso progresivo del sistema con usuario y flags finales del grupo. |

---

**Contexto:** Sala CTF de nivel Insane ambientada en la banda de hackers "Crocc Crew". La primera fase pide resultados interactivos sin respuesta escrita, y la segunda entrega la cadena completa de compromiso: usuario invitado, cuenta de administrador y la flag final que firma el golpe del grupo.

> **ES:** Sala CTF de nivel Insane ambientada en la banda de hackers "Crocc Crew". La primera fase pide resultados interactivos sin respuesta escrita, y la segunda entrega la cadena completa de compromiso: usuario invitado, cuenta de administrador y la flag final que firma el golpe del grupo.

> **EN:** Insane-difficulty CTF room themed around the hacker crew "Crocc Crew". The first phase asks for interactive results with no written answer, and the second delivers the full compromise chain: guest user, administrator account, and the final flag that seals the crew's strike.

## Solucionario

### Task 1: Respuestas del laboratorio / Lab answers

**Explicación:**
Lista completa de respuestas de la sala tal como se recoge en la nota original, sin modificar:

1. 1. No answer needed
   2. No answer needed
   3. No answer needed
   4. No answer needed
   5. No answer needed
2. 1. THM{Gu3st_Pl3as3}
   2. admcrocccrew
   3. THM{0n-Y0ur-Way-t0-DA}
   4. THM{Wh4t-t0-d0...Wh4t-t0-d0}
   5. THM{Cr0ccCrewStr1kes!}

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | 1.1 | `No answer needed` |
| 2 | 1.2 | `No answer needed` |
| 3 | 1.3 | `No answer needed` |
| 4 | 1.4 | `No answer needed` |
| 5 | 1.5 | `No answer needed` |
| 6 | 2.1 | `THM{Gu3st_Pl3as3}` |
| 7 | 2.2 | `admcrocccrew` |
| 8 | 2.3 | `THM{0n-Y0ur-Way-t0-DA}` |
| 9 | 2.4 | `THM{Wh4t-t0-d0...Wh4t-t0-d0}` |
| 10 | 2.5 | `THM{Cr0ccCrewStr1kes!}` |

---

**Metodología:**
1. **Fase de reconocimiento:** completar los pasos interactivos iniciales del laboratorio (sin respuesta escrita).
2. **Acceso inicial:** obtener el acceso como invitado y recoger la primera flag (`THM{Gu3st_Pl3as3}`).
3. **Escalada de acceso:** validar la cuenta interna `admcrocccrew` para ganar superficie como administrador.
4. **Compromiso final:** seguir la cadena hasta la flag definitiva del grupo.

### Cadena de ataque / Attack Chain

1. Pasos interactivos iniciales (sin respuesta).
2. Acceso invitado → `THM{Gu3st_Pl3as3}`.
3. Cuenta `admcrocccrew` → camino a administrador.
4. Flags 2.3 → 2.4 → `THM{Cr0ccCrewStr1kes!}`.

**Learning chain:** invitado → `admcrocccrew` → administrador → cadena de flags → flag final del grupo.

**Lección:** *En los CTF de acceso inicial conviene registrar cada flag intermedia aunque parezca trivial: es la única forma de reconstruir una cadena de compromiso y no perder pistas en el camino.*

**MITRE ATT&CK:** N/A (CTF interactivo sin infraestructura ofensiva documentada)

**Fuente:** [TryHackMe - Crocc Crew](https://tryhackme.com/room/crocccrew)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.