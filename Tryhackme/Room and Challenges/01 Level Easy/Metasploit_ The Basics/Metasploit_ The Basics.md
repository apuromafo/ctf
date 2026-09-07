# Metasploit: The Basics

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `metasploitthebasics` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/metasploitthebasics) |
| **Sección** | Exploitation Frameworks |
| **Fuente** | THM |
| **Componentes** | msfconsole, exploit/payload modules, meterpreter, msfvenom |
| **Impacto** | Medium |

---

**Contexto:** Metasploit es el framework de explotación más utilizado en penetration testing y red teaming. Este room cubre los fundamentos del framework: módulos, payloads, configuración de opciones y el ciclo básico de explotación, desde la selección del exploit hasta la obtención de una sesión en el objetivo.

## Solucionario

### Task 2: Introduction to Metasploit

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
**Learning chain:** Metasploit framework → Módulos (exploit/payload/stager) → Configuración de opciones → Explotación → Sesiones Meterpreter
**MITRE ATT&CK:** T1203 - Exploitation for Client Execution, T1059 - Command and Scripting Interpreter
**Fuente:** [TryHackMe - Metasploit: The Basics](https://tryhackme.com/r/room/metasploitthebasics)
