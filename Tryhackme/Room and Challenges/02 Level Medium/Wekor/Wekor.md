# Wekor

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | wekor | https://tryhackme.com/room/wekor | 02 Level Medium | TryHackMe | Linux, explotación web, hashes MD5, escalada de privilegios | Compromiso total de la máquina (obtención de las dos flags) |

---

**Contexto:** **Wekor** es una máquina de dificultad media estilo *boot2root* en la que, partiendo de un escaneo de puertos, se explota una aplicación web vulnerable para obtener acceso inicial y, posteriormente, escalar privilegios hasta comprometer el sistema por completo. La prueba se completa recogiendo dos flags representadas como hashes MD5.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Arranque de la máquina y planteamiento del reto. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Recolección de flags / Flag capture
**Explicación:**

Tras explotar la aplicación vulnerable y escalar privilegios se recogen las dos flags del sistema, entregadas como hashes MD5.

1. `1a26a6d51c0172400add0e297608dec6`
2. `f4e788f87cc3afaecbaf0f0fe9ae6ad7`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Inicio del reto | `No answer needed` |
| 2.1 | Flag 1 del compromiso | `1a26a6d51c0172400add0e297608dec6` |
| 2.2 | Flag 2 del compromiso | `f4e788f87cc3afaecbaf0f0fe9ae6ad7` |

---

**Metodología:** Enumeración de servicios con nmap, análisis y explotación de la aplicación web, obtención de shell, escalada de privilegios locales y captura de las flags asociadas al usuario y a root.

**Learning chain:** Reconocimiento → explotación web → acceso inicial → escalada de privilegios → captura de flags.

**Lección:** *Una aplicación web mal administrada sigue siendo la puerta de entrada más rentable para comprometer por completo una máquina de nivel medio.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation · T1003 OS Credential Dumping.

**Fuente:** [TryHackMe - Wekor](https://tryhackme.com/room/wekor)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.