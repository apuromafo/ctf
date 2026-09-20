# Vulnerabilities 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `vulnerabilities101` | [TryHackMe](https://tryhackme.com/room/vulnerabilities101) | 01 Level Easy | THM | Vulnerabilidades, CVSS, VPR, CVE, NVD, Exploit-DB, Version Disclosure, investigación | Resolución completa de la sala teórica |

---

**Contexto:** Sala que enseña a entender las fallas (flaws) de una aplicación y a aplicar habilidades de investigación sobre bases de datos de vulnerabilidades. Cubre los tipos de vulnerabilidades (Operating System, Application Logic, entre otros), los sistemas de puntuación CVSS y VPR, las bases de datos CVE/NVD y Exploit-DB, y un ejercicio de version disclosure aplicado a un engagement sobre la aplicación de ACKme.

> **ES:** Sala teórica sobre vulnerabilidades: tipos de fallas, puntuación CVSS/VPR, bases de datos CVE/NVD/Exploit-DB, version disclosure y un showcase de explotación sobre la aplicación de ACKme.
> **EN:** Theoretical room on vulnerabilities: flaw types, CVSS/VPR scoring, CVE/NVD/Exploit-DB databases, version disclosure and an exploitation showcase against the ACKme application.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de los objetivos: entender las vulnerabilidades y aplicar técnicas de investigación sobre bases de datos de vulnerabilidades. No requiere respuesta.

1. No answer needed

### Task 2: Introducción a las vulnerabilidades / Introduction to Vulnerabilities

**Explicación:** Se clasifican las vulnerabilidades por tipo: una elevación de privilegios de cuenta de usuario a administrador corresponde al sistema operativo; eludir un panel de login con cookies es una falla de lógica de aplicación.

1. `Operating System`
2. `Application Logic`

### Task 3: Puntuación de vulnerabilidades (CVSS & VPR) / Scoring Vulnerabilities (CVSS & VPR)

**Explicación:** Se presentan los marcos de puntuación: CVSS (introducido en 2005, framework libre y open-source) y VPR (basado en el riesgo para la organización).

1. `2005`
2. `VPR`
3. `CVSS`

### Task 4: Bases de datos de vulnerabilidades / Vulnerability Databases

**Explicación:** Se utilizan bases de datos como NVD y Exploit-DB: el número de CVEs publicados en julio de 2021 según NVD y el autor de Exploit-DB.

1. `1554`
2. `OffSec`

### Task 5: Un ejemplo de búsqueda de una vulnerabilidad / An Example of Finding a Vulnerability

**Explicación:** Se aprovecha la vulnerabilidad Version Disclosure para conocer el nombre y la versión de la aplicación de ejemplo y, con ello, buscar exploits compatibles.

1. `Version Disclosure`

### Task 6: Showcase: explotando la aplicación de ACKme / Showcase: Exploiting Ackme's Application

**Explicación:** Se sigue el showcase completo de explotación de la aplicación de ACKme hasta obtener la flag final del engagement.

1. `THM{ACKME_ENGAGEMENT}`

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala. No requiere respuesta.

1. No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1 | — | `No answer needed` |
| 2.1 | An attacker has been able to upgrade the permissions of their system account from "user" to "administrator". What type of vulnerability is this? | `Operating System` |
| 2.2 | You manage to bypass a login panel using cookies to authenticate. What type of vulnerability is this? | `Application Logic` |
| 3.1 | What year was the first iteration of CVSS published? | `2005` |
| 3.2 | If you wanted to assess vulnerability based on the risk it poses to an organization, what framework would you use? | `VPR` |
| 3.3 | If you wanted to use a framework that was free and open-source, what framework would that be? | `CVSS` |
| 4.1 | Using NVD, how many CVEs were published in July 2021? | `1554` |
| 4.2 | Who is the author of Exploit-DB? | `OffSec` |
| 5 | What type of vulnerability did we use to find the name and version of the application in this example? | `Version Disclosure` |
| 6 | Follow along with the showcase of exploiting ACKme's application to the end to retrieve a flag. What is this flag? | `THM{ACKME_ENGAGEMENT}` |
| 7 | — | `No answer needed` |

---

**Metodología:** 1) Clasificar vulnerabilidades (Operating System, (Mis)Configuration, Application Logic, Human-Factor). 2) Comparar CVSS (2005, libre y open-source) y VPR (orientado al riesgo). 3) Consultar NVD (CVEs de julio 2021: 1554) y Exploit-DB (autor: OffSec). 4) Aplicar Version Disclosure para identificar nombre y versión de la aplicación. 5) Seguir el showcase de explotación de la aplicación de ACKme y capturar la flag del engagement.

### Cadena de ataque / Attack Chain

Introducción a vulnerabilidades → tipos de fallas (OS, lógica de aplicación) → CVSS/VPR → bases de datos (NVD, Exploit-DB) → Version Disclosure → explotación del engagement ACKme → THM{ACKME_ENGAGEMENT}

**Learning chain:** Vulnerability types → CVSS & VPR → NVD/CVE → Exploit-DB → Version Disclosure → exploitation showcase

**Lección:** *Conocer los tipos de vulnerabilidad y las bases de datos de puntuación y referencia (CVSS, VPR, NVD, Exploit-DB) permite convertir un simple detalle como la versión de una aplicación (Version Disclosure) en un vector de explotación completo.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1592 (Gather Victim Host Information), T1210 (Exploitation of Remote Services)

**Fuente:** [TryHackMe - Vulnerabilities 101](https://tryhackme.com/room/vulnerabilities101)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.