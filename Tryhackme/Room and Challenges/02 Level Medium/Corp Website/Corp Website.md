# Corp Website [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e7`
* **Link:** https://tryhackme.com/room/lafb2026e7
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e7` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026, listada en la API como "Romance and Co") de dificultad Media. El tema es una **web corporativa con un componente vulnerable a RCE**: la versión de una librería está afectada por CVE-2025-55182 y da ejecución de código como el usuario de la web; desde ahí, enumeración de privilegios local (sudo, SUID, credenciales en configs) eleva a root y se leen las dos flags.
> **EN:** Event room (Love at First Breach 2026, listed in the API as "Romance and Co") of Medium difficulty. The theme is a **corporate website with an RCE-able component**: the version of a library is affected by CVE-2025-55182 and gives code execution as the web user; from there, local privilege enumeration (sudo, SUID, credentials in configs) elevates to root and both flags are read.

### Task 1 - Web to Shell

> **ES:** `nmap` revela `80/tcp` (y `22`). El sitio corporativo identifica su stack (banner, `/robots.txt`, páginas de error, headers) y se descubre una librería desactualizada afectada por **CVE-2025-55182** (RCE sin autenticación en ese componente). El exploit devuelve una shell como el usuario web (`www-data`/`apache`): ahí se lee la **user flag** (`/var/www/...` o `/home/usuario`). Para root: `sudo -l`, binarios SUID y credenciales en ficheros de config/`.env`; la credencial (o el binario explotable) permite `sudo su`/ejecutar privilegiado y leer la **root flag**. 2 preguntas.
> **EN:** `nmap` reveals `80/tcp` (and `22`). The corporate site fingerprints its stack (banner, `/robots.txt`, error pages, headers) and an outdated library affected by **CVE-2025-55182** (unauthenticated RCE in that component) is found. The exploit drops a shell as the web user (`www-data`/`apache`): there you read the **user flag** (`/var/www/...` or `/home/user`). For root: `sudo -l`, SUID binaries and credentials in config/`.env` files; the credential (or the exploitable binary) allows `sudo su`/privileged execution and reading the **root flag**. 2 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user flag? | `THM{R34c7_2_5h311_3xpl017}` |
| What is the root flag? | `THM{Pr1v_35c_47_175_f1n357}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `nmap -sV -sC` → puerto web y servicios. Fingerprint del framework/versión mediante headers, fuentes y páginas de error.
2. **Paso / Step - Identificación del CVE:** Se detecta que una librería del stack está en versión afectada por **CVE-2025-55182** (RCE por el lado servidor, sin auth). 
3. **Paso / Step - RCE como usuario web:** Se lanza el exploit (metasploit o script manual) → shell como el usuario de la web.
4. **Paso / Step - User flag:** Se ubica la flag del usuario (`/var/www/flag*.txt`, `/home/<user>/user.txt`) → `THM{R34c7_2_5h311_3xpl017}`.
5. **Paso / Step - PrivEsc:** Enumeración local (`sudo -l`, SUID, cron, `.env`/configs). Se encuentra la vía de elevación (binario con sudo/SUID o credencial root en configuración).
6. **Paso / Step - Root flag:** `sudo`/exploit → cuenta `root` → `cat /root/root.txt` (o root flag) → `THM{Pr1v_35c_47_175_f1n357}`.

### Cadena de ataque / Attack Chain

```
webapp corporativa -> fingerprint de versión/librería
  -> librería vulnerable -> CVE-2025-55182 (RCE sin auth)
  -> shell como usuario web (www-data/apache)
  -> user flag -> THM{R34c7_2_5h311_3xpl017}
  -> enum privEsc (sudo -l / SUID / .env / configs) -> root
  -> root flag -> THM{Pr1v_35c_47_175_f1n357}
```

**Lección:** Mantén las dependencias al día: un CVE conocido en un componente de la web convierte el sitio en una shell, y una flag "user" sin endurecer el host es solo la antesala de la root.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.