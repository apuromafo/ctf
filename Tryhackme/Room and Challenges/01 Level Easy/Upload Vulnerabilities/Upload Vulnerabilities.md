# Upload Vulnerabilities

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `uploadvulnerabilities` | [TryHackMe](https://tryhackme.com/room/uploadvulnerabilities) | 01 Level Easy | THM | File upload, sobrescritura de archivos, RCE, webshells, reverse shells, filtrado client-side y server-side, extensiones, MIME types, magic numbers, Gobuster, BurpSuite | Resolución completa de la sala tutorial |

---

**Contexto:** Sala tutorial que explora vulnerabilidades de subida de archivos en sitios web: sobrescribir archivos existentes en el servidor, subir y ejecutar shells (webshells y reverse shells) para lograr Remote Code Execution (RCE), y evadir los filtrados de tipo client-side y server-side (validación de extensiones, MIME types y magic numbers). Utiliza subdominios virtuales (overwrite, shell, java, annex, magic y jewel .uploadvulns.thm) además de Gobuster y BurpSuite.

> **ES:** Sala tutorial sobre vulnerabilidades de subida de archivos: sobrescritura de archivos, RCE con webshells y reverse shells, bypass del filtrado cliente (JavaScript) y servidor (extensiones, MIME y magic numbers) usando Gobuster, BurpSuite y hosts virtuales.
> **EN:** Tutorial room on file upload vulnerabilities: overwriting existing files, RCE with webshells and reverse shells, and bypassing client-side (JavaScript) and server-side filtering (extensions, MIME and magic numbers) using Gobuster, BurpSuite and virtual hosts.

## Solucionario

### Task 1: Introducción y configuración / Getting Started

**Explicación:** Se despliega la máquina y se configura el archivo hosts con los subdominios virtuales de la sala (overwrite, shell, java, annex, magic y jewel .uploadvulns.thm), tal como indican las instrucciones, tanto en Linux/MacOS como en Windows (PowerShell como administrador).

1. Configure your hosts file for the task, as per the instructions above.
2. `No answer needed`

### Task 2: Introducción / Introduction

**Explicación:** Se explican los riesgos de una subida de archivos mal gestionada: desde la alteración de contenido existente (defacement) hasta la ejecución remota de código, pasando por XSS/CSRF y el uso del servidor como hosting de contenido ilegal. El propósito de la sala es explorar la sobrescritura de archivos, la subida de shells, y el bypass de filtros client-side y server-side.

1. Read and understand the above information.
2. `No answer needed`

### Task 3: Metodología general / General Methodology

**Explicación:** Se presenta la metodología: enumeración (código fuente, Gobuster, BurpSuite, Wappalyser), identificación del tipo de filtrado (client-side vs server-side) y pruebas iterativas con errores controlados.

1. Read the General Methodology
2. `No answer needed`

### Task 4: Sobrescribir archivos existentes / Overwriting Existing Files

**Explicación:** Al no existir precauciones contra sobrescritura, es posible reemplazar archivos del servidor. Sobre overwrite.uploadvulns.thm se identifica el archivo de imagen vulnerable y se sobrescribe para obtener la flag.

1. What is the name of the image file which can be overwritten?
2. `mountains.jpg`
3. Overwrite the image. What is the flag you receive?
4. `THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}`

### Task 5: Ejecución remota de código / Remote Code Execution

**Explicación:** Se logra RCE subiendo una webshell PHP o una reverse shell (Pentest Monkey). Sobre shell.uploadvulns.thm se enumera con Gobuster el directorio de subida (/resources) y se obtiene la flag situada en /var/www del servidor.

1. Run a Gobuster scan on the website. What directory looks like it might be used for uploads?
2. `/resources`
3. Get either a web shell or a reverse shell on the machine. What's the flag in the /var/www/ directory of the server?
4. `THM{YWFhY2U3ZGI4N2QxNmQzZjk0YjgzZDZk}`

### Task 6: Filtrado / Filtering

**Explicación:** Teoría sobre los tipos de filtrado: validación de extensiones (blacklist/whitelist), file type filtering (MIME types y magic numbers), file length filtering y file name filtering. Se responde al lenguaje tradicional del backend, a las listas de extensiones aceptadas y al MIME type de los CSV.

1. What is the traditional server-side scripting language?
2. `PHP`
3. When validating by file extension, what would you call a list of accepted extensions (whereby the server rejects any extension not in the list)?
4. `Whitelist`
5. [Research] What MIME type would you expect to see when uploading a CSV file?
6. `text/csv`

### Task 7: Bypass del filtrado cliente / Bypassing Client-Side Filtering

**Explicación:** Los filtros client-side corren en el navegador (JavaScript) y son trivialmente fáciles de evadir: desactivando JavaScript, eliminando el filtro con BurpSuite o modificando la petición de subida. Sobre java.uploadvulns.thm se obtiene una reverse shell y la flag en /var/www.

1. What is the flag in /var/www/?
2. `THM{NDllZDQxNjJjOTE0YWNhZGY3YjljNmE2}`

### Task 8: Bypass del filtrado servidor: extensiones de archivo / Bypassing Server-Side Filtering: File Extensions

**Explicación:** Los filtros server-side no se pueden ver ni manipular; hay que enumerar qué se acepta. Sobre annex.uploadvulns.thm se prueba con extensiones alternativas (.phar, .php5, .pht...) hasta conseguir activar la shell y leer la flag en /var/www.

1. What is the flag in /var/www/?
2. `THM{MGEyYzJiYmI3ODIyM2FlNTNkNjZjYjFl}`

### Task 9: Bypass del filtrado servidor: magic numbers / Bypassing Server-Side Filtering: Magic Numbers

**Explicación:** Los magic numbers (bytes al inicio del archivo, como `89 50 4E 47 0D 0A 1A 0A` para PNG) verifican el contenido real del archivo. Sobre magic.uploadvulns.thm se falsifica el magic number del payload, se localiza el shell subido y se obtiene la flag de /var/www.

1. Grab the flag from /var/www/
2. `THM{MWY5ZGU4NzE0ZDlhNjE1NGM4ZThjZDJh}`

### Task 10: Metodología de ejemplo / Example Methodology

**Explicación:** Metodología global para auditar subidas de archivos: análisis del sitio y de vectores (lenguajes, frameworks, página de subida), inspección del código fuente (filtros client-side), subida inocente para estudiar el acceso a los archivos, y prueba de extensiones/MIME/magic numbers inválidos para deducir el tipo de filtro server-side.

1. No answer needed

### Task 11: Desafío / Challenge

**Explicación:** Desafío final sobre jewel.uploadvulns.thm: hay que combinar todo lo aprendido (posiblemente múltiples filtros y un backend que no es PHP) para obtener una shell y leer la flag en /var/www.

1. No answer needed

### Task 12: Conclusión / Conclusion

**Explicación:** Cierre de la sala. No requiere respuesta.

1. No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1 | Configure your hosts file for the task, as per the instructions above. | `No answer needed` |
| 2 | Read and understand the above information. | `No answer needed` |
| 3 | Read the General Methodology | `No answer needed` |
| 4.1 | What is the name of the image file which can be overwritten? | `mountains.jpg` |
| 4.2 | Overwrite the image. What is the flag you receive? | `THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}` |
| 5.1 | What directory looks like it might be used for uploads? | `/resources` |
| 5.2 | What's the flag in the /var/www/ directory of the server? | `THM{YWFhY2U3ZGI4N2QxNmQzZjk0YjgzZDZk}` |
| 6.1 | What is the traditional server-side scripting language? | `PHP` |
| 6.2 | What would you call a list of accepted extensions (whereby the server rejects any extension not in the list)? | `Whitelist` |
| 6.3 | What MIME type would you expect to see when uploading a CSV file? | `text/csv` |
| 7 | What is the flag in /var/www/? | `THM{NDllZDQxNjJjOTE0YWNhZGY3YjljNmE2}` |
| 8 | What is the flag in /var/www/? | `THM{MGEyYzJiYmI3ODIyM2FlNTNkNjZjYjFl}` |
| 9 | Grab the flag from /var/www/ | `THM{MWY5ZGU4NzE0ZDlhNjE1NGM4ZThjZDJh}` |
| 10 | — | `No answer needed` |
| 11 | Hack the machine and grab the flag from /var/www/ | `No answer needed` |
| 12 | — | `No answer needed` |

---

**Metodología:** 1) Configurar los hosts virtuales y desplegar la máquina. 2) Enumerar con Gobuster y el código fuente. 3) Sobrescribir archivos existentes (overwrite.uploadvulns.thm). 4) Lograr RCE con webshells/reverse shells sobre shell.uploadvulns.thm. 5) Estudiar el filtrado (extensiones, MIME, magic numbers). 6) Evadir el filtro client-side (java.uploadvulns.thm). 7) Evadir filtros server-side de extensiones (annex) y magic numbers (magic). 8) Aplicar la metodología completa en el desafío final (jewel).

### Cadena de ataque / Attack Chain

Reconocimiento (Gobuster + Wappalyser + código fuente) → Sobrescritura de archivos existentes → Subida de webshell/reverse shell (RCE) → Bypass de filtrado client-side (JavaScript interceptado con BurpSuite) → Bypass de filtrado server-side (extensiones alternativas: .phar/.php5) → Bypass de magic numbers (inyección de bytes mágicos) → Obtención de flags en /var/www

**Learning chain:** File upload → overwrite existing files → webshells → reverse shells → client-side filtering bypass → server-side filtering bypass (extensions) → magic numbers bypass → RCE

**Lección:** *Una subida de archivos sin filtros correctos es una puerta abierta a RCE: el enumerar el directorio de subida, probar extensiones alternativas y falsificar MIME types y magic numbers convierte una funcionalidad inocua en una shell sobre el servidor.*

**MITRE ATT&CK:** T1505.003 (Server Software Component: Web Shell), T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1105 (Ingress Tool Transfer), T1036 (Masquerading), T1027 (Obfuscated Files or Information), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Upload Vulnerabilities](https://tryhackme.com/room/uploadvulnerabilities)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.