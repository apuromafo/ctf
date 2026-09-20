# Metasploit: The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Medium | walkthrough | `metasploitthebasics` | [TryHackMe](https://tryhackme.com/r/room/metasploitthebasics) | Exploitation Frameworks | THM | msfconsole, exploit/payload modules, meterpreter, msfvenom | Medium |

> **Objeto:** Conocer los fundamentos del framework Metasploit: módulos, payloads, configuración de opciones y el ciclo básico de explotación sobre un objetivo.

---

**Contexto:** Metasploit es el framework de explotación más utilizado en penetration testing y red teaming. Este room cubre los fundamentos del framework: módulos, payloads, configuración de opciones y el ciclo básico de explotación, desde la selección del exploit hasta la obtención de una sesión en el objetivo.

> **ES:** Sala de fundamentos de Metasploit: módulos, payloads, configuración de opciones y ciclo básico de explotación.
> **EN:** Metasploit basics room: modules, payloads, option configuration and the basic exploitation cycle.

## Solucionario

### Task 2: Introducción a Metasploit / Introduction to Metasploit
**Explicación:** Se identifican los tipos de módulos de Metasploit (exploit, payload) y se practican las búsquedas, la configuración de opciones (LPORT, payload) y la ejecución del exploit para obtener una sesión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the code taking advantage of a flaw on the target system? | `Exploit` |
| 2 | What is the name of the code that runs on the target system to achieve the attacker's goal? | `Payload` |
| 3 | How would you search for all exploit modules related to Apache? | `search type:exploit apache` |
| 4 | How would you set the LPORT value to 6666? | `set LPORT 6666` |
| 5 | What command would you use to clear a set payload? | `unset PAYLOAD` |
| 6 | What command do you use to proceed with the exploitation phase? | `exploit` |
| 7 | What flag do you add to the exploit command to run the exploit but background the session? | `-z` |

---

**Metodología:** Se comienza con `msfconsole` para interactuar con el framework. Se identifican módulos de exploit y payload con `search`, se configuran opciones con `set` y se ejecuta la explotación con `exploit` o `exploit -z` para sesiones en background. El payload se puede deseleccionar con `unset PAYLOAD`.

### Cadena de ataque / Attack Chain

msfconsole → búsqueda de módulos (search) → selección de exploit/payload → configuración de opciones (set) → explotación → sesión en el objetivo.

**Learning chain:** Metasploit framework → Módulos (exploit/payload/stager) → Configuración de opciones → Explotación → Sesiones Meterpreter

*Lección:* Dominar el ciclo módulo-payload-opciones de Metasploit permite explotar servicios de forma repetible y estable.

**MITRE ATT&CK:** T1203 - Exploitation for Client Execution, T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Metasploit: The Basics](https://tryhackme.com/r/room/metasploitthebasics)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.