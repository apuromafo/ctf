# Deja Vu

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `dejavu` | [TryHackMe](https://tryhackme.com/room/dejavu) | 01 Level Easy | THM | ExifTool, CVE-2021-22204, Subida de ficheros, RCE | RCE por deserialización (ExifTool) y escalada |

> **Objeto:** Comprometer la máquina Deja Vu explotando la vulnerabilidad CVE-2021-22204 en la herramienta ExifTool a través de la subida de imágenes, obtener una shell y escalar privilegios.

---

**Contexto:** Sala de laboratorio sobre la vulnerabilidad CVE-2021-22204 de ExifTool: enumeración de los servicios y de la aplicación web, análisis del endpoint de subida de imágenes, detección de la versión de ExifTool y construcción de una imagen maliciosa que ejecuta código remoto hasta obtener una shell y escalar a root.

> **ES:** Enumera la web, encuentra la subida de imágenes, detecta ExifTool 12.23 y explota el CVE-2021-22204 para conseguir una shell y escalar.
> **EN:** Enumerate the web app, find the image upload, spot ExifTool 12.23 and exploit CVE-2021-22204 to get a shell and escalate.

## Solucionario

### Task 1: Reconocimiento / Reconnaissance
**Explicación:** Reconocimiento inicial de la máquina.

No answer needed

### Task 2: Escaneo / Scanning
**Explicación:** Escaneo de puertos y servicios del objetivo.

1. No answer needed
2. No answer needed
3. OpenSSH 8.0 (protocol 2.0)

### Task 3: Aplicación web / Web Application
**Explicación:** Enumeración de la aplicación web: directorios, API y detección de la versión de ExifTool.

1. /upload/
2. /dog/getmetadata
3. /dog/getexifdata
4. ExifToolVersion
5. 12.23
6. CVE-2021-22204

### Task 4: Explotación / Exploitation
**Explicación:** Construcción de la imagen maliciosa con EPS de ExifTool para obtener una shell en el objetivo.

1. No answer needed
2. No answer needed
3. dejavu{735c0553063625f41879e57d5b4f3352}

### Task 5: Escalada / Privilege Escalation
**Explicación:** Escalada de privilegios dentro de la máquina hasta obtener la flag de root.

1. No answer needed
2. No answer needed
3. No answer needed
4. No answer needed
5. dejavu{5ad931368bdc46f856febe4834ace627}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | — | `No answer needed` |
| 2.2 | — | `No answer needed` |
| 2.3 | Versión del servicio SSH | `OpenSSH 8.0 (protocol 2.0)` |
| 3.1 | Directorio de subida | `/upload/` |
| 3.2 | Endpoint de metadatos | `/dog/getmetadata` |
| 3.3 | Endpoint de datos EXIF | `/dog/getexifdata` |
| 3.4 | Campo de versión EXIF | `ExifToolVersion` |
| 3.5 | Versión de ExifTool | `12.23` |
| 3.6 | CVE explotada | `CVE-2021-22204` |
| 4.1 | — | `No answer needed` |
| 4.2 | — | `No answer needed` |
| 4.3 | Flag de usuario | `dejavu{735c0553063625f41879e57d5b4f3352}` |
| 5.1 | — | `No answer needed` |
| 5.2 | — | `No answer needed` |
| 5.3 | — | `No answer needed` |
| 5.4 | — | `No answer needed` |
| 5.5 | Flag de root | `dejavu{5ad931368bdc46f856febe4834ace627}` |

---

**Metodología:** Escaneo de puertos, enumeración de la aplicación web, descubrimiento de la subida de ficheros y de los endpoints de metadatos, detección de ExifTool 12.23, generación de un fichero EPS malicioso que desencadena el CVE-2021-22204, obtención de la shell y escalada de privilegios hasta root.

### Cadena de ataque / Attack Chain

Scan → web enum → /upload/ → ExifTool 12.23 → CVE-2021-22204 → shell → escalada → root.

**Learning chain:** recon → web → subida de imágenes → ExifTool → CVE-2021-22204 → RCE → privesc → root

*Lección:* Las vulnerabilidades de ExifTool (CVE-2021-22204) convierten las subidas de imágenes en RCE; hay que actualizar la herramienta y validar los ficheros subidos.

**MITRE ATT&CK:** TA0001 Initial Access, TA0002 Execution, T1203 Exploitation for Client Execution, TA0004 Privilege Escalation.

**Fuente:** [TryHackMe - Deja Vu](https://tryhackme.com/room/dejavu)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.