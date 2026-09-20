# Thompson

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `thompson` | [TryHackMe - Thompson](https://tryhackme.com/room/thompson) | 01 Level Easy | THM | Jenkins, reverse shell, escalada de privilegios | Explotación de Jenkins para ejecución remota de comandos (RCE) y escalada de privilegios |

---

**Contexto:** Máquina Linux de dificultad fácil: se explota una instancia de Jenkins para obtener una reverse shell y, mediante credenciales locales, escalar privilegios a root.

> **ES:** El reto consiste en comprometer una máquina que ejecuta Jenkins, abusando de la consola de scripts para obtener ejecución de código y escalar a root.
> **EN:** The challenge involves compromising a machine running Jenkins, abusing its script console to gain code execution and escalate to root.

## Solucionario

### Task 1: Banderas / Flags

**Explicación:** Las flags de usuario y de root se obtienen tras explotar Jenkins y escalar privilegios en el sistema.

1. 1. 39400c90bc683a41a8935e4719f181bf
   2. d89d5391984c0450a95497153ae7ca3a

| # | Pregunta / Question | Respuesta / Answer |
|---|---|---|
| 1 | User flag | `39400c90bc683a41a8935e4719f181bf` |
| 2 | Root flag | `d89d5391984c0450a95497153ae7ca3a` |

---

**Metodología:** Se enumeró el servicio web y se detectó Jenkins. Abusando de la Script Console de Jenkins, se ejecutó un payload para obtener una reverse shell; posteriormente se localizaron credenciales que permitieron la escalada a root.

### Cadena de ataque / Attack Chain

1. Reconocimiento y detección de Jenkins en el puerto web.
2. Acceso a la Script Console de Jenkins.
3. Ejecución de payload para obtener una reverse shell.
4. Descubrimiento de credenciales en el sistema.
5. Escalada de privilegios a root.

**Learning chain:** Enumeration → Jenkins → RCE → reverse shell → credential discovery → privilege escalation

**Lección:** *Una consola de administración de Jenkins expuesta permite ejecución remota de código, y las credenciales almacenadas en el sistema completan la escalada a root.*

**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter, T1068 - Exploitation for Privilege Escalation, T1082 - System Information Discovery

**Fuente:** [TryHackMe - Thompson](https://tryhackme.com/room/thompson)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.