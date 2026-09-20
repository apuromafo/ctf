# Dear QA

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `dearqa` | [TryHackMe](https://tryhackme.com/room/dearqa) | 01 Level Easy | THM | PWN, Buffer Overflow, x64, Explotación de binario | Explotación de binarios x64 |

> **Objeto:** Analizar un binario vulnerable (ret2win/buffer overflow) en arquitectura x64, identificar la arquitectura del objetivo y explotarlo para obtener el shell y la flag.

---

**Contexto:** Sala de PWN centrada en un binario vulnerable. El objetivo es analizar el fichero (arquitectura y protecciones), identificar la vulnerabilidad de desbordamiento de búfer y explotarla para recuperar la flag.

> **ES:** Analiza el binario, confirma la arquitectura x64, explota el desbordamiento y captura la flag.
> **EN:** Analyse the binary, confirm the x64 architecture, exploit the overflow and capture the flag.

## Solucionario

### Task 1: Análisis / Analysis
**Explicación:** Preparación del laboratorio y análisis inicial del binario vulnerable.

No answer needed

### Task 2: Explotación / Exploitation
**Explicación:** Determinación de la arquitectura del binario y explotación del desbordamiento para obtener la flag.

1. x64
2. THM{PWN_1S_V3RY_E4SY}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Arquitectura del binario | `x64` |
| 2.2 | Flag de la sala | `THM{PWN_1S_V3RY_E4SY}` |

---

**Metodología:** Análisis del binario con herramientas de trazado y desensamblado, identificación de la arquitectura (x64) y de la vulnerabilidad de buffer overflow, cálculo del offset, control del flujo de ejecución y obtención de la flag.

### Cadena de ataque / Attack Chain

Binario → análisis estático → x64 → buffer overflow → control del RIP → shell → flag.

**Learning chain:** binario → análisis → x64 → overflow → ret2win → flag

*Lección:* Los binarios con buffers vulnerables y sin protecciones adecuadas de pila son explotables fácilmente incluso en x64.

**MITRE ATT&CK:** TA0002 Execution, TA0004 Privilege Escalation, T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Dear QA](https://tryhackme.com/room/dearqa)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.