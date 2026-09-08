# Aratus
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `aratus` |
| **Link** | [TryHackMe](https://tryhackme.com/room/aratus) |
| **Sección** | Linux / CTF |
| **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Linux, enumeración (servicios/vulnerabilidades), explotación, escalada de privilegios |
| **Impacto** | Sala de CTF Linux de nivel medio donde se debe comprometer un sistema para obtener las flags user.txt y root.txt. |
---
**Contexto:** Sala de CTF Linux de nivel medio donde se debe comprometer un sistema para obtener las flags user.txt y root.txt.
*EN: Medium-level Linux CTF room where you must compromise the system to obtain the user.txt and root.txt flags.*
## Solucionario
### Task 1 — Flags
**Explicación:** Cadena de ataque: enumeración del sistema (identificar servicios y vulnerabilidades) → explotación de vulnerabilidades → acceso inicial → escalada de privilegios a root → obtención de las flags. La combinación de enumeración cuidadosa y explotación permite comprometer sistemas Linux de nivel medio.
*EN: Attack chain: system enumeration (services and vulnerabilities) → exploitation → initial access → privilege escalation to root → flags. Careful enumeration combined with exploitation compromises medium-level Linux systems.*

```
Enumeración → Explotación → Acceso Inicial → Escalada de Privilegios → Obtención de Flags
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user.txt flag? | `THM{ba8d3b87bfdb9d10115cbe24feabbc20}` |
| 2 | What is the root.txt flag? | `THM{d8afc85983603342f6c6979b20e06cf6}` |
---
**Metodología:** Enumeración (servicios y vulnerabilidades) → explotación → acceso inicial → escalada a root → user.txt y root.txt.
**Learning chain:** enumeración → explotación del vector → escalada de privilegios → flags.
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - Aratus](https://tryhackme.com/room/aratus)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
