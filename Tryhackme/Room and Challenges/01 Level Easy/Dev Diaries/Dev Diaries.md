# Dev Diaries [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF
* **Slug:** `devdiaries`
* **Link:** https://tryhackme.com/room/devdiaries
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=devdiaries` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT sobre infraestructura web y control de versiones. Se descubren subdominios vía certificados (crt.sh), se rastrea al desarrollador hasta GitHub y se usan los `.patch` y el historial de commits para filtrar su email, su motivación para retirar el código y una flag oculta en un diff.
> **EN:** OSINT room about web infrastructure and version control. Subdomains are discovered via certificates (crt.sh), the developer is traced to GitHub and the `.patch` files and commit history are used to leak his email, his reason for removing the code and a hidden flag in a diff.

### Task 1 - Dev tunes

> **ES:** `marvenly.com` no responde. Consultando crt.sh por `%.marvenly.com` se listan subdominios, incluido `uat-testing.marvenly.com`. Al abrir el subdominio dev, el footer del HTML firma con el usuario `notvibecoder23`. En GitHub existe el usuario `notvibecoder23` con el repo `marvenly_site` (4 commits); el `.patch` de un commit revela el email del autor `freelancedevbycoder23@gmail.com`. El historial de commits incluye el mensaje de abandono ("The project was marked as abandoned due to a payment dispute") y un commit "Removed my signature" cuyo diff aún contiene un comentario HTML oculto con la flag. 5 preguntas.
> **EN:** `marvenly.com` does not respond. Querying crt.sh for `%.marvenly.com` lists subdomains, including `uat-testing.marvenly.com`. Opening the dev subdomain, the HTML footer is signed with the user `notvibecoder23`. On GitHub there is the user `notvibecoder23` with the repo `marvenly_site` (4 commits); a commit `.patch` reveals the author email `freelancedevbycoder23@gmail.com`. The commit history includes the abandonment message ("The project was marked as abandoned due to a payment dispute") and a commit "Removed my signature" whose diff still contains a hidden HTML comment with the flag. 5 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the subdomain where the development version of the website is hosted? | `uat-testing.marvenly.com` |
| What is the GitHub username of the developer? | `notvibecoder23` |
| What is the developer's email address? | `freelancedevbycoder23@gmail.com` |
| What reason did the developer mention in the commit history for removing the source code? | `The project was marked as abandoned due to a payment dispute` |
| What is the value of the hidden flag? | `THM{g1t_h1st0ry_n3v3r_f0rg3ts}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `marvenly.com` no resuelve/responda; se pasa a enumeración pasiva de subdominios.
2. **Paso / Step - crt.sh:** Consultar `%.marvenly.com` en crt.sh → aparece `uat-testing.marvenly.com` (subdominio de desarrollo).
3. **Paso / Step - Fingerprint del dev:** El HTML del subdominio UAT firma en el footer con `notvibecoder23`.
4. **Paso / Step - GitHub:** Usuario `notvibecoder23` → repo `marvenly_site` (4 commits); un `.patch` revela el email `freelancedevbycoder23@gmail.com`.
5. **Paso / Step - Historial de commits:** El mensaje de abandono ("The project was marked as abandoned due to a payment dispute") y el commit "Removed my signature".
6. **Paso / Step - Diff:** El diff del commit de la "signature" aún guarda un comentario HTML oculto con la flag.

### Cadena de ataque / Attack Chain

```
marvenly.com (caído)
  -> crt.sh %.marvenly.com -> subdominios
  -> uat-testing.marvenly.com (versión dev)
  -> HTML subdominio -> footer -> firma notvibecoder23
  -> GitHub notvibecoder23 / repo marvenly_site (4 commits)
  -> .patch del commit -> email freelancedevbycoder23@gmail.com
  -> historial -> "abandoned due to a payment dispute" + commit "Removed my signature"
  -> diff -> comentario HTML oculto -> flag
  -> THM{g1t_h1st0ry_n3v3r_f0rg3ts}
```

**Lección:** El historial de Git nunca olvida: ni los emails (en los `.patch`) ni las flags escondidas en los diffs de commits "eliminados".

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
