# Oh My WebServer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | ohmywebserver | https://tryhackme.com/room/ohmywebserver | 02 Level Medium | TryHackMe | Apache 2.4.49, path traversal + CGI (CVE-2021-41773), capabilities cap_setuid, Docker, OMI WMI (CVE-2021-38647, OMIGOD) | Compromiso total del entorno: explotación del path traversal + CGI de Apache 2.4.49 en un contenedor Docker, escalada a root por capabilities (cap_setuid + python3.7) y salto lateral a un host Windows con OMI vulnerable (CVE-2021-38647). |

---

**Contexto:** La sala **Oh My WebServer** es un reto CTF de dificultad media que mezcla varias etapas. El acceso inicial explota el **path traversal + CGI** de **Apache/2.4.49** (CVE-2021-41773) para ejecutar comandos dentro de un **contenedor Docker**. Desde la shell del contenedor se escala a root mediante las **capabilities** del SO (contando con `python3.7` en el sistema) y, tras descubrir que el contenedor tiene acceso a una red interna (`172.17.0.1`), se salta a un host Windows que expone un agente **OMI (Open Management Infrastructure)** vulnerable a **CVE-2021-38647 (OMIGOD)**, ejecutando RCE sin autenticación y recuperando las flags de usuario y root.

> **ES:** CTF medio que encadena CVE-2021-41773 (path traversal + CGI en Apache 2.4.49), escalada por capabilities en un contenedor Docker y RCE sin autenticación contra OMI/OMIGOD (CVE-2021-38647) en un host Windows.
> **EN:** A medium CTF chaining CVE-2021-41773 (Apache 2.4.49 path traversal + CGI), capability-based escalation inside a Docker container, and unauthenticated RCE against OMI/OMIGOD (CVE-2021-38647) on a Windows host.

## Solucionario

### Task 1: Flag de Usuario / User Flag
**Explicación:** Se explota el conocido path traversal con activación de CGI de Apache 2.4.49 (CVE-2021-41773): peticiones codificadas con `.%2e` permiten leer ficheros fuera de la document root y, combinadas con `mod_cgi`, ejecutar comandos (`cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh`). Con esa shell inicial se consigue la flag de usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? / ¿Cuál es la flag de usuario? | `THM{eacffefe1d2aafcc15e70dc2f07f7ac1}` |

### Task 2: Flag de Root / Root Flag
**Explicación:** En el contenedor, el proceso de Apache cuenta con capabilities especiales: aplicando la escalada estándar con `cap_setuid` (cambio de UID a 0 para root) y usando el Python disponible (por ejemplo `python3.7`) se consigue root en el contenedor. El descubrimiento de la red `172.17.0.1` permite saltar al host Windows, que expone OMI en el puerto 5986; con un exploit de **CVE-2021-38647 (OMIGOD)** se obtiene RCE sin autenticación y se lee la flag de root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root flag? / ¿Cuál es la flag de root? | `THM{7f147ef1f36da9ae29529890a1b6011f}` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? / ¿Cuál es la flag de usuario? | `THM{eacffefe1d2aafcc15e70dc2f07f7ac1}` |
| 2 | What is the root flag? / ¿Cuál es la flag de root? | `THM{7f147ef1f36da9ae29529890a1b6011f}` |

---

**Metodología:** Reconocimiento (puertos 80, 5986) → explotación de CVE-2021-41773 (path traversal + CGI) en Apache 2.4.49 → shell en el contenedor Docker → escalada a root del contenedor con cap_setuid + python3.7 → pivoting hacia 172.17.0.1 (host Windows) → RCE sin autenticación contra OMI con CVE-2021-38647 → flags de usuario y root.

**Learning chain:** Apache 2.4.49 path traversal + CGI → RCE en el contenedor → escalada por capabilities (cap_setuid) → descubrimiento de la red interna → OMI/WMI (5986) → CVE-2021-38647 (OMIGOD) → compromiso del host Windows.

**Lección:** *Una versión vulnerable de Apache dentro de un contenedor no es un límite seguro: combinando path traversal + CGI, capabilities mal concedidas y un vecino Windows mal expuesto, el perímetro completo se derrumba.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1059.003 (Command and Scripting Interpreter: Windows Command Shell) · T1068 (Exploitation for Privilege Escalation) · T1021.001 (Remote Services: Remote Desktop Protocol) · T1021.006 (Remote Services: Windows Remote Management) · T1210 (Exploitation of Remote Services).

**Fuente:** [TryHackMe - Oh My WebServer](https://tryhackme.com/room/ohmywebserver)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.