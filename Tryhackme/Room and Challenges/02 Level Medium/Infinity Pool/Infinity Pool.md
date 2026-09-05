# Infinity Pool [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-infinitypool-5b3548af`
* **Link:** https://tryhackme.com/room/hh-infinitypool-5b3548af
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-infinitypool-5b3548af` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium tipo **Linux / PrivEsc** sobre una VM. El tema "no visible edge" (borde no visible del hotel) orienta a servicios escuchando en puertos no estándar y a binarios con capabilities: enumeración web → shell inicial como usuario → escalada de privilegios (capabilities posix, PATH hijack o sudo) → flag root.
> **EN:** Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty, **Linux / PrivEsc** over a VM. The "no visible edge" theme points to services listening on non-standard ports and to binaries with capabilities: web enumeration → initial shell as user → privilege escalation (posix capabilities, PATH hijack or sudo) → root flag.

### Task 1 - Infinity Pool

> **ES:** Tras la enumeration web se explota una superficie de entrada (LFI/RCE limitada) que entrega una shell inicial como usuario; ahí se lee la **user flag**. Para la escalada se revisan binarios con capabilities posix (p. ej. lectura arbitraria de archivos) o `sudo -l`/PATH hijack; con ello se lee la **root flag**. 2 preguntas.
> **EN:** After web enumeration an entry surface (limited LFI/RCE) is exploited to get an initial shell as a user, where the **user flag** is read. For escalation, binaries with posix capabilities (e.g. arbitrary file read) or `sudo -l`/PATH hijack are reviewed; with that the **root flag** is read. 2 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user flag? | `THM{n0_v1s1bl3_3dg3}` |
| What is the root flag? | `THM{tr4c3d_t0_th3_h0r1z0n}` |

## Metodología / Methodology

1. **Paso / Step - Enumeración:** `nmap -sV -p-` y fuzzing web sobre el target; el tema "no visible edge" sugiere descubrir servicios escuchando en puertos altos/no estándar.
2. **Paso / Step - Acceso inicial:** Se explota una entrada web (LFI que escala a RCE limitada) y se obtiene una shell inicial como usuario no privilegiado.
3. **Paso / Step - User flag:** En el directorio del usuario se lee `THM{n0_v1s1bl3_3dg3}`.
4. **Paso / Step - PrivEsc:** Se revisan binarios con capabilities posix (p. ej. `cap_dac_read_search`) y `sudo -l`; se abusa de una capability o de un PATH hijack/script con sudo para leer archivos de root.
5. **Paso / Step - Root flag:** Con acceso root se lee `THM{tr4c3d_t0_th3_h0r1z0n}`.

### Cadena de ataque / Attack Chain

```
web (puertos no estándar, "no visible edge")
  -> LFI/RCE limitada -> shell inicial como usuario
  -> user flag                    -> THM{n0_v1s1bl3_3dg3}
  -> enumeration -> binary con capabilities / sudo -l / PATH hijack
  -> privEsc -> root
  -> root flag                    -> THM{tr4c3d_t0_th3_h0r1z0n}
```

**Lección:** Revisar las capabilities de binarios (posix) y los servicios que escuchan en puertos altos: lo "invisible" desde una enumeración superficial suele ser la superficie real de ataque y de escalada.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.