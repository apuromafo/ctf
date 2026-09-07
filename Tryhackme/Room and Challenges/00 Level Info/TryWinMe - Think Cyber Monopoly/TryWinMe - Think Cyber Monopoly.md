# TryWinMe - Think Cyber Monopoly

| **Dificultad** | Info |
| **Tipo** | CTF |
| **Slug** | `trywinme` |
| **Link** | [TryHackMe](https://tryhackme.com/room/trywinme) |
| **Seccion** | 00 Level Info |
| **Fuente** | Medium (suschillxettri021), Hashnode (jebitok), LinkedIn (mkfih3r), CourseHive |
| **Componentes** | Google dorking / Shodan / VirusTotal / OSINT / CVE lookup |
| **Impacto** | Evalua habilidades de busqueda, OSINT y uso de motores especializados en ciberseguridad |

---

**Contexto:** Esta sala es parte del camino de aprendizaje "Cybersecurity 101" y cubre habilidades de busqueda, motores de busqueda especializados, documentacion tecnica, vulnerabilidades y OSINT en redes sociales. Esta disenada como un desafio conceptual y practico donde se aplican tecnicas de reconocimiento e investigacion.

## Solucionario

### Task 1: Search Skills

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do you call a cryptographic method or product considered bogus or fraudulent? | `snake oil` |
| 2 | What is the name of the command replacing `netstat` in Linux systems? | `ss` |
| 3 | How would you limit your Google search to PDF files containing the terms **cyber warfare report**? | `filetype:pdf cyber warfare report` |
| 4 | What phrase does the Linux command `ss` stand for? | `socket statistics` |
| 5 | What is the top country with **lighttpd** servers? | `United States` |
| 6 | What does BitDefenderFalx detect the file with the hash `2de70ca737c1f4602517c555ddd54165432cf231ffc0e21fb2e23b9dd14e7fb4` as? | `Android.Riskware.Agent.LHH` |

### Task 2: Specialized Search Engines

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the Linux command `cat` stand for? | `concatenate` |
| 2 | What is the `netstat` parameter in MS Windows that displays the executable associated with each active connection and listening port? | `-b` |

### Task 3: Vulnerabilities and Exploitation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. | No answer needed |

### Task 4: Technical Documentation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. | No answer needed |

### Task 5: Social Media

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
