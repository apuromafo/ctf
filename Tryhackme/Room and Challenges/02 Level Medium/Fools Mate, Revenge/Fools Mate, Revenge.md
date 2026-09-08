# Fools Mate, Revenge

| **Dificultad** | MEDIUM | **Tipo** | CTF | **Slug** | `foolsm8v2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/foolsm8v2) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Prototype Pollution / Web Exploitation / Node.js | **Impacto** | Evalúa la capacidad de explotar merge descontrolados en APIs JSON para manipular el estado de la aplicación |

---

**Contexto:** Secuela de "Fools Mate": ahora el servidor sí valida, pero el endpoint de configuración hace un merge shallow del JSON del cliente que es explotable por **prototype pollution**. Al "envenenar" el prototipo de `Object` con `unlocked: true` se abre la puerta del reward gate y se puede completar el mate para obtener la flag. Chess app at `http://MACHINE_IP:3000`. Playing `Ra8` the server answers with `locked: "Checkmate! No reward for you."` and `"reason":"reward gate closed: session.config.unlocked is not set"`. Enumerating the endpoints (`/api/state`, `/api/move`, `/api/reset`, `/api/settings`) shows that `/api/settings` does a recursive merge of the client JSON. Trying `{"unlocked":true}` and `{"config":{"unlocked":true}}` are ignored by a whitelist, and `__proto__` is filtered. The path is **prototype pollution** by sending `{"constructor":{"prototype":{"unlocked":true}}}` (or the flat variant `{"constructor":{"prototype":{"config":true}}}`). After `POST /api/reset` to regenerate the config, `POST /api/move {"from":"a1","to":"a8"}` passes the gate and returns the flag.

## Solucionario

### Task 1: play

**Explicación:** App de ajedrez en `http://MACHINE_IP:3000`. Al jugar `Ra8` el servidor responde con `locked: "Checkmate! No reward for you."` y `"reason":"reward gate closed: session.config.unlocked is not set"`. Enumerando los endpoints (`/api/state`, `/api/move`, `/api/reset`, `/api/settings`) se ve que `/api/settings` hace un merge recursivo del JSON del cliente. Intenta forzar `{"unlocked":true}` y `{"config":{"unlocked":true}}` son ignorados por una whitelist, y `__proto__` está filtrado. La vía es **prototype pollution** enviando `{"constructor":{"prototype":{"unlocked":true}}}` (o la variante plana `{"constructor":{"prototype":{"config":true}}}`). Tras `POST /api/reset` para regenerar la config, `POST /api/move {"from":"a1","to":"a8"}` pasa el gate y devuelve la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{pr0t0_p0lluted_th3_r3f3r33}` |

---

**Metodología:**
1. Se abre `http://MACHINE_IP:3000` y se juega `Ra8`; el servidor responde `locked: "Checkmate! No reward for you."` con `"reason":"reward gate closed: session.config.unlocked is not set"`.
2. Se prueban `/api/state`, `/api/move`, `/api/reset` y `/api/settings`. `/api/settings` hace un merge recursivo del JSON enviado por el cliente contra la config.
3. `{"unlocked":true}` y `{"config":{"unlocked":true}}` se ignoran por whitelist; la clave `__proto__` está filtrada por el merge.
4. Se envía `POST /api/settings` con `{"constructor":{"prototype":{"unlocked":true}}}` (o `{"constructor":{"prototype":{"config":true}}}`), "envenenando" `Object.prototype.unlocked = true` de forma que la config regenerada hereda `unlocked: true`.
5. `POST /api/reset` fuerza la regeneración de la config desde el prototipo contaminado.
6. `POST /api/move {"from":"a1","to":"a8"}`; el gate pasa y se devuelve la flag.

**Learning chain:** Reconocimiento → Enumeración de endpoints → Whitelist y filtros → Prototype pollution → Regenerar config → Flag

**Lección:** *La prototype pollution (CWE-1321) nace de merges descontrolados; el fix es validar con `Object.hasOwn()`, filtrar claves `__proto__`/`constructor`/`prototype` y congelar objetos compartidos.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; CWE-1321 - Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')

**Fuente:** [TryHackMe - Fools Mate, Revenge](https://tryhackme.com/room/foolsm8v2)