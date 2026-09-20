# Empline

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `empline` |
| **Link** | [TryHackMe](https://tryhackme.com/room/empline) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Web exploitation / OpenCATS / upload inseguro / Linux / escalada de privilegios / flags |
| **Impacto** | Compromiso de una máquina que ejecuta la aplicación de reclutamiento OpenCATS: acceso inicial, escalada de privilegios y captura de las flags (hashes) |

---

**Contexto:** Empline es una sala CTF construida sobre una aplicación web de gestión de candidatos basada en OpenCATS. Se enumeran los servicios web, se explota una vulnerabilidad de la aplicación (subida de archivos/ejecución) para ganar una shell, y se escala privilegios dentro de la máquina hasta obtener las flags finales en formato hash.

## Solucionario

### Task 1: Acceso inicial

**Explicación:** La primera tarea corresponde a la enumeración y compromiso inicial de la máquina. No requiere introducir ninguna respuesta: la validación se hace accediendo al entorno y explotando la aplicación OpenCATS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compromiso inicial y acceso a la máquina | `No answer needed` |

### Task 2: Flags del reto

**Explicación:** Tras explotar la aplicación y escalar privilegios se obtienen las dos flags del reto en formato hash: **91cb89c70aa2e5ce0e0116dab099078e** y **74fea7cd0556e9c6f22e6f54bc68f5d5**.

1. 91cb89c70aa2e5ce0e0116dab099078e
2. 74fea7cd0556e9c6f22e6f54bc68f5d5

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag (hash) del reto? | `91cb89c70aa2e5ce0e0116dab099078e` |
| 2 | ¿Cuál es la segunda flag (hash) del reto? | `74fea7cd0556e9c6f22e6f54bc68f5d5` |

### Task 3: Cierre

**Explicación:** Tarea de cierre de la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala | `No answer needed` |

---

**Metodología:**

1. Enumerar la máquina objetivo y descubrir el servicio web.
2. Identificar la aplicación (OpenCATS) y localizar una vulnerabilidad explotable (subida de archivos/ejecución).
3. Ganar una shell inicial y enumerar el sistema para la escalada.
4. Escalar privilegios hasta obtener las flags en formato hash.

**Learning chain:** Enumeración -> OpenCATS -> Explotación web -> Shell -> Escalada de privilegios -> Flags

**Lección:** *Las aplicaciones de reclutamiento y sus frameworks (OpenCATS) con subidas de archivos inseguras suelen ser una vía directa hacia una shell remota.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1505.003 (Web Shell)

**Fuente:** [TryHackMe - Empline](https://tryhackme.com/room/empline)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.