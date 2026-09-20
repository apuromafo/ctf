# Willow

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | willow | https://tryhackme.com/room/willow | 02 Level Medium | TryHackMe | Linux, explotación, estego/sistema de archivos, escalada de privilegios | Compromiso total de la máquina (usuario y root) |

---

**Contexto:** **Willow** es una máquina de dificultad media con una temática ambientada en un cementerio bajo un sauce llorón. El reto combina explotación de servicios, inspección del sistema de archivos y escalada de privilegios para obtener las flags de usuario y de root, cuyos textos hacen alusión al entorno temático de la sala.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Arranque de la máquina y planteamiento del reto. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Recolección de flags / Flag capture
**Explicación:**

Tras comprometer la máquina se recogen las dos flags del sistema: la del usuario y la de root.

1. `THM{beneath_th_weeping_willow_tree}`
2. `THM{find_a_red_rose_on_the_grave}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Inicio del reto | `No answer needed` |
| 2.1 | Flag del usuario | `THM{beneath_th_weeping_willow_tree}` |
| 2.2 | Flag de root | `THM{find_a_red_rose_on_the_grave}` |

---

**Metodología:** Enumeración de servicios y puertos, explotación del vector inicial, análisis del sistema de archivos y de artefactos ocultos, escalada de privilegios local y captura de las flags de usuario y root.

**Learning chain:** Reconocimiento → explotación del servicio expuesto → acceso inicial → búsqueda de artefactos → escalada de privilegios → captura de flags.

**Lección:** *Los detalles escondidos en el sistema de archivos y los servicios no evidentes de una máquina temática suelen encadenar el camino hacia root.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Willow](https://tryhackme.com/room/willow)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.