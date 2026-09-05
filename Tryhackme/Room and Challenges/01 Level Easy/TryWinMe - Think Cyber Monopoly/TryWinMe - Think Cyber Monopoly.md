# TryWinMe: Think Cyber Monopoly [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `trywinme`
* **Link:** https://tryhackme.com/room/trywinme
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Medium (suschillxettri021), Hashnode (jebitok), LinkedIn (mkfih3r), CourseHive

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala es parte del camino de aprendizaje "Cybersecurity 101" y cubre habilidades de búsqueda, motores de búsqueda especializados, documentación técnica, vulnerabilidades y OSINT en redes sociales. Está diseñada como un desafío conceptual y práctico donde se aplican técnicas de reconocimiento e investigación.
> **EN:** This room is part of the "Cybersecurity 101" learning path and covers search skills, specialized search engines, technical documentation, vulnerabilities, and social media OSINT. It is designed as a conceptual and practical challenge where reconnaissance and research techniques are applied.

### Task 1 - Search Skills

> **ES:** Esta tarea cubre fundamentos de búsqueda en ciberseguridad, incluyendo motores de búsqueda como Google, operadores de búsqueda avanzada, y herramientas como Shodan y VirusTotal. Se practica el uso de operadores de Google como `filetype:` y se investigan herramientas especializadas.
> **EN:** This task covers cybersecurity search fundamentals, including search engines like Google, advanced search operators, and tools like Shodan and VirusTotal. It practices using Google operators like `filetype:` and investigating specialized tools.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What do you call a cryptographic method or product considered bogus or fraudulent? | `snake oil` |
| What is the name of the command replacing `netstat` in Linux systems? | `ss` |
| How would you limit your Google search to PDF files containing the terms **cyber warfare report**? | `filetype:pdf cyber warfare report` |
| What phrase does the Linux command `ss` stand for? | `socket statistics` |
| What is the top country with **lighttpd** servers? | `United States` |
| What does BitDefenderFalx detect the file with the hash `2de70ca737c1f4602517c555ddd54165432cf231ffc0e21fb2e23b9dd14e7fb4` as? | `Android.Riskware.Agent.LHH` |

### Task 2 - Specialized Search Engines

> **ES:** Esta tarea profundiza en motores de búsqueda especializados para ciberseguridad, incluyendo Shodan (para dispositivos IoT), Censys, y VirusTotal. Se practica la búsqueda de dispositivos expuestos y la verificación de hashes de malware.
> **EN:** This task delves into specialized search engines for cybersecurity, including Shodan (for IoT devices), Censys, and VirusTotal. It practices searching for exposed devices and verifying malware hashes.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What does the Linux command `cat` stand for? | `concatenate` |
| What is the `netstat` parameter in MS Windows that displays the executable associated with each active connection and listening port? | `-b` |

### Task 3 - Vulnerabilities and Exploitation

> **ES:** Se explora cómo buscar vulnerabilidades y recursos de explotación. Se revisan bases de datos de vulnerabilidades como CVE y se practica la búsqueda de exploits en Metasploit y otros repositorios.
> **EN:** The task explores how to search for vulnerabilities and exploitation resources. It reviews vulnerability databases like CVE and practices finding exploits in Metasploit and other repositories.

> **ES:** Se explora cómo buscar vulnerabilidades y recursos de explotación. Se revisan bases de datos de vulnerabilidades como CVE y se practica la búsqueda de exploits en Metasploit y otros repositorios. Esta sección es principalmente conceptual, sin flags específicos para introducir en el campo de respuesta.
> **EN:** The task explores how to search for vulnerabilities and exploitation resources. It reviews vulnerability databases like CVE and practices finding exploits in Metasploit and other repositories. This section is primarily conceptual, with no specific flags to enter in the answer field.

### Task 4 - Technical Documentation

> **ES:** Esta tarea se enfoca en la importancia de la documentación técnica en ciberseguridad, incluyendo la lectura de documentación de herramientas, CVEs y la búsqueda de información técnica relevante para el análisis de seguridad. Es una tarea de lectura y comprensión.
> **EN:** This task focuses on the importance of technical documentation in cybersecurity, including reading tool documentation, CVEs, and finding relevant technical information for security analysis. It is a reading and comprehension task.

### Task 5 - Social Media

> **ES:** Esta tarea cubre OSINT en redes sociales. Se practica la investigación de perfiles, la extracción de información pública y el uso de redes sociales para reconnaissance. Se identifican plataformas clave como LinkedIn y Facebook para obtener información de objetivos.
> **EN:** This task covers OSINT on social media. It practices profile research, public information extraction, and using social media for reconnaissance. Key platforms like LinkedIn and Facebook are identified for target information gathering.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| You are hired to evaluate the security of a particular company. What is a popular social media website you would use to learn about the technical background of one of their employees? | `LinkedIn` |
| Continuing with the previous scenario, you are trying to find the answer to the secret question, "Which school did you go to as a child?". What social media website would you consider checking to find the answer to such secret questions? | `Facebook` |

## Metodología / Methodology

1. **Paso / Step - Identificación del motor de búsqueda adecuado:** Evaluar qué herramienta de búsqueda es más apropiada para la tarea (Google, Shodan, VirusTotal, etc.) según el tipo de información que se necesita.
2. **Paso / Step - Uso de operadores de búsqueda avanzada:** Aplicar operadores como `filetype:`, `site:`, `intitle:` para filtrar resultados y encontrar información específica más rápidamente.
3. **Paso / Step - Herramientas especializadas:** Utilizar plataformas como Shodan para descubrir dispositivos expuestos, Censys para infraestructura, y VirusTotal para análisis de malware.
4. **Paso / Step - OSINT en redes sociales:** Investigar perfiles en LinkedIn para información profesional y en Facebook para datos personales que puedan servir como respuestas a preguntas de seguridad.
5. **Paso / Step - Verificación cruzada:** Contrastar la información obtenida de múltiples fuentes para confirmar su veracidad y completitud.
6. **Paso / Step - Documentación de hallazgos:** Registrar todas las herramientas, técnicas y resultados encontrados durante el proceso de investigación.

### Cadena de ataque / Attack Chain

```
Identificación del objetivo
        |
        v
Selección de motor de búsqueda (Google/Shodan/VirusTotal)
        |
        v
Aplicación de operadores avanzados (filetype:, site:, etc.)
        |
        v
Recopilación de información (OSINT + herramientas especializadas)
        |
        v
Análisis y verificación cruzada
        |
        v
Documentación de hallazgos
```

**Lección:** Las habilidades de búsqueda y OSINT son fundamentales en ciberseguridad; saber qué herramienta usar y cómo usarla eficientemente marca la diferencia entre un reconocimiento superficial y uno exhaustivo.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
