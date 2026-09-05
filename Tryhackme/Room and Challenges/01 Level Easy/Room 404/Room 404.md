# Room 404 [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-room404-804573bf`
* **Link:** https://tryhackme.com/room/hh-room404-804573bf
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-room404-804573bf` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala Web/Linux (VM) del evento Hacker Holidays. El servidor web expone el directorio `.git/` de un repositorio de la "Room 404" del hotel. Se vuelcan los objetos con un dumper de repositorios (git-dumper / herramientas de payloads) o leyendo directamente `.git/logs/HEAD`; en el historial de commits, un commit antiguo (con mensaje tipo "oops" / "flag") retiene la flag que se creía borrada.
> **EN:** Web/Linux room (VM) from the Hacker Holidays event. The web server exposes the `.git/` directory of a repository of the hotel's "Room 404". Dump the objects with a repository dumper (git-dumper / payloads tooling) or by reading `.git/logs/HEAD` directly; in the commit history, an old commit (with a message like "oops" / "flag") keeps a flag believed to have been deleted.

### Task 1 - Room 404

> **ES:** Tras descubrir los puertos web, se detecta un repositorio `.git/` expuesto en el servidor. Con un volcador de repositorios (git-dumper) o herramientas de payload se descarga todo el historial; alternativamente, se lee `.git/logs/HEAD` para listar los commits y se ejecuta `git show <commit>` para inspeccionarlos. En un commit antiguo (mensaje tipo "oops" / "flag") se encuentra la flag completa.
> **EN:** After discovering the web ports, an exposed `.git/` repository is found on the server. Dump the full history with a repository dumper (git-dumper) or payloads tooling; alternatively, read `.git/logs/HEAD` to list the commits and run `git show <commit>` to inspect them. In an old commit (message like "oops" / "flag") the full flag is found.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{byt3_l0tus_n3v3r_f0rg3ts}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Con `nmap` se identifican los puertos abiertos y el servicio web del hotel.
2. **Paso / Step - Descubrimiento del `.git`:** En el servidor web se detecta un repositorio `.git/` expuesto (directorio sin protección de servidor).
3. **Paso / Step - Volcado del repositorio:** Con un dumper de repositorios (git-dumper) o herramientas de payloads se descarga todo el historial; como alternativa se lee `.git/logs/HEAD` para listar los commits.
4. **Paso / Step - Inspección del historial:** Se recorren los commits con `git show <commit>`; en un commit antiguo (mensaje tipo "oops" / "flag") se encuentra la flag completa.

### Cadena de ataque / Attack Chain

```
nmap -> puertos web -> /.git/ expuesto en el servidor
  -> git-dumper / volcado del repo (o .git/logs/HEAD)
  -> recorrido de commits -> git show <commit>
  -> commit antiguo ("oops" / "flag") -> THM{byt3_l0tus_n3v3r_f0rg3ts}
```

**Lección:** Nunca despliegues el directorio `.git` en producción; el historial guarda secretos borrados.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
