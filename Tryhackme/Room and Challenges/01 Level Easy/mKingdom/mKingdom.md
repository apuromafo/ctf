# mKingdom

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (boT2root) | `mkingdom` | https://tryhackme.com/room/mkingdom | 01 Level Easy | TryHackMe | Reconocimiento web / explotación / escalada de privilegios en Linux / flags de usuario y root | Boot2root de nivel Easy: comprometer la máquina mKingdom y recuperar las flags de usuario y de root. |

---

**Contexto:** Sala tipo CTF del catálogo de TryHackMe. El objetivo es comprometer la máquina mKingdom completando las fases de acceso inicial y escalada de privilegios, recuperando una flag de usuario y una flag de root. El registro de respuestas de esta migración conserva únicamente las dos flags finales del recorrido.

> **ES:** Enumerar la máquina, obtener acceso inicial y escalar privilegios para recuperar la flag de usuario y la de root.
> **EN:** Enumerate the target, gain initial access and escalate privileges to recover the user flag and the root flag.

## Solucionario

### Task 1: Obtener la flag de usuario / Capture the user flag

**Explicación:** La primera fase del reto consiste en ganar acceso a la máquina y localizar la flag de usuario (formato `thm{...}`). Corresponde a la primera respuesta registrada en la sala.

Contenido original de la tarea / Original task content:

```text
1. thm{030a769febb1b3291da1375234b84283}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario / User flag | `thm{030a769febb1b3291da1375234b84283}` |

### Task 2: Escalada y flag de root / Privilege escalation and root flag

**Explicación:** La segunda fase del reto consiste en escalar privilegios hasta el usuario root y recuperar la flag de root (formato `thm{...}`). Corresponde a la segunda respuesta registrada en la sala.

Contenido original de la tarea / Original task content:

```text
2. thm{e8b2f52d88b9930503cc16ef48775df0}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de root / Root flag | `thm{e8b2f52d88b9930503cc16ef48775df0}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario / User flag | `thm{030a769febb1b3291da1375234b84283}` |
| 2 | Flag de root / Root flag | `thm{e8b2f52d88b9930503cc16ef48775df0}` |

---

**Metodología:** Recorrer las fases clásicas de un boot2root: enumeración del objetivo y acceso inicial, obtención de la flag de usuario, escalada de privilegios a root y captura de la flag final.

### Cadena de ataque / Attack Chain

```text
Reconocimiento -> acceso inicial -> flag de usuario (thm{...}) -> escalada de privilegios -> flag de root (thm{...})
```

**Learning chain:** Enumeración -> explotación/acceso inicial -> flag de usuario -> escalada de privilegios -> flag de root.

**Lección:** *El modelo de dos flags (usuario y root) obliga a completar una cadena completa de explotación y escalada antes de cerrar una máquina.* 

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - mKingdom](https://tryhackme.com/room/mkingdom)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.