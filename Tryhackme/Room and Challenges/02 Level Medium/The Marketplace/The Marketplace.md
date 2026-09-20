# The Marketplace
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Challenge / Web (Boot2Root) | themarketplace | https://tryhackme.com/room/themarketplace | 02 Level Medium | TryHackMe | Linux, aplicación web (marketplace), vulnerabilidades web, escalada de privilegios | Compromiso de la infraestructura de The Marketplace hasta root y captura de las tres flags |

> **Objeto:** Tomar el control de la infraestructura de The Marketplace y obtener acceso root.

---
**Contexto:** **The Marketplace** es una sala de tipo boot2root de dificultad Media. El administrador del sistema, *Michael*, ha dado acceso a un servidor interno para hacer pentesting de la plataforma marketplace que su equipo está desarrollando, advirtiendo que aún quedan algunos bugs por pulir. El reto consiste en aprovechar esas debilidades de la aplicación web para ganar acceso al servidor y, finalmente, escalar hasta **root**. La sala pide tres respuestas: la flag 1, la flag de usuario (`User.txt`) y la flag de root (`Root.txt`).
> **ES:** ¿Puedes tomar el control de la infraestructura de The Marketplace?
> **EN:** Can you take over The Marketplace's infrastructure?

## Solucionario
### Task 1: The Marketplace / The Marketplace
**Explicación:** Se realiza enumeración del servidor interno y se analiza la aplicación marketplace para localizar los bugs mencionados por Michael. Aprovechando las vulnerabilidades de la plataforma se obtiene una primera flag (flag 1), después acceso al sistema y finalmente se escala privilegios hasta root, recuperando las flags de usuario y de root.

Descripción original de la tarea:

> The sysadmin of **The Marketplace**, Michael, has given you access to an internal server of his, so you can pentest the marketplace platform he and his team has been working on. He said it still has a few bugs he and his team need to iron out.
> Can you take advantage of this and will you be able to gain root access on his server?

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is flag 1? | `THM{c37a63895910e478f28669b048c348d5}` |
| What is flag 2? (User.txt) | `THM{c3648ee7af1369676e3e4b15da6dc0b4}` |
| What is flag 3? (Root.txt) | `THM{d4f76179c80c0dcf46e0f8e43c9abd62}` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is flag 1? | `THM{c37a63895910e478f28669b048c348d5}` |
| 2 | What is flag 2? (User.txt) | `THM{c3648ee7af1369676e3e4b15da6dc0b4}` |
| 3 | What is flag 3? (Root.txt) | `THM{d4f76179c80c0dcf46e0f8e43c9abd62}` |

---
**Metodología:** Enumeración del servidor interno → análisis de la aplicación web marketplace → explotación de los bugs encontrados → obtención de la flag 1 → acceso al sistema → escalada de privilegios a root → captura de User.txt y Root.txt.

### Cadena de ataque / Attack Chain
```
Enumeración (servidor + web marketplace) -> identificar bugs de la plataforma
-> explotación web -> flag 1 -> acceso inicial -> escalada de privilegios a root
-> User.txt + Root.txt
```
**Learning chain:** Enumeración → análisis web → explotación → acceso → escalada → flags.
**Lección:** *Basta con "unos pocos bugs" en una aplicación interna para comprometer toda la infraestructura y alcanzar root.*
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - The Marketplace](https://tryhackme.com/room/themarketplace)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
