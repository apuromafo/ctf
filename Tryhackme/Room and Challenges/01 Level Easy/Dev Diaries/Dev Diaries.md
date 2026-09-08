# Dev Diaries

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `devdiaries` |
| **Link** | [TryHackMe](https://tryhackme.com/room/devdiaries) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=devdiaries` + websearch de walkthroughs) |
| **Componentes** | OSINT / crt.sh / certificados / GitHub / .patch / historial de commits / subdominios |
| **Impacto** | Filtra email, motivación y una flag oculta en un diff rastreando a un desarrollador desde los certificados y el historial de commits de su repositorio. |

---

**Contexto:** Sala de OSINT sobre infraestructura web y control de versiones. Se descubren subdominios vía certificados (crt.sh), se rastrea al desarrollador hasta GitHub y se usan los `.patch` y el historial de commits para filtrar su email, su motivación para retirar el código y una flag oculta en un diff.

## Solucionario

### Task 1: Dev tunes

**Explicación:** `marvenly.com` no responde. Consultando crt.sh por `%.marvenly.com` se listan subdominios, incluido `uat-testing.marvenly.com`. Al abrir el subdominio dev, el footer del HTML firma con el usuario `notvibecoder23`. En GitHub existe el usuario `notvibecoder23` con el repo `marvenly_site` (4 commits); el `.patch` de un commit revela el email del autor `freelancedevbycoder23@gmail.com`. El historial de commits incluye el mensaje de abandono ("The project was marked as abandoned due to a payment dispute") y un commit "Removed my signature" cuyo diff aún contiene un comentario HTML oculto con la flag. 5 preguntas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the subdomain where the development version of the website is hosted? | `uat-testing.marvenly.com` |
| 2 | What is the GitHub username of the developer? | `notvibecoder23` |
| 3 | What is the developer's email address? | `freelancedevbycoder23@gmail.com` |
| 4 | What reason did the developer mention in the commit history for removing the source code? | `The project was marked as abandoned due to a payment dispute` |
| 5 | What is the value of the hidden flag? | `THM{g1t_h1st0ry_n3v3r_f0rg3ts}` |

---

**Metodología:**
1. **Reconocimiento:** `marvenly.com` no resuelve/responda; se pasa a enumeración pasiva de subdominios.
2. **crt.sh:** consultar `%.marvenly.com` en crt.sh → aparece `uat-testing.marvenly.com` (subdominio de desarrollo).
3. **Fingerprint del dev:** el HTML del subdominio UAT firma en el footer con el usuario `notvibecoder23`.
4. **GitHub:** usuario `notvibecoder23` → repo `marvenly_site` (4 commits); un `.patch` de un commit revela el email del autor `freelancedevbycoder23@gmail.com`.
5. **Historial de commits:** el mensaje de abandono ("The project was marked as abandoned due to a payment dispute") y el commit "Removed my signature".
6. **Diff:** el diff del commit de la "signature" aún guarda un comentario HTML oculto con la flag `THM{g1t_h1st0ry_n3v3r_f0rg3ts}`.

**Learning chain:** marvenly.com (caído) → crt.sh %.marvenly.com → subdominios → uat-testing.marvenly.com (versión dev) → HTML subdominio → footer → firma notvibecoder23 → GitHub notvibecoder23 / repo marvenly_site (4 commits) → .patch del commit → email freelancedevbycoder23@gmail.com → historial → "abandoned due to a payment dispute" + "Removed my signature" → diff → comentario HTML oculto → flag.

**Lección:** El historial de Git nunca olvida: ni los emails (en los `.patch`) ni las flags escondidas en los diffs de commits "eliminados".

**MITRE ATT&CK:** T1596 (Search Open Technical Databases), T1593.001 (Search Open Websites/Domains: Social Engineering), T1589 (Gather Victim Identity Information).

**Fuente:** [TryHackMe - Dev Diaries](https://tryhackme.com/room/devdiaries)