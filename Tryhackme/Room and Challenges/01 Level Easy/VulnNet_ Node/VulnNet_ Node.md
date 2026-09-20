# VulnNet_ Node

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `vulnnetnode` | [TryHackMe](https://tryhackme.com/room/vulnnetnode) | 01 Level Easy | THM | Node.js, enumeración web, NPM, desarrollo de exploits, escalada de privilegios, user.txt, root.txt | Resolución completa del reto |

---

**Contexto:** Box Linux que combina una aplicación web basada en Node.js con el acceso a un repositorio NPM interno. Se explota la funcionalidad de la web para descubrir credenciales, se crea un paquete malicioso que se propaga como update de una dependencia y se consigue acceso como el usuario node; después se escala privilegios para obtener root.

> **ES:** Box Linux: aplicación web Node.js → credenciales por enumeración → paquete malicioso como actualización NPM → shell como node → escalada de privilegios → root; flags user.txt y root.txt.
> **EN:** Linux box: Node.js web app → credentials via enumeration → malicious package as an NPM update → shell as node → privilege escalation to root; user.txt and root.txt flags.

## Solucionario

### Task 1: Encuentra las flags / Find the flags

**Explicación:** Se explota la aplicación Node.js para obtener credenciales, se produce un paquete malicioso que se distribuye como update dentro de una instancia de la máquina y, tras conseguir acceso como el usuario node, se escala a root.

1. `THM{064640a2f880ce9ed7a54886f1bde821}`
2. `THM{abea728f211b105a608a720a37adabf9}`

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the user flag? | `THM{064640a2f880ce9ed7a54886f1bde821}` |
| 2 | What is the root flag? | `THM{abea728f211b105a608a720a37adabf9}` |

---

**Metodología:** nmap (22 SSH, 80 Node.js) → enumeración web → credenciales → creación de paquete malicioso (update de dependencia NPM) → acceso como node → enumeración post-explotación → escalada de privilegios → root. Captura de user.txt y root.txt.

### Cadena de ataque / Attack Chain

Reconocimiento (Node.js en :80) → Enumeración web → Credenciales → Paquete NPM malicioso (update) → Acceso como node → Escalada de privilegios → root → user.txt → root.txt

**Learning chain:** Enumeration → Node.js web exploitation → NPM supply-chain (malicious update) → user access → privilege escalation → root

**Lección:** *El desarrollo de exploits no solo consiste en vulnerabilidades de código: el ecosistema de dependencias (NPM) y las configuraciones por defecto de desarrollo permiten inyectar actualizaciones maliciosas que se ejecutan con los privilegios del proceso que las consume.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1071 (Application Layer Protocol), T1068 (Exploitation for Privilege Escalation), T1195 (Supply Chain Compromise)

**Fuente:** [TryHackMe - VulnNet: Node](https://tryhackme.com/room/vulnnetnode)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.