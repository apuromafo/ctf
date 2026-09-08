# AVenger
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `avenger` |
| **Link** | [TryHackMe](https://tryhackme.com/room/avenger) |
| **Sección** | Windows / CTF |
| **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Linux, enumeración, acceso inicial, escalada de privilegios (vector específico de la sala) |
| **Impacto** | Sala de CTF (Premium) de nivel medio en la que hay que comprometer un sistema para obtener las flags de usuario y root. |
---
**Contexto:** Sala de CTF (Premium) de nivel medio en la que hay que comprometer un sistema para obtener las flags de usuario y root. Nota: la sala se lista en contexto Windows pero el flujo es de compromiso Linux.
*EN: Medium-level CTF room (Premium) where you must compromise the system to obtain user and root flags. Note: the room is listed under Windows context but the flow is a Linux compromise.*
## Solucionario
### Task 1 — Flags
**Explicación:** Cadena de ataque: enumerar el objetivo para descubrir servicios y vulnerabilidades explotables → obtener acceso inicial como usuario y capturar la flag de usuario → escalar privilegios hasta root para obtener la flag. La identificación correcta de vectores de escalada de privilegios permite completar la cadena de compromiso hasta root.
*EN: Attack chain: enumerate the target to discover exploitable services and vulnerabilities → gain initial access and grab the user flag → escalate privileges to root for the root flag. Correctly identifying privilege escalation vectors completes the chain to root.*

```
Enumeración → Acceso Inicial → User Flag → Escalada de Privilegios → Root
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which is the user flag? | `THM{WITH_GREAT_POWER_COMES_GREAT_RESPONSIBILITY}` |
| 2 | Which is the root flag? | `THM{I_CAN_DO_THIS_ALL_DAY}` |
---
**Metodología:** Enumeración → acceso inicial (user flag) → escalada de privilegios → root flag.
**Learning chain:** enumeración → explotación → escalada de privilegios → compromiso total.
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - AVenger](https://tryhackme.com/room/avenger)