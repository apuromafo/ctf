# The Hollow Shell

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `hh-thehollowshell-ddb582ac` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-thehollowshell-ddb582ac) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Zip Slip / CWE-687 / arbitrary file write / RCE / web upload / PHP |
| **Impacto** | Explotar un Zip Slip en la subida de archivos para escribir una shell fuera del directorio destino y lograr RCE |

---

**Contexto:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en **Linux / web con Zip Slip**: la aplicación permite subir archivos ZIP que se extraen a una carpeta; un ZIP con rutas `../../` (CWE-687) permite escribir fuera del directorio destino (p. ej. `webroot/shell.php`) y ejecutar una shell PHP → RCE → flag.

## Solucionario

### Task 1: The Hollow Shell

**Explicación:**

La aplicación tiene una funcionalidad de subida de archivos y extracción de ZIPs. Al no sanear los nombres de las entradas del ZIP, una entrada `../../../../var/www/html/shell.php` se extrae fuera del directorio de trabajo, escribiendo la shell en la webroot. Accediendo a esa URL se ejecuta `shell.php` y se lee la flag: `THM{z1p_sl1pp3d_1nt0_a_sh3ll}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{z1p_sl1pp3d_1nt0_a_sh3ll}` |

---

**Metodología:**

1. **Reconocimiento:** Se encuentra una aplicación web con subida de ZIP que los descomprime en una carpeta del servidor (sin validación de nombres de entrada).
2. **Crear el ZIP malicioso:** Con un script PHP simple y Linux/BSD Zip (precediendo las rutas con `../../`) se crea un ZIP cuya entrada `../../../../var/www/html/shell.php` escapa del directorio de extracción.
3. **Subida:** Se sube el ZIP; el extractor confía en las rutas y escribe `shell.php` fuera del destino previsto.
4. **RCE:** Se navega a `http://target/shell.php` con un parámetro de comando → ejecución de comandos → se lee la flag `THM{z1p_sl1pp3d_1nt0_a_sh3ll}`.

**Learning chain:** upload ZIP (sin saneo) -> entrada ../../../../var/www/html/shell.php (Zip Slip/CWE-687) -> extracción fuera del directorio -> shell.php en webroot -> GET /shell.php -> RCE -> flag

**Lección:** *Sanear siempre los nombres de las entradas del ZIP antes de extraer (rechazar `..`, validar rutas, usar APIs seguras de descompresión): un Zip Slip convierte una subida de archivos en escritura arbitraria y RCE.*

**MITRE ATT&CK:** T1203 (Exploitation for Client Execution) · T1505.003 (Web Shell) · T1059 (Command and Scripting Interpreter) · CWE-22 (Path Traversal)

**Fuente:** [TryHackMe - The Hollow Shell](https://tryhackme.com/room/hh-thehollowshell-ddb582ac)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
