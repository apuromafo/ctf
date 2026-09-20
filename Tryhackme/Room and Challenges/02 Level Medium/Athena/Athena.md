# Athena

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | athena | https://tryhackme.com/room/athena | 02 Level Medium | TryHackMe | Windows, Web App, Escalada de privilegios | Compromiso total de la máquina |

---

**Contexto:** La sala **Athena** es un CTF de una máquina Windows con una aplicación web expuesta. El flujo de resolución pasa por enumerar la superficie web, explotar la aplicación para ganar acceso inicial, moverse por el sistema y escalar privilegios hasta el máximo nivel, recolectando las flags (hashes MD5) que acreditan cada etapa del compromiso. Las respuestas documentan los dos valores finales obtenidos durante la explotación.

## Solucionario

### Task 1: Compromiso de la máquina
**Explicación:**

Se enumera la máquina y se identifica la aplicación web vulnerable, se explota para obtener un shell y se escala privilegios dentro del sistema Windows. Cada etapa validada devuelve un flag en formato hash MD5 que acredita el compromiso.

1. `857c4a4fbac638afb6c7ee45eb3e1a28`
2. `aecd4a3497cd2ec4c71a2315030bd48`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag/valor obtenido en la tarea 1 | `857c4a4fbac638afb6c7ee45eb3e1a28` |
| 1.2 | Flag/valor obtenido en la tarea 1 | `aecd4a3497cd2ec4c71a2315030bd48` |

---

**Metodología:** Enumeración web y de servicios, explotación de la aplicación Windows, obtención de acceso inicial, escalada de privilegios y captura de flags (hashes MD5).

**Learning chain:** Reconocimiento → análisis de la app web → explotación → acceso → escalada → flags.

**Lección:** *Cada bandera de un CTF es un punto de verificación: unir cada hash a su fase permite reconstruir la cadena de compromiso completa.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1068 Exploitation for Privilege Escalation · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Athena](https://tryhackme.com/room/athena)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.