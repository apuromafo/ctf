# Introductory Researching

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductoryresearching` | [TryHackMe](https://tryhackme.com/room/introductoryresearching) | 01 Level Easy | TryHackMe | investigación OSINT, Google dorking, CVE, NVD, man pages y ayuda de herramientas | Saber investigar eficazmente: buscar curiosidades técnicas, localizar CVEs y leer la documentación de las herramientas (man pages) para resolver problemas. |

---

**Contexto:** Sala que entrena las habilidades de investigación que todo hacker necesita: uso eficiente de buscadores y de operadores avanzados, lectura de resultados como páginas web, manejo del National Vulnerability Database para encontrar CVEs y consulta de la documentación local de las herramientas mediante man y sus flags. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Practicar la investigación web con dorking, resolver curiosidades técnicas y herramientas (Repeater, NTLM, cron jobs, base 16, sha512crypt), buscar CVEs concretos y consultar las man pages para deducir los flags de herramientas como nc.
> **EN:** Practice web research with dorking, answer technical curiosities and tools (Repeater, NTLM, cron jobs, base 16, sha512crypt), search for specific CVEs and read the man pages to infer the flags of tools such as nc.

## Solucionario

### Task 1: Investigación web / Web Research
**Explicación:** Se presentan las técnicas de búsqueda avanzada en la web como punto de partida de toda investigación.

1. No answer needed

### Task 2: Curiosidades técnicas / Technical Curiosities
**Explicación:** Se resuelven preguntas de cultura técnica: la herramienta de repetición de Burp Suite (Repeater), el protocolo de autenticación NTLM, la automatización con cron jobs, el sistema de numeración en base 16 y la función de hashing sha512crypt.

1. Repeater
2. NTLM
3. Cron Jobs
4. Base 16
5. sha512crypt

### Task 3: CVEs / CVEs
**Explicación:** Se buscan en bases de datos de vulnerabilidades los CVEs asociados a productos concretos, como CVE-2020-10385, CVE-2016-1240, CVE-2007-0017 y CVE-2019-18634.

1. CVE-2020-10385
2. CVE-2016-1240
3. CVE-2007-0017
4. CVE-2019-18634

### Task 4: Man pages / Man Pages
**Explicación:** Se consulta la documentación local de las herramientas para deducir los flags correctos, incluido el comando de escucha con netcat.

1. -r
2. -l
3. -B
4. nc -l -p 12345

### Task 5: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo que integra todo el proceso de investigación.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | Herramienta de repetición de peticiones / Request repeater tool | `Repeater` |
| 3 | Protocolo de autenticación / Authentication protocol | `NTLM` |
| 4 | Tareas automatizadas en el tiempo / Scheduled automation | `Cron Jobs` |
| 5 | Sistema de numeración hexadecimal / Base 16 numbering system | `Base 16` |
| 6 | Función de hash indicada / Indicated hash function | `sha512crypt` |
| 7 | CVE de WP Time Capsule / CVE for WP Time Capsule | `CVE-2020-10385` |
| 8 | CVE del panel de Nagios / CVE for Nagios panel | `CVE-2016-1240` |
| 9 | CVE de Adobe / CVE for Adobe | `CVE-2007-0017` |
| 10 | CVE de sudo / CVE for sudo | `CVE-2019-18634` |
| 11 | Flag de reverso de netcat / Netcat reverse flag | `-r` |
| 12 | Flag de escucha de netcat / Netcat listen flag | `-l` |
| 13 | Flag de modo de edición / Flag for edit mode | `-B` |
| 14 | Comando de escucha indicado / Indicated listening command | `nc -l -p 12345` |
| 15 | (Pregunta 15 no especificada en el original) | `No answer needed` |

---

**Metodología:** Aplicar técnicas de investigación web y dorking, responder curiosidades técnicas consultando fuentes fiables, buscar cada CVE en bases de vulnerabilidades y consultar las man pages locales para deducir los flags y comandos de las herramientas.

### Cadena de ataque / Attack Chain

```text
búsqueda web + dorking -> curiosidades técnicas (Repeater/NTLM/cron/base16/sha512crypt) -> bases de CVEs -> man pages -> construcción del comando nc
```

**Learning chain:** Investigación web -> dorking -> CVE/NVD -> man pages -> flags de herramientas -> verificación empírica.

**Lección:** *La investigación metódica y la lectura de la documentación local valen más que la memorización: saber formular la consulta correcta y consultar la fuente primaria (CVE, man) resuelve el problema sin adivinar.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1590 (Gather Victim Network Information), T1210 (Exploitation of Remote Services)

**Fuente:** [TryHackMe - Introductory Researching](https://tryhackme.com/room/introductoryresearching)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.