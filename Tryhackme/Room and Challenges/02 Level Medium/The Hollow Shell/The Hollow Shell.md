# The Hollow Shell [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-thehollowshell-ddb582ac`
* **Link:** https://tryhackme.com/room/hh-thehollowshell-ddb582ac
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-thehollowshell-ddb582ac` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en **Linux / web con Zip Slip**: la aplicación permite subir archivos ZIP que se extraen a una carpeta; un ZIP con rutas `../../` (CWE-687) permite escribir fuera del directorio destino (p. ej. `webroot/shell.php`) y ejecutar una shell PHP → RCE → flag.
> **EN:** Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty centered on **Linux / web with Zip Slip**: the app allows uploading ZIP files that are extracted to a folder; a ZIP with `../../` paths (CWE-687) allows writing outside the destination directory (e.g. `webroot/shell.php`) and executing a PHP shell → RCE → flag.

### Task 1 - The Hollow Shell

> **ES:** La aplicación tiene una funcionalidad de subida de archivos y extracción de ZIPs. Al no sanear los nombres de las entradas del ZIP, una entrada `../../../../var/www/html/shell.php` se extrae fuera del directorio de trabajo, escribiendo la shell en la webroot. Accediendo a esa URL se ejecuta `shell.php` y se lee la flag. 1 pregunta.
> **EN:** The app has a file-upload / ZIP-extraction feature. Since ZIP entry names are not sanitized, an entry `../../../../var/www/html/shell.php` is extracted outside the working directory, writing the shell into the webroot. Accessing that URL executes `shell.php` and the flag is read. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{z1p_sl1pp3d_1nt0_a_sh3ll}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Se encuentra una aplicación web con subida de ZIP que los descomprime en una carpeta del servidor (sin validación de nombres de entrada).
2. **Paso / Step - Crear el ZIP malicioso:** Con un script PHP simple y Linux/BSD Zip (precediendo las rutas con `../../`) se crea un ZIP cuya entrada `../../../../var/www/html/shell.php` escapa del directorio de extracción.
3. **Paso / Step - Subida:** Se sube el ZIP; el extractor confía en las rutas y escribe `shell.php` fuera del destino previsto.
4. **Paso / Step - RCE:** Se navega a `http://target/shell.php` con un parámetro de comando → ejecución de comandos → se lee la flag `THM{z1p_sl1pp3d_1nt0_a_sh3ll}`.

### Cadena de ataque / Attack Chain

```
upload ZIP (sin saneo de rutas)
  -> entrada ../../../../var/www/html/shell.php (Zip Slip / CWE-687)
  -> extracción fuera del directorio destino -> shell.php en webroot
  -> GET /shell.php?cmd=... -> RCE
  -> cat flag -> THM{z1p_sl1pp3d_1nt0_a_sh3ll}
```

**Lección:** Sanear siempre los nombres de las entradas del ZIP antes de extraer (rechazar `..`, validar rutas, usar APIs seguras de descompresión): un Zip Slip convierte una subida de archivos en escritura arbitraria y RCE.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.