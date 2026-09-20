# Frosteau Busy with Vim

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `busyvimfrosteau` | [TryHackMe](https://tryhackme.com/room/busyvimfrosteau) | 04 Level Insane | TryHackMe | vim / hosting / rutas / escalada de privilegios | Recorrido por un laboratorio estilo "busy" de Frosteau: flags encadenadas sobre rutas y raíces, finalizando con una cadena hash dedicada a la fase final. |

---

**Contexto:** Sala CTF de nivel Insane centrada en un reto estilo "Busy Box" de Frosteau. Las flags avanzan por fases: comienzo del juego, escalado de actividad, distinción de raíces y rutas, y una valoración final de Frosteau; la última respuesta es una cadena con prefijo numérico y hash largo.

> **ES:** Sala CTF de nivel Insane centrada en un reto estilo "Busy Box" de Frosteau. Las flags avanzan por fases: comienzo del juego, escalado de actividad, distinción de raíces y rutas, y una valoración final de Frosteau; la última respuesta es una cadena con prefijo numérico y hash largo.

> **EN:** Insane-difficulty CTF room centered on a Frosteau "Busy Box"-style challenge. Flags progress through phases: beginning of the game, activity ramp-up, roots versus routes distinction, and a final evaluation by Frosteau; the last answer is a string with a numeric prefix and a long hash.

## Solucionario

### Task 1: Respuestas del laboratorio / Lab answers

**Explicación:**
Lista completa de respuestas de la sala tal como se recoge en la nota original, sin modificar:

1. 1. THM{Let.the.game.begin}
   2. THM{Seems.like.we.are.getting.busy}
   3. THM{Not.all.roots.and.routes.are.equal}
   4. THM{Frosteau.would.be.both.proud.and.disappointed}
   5. 3-d2dc6a02db03401177f0511a6c99007e945d9cb9b96b8c6294f8c5a2c8e01f60

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | 1.1 | `THM{Let.the.game.begin}` |
| 2 | 1.2 | `THM{Seems.like.we.are.getting.busy}` |
| 3 | 1.3 | `THM{Not.all.roots.and.routes.are.equal}` |
| 4 | 1.4 | `THM{Frosteau.would.be.both.proud.and.disappointed}` |
| 5 | 1.5 | `3-d2dc6a02db03401177f0511a6c99007e945d9cb9b96b8c6294f8c5a2c8e01f60` |

---

**Metodología:**
1. **Fase inicial:** preparar el entorno ("let the game begin") y avanzar hasta activar el ritmo creciente del reto.
2. **Distinción raíz/ruta:** identificar para cada fase si se opera sobre la raíz (`/`) o sobre rutas concretas.
3. **Valoración final:** cumplir la condición buscada por Frosteau y registrar la cadena de cierre con su hash.

### Cadena de ataque / Attack Chain

1. Comienzo → `THM{Let.the.game.begin}`.
2. Actividad creciente → `THM{Seems.like.we.are.getting.busy}`.
3. Juego de raíces y rutas → `THM{Not.all.roots.and.routes.are.equal}`.
4. Condición de Frosteau → `THM{Frosteau.would.be.both.proud.and.disappointed}`.
5. Cierre → `3-d2dc6a02db03401177f0511a6c99007e945d9cb9b96b8c6294f8c5a2c8e01f60`.

**Learning chain:** inicio → busy → raíces vs rutas → valoración de Frosteau → cadena-hash final.

**Lección:** *En los retos de tipo "busy box" el detalle del enunciado es la llave: distinguir cuándo una acción afecta a la raíz y cuándo a una ruta concreta determina qué flag aparece y cuál no.*

**MITRE ATT&CK:** N/A (CTF interactivo sin infraestructura ofensiva documentada)

**Fuente:** [TryHackMe - Frosteau Busy with Vim](https://tryhackme.com/room/busyvimfrosteau)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.