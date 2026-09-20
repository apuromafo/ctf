# Search Skills

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `searchskillscS` | [TryHackMe](https://tryhackme.com/room/searchskillscS) | Reconnaissance | THM | Shodan, VirusTotal, CVE databases, GitHub, Technical docs | OSINT y búsqueda de información |

---

**Contexto:** Habilidades de búsqueda OSINT para ciberseguridad: Shodan para IPs, VirusTotal para análisis de archivos, bases de datos CVE, documentación técnica y GitHub para scripts de exploits.

> **ES:** Habilidades de búsqueda OSINT para ciberseguridad: Shodan para IPs, VirusTotal para análisis de archivos, bases de datos CVE, documentación técnica y GitHub para scripts de exploits.
> **EN:** OSINT search skills for cybersecurity: Shodan for IPs, VirusTotal for file analysis, CVE databases, technical documentation and GitHub for exploit scripts.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea introductoria de la room: basta con prepararse para comenzar el recorrido; la respuesta es una confirmación.

| Pregunta | Respuesta |
|----------|-----------|
| Estoy listo para comenzar | Completar |

### Task 2: Shodan (TryScanMe) / Shodan (TryScanMe)

**Explicación:** Se utiliza Shodan para resolver el dominio asociado a la IP proporcionada en el reto.

| Pregunta | Respuesta |
|----------|-----------|
| Dominio asociado con IP 185.243.115.47 | tryscanme.thm |

### Task 3: VirusTotal (TryDetectMe) / VirusTotal (TryDetectMe)

**Explicación:** La tarea requiere consultar VirusTotal en vivo para contar cuántos vendors de seguridad identificaron el archivo como peligroso (depende del static-site de la room).

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántos vendors de seguridad identificaron el archivo como peligroso? | *(Requiere consultar VirusTotal en vivo; interactuar con el static-site de la room)* |

### Task 4: Bases de datos de vulnerabilidades (CVE) / Vulnerability Databases (CVE)

**Explicación:** Se consulta una base de datos CVE en vivo para obtener la clasificación CVSS de la vulnerabilidad.

| Pregunta | Respuesta |
|----------|-----------|
| Clasificación CVSS de la vulnerabilidad | *(Requiere consultar la base de datos CVE en vivo)* |

### Task 5: Documentación técnica (MAN) / Technical Documentation (MAN)

**Explicación:** Se revisa la documentación técnica en vivo para encontrar el comando de ejemplo solicitado.

| Pregunta | Respuesta |
|----------|-----------|
| Comando de ejemplo en la documentación | *(Requiere revisar documentación en vivo)* |

### Task 6: GitHub / GitHub

**Explicación:** Se revisa un repositorio en vivo para localizar el script que demuestra la vulnerabilidad.

| Pregunta | Respuesta |
|----------|-----------|
| Nombre del script en el repositorio que demuestra la vulnerabilidad | *(Requiere revisar repositorio en vivo)* |

> **Nota**: Las tasks T3-T6 dependen de interacción en vivo con servicios externos (VirusTotal, CVE databases, documentación específica). Se recomienda resolverlas directamente en la plataforma.

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Estoy listo para comenzar | `Completar` |
| 2.1 | Dominio asociado con IP 185.243.115.47 | `tryscanme.thm` |
| 3.1 | ¿Cuántos vendors de seguridad identificaron el archivo como peligroso? | `*(Requiere consultar VirusTotal en vivo; interactuar con el static-site de la room)*` |
| 4.1 | Clasificación CVSS de la vulnerabilidad | `*(Requiere consultar la base de datos CVE en vivo)*` |
| 5.1 | Comando de ejemplo en la documentación | `*(Requiere revisar documentación en vivo)*` |
| 6.1 | Nombre del script en el repositorio que demuestra la vulnerabilidad | `*(Requiere revisar repositorio en vivo)*` |

---

**Metodología:** 1) Comenzar la room y confirmar. 2) Resolver el dominio de la IP con Shodan (tryscanme.thm). 3) Consultar VirusTotal para el conteo de vendors. 4) Buscar la clasificación CVSS en bases de datos CVE. 5) Revisar la documentación técnica para el comando de ejemplo. 6) Localizar el script de prueba en el repositorio de GitHub.

### Cadena de ataque / Attack Chain

```text
Confirmación inicial -> Shodan (IP 185.243.115.47 -> tryscanme.thm) -> VirusTotal (vendor detection) -> CVE databases (CVSS) -> Technical documentation (MAN) -> GitHub (exploit script)
```

**Learning chain:** OSINT search fundamentals -> Shodan para IPs -> VirusTotal para archivos -> bases de datos CVE -> documentación técnica -> GitHub

**Lección:** *Las habilidades de búsqueda son la base de la inteligencia: saber dónde (Shodan, VirusTotal, CVE, docs, GitHub) y cómo buscar convierte datos públicos en información accionable.*

**MITRE ATT&CK:** T1596.001 (Search Open Technical Databases: DNS/Passive DNS), T1598.004 (Search Victim-Owned Websites), T1595 (Active Scanning)

**Fuente:** [TryHackMe - Search Skills](https://tryhackme.com/room/searchskillscS)

> **Fuente original / Original source:** https://github.com/Cajac/TryHackMe-Writeups/blob/main/Walkthroughs/Easy/Search_Skills.md | https://github.com/adnansabbir/tryhackme/blob/main/search-skills.md

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.