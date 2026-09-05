# Cache Me Outside [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF
* **Slug:** `cachemeoutside`
* **Link:** https://tryhackme.com/room/cachemeoutside
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=cachemeoutside` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT activo. A partir de una captura de pantalla de una conversación, se rastrea la huella digital de un hacker retirado saltando entre plataformas: perfil deportivo, repositorio de GitHub, un email expuesto y redes sociales, hasta reconstruir su identidad, ubicación y un desplazamiento concreto en el transporte público de Timișoara.
> **EN:** Active OSINT room. Starting from a screenshot of a conversation, the digital footprint of a retired hacker is traced by hopping between platforms: an activity profile, a GitHub repository, an exposed email and social media, until reconstructing his identity, location and a specific public-transport trip in Timișoara.

### Task 1 - Challenge Questions

> **ES:** Se parte de un screenshot de una conversación de solo lectura. Siguiendo al usuario se llega a su perfil de Komoot (`komoot.com/user/5667624959835`) cuya bio es "Jim Lee" y enlaza a un GitHub (`jiml33t`, repo homónimo). Un commit `.patch` revela el email del autor; escribirle provoca un auto-responder ("preparing for a marathon...") que filtra el teléfono. Buscando `jiml33t` se halla su Instagram/Threads con un post del 7-may-2026 con foto de un cartel `irigatii.ro` (Calea Buziașului, Timișoara); con Google Lens y las coordenadas de a pie se ubica la parada de tranvía cerca del supermercado Auchan: Piața Gheorghe Domășneanu. 5 preguntas.
> **EN:** It starts from a read-only screenshot of a conversation. Following the user leads to his Komoot profile (`komoot.com/user/5667624959835`) whose bio is "Jim Lee" and links a GitHub (`jiml33t`, homonymous repo). A commit `.patch` reveals the author email; emailing him triggers an auto-responder ("preparing for a marathon...") that leaks the phone. Searching `jiml33t` finds his Instagram/Threads with a 7-May-2026 post featuring a photo of an `irigatii.ro` sign (Calea Buziașului, Timișoara); using Google Lens and walking coordinates the tram stop near the Auchan supermarket is located: Piața Gheorghe Domășneanu. 5 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the retired hacker's full name? | `Jim Lee` |
| What email address did he accidentally expose? | `jimleepro1@gmail.com` |
| What is his phone number? | `+40 743 321 239` |
| In which city is he located? | `Timișoara` |
| Submit the name of the tram station where he got off on the 7th of May, 2026. | `Piața Gheorghe Domășneanu` |

## Metodología / Methodology

1. **Paso / Step - Fuente inicial:** Se examina el screenshot de la conversación (solo lectura) para identificar al objetivo.
2. **Paso / Step - Perfil deportivo:** Se localiza el perfil de Komoot (`komoot.com/user/5667624959835`); la bio dice "Jim Lee" y enlaza un GitHub.
3. **Paso / Step - GitHub:** Repo `jiml33t`; un archivo `.patch` de un commit expone el email del autor `jimleepro1@gmail.com`.
4. **Paso / Step - Auto-responder:** Enviar un email al objetivo dispara un auto-responder ("preparing for a marathon...") que revela el teléfono `+40 743 321 239`.
5. **Paso / Step - Redes sociales:** Buscar `jiml33t` lleva a Instagram/Threads; un post del 7-may-2026 muestra una foto con un cartel `irigatii.ro` (Calea Buziașului, Timișoara).
6. **Paso / Step - Geolocalización:** Con Google Lens sobre la foto y los datos de a pie, la parada de tranvía está cerca del supermercado Auchan (francés): Piața Gheorghe Domășneanu.

### Cadena de ataque / Attack Chain

```
screenshot (conversación)
  -> Komoot (komoot.com/user/5667624959835) -> bio "Jim Lee"
  -> GitHub jiml33t / repo jiml33t
  -> .patch del commit -> email autor jimleepro1@gmail.com
  -> enviar email -> auto-responder -> teléfono +40 743 321 239
  -> buscar jiml33t -> Instagram/Threads
  -> post 7-may-2026 -> cartel irigatii.ro (Calea Buziașului, Timișoara)
  -> Google Lens -> tram stop cerca del Auchan
  -> Piața Gheorghe Domășneanu
```

**Lección:** Un solo perfil conecta (cross-platform futaging) el anonimato entre plataformas; además, los `.patch` de commits filtran el email del autor y los auto-responders pueden exfiltrar el teléfono.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
