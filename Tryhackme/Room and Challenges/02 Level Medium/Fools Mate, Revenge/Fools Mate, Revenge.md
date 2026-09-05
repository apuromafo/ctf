# Fools Mate, Revenge [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF
* **Slug:** `foolsm8v2`
* **Link:** https://tryhackme.com/room/foolsm8v2
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=foolsm8v2` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Secuela de "Fools Mate": ahora el servidor sí valida, pero el endpoint de configuración hace un merge shallow del JSON del cliente que es explotable por **prototype pollution**. Al "envenenar" el prototipo de `Object` con `unlocked: true` se abre la puerta del reward gate y se puede completar el mate para obtener la flag.
> **EN:** Sequel to "Fools Mate": now the server does validate, but the settings endpoint does a shallow merge of the client JSON that is exploitable via **prototype pollution**. By "poisoning" `Object.prototype` with `unlocked: true` the reward gate opens and the checkmate can be completed to get the flag.

### Task 1 - play

> **ES:** App de ajedrez en `http://MACHINE_IP:3000`. Al jugar `Ra8` el servidor responde con `locked: "Checkmate! No reward for you."` y `"reason":"reward gate closed: session.config.unlocked is not set"`. Enumerando los endpoints (`/api/state`, `/api/move`, `/api/reset`, `/api/settings`) se ve que `/api/settings` hace un merge recursivo del JSON del cliente. Intenta forzar `{"unlocked":true}` y `{"config":{"unlocked":true}}` son ignorados por una whitelist, y `__proto__` está filtrado. La vía es **prototype pollution** enviando `{"constructor":{"prototype":{"unlocked":true}}}` (o la variante plana `{"constructor":{"prototype":{"config":true}}}`). Tras `POST /api/reset` para regenerar la config, `POST /api/move {"from":"a1","to":"a8"}` pasa el gate y devuelve la flag.
> **EN:** Chess app at `http://MACHINE_IP:3000`. Playing `Ra8` the server answers with `locked: "Checkmate! No reward for you."` and `"reason":"reward gate closed: session.config.unlocked is not set"`. Enumerating the endpoints (`/api/state`, `/api/move`, `/api/reset`, `/api/settings`) shows that `/api/settings` does a recursive merge of the client JSON. Trying `{"unlocked":true}` and `{"config":{"unlocked":true}}` are ignored by a whitelist, and `__proto__` is filtered. The path is **prototype pollution** by sending `{"constructor":{"prototype":{"unlocked":true}}}` (or the flat variant `{"constructor":{"prototype":{"config":true}}}`). After `POST /api/reset` to regenerate the config, `POST /api/move {"from":"a1","to":"a8"}` passes the gate and returns the flag.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{pr0t0_p0lluted_th3_r3f3r33}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Se abre `http://MACHINE_IP:3000` y se juega `Ra8`; el servidor responde `locked: "Checkmate! No reward for you."` con `"reason":"reward gate closed: session.config.unlocked is not set"`.
2. **Paso / Step - Enumeración de endpoints:** Se prueban `/api/state`, `/api/move`, `/api/reset` y `/api/settings`. `/api/settings` hace un merge recursivo del JSON enviado por el cliente contra la config.
3. **Paso / Step - Whitelist y filtros:** `{"unlocked":true}` y `{"config":{"unlocked":true}}` se ignoran por whitelist; la clave `__proto__` está filtrada por el merge.
4. **Paso / Step - Prototype pollution:** Se envía `POST /api/settings` con `{"constructor":{"prototype":{"unlocked":true}}}` (o `{"constructor":{"prototype":{"config":true}}}`), "envenenando" `Object.prototype.unlocked = true` de forma que la config regenerada hereda `unlocked: true`.
5. **Paso / Step - Regenerar config:** `POST /api/reset` fuerza la regeneración de la config desde el prototipo contaminado.
6. **Paso / Step - Flag:** `POST /api/move {"from":"a1","to":"a8"}`; el gate pasa y se devuelve la flag.

### Cadena de ataque / Attack Chain

```
http://MACHINE_IP:3000 (ajedrez web)
  -> jugar Ra8 -> locked: "reward gate closed: session.config.unlocked is not set"
  -> enumerar /api/state /api/move /api/reset /api/settings
  -> /api/settings hace merge shallow del JSON del cliente
  -> prototype pollution POST {"constructor":{"prototype":{"unlocked":true}}}
  -> POST /api/reset (regenera config con unlocked:true heredado)
  -> POST /api/move {"from":"a1","to":"a8"} -> gate abierto -> flag
  -> THM{pr0t0_p0lluted_th3_r3f3r33}
```

**Lección:** La prototype pollution (CWE-1321) nace de merges descontrolados; el fix es validar con `Object.hasOwn()`, filtrar claves `__proto__`/`constructor`/`prototype` y congelar objetos compartidos.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
