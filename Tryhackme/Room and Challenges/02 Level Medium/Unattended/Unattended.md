# Unattended

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense digital / Windows | unattended | https://tryhackme.com/room/unattended | 02 Level Medium | TryHackMe | Autopsy, Registry Explorer, KAPE, NTUSER.DAT, WordWheelQuery, Web History | Detección de actividad no autorizada y exfiltración de datos |

---

**Contexto:** La sala **Unattended** es un reto de **forensia digital** (DFIR) sobre un caso: un empleado recién contratado vio a un conserje sospechoso salir de su oficina mientras él estaba fuera comiendo. Hay que investigar si hubo actividad de usuario entre **12:05 PM y 12:45 PM del 19 de noviembre de 2022**, qué ficheros se accedieron y qué se exfiltró. Se trabaja sobre la salida de **KAPE** (imagen de disco en `kape-results\C`) usando **Registry Explorer** (`NTUSER.DAT`: WordWheelQuery, RecentDocs) y **Autopsy** (Web Downloads, Web History) para reconstruir la línea temporal: búsqueda de `.pdf` y `continental`, descarga de `7z2201-x64.exe`, apertura de un PNG, uso de un fichero de texto y su exfiltración a **pastebin.com**.

## Solucionario

### Task 1: Intro / Introducción
**Explicación:**

Se contextualiza el caso y se prepara el entorno forense con los resultados de KAPE y las herramientas (Registry Explorer, Autopsy, JLECmd).

| Pregunta | Respuesta |
|----------|-----------|
| Download the files and explore the case | `No answer needed` |

### Task 2: KAPE / Investigación
**Explicación:**

Se examina la imagen de disco con KAPE: se busca qué archivo se intentó recuperar y con qué contraseña se usó la herramienta de recuperación (respuestas de contexto del volcado).

| Pregunta | Respuesta |
|----------|-----------|
| KAPE investigation | `No answer needed` |

### Task 3: Registry / Registro
**Explicación:**

Con **Registry Explorer** se abre el `NTUSER.DAT` capturado. En `Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery` se recupera lo tecleado en la barra de búsqueda de Windows Explorer: el tipo de fichero buscado es `.pdf` y la palabra clave "top-secret" buscada es `continental`.

```text
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
```

| Pregunta | Respuesta |
|----------|-----------|
| What file type was searched for using the search bar in Windows Explorer? | `.pdf` |
| What top-secret keyword was searched for using the search bar in Windows Explorer? | `continental` |

### Task 4: Downed File / Fichero descargado
**Explicación:**

En **Autopsy** (Data Artifacts → Web Downloads) se localiza el fichero más reciente descargado dentro de la franja horaria investigada: `7z2201-x64.exe`, descargado a las `2022-11-19 12:09:19 UTC`. Además, gracias a ese 7-Zip, se abrió un PNG (`continental.png`) que quedó registrado en `RecentDocs\.png` con su marca temporal.

```bash
# Registry Explorer: RecentDocs\.png → continental.png
# Autopsy: Web Downloads → 7z2201-x64.exe, 2022-11-19 12:09:19 UTC
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the name of the downloaded file to the Downloads folder? | `7z2201-x64.exe` |
| When was the file downloaded? | `2022-11-19 12:09:19 UTC` |
| Thanks to the previously downloaded file, a PNG file was opened. When was this file opened? | `2022-11-19 12:10:21` |

### Task 5: User Activity / Actividad del usuario
**Explicación:**

Se creó un fichero de texto (`launchcode.txt`) en el Desktop cuyo análisis con **JLECmd** muestra el número de interacciones (2) y su última modificación (`11/19/2022 12:12`). El contenido se exfiltró a **pastebin.com**: buscando en Para "Web History" de Autopsy por `pastebin` se obtiene la URL generada y, en el campo *Title*, la cadena que se copió/pegó al servicio.

```bash
# JLECmd.exe -d <kape-results>/... -r timeline.csv
# Autopsy → Data Artifacts → Web History → pastebin
```

| Pregunta | Respuesta |
|----------|-----------|
| A text file was created in the Desktop folder. How many times was this file opened? | `2` |
| When was the text file last modified? | `11/19/2022 12:12` |
| The contents of the file were exfiltrated to pastebin.com. What is the generated URL of the exfiltrated data? | `https://pastebin.com/1FQASAav` |
| What is the string that was copied to the pastebin URL? | `ne7AIRhi3PdESy9RnOrN` |

### Task 6: Content / Contenido
**Explicación:**

Tarea de cierre de la sala una vez reconstruida toda la línea temporal de la exfiltración.

| Pregunta | Respuesta |
|----------|-----------|
| Content | `No answer needed` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Download the files and explore the case | `No answer needed` |
| 2 | KAPE investigation | `No answer needed` |
| 3 | What file type was searched for using the search bar in Windows Explorer? | `.pdf` |
| 3 | What top-secret keyword was searched for using the search bar in Windows Explorer? | `continental` |
| 4 | What is the name of the downloaded file to the Downloads folder? | `7z2201-x64.exe` |
| 4 | When was the file downloaded? | `2022-11-19 12:09:19 UTC` |
| 4 | Thanks to the previously downloaded file, a PNG file was opened. When was this file opened? | `2022-11-19 12:10:21` |
| 5 | A text file was created in the Desktop folder. How many times was this file opened? | `2` |
| 5 | When was the text file last modified? | `11/19/2022 12:12` |
| 5 | The contents of the file were exfiltrated to pastebin.com. What is the generated URL of the exfiltrated data? | `https://pastebin.com/1FQASAav` |
| 5 | What is the string that was copied to the pastebin URL? | `ne7AIRhi3PdESy9RnOrN` |
| 6 | Content | `No answer needed` |

---

**Metodología:** Procesado con KAPE, análisis de registro (`NTUSER.DAT`: WordWheelQuery y RecentDocs) con Registry Explorer, correlación de artefactos de Web Downloads/Web History con Autopsy, parseo de archivos con JLECmd y reconstrucción temporal de la exfiltración vía pastebin.

### Cadena de ataque / Attack Chain

```
NTUSER.DAT (WordWheelQuery: .pdf / continental) → Web Downloads (7z2201-x64.exe @ 12:09:19) → RecentDocs .png (continental.png @ 12:10:21) → Desktop launchcode.txt (2 usos, mod 12:12) → Web History pastebin (URL + string ne7AIRhi3PdESy9RnOrN)
```

**Learning chain:** Preparación de evidencia con KAPE → análisis de registro de usuario → correlación de artefactos de descargas y uso reciente → análisis de aplicaciones (JLECmd) → reconstrucción de exfiltración web.

**Lección:** *El registro de Windows y los artefactos de navegador (WordWheelQuery, RecentDocs, Web Downloads, Web History) permiten reconstruir segundo a segundo la actividad de un usuario ausente; la exfiltración a servicios de pegado de texto deja rastro en el Title del historial.*

**MITRE ATT&CK:** T1005 Data from Local System · T1567.002 Exfiltration Over Web Service (pastebin) · T1053.005 Scheduled Task (índole del caso).

**Fuente:** [TryHackMe - Unattended](https://tryhackme.com/room/unattended)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.