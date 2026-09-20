# The Blob Blog
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Challenge / Boot2Root | theblobblog | https://tryhackme.com/room/theblobblog | 02 Level Medium | TryHackMe | Linux, blog web, enumeración de servicios, explotación web, escalada de privilegios | Compromiso de la máquina de bobloblaw hasta obtener las flags de usuario y root |

> **Objeto:** Comprometer con éxito el equipo de bobloblaw y capturar las flags de usuario y de root.

---
**Contexto:** La sala **The Blob Blog** es un reto tipo boot2root de dificultad Media sobre una máquina Linux que aloja el blog de *bobloblaw*. El objetivo es enumerar los servicios expuestos, analizar la aplicación web y encadenar las vulnerabilidades necesarias para obtener acceso inicial y escalar privilegios. La resolución termina con la captura de dos flags: la de usuario y la de root. Es una sala clásica de práctica de enumeración y explotación de servicios web.
> **ES:** Comprometer con éxito el equipo de bobloblaw.
> **EN:** Successfully hack into bobloblaw's computer.

## Solucionario
### Task 1: Rootear la caja / Root The Box
**Explicación:** Se realiza enumeración de la máquina y de la aplicación web para identificar la superficie de ataque; tras explotar los vectores encontrados se obtiene acceso y se escala hasta root. La tarea solicita dos respuestas: la flag de usuario y la flag de root.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| User Flag | `THM{C0NGR4t$_g3++ing_this_fur}` |
| Root Flag | `THM{G00D_J0B_G3++1NG+H3R3!}` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User Flag | `THM{C0NGR4t$_g3++ing_this_fur}` |
| 2 | Root Flag | `THM{G00D_J0B_G3++1NG+H3R3!}` |

---
**Metodología:** Enumeración de servicios → análisis de la superficie web del blog → explotación del vector → acceso inicial → escalada de privilegios → captura de user y root.

### Cadena de ataque / Attack Chain
```
Reconocimiento/enumeración -> superficie web (The Blob Blog) -> explotación -> acceso inicial -> escalada de privilegios -> user flag + root flag
```
**Learning chain:** Enumeración → descubrimiento del vector → explotación → acceso → escalada → flags.
**Lección:** *Una enumeración minuciosa de los servicios expuestos es lo que revela el camino hasta root en un boot2root.*
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - The Blob Blog](https://tryhackme.com/room/theblobblog)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
