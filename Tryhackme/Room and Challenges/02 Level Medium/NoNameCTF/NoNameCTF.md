# NoNameCTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | nonamectf | https://tryhackme.com/room/nonamectf | 02 Level Medium | TryHackMe | Server-Side Template Injection (SSTI), buffer overflow, cadena de suministro de software (paquete pip malicioso) | Compromiso de la máquina mediante explotación de una plantilla vulnerable (SSTI) combinada con un buffer overflow, seguido de un ataque de cadena de suministro con un paquete pip falso que entrega la flag final. |

---

**Contexto:** La sala **NoNameCTF** es un reto CTF de dificultad media que encadena varias técnicas ofensivas. La primera fase se resuelve explotando una **Server-Side Template Injection (SSTI)** junto con un **buffer overflow** para ejecutar código en el objetivo y obtener la primera flag. La segunda fase es un ataque de **cadena de suministro**: se engaña al entorno para que instale un **paquete pip malicioso** que suplanta a uno legítimo, y al ejecutar la instalación el código malicioso entrega la segunda flag. El reto combina así web exploitation y abuso de la confianza en las dependencias de software.

> **ES:** Reto CTF de dificultad media que combina SSTI, buffer overflow y un ataque de cadena de suministro mediante la instalación de un paquete pip falso.
> **EN:** Medium CTF challenge combining SSTI, a buffer overflow, and a supply-chain attack that installs a fake pip package.

## Solucionario

### Task 1: Compromete la máquina (user.txt) / Compromise the Machine (user.txt)
**Explicación:** El objetivo de la primera fase es comprometer la máquina y obtener `user.txt`. Se consigue explotando una **Server-Side Template Injection (SSTI)** concatenada con un **buffer overflow** presente en la aplicación o servicio expuesto. La inyección en la plantilla permite ejecutar código en el lado del servidor y, con el desbordamiento de buffer, se completa el compromiso inicial. La primera flag refleja ambas técnicas: SSTI + buffer overflow.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compromise this machine and obtain user.txt / Compromete la máquina y obtén user.txt. | `THM{SSTI_AND_BUFFER_OVERFLOW_W4S_HERE}` |

### Task 2: Escala privilegios y obtén root.txt / Escalate Privileges and Obtain root.txt
**Explicación:** La última fase escala privilegios dentro del objetivo. Se abusa de la cadena de suministro del software: se suplanta a un paquete legítimo del ecosistema **pip** con una versión maliciosa y, cuando la víctima o el entorno procede a la instalación (paquete pip falso), su código malicioso se ejecuta con los privilegios del proceso y permite escalar, obteniendo `root.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escalate privileges and obtain root.txt / Escala privilegios y obtén root.txt. | `THN{F4KE_PIP_PACKAGE_INSTALL}` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compromise this machine and obtain user.txt / Compromete la máquina y obtén user.txt. | `THM{SSTI_AND_BUFFER_OVERFLOW_W4S_HERE}` |
| 2 | Escalate privileges and obtain root.txt / Escala privilegios y obtén root.txt. | `THN{F4KE_PIP_PACKAGE_INSTALL}` |

---

**Metodología:** Reconocimiento web → detección de template engine → abuso de SSTI para ejecución de código → explotación del buffer overflow → compromiso inicial y extracción de la flag 1 → abuso de la cadena de suministro con un paquete pip falso → ejecución del payload durante la instalación → obtención de la flag 2.

**Learning chain:** SSTI → RCE → buffer overflow → compromiso inicial → supply-chain (pip) → flag final.

**Lección:** *Una dependencia confiable como pip puede convertirse en vector de ataque: instalar paquetes sin verificar su procedencia permite a un atacante ejecutar código con los privilegios del proceso de instalación.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1595.003 (Active Scanning: Wordlist Scanning) · T1059.006 (Command and Scripting Interpreter: Python) · T1195.002 (Supply Chain Compromise: Compromise Software Supply Chain) · T1204.002 (User Execution: Malicious File).

**Fuente:** [TryHackMe - NoNameCTF](https://tryhackme.com/room/nonamectf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.