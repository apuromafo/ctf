# Room 404

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `hh-room404-804573bf` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-room404-804573bf) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=hh-room404-804573bf` + websearch de walkthroughs) |
| **Componentes** | nmap / git-dumper / .git directory / git show / payloads tooling |
| **Impacto** | Recuperar una flag eliminada explotando un repositorio `.git/` expuesto y su historial de commits |

---

**Contexto:** Sala Web/Linux (VM) del evento Hacker Holidays. El servidor web expone el directorio `.git/` de un repositorio de la "Room 404" del hotel. Se vuelcan los objetos con un dumper de repositorios (git-dumper / herramientas de payloads) o leyendo directamente `.git/logs/HEAD`; en el historial de commits, un commit antiguo (con mensaje tipo "oops" / "flag") retiene la flag que se creía borrada.

## Solucionario

### Task 1: Room 404

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{byt3_l0tus_n3v3r_f0rg3ts}` |

---

**Metodología:**
1. **Reconocimiento:** con `nmap` se identifican los puertos abiertos y el servicio web del hotel.
2. **Descubrimiento del `.git`:** en el servidor web se detecta un repositorio `.git/` expuesto (directorio sin protección de servidor).
3. **Volcado del repositorio:** con un dumper de repositorios (git-dumper) o herramientas de payloads se descarga todo el historial; como alternativa se lee `.git/logs/HEAD` para listar los commits y se ejecuta `git show <commit>` para inspeccionarlos.
4. **Inspección del historial:** se recorren los commits; en un commit antiguo (mensaje tipo "oops" / "flag") se encuentra la flag completa: `THM{byt3_l0tus_n3v3r_f0rg3ts}`.

**Learning chain:** nmap → puertos web → `/.git/` expuesto en el servidor → git-dumper / volcado del repo (o `.git/logs/HEAD`) → recorrido de commits → `git show <commit>` → commit antiguo ("oops" / "flag") → THM{byt3_l0tus_n3v3r_f0rg3ts}

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1552 (Unsecured Credentials)

**Fuente:** [TryHackMe - Room 404](https://tryhackme.com/room/hh-room404-804573bf)