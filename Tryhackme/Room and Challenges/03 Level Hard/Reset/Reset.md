# Reset

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `resetui` | https://tryhackme.com/room/resetui | 03 Level Hard | TryHackMe | CTF / Windows / UI reset / flags | Reto CTF centrado en el restablecimiento de la interfaz de usuario de Windows: dos flags que validan el análisis de la máquina Windows. |

---

**Contexto:** Sala de reto CTF en un entorno Windows. La mecánica se centra en el restablecimiento de la interfaz de usuario (UI reset / resetui) de la máquina; el contenido original recogido es únicamente el par de flags resultantes de completar las dos fases del análisis.

> **ES:** "Resuelve el reto Windows de reseteo de UI y entrega las dos flags."
> **EN:** "Solve the Windows UI reset challenge and submit the two flags."

## Solucionario

### Task 1: Flags del reto / Challenge flags

**Explicación:** Las dos flags del reto, relacionadas con la automatización y el reaprovechamiento/configuración de la interfaz. Contenido original de la tarea:

```text
1. 1. THM{AUTOMATION_WILL_REPLACE_US}
   2. THM{RE_RE_RE_SET_AND_DELEGATE}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{AUTOMATION_WILL_REPLACE_US}` |
| 2 | Flag 2 del reto. | `THM{RE_RE_RE_SET_AND_DELEGATE}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{AUTOMATION_WILL_REPLACE_US}` |
| 2 | Flag 2 del reto. | `THM{RE_RE_RE_SET_AND_DELEGATE}` |

---

**Metodología:**
1. Acceder al entorno Windows del reto.
2. Analizar la configuración y el comportamiento de la interfaz de usuario (UI reset).
3. Obtener la primera flag tras el análisis inicial.
4. Completar la segunda fase (re-set / delegación de configuración) y capturar la segunda flag.

### Cadena de ataque / Attack Chain

```text
Acceso Windows -> análisis UI / reset -> THM{AUTOMATION_WILL_REPLACE_US} -> re-set + delegación -> THM{RE_RE_RE_SET_AND_DELEGATE}
```

**Learning chain:** `Windows -> UI reset -> automatización -> delegación -> flags`

**Lección:** *Los retos Windows enseñan a inspeccionar la configuración de usuario y sus mecanismos de reutilización; cada fase del reseteo/delegación valida una flag distinta.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1083 (File and Directory Discovery), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Reset](https://tryhackme.com/room/resetui)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.