# Shells Overview

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Walkthrough | `shellsoverview` | https://tryhackme.com/room/shellsoverview | 01 Level Easy | TryHackMe | Reverse Shell / Bind Shell / Netcat / socat / rlwrap / ncat / Python / PHP / Web Shell / flags | Formativo: comprender los tipos de shell (reverse, bind y web), las herramientas para crearlas y estabilizarlas, y practicar el modelo obteniendo dos flags. |

---

**Contexto:** Sala introductoria sobre shells. Explica por qué un atacante quiere conseguir una shell (para navegar por el sistema, pivotar y escalar privilegios), diferencia una **reverse shell** de una **bind shell**, presenta las herramientas para crearlas (`netcat`, `socat`), los métodos para estabilizarlas (`rlwrap`, `ncat`, Python) y cómo obtenerlas a través de aplicaciones web (subida de archivos sin restricciones + **web shell**). Termina con un ejercicio práctico que entrega dos flags.

> **ES:** "Shells Overview" — los fundamentos de reverse shells, bind shells y web shells, con las herramientas para crearlas (netcat, socat) y estabilizarlas (rlwrap, ncat, Python, PHP).
> **EN:** "Shells Overview" — the fundamentals of reverse shells, bind shells and web shells, with the tools to create them (netcat, socat) and to stabilise them (rlwrap, ncat, Python, PHP).

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de la terminal interactiva. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start the room and read the intro. / Inicia la sala y lee la introducción. | `No answer needed` |

### Task 2: Razones para obtener una shell / Reasons to Get a Shell

**Explicación:** Una vez obtenida una shell se pueden hacer tres cosas: tener una **shell** para ejecutar comandos, **pivotar** hacia otras máquinas de la red y **escalar privilegios** (`Privilege Escalation`) dentro del sistema comprometido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | First thing you can do once you get a shell. / Primera cosa que puedes hacer al obtener una shell. | `Shell` |
| 3 | Second thing you can do once you get a shell. / Segunda cosa que puedes hacer al obtener una shell. | `Pivoting` |
| 4 | Third thing you can do once you get a shell. / Tercera cosa que puedes hacer al obtener una shell. | `Privilege Escalation` |

### Task 3: Reverse Shell / Reverse Shell

**Explicación:** La **reverse shell** hace que la víctima se conecte de vuelta al atacante; la herramienta típica para escuchar y lanzar este tipo de shell es `netcat`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | Type of shell that connects back to the attacker. / Tipo de shell que se conecta de vuelta al atacante. | `Reverse Shell` |
| 6 | Tool used to handle this shell. / Herramienta usada para manejarla. | `Netcat` |

### Task 4: Bind Shell / Bind Shell

**Explicación:** La **bind shell** abre un puerto en la máquina víctima (el puerto `1024` en el ejemplo) al que el atacante se conecta para obtener la shell.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | Type of shell that listens on a port of the target. / Tipo de shell que escucha en un puerto del objetivo. | `Bind Shell` |
| 8 | Port number used in the example. / Número de puerto usado en el ejemplo. | `1024` |

### Task 5: Herramientas de shell / Shell Tools

**Explicación:** Las herramientas que presenta la sala para trabajar con shells son `socat` (más potente que netcat, permite shells totalmente interactivas), `rlwrap` (añade historial y edición de línea para netcat) y `ncat` (la versión de Nmap).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9 | First shell tool. / Primera herramienta de shell. | `socat` |
| 10 | Second shell tool. / Segunda herramienta de shell. | `rlwrap` |
| 11 | Third shell tool. / Tercera herramienta de shell. | `ncat` |

### Task 6: Spawning de shells / Spawning Shells

**Explicación:** Para lanzar una shell desde distintos entornos, la sala menciona el módulo `subprocess` de Python y los lenguajes `PHP` y `Python` como vías para spawnear una shell dentro del sistema.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 12 | Python module used to spawn a shell. / Módulo de Python usado para lanzar una shell. | `subprocess` |
| 13 | Language used to spawn a shell. / Lenguaje usado para lanzar una shell. | `PHP` |
| 14 | Language used to spawn a shell. / Lenguaje usado para lanzar una shell. | `Python` |

