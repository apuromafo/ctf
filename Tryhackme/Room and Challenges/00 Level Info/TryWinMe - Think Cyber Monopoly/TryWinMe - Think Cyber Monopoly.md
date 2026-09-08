# TryWinMe - Think Cyber Monopoly

| **Dificultad** | Info |
| **Tipo** | CTF |
| **Slug** | `trywinme` |
| **Link** | [TryHackMe](https://tryhackme.com/room/trywinme) |
| **Sección** | 00 Level Info |
| **Fuente** | Medium (suschillxettri021), Hashnode (jebitok), LinkedIn (mkfih3r), CourseHive |
| **Componentes** | Google dorking / Shodan / VirusTotal / OSINT / CVE lookup |
| **Impacto** | Evalua habilidades de busqueda, OSINT y uso de motores especializados en ciberseguridad |

---

**Contexto:** Esta sala es parte del camino de aprendizaje "Cybersecurity 101" y cubre habilidades de busqueda, motores de busqueda especializados, documentacion tecnica, vulnerabilidades y OSINT en redes sociales. Esta disenada como un desafio conceptual y practico donde se aplican tecnicas de reconocimiento e investigacion.

## Solucionario

### Task 1: Search Skills

**Explicación:** La tarea ejercita las búsquedas clásicas de ciberseguridad: terminología ("snake oil" = método o producto criptográfico falso/fraudulento), conocimiento de comandos Linux y operadores de Google. `ss` es el sucesor moderno de `netstat` en Linux y significa "socket statistics". Para filtrar por tipo de archivo se usa `filetype:pdf` (o `filetype` funciona con otros tipos de documento), así `filetype:pdf cyber warfare report` devuelve solo PDFs que contengan esos términos. La búsqueda de servidores lighttpd se hace en Shodan (buscando por servidor web) y el top país según ese moldeo de búsqueda es United States; el hash de malware se vuelca en VirusTotal y BitDefenderFalx lo clasifica como `Android.Riskware.Agent.LHH`.

```text
filetype:pdf cyber warfare report
ss -ltnp            # reemplazo moderno de netstat -tulpn
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do you call a cryptographic method or product considered bogus or fraudulent? | `snake oil` |
| 2 | What is the name of the command replacing `netstat` in Linux systems? | `ss` |
| 3 | How would you limit your Google search to PDF files containing the terms **cyber warfare report**? | `filetype:pdf cyber warfare report` |
| 4 | What phrase does the Linux command `ss` stand for? | `socket statistics` |
| 5 | What is the top country with **lighttpd** servers? | `United States` |
| 6 | What does BitDefenderFalx detect the file with the hash `2de70ca737c1f4602517c555ddd54165432cf231ffc0e21fb2e23b9dd14e7fb4` as? | `Android.Riskware.Agent.LHH` |

### Task 2: Specialized Search Engines

**Explicación:** Los motores especializados (Shodan para dispositivos/IoT, Censys para infraestructura, VirusTotal para hashes y muestras) no sustituyen al shell. `cat` viene de "concatenate": concatena y muestra el contenido de archivos. En Windows, `netstat -b` muestra el ejecutable (binary) asociado a cada conexión activa o puerto en escucha, cosa que el `ss` de Linux hace por defecto; de ahí que la respuesta sea el parámetro `-b`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the Linux command `cat` stand for? | `concatenate` |
| 2 | What is the `netstat` parameter in MS Windows that displays the executable associated with each active connection and listening port? | `-b` |

### Task 3: Vulnerabilities and Exploitation

**Explicación:** Tarea conceptual: aprender dónde buscar vulnerabilidades y recursos de explotación. Las fuentes canónicas son las bases de datos de CVE (NVD, CVE.org), los exploits públicos de Metasploit/Exploit-DB y los repositorios de la comunidad. No hay respuestas que introducir: es una tarea de lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. | No answer needed |

### Task 4: Technical Documentation

**Explicación:** Tarea de lectura y comprensión sobre la importancia de la documentación técnica: man pages, doc de herramientas, descripciones de CVEs y advisories. Saber leer documentación es parte del reconocimiento pasivo. Sin preguntas que responder.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. | No answer needed |

### Task 5: Social Media

**Explicación:** Se practica OSINT en redes sociales para reconocimiento. Para conocer la formación técnica de un empleado, la plataforma profesional de referencia es LinkedIn. Para encontrar respuestas a preguntas de seguridad personales ("¿a qué colegio fuiste de niño?"), la habitual es Facebook, donde el contenido personal y de historial suele revelar esos datos sin darse cuenta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | You are hired to evaluate the security of a particular company. What is a popular social media website you would use to learn about the technical background of one of their employees? | `LinkedIn` |
| 2 | Continuing with the previous scenario, you are trying to find the answer to the secret question, "Which school did you go to as a child?". What social media website would you consider checking to find the answer to such secret questions? | `Facebook` |

---

**Metodologia:**

1. Evaluar que herramienta de busqueda es mas apropiada para la tarea (Google, Shodan, VirusTotal, etc.) segun el tipo de informacion que se necesita.
2. Aplicar operadores como `filetype:`, `site:`, `intitle:` para filtrar resultados y encontrar informacion especifica mas rapidamente.
3. Utilizar plataformas como Shodan para descubrir dispositivos expuestos, Censys para infraestructura, y VirusTotal para analisis de malware.
4. Investigar perfiles en LinkedIn para informacion profesional y en Facebook para datos personales que puedan servir como respuestas a preguntas de seguridad.
5. Contrastar la informacion obtenida de multiples fuentes para confirmar su veracidad y completitud.
6. Registrar todas las herramientas, tecnicas y resultados encontrados durante el proceso de investigacion.

**Learning chain:** Identificacion del objetivo -> Seleccion de motor de busqueda (Google/Shodan/VirusTotal) -> Aplicacion de operadores avanzados (filetype:, site:, etc.) -> Recopilacion de informacion (OSINT + herramientas especializadas) -> Analisis y verificacion cruzada -> Documentacion de hallazgos

**MITRE ATT&CK:** T1593.001 (Search Open Websites/Domains), T1593.002 (Search Open Websites/Domains: Social Media), T1596 (Search Open Technical Databases)

**Fuente:** [TryHackMe - TryWinMe - Think Cyber Monopoly](https://tryhackme.com/room/trywinme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
