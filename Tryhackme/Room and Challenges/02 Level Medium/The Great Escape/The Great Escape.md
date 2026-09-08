# The Great Escape

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `thegreatescape` |
| **Link** | [TryHackMe](https://tryhackme.com/room/thegreatescape) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | web exploit / container escape / privesc / Docker / Linux |
| **Impacto** | Escapar de un entorno de contenedor mediante explotación web y escalada de privilegios para alcanzar el root real y encontrar la flag definitiva |

---

**Contexto:** CTF de Linux centrado en escapar del entorno mediante una explotación inicial vía una aplicación web, seguida de una escalada de privilegios con técnicas de "container escape" o escape de restricciones, que culmina en la obtención de varias flags de root.

## Solucionario

### Task 1: Flag en la Webapp / Webapp Flag

**Explicación:**

Enumerando y analizando la aplicación web se localiza la flag oculta dentro de ella: `THM{b801135794bf1ed3a2aafaa44c2e5ad4}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the flag hidden in the webapp | `THM{b801135794bf1ed3a2aafaa44c2e5ad4}` |

### Task 2: Flags de Root / Root Flags

**Explicación:**

Tras obtener una shell en el host a través de la vulnerabilidad de la webapp y escalar privilegios se lee la primera flag de root: `THM{0cb4b947043cb5c0486a454b75a10876}`. Continuando el proceso de escape del entorno (container/restricciones) hasta alcanzar el root real se captura la flag raíz definitiva: `THM{c62517c0cad93ac93a92b1315a32d734}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the root flag? | `THM{0cb4b947043cb5c0486a454b75a10876}` |
| 2 | Find the real root flag | `THM{c62517c0cad93ac93a92b1315a32d734}` |

---

**Metodología:**

1. Enumerar y analizar la aplicación web hasta localizar la flag oculta dentro de ella.
2. Obtener una shell en el host a través de la vulnerabilidad de la webapp y escalar privilegios para leer la primera flag de root.
3. Continuar el proceso de escape del entorno (container/restricciones) para alcanzar el nivel real de root y capturar la flag raíz definitiva.

**Learning chain:** webapp -> flag oculta -> explotación -> shell -> privesc -> root flag (señuelo) -> escapar del contenedor -> real root flag

**Lección:** *Las flags "falsas" o intermedias pueden actuar como señuelos; hay que continuar la investigación más allá del primer root para escapar de las restricciones del entorno y encontrar la flag real.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1068 (Exploitation for Privilege Escalation) · T1611 (Escape to Host) · T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - The Great Escape](https://tryhackme.com/room/thegreatescape)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