### Task 7: Web Shells / Web Shells

**Explicación:** Para obtener una web shell en una aplicación web se necesita una subida de archivos sin restricciones (`Unrestricted File Upload`) y alojar el **web shell** como payload que se ejecuta en el servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 15 | File upload condition needed to upload a web shell. / Condición de subida necesaria para cargar una web shell. | `Unrestricted File Upload` |
| 16 | Payload that gets uploaded to the server. / Payload que se sube al servidor. | `Web Shell` |

### Task 8: Ejercicio práctico / Practical

**Explicación:** La sala incluye un ejercicio práctico en el que se aplican los conceptos de las tareas anteriores y se obtienen dos flags.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 17 | First flag. / Primera flag. | `THM{0f28b3e1b00becf15d01a1151baf10fd713bc625}` |
| 18 | Second flag. / Segunda flag. | `THM{202bb14ed12120b31300cfbbbdd35998786b44e5}` |

### Task 9: Conclusión / Conclusion

**Explicación:** Cierre de la sala repasando lo aprendido sobre shells. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 19 | Complete the room. / Completa la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start the room and read the intro. | `No answer needed` |
| 2 | First thing you can do once you get a shell. | `Shell` |
| 3 | Second thing you can do once you get a shell. | `Pivoting` |
| 4 | Third thing you can do once you get a shell. | `Privilege Escalation` |
| 5 | Type of shell that connects back to the attacker. | `Reverse Shell` |
| 6 | Tool used to handle this shell. | `Netcat` |
| 7 | Type of shell that listens on a port of the target. | `Bind Shell` |
| 8 | Port number used in the example. | `1024` |
| 9 | First shell tool. | `socat` |
| 10 | Second shell tool. | `rlwrap` |
| 11 | Third shell tool. | `ncat` |
| 12 | Python module used to spawn a shell. | `subprocess` |
| 13 | Language used to spawn a shell. | `PHP` |
| 14 | Language used to spawn a shell. | `Python` |
| 15 | File upload condition needed to upload a web shell. | `Unrestricted File Upload` |
| 16 | Payload that gets uploaded to the server. | `Web Shell` |
| 17 | First flag. | `THM{0f28b3e1b00becf15d01a1151baf10fd713bc625}` |
| 18 | Second flag. | `THM{202bb14ed12120b31300cfbbbdd35998786b44e5}` |
| 19 | Complete the room. | `No answer needed` |

---

**Metodología:** Comprender la diferencia entre reverse shell y bind shell, conocer las herramientas para crearlas (`netcat`, `socat`) y estabilizarlas (`rlwrap`, `ncat`), saber spawnear shells con lenguajes (`subprocess` en Python, `PHP`) y relacionar la subida de archivos sin restricciones con las web shells, cerrando con el ejercicio práctico de dos flags.

### Cadena de ataque / Attack Chain

```text
concepto de shell -> reverse shell (netcat) -> bind shell (puerto 1024) -> socat / rlwrap / ncat -> subprocess / PHP / Python -> Unrestricted File Upload + Web Shell -> flags THM{...}
```

**Learning chain:** Shell types -> Reverse vs Bind shells -> netcat / socat / rlwrap / ncat -> spawning shells (Python subprocess, PHP) -> Web Shells (unrestricted upload) -> practical flags.

**Lección:** *Dominar los tipos de shell (reverse, bind y web), sus herramientas y sus métodos de estabilización es la base de cualquier acceso inicial y de la post-explotación: con un simple web shell subido sin restricciones suele empezar toda la intrusión.*

**MITRE ATT&CK:** T1059.006 — Command and Scripting Interpreter: Python; T1505.003 — Server Software Component: Web Shell; T1105 — Ingress Tool Transfer; T1021.004 — Remote Services: SSH

**Fuente:** [TryHackMe - Shells Overview](https://tryhackme.com/room/shellsoverview)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.