# Grand Larceny Auto II

| **Dificultad** | MEDIUM | **Tipo** | CTF | **Slug** | `grandlarcenyautoii` |
| **Link** | [TryHackMe](https://tryhackme.com/room/grandlarcenyautoii) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Game Hacking / Godot Mono / HMAC / GDRE Tools / API Authentication Bypass | **Impacto** | Evalúa cómo analizar el cliente de un juego y explotar firmas HMAC incompletas para reclamar la flag real |

---

**Contexto:** Sala de **game hacking de backend** (Linux, **Godot Mono**) de dificultad Media, secuela de Grand Larceny Auto. El cliente guarda la lógica de progreso/flag en un servidor: hay que extraer el proyecto del `.pck` con **GDRE Tools**, leer `PoPClient.cs` para recuperar los endpoints y entender el esquema de sesión/HMAC, y explotar el hecho de que **la firma del `/claim` NO cubre el campo `role`**: cambiando `role=player` → staff sobre una firma válida se reclama la flag real de la "staff vault". **Backend game hacking** room (Linux, **Godot Mono**) of Medium difficulty, sequel to Grand Larceny Auto. The client keeps the progress/flag logic on a server: extract the project from the `.pck` with **GDRE Tools**, read `PoPClient.cs` to recover the endpoints and understand the session/HMAC scheme, and exploit the fact that **the `/claim` signature does NOT cover the `role` field**: flipping `role=player` → staff on a valid signature claims the real flag from the "staff vault".

## Solucionario

### Task 1: Setup

**Explicación:** Preparación: añadir la máquina al `/etc/hosts` como `gla2.thm` (`<MACHINE_IP> gla2.thm`) ya que el cliente del juego apunta al hostname `gla2.thm`. 1 pregunta de confirmación: se responde con el enunciado de confirmación. Setup: add the machine to `/etc/hosts` as `gla2.thm` (`<MACHINE_IP> gla2.thm`) since the game client targets the hostname `gla2.thm`. 1 confirmation question: answered with the confirmation statement.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I'm ready for the challenge! | `I'm ready for the challenge!` |

### Task 2: Challenge

**Explicación:** 2ª tarea: obtener la flag real. Al completar la cadena de checkpoints y reclamar como `player`, el server responde con la flag **falsa/decoys** `THM{n1c3_dr1v1ng_but_th4ts_th3_wr0ng_v4ult}` ("civilian access — the real vault is staff-only"). La flag REAL no está publicada literalmente: se obtiene reutilizando una claim válida con `role=staff`. 2nd task: obtain the real flag. Completing the checkpoint chain and claiming as `player` returns the **fake/decoy** flag `THM{n1c3_dr1v1ng_but_th4ts_th3_wr0ng_v4ult}` ("civilian access — the real vault is staff-only"). The REAL flag is not published literally: it is obtained by reusing a valid claim with `role=staff`.

Nota: La flag real no está publicada por los walkthroughs (solo confirman la falsa `THM{n1c3_dr1v1ng_but_th4ts_th3_wr0ng_v4ult}`); se documenta el método con el que se reclama (replay del HMAC con `role=staff`), no el literal. English: The real flag is not published by walkthroughs (only the fake `THM{n1c3_dr1v1ng_but_th4ts_th3_wr0ng_v4ult}` is confirmed); the method to claim it (HMAC replay with `role=staff`) is documented, not the literal.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{...redacted...}` |

---

**Metodología:**
1. Extraer el proyecto del `.pck` con **GDRE Tools** (Godot RE: script decompilation) → se obtienen scripts C# de `Godot Mono` (PoPClient, etc.) con la lógica del cliente.
2. `PoPClient.cs` apunta al backend **`http://gla2.thm`** y define los endpoints: `POST /session`, `POST /checkpoint` y `POST /claim`.
3. `POST /session` devuelve `session_id`, `token` y `stash_order`; el `stash_order` lo controla el servidor. Autenticación por **HMAC-SHA256** con mensaje `session_id|step|token`, y el `token` rota en cada checkpoint (firmado por el server).
4. La secuencia de pasos del `stash_order` es `heat5 → stash2 → stash1 → stash0 → vault`. Enviar cada checkpoint correcto con su firma para avanzar en el progreso.
5. `POST /claim` como `role=player` devuelve la flag falsa `THM{n1c3_dr1v1ng_but_th4ts_th3_wr0ng_v4ult}` (solo funciona tras completar el stash_order).
6. Analizando `DeriveStaffRole()`, el rol staff se deriva por **SHA-1** del `stash_order`. Lo crítico: la firma HMAC de `/claim` cubre **SOLO** `session_id|claim|token` — el campo **`role` NO está dentro del mensaje firmado**.
7. Reutilizar una petición de claim válida (misma `sig`) cambiando únicamente `role` de `player` a `staff` sin tocar la firma → el server acepta la firma y la claim se procesa con rol staff.
8. La claim `role=staff` responde con la flag de la "staff vault" → flag real.

**Learning chain:** GrandLarcenyAutoII .pck (Godot Mono) → GDRE Tools → PoPClient.cs → backend http://gla2.thm → POST /session → HMAC-SHA256 session_id|step|token → cadena de checkpoints heat5 → stash2 → stash1 → stash0 → vault → POST /claim role=player (flag falsa) → DeriveStaffRole() SHA-1 → fallo: role NO firmado → replay con role=staff → flag real

**Lección:** *Si un campo de autorización (`role`) cae **fuera** del material firmado (HMAC), el atacante lo muta libremente reutilizando una firma válida: el "vault real" era simplemente un campo que el servidor nunca pensó en firmar. Siempre hay que firmar TODO lo que afecta a la decisión de autorización.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1557 - Adversary-in-the-Middle; CWE-347 - Improper Verification of Cryptographic Signature

**Fuente:** [TryHackMe - Grand Larceny Auto II](https://tryhackme.com/room/grandlarcenyautoii)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
