# Annie
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `annie` |
| **Link** | [TryHackMe](https://tryhackme.com/room/annie) |
| **Sección** | Linux / CTF |
| **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Linux, enumeración (puertos/servicios/archivos), acceso inicial, escalada de privilegios (Linux 5.5.2 / Ubuntu) |
| **Impacto** | Sala de CTF Linux de nivel medio que implica enumeración, acceso inicial y escalada de privilegios para encontrar las flags user.txt y root.txt. |
---
**Contexto:** Sala de CTF Linux de nivel medio que implica enumeración, acceso inicial y escalada de privilegios para encontrar las flags user.txt y root.txt.
*EN: Medium-level Linux CTF room involving enumeration, initial access, and privilege escalation to find the user.txt and root.txt flags.*
## Solucionario
### Task 1 — Flags
**Explicación:** Cadena de ataque: enumeración exhaustiva (puertos, servicios y archivos) → acceso inicial mediante las vulnerabilidades identificadas → escalada de privilegios hasta root (vía kernel/exploit local) → obtención de las flags. La enumeración es clave para encontrar vectores de ataque en sistemas Linux.
*EN: Attack chain: exhaustive enumeration (ports, services, files) → initial access through identified vulnerabilities → privilege escalation to root → flags. Thorough enumeration is key to finding Linux attack vectors.*

```
Enumeración → Acceso Inicial → Escalada de Privilegios → Obtención de Flags
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is user.txt? | `THM{N0t_Ju5t_ANY_D3sk}` |
| 2 | What is root.txt? | `THM{0nly_th3m_5.5.2_D3sk}` |
---
**Metodología:** Enumeración inicial (puertos, servicios, archivos) → acceso inicial → escalada de privilegios hasta root → extracción de user.txt y root.txt.
**Learning chain:** enumeración → explotación del servicio expuesto → escalada local → flags.
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - Annie](https://tryhackme.com/room/annie)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
