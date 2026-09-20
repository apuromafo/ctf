# WhyHackMe

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | whyhackme | https://tryhackme.com/room/whyhackme | 02 Level Medium | TryHackMe | Linux, explotación, hashes MD5, escalada de privilegios | Compromiso total de la máquina (obtención de las dos flags) |

---

**Contexto:** **WhyHackMe** es una máquina de dificultad media en la que se combina la explotación de una aplicación o servicio expuesto con la escalada de privilegios local hasta comprometer el sistema por completo. La prueba se completa recogiendo dos flags entregadas como hashes MD5.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Arranque de la máquina y planteamiento del reto. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Recolección de flags / Flag capture
**Explicación:**

Tras explotar el servicio vulnerable y escalar privilegios se recogen las dos flags del sistema, entregadas como hashes MD5.

1. `1ca4eb201787acbfcf9e70fca87b866a`
2. `4dbe2259ae53846441cc2479b5475c72`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Inicio del reto | `No answer needed` |
| 2.1 | Flag 1 del compromiso | `1ca4eb201787acbfcf9e70fca87b866a` |
| 2.2 | Flag 2 del compromiso | `4dbe2259ae53846441cc2479b5475c72` |

---

**Metodología:** Enumeración de servicios, explotación del vector vulnerable, obtención de acceso inicial, escalada de privilegios local y captura de las flags asociadas al usuario y a root.

**Learning chain:** Reconocimiento → explotación del servicio → acceso inicial → escalada de privilegios → captura de flags.

**Lección:** *La enumeración completa de la máquina revela habitualmente más de un camino: el acceso parece trivial cuando se combina reconocimiento y escalada sistemática.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation · T1003 OS Credential Dumping.

**Fuente:** [TryHackMe - WhyHackMe](https://tryhackme.com/room/whyhackme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.