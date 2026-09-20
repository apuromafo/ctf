# Smol
| **Dificultad** | Medium |
| **Tipo** | Boot2Root / Challenge |
| **Slug** | `smol` |
| **Link** | [TryHackMe](https://tryhackme.com/room/smol) |
| **Sección** | Boot2Root / Linux |
| **Fuente** | TryHackMe |
| **Componentes** | WordPress, enumeración web, escalada de privilegios Linux, hashes MD5 |
| **Impacto** | Máquina Linux tipo CTF: enumeración de un sitio WordPress, obtención de acceso inicial y escalada de privilegios hasta root para leer las dos flags (user y root). |
---
**Contexto:** Smol es una máquina Linux de dificultad media orientada a la explotación de una aplicación web (WordPress) con algún componente vulnerable. El reto consiste en enumerar los servicios expuestos, conseguir acceso inicial (normalmente reutilizando credenciales o explotando un plugin/tema) y escalar privilegios hasta `root`. Las dos respuestas son los hashes MD5 de las flags de usuario y de root.
## Solucionario
### Task 1: User Flag / Flag de usuario
**Explicación:** Tras la enumeración de puertos y servicios (web con WordPress, SSH) y el descubrimiento del vector de acceso inicial, se obtiene una shell como usuario no privilegiado y se lee la flag de usuario, cuyo hash MD5 se registra aquí.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the user flag? | `45edaec653ff9ee06236b7ce72b86963` |
### Task 2: Root Flag / Flag de root
**Explicación:** Aplicando la escalada de privilegios local (revisión de permisos SUID, sudoers, cron, credenciales reutilizadas o vulnerabilidad del kernel), se consigue una shell como `root` y se lee la flag final, cuyo hash MD5 se registra aquí.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the root flag? | `bf89ea3ea01992353aef1f576214d4e4` |
---
**Metodología:** `nmap` para enumeración de puertos → enumeración web (WordPress: `wpscan`, plugins/temas y usuarios) → acceso inicial (credenciales o vulnerabilidad) → lectura de `user.txt` → enumeración local y escalada de privilegios → lectura de `root.txt`.
### Cadena de ataque / Attack Chain
```
nmap -> WordPress (wpscan / plugin vulnerable) -> acceso inicial (shell) -> user flag -> enumeración local (SUID/sudo/cron) -> escalada a root -> root flag
```
**Learning chain:** enumeración de servicios → enumeración de CMS → acceso inicial → escalada de privilegios → captura de flags.
**Lección:** *La enumeración minuciosa (versiones, plugins, usuarios y permisos locales) es determinante para encadenar el acceso inicial y la escalada de privilegios en máquinas Linux.*
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts), T1548.001 (Setuid and Setgid), T1068 (Exploitation for Privilege Escalation).
**Fuente:** [TryHackMe - Smol](https://tryhackme.com/room/smol)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
