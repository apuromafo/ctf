# Memory Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `memoryforensics` | [TryHackMe](https://tryhackme.com/room/memoryforensics) | 01 Level Easy | THM | Volatility, volcados de memoria, PS list, credentials | Análisis forense de volcados de memoria con Volatility |

> **Objeto:** Aplicar Volatility sobre un volcado de memoria para extraer procesos, credenciales y artefactos que responden a las preguntas del reto.

---

**Contexto:** Sala de análisis forense de memoria: se trabaja con un volcado de un sistema Windows usando Volatility, extrayendo información de procesos, usuarios, credenciales y artefactos (comandos, contraseñas) ocultos en la imagen de memoria.

> **ES:** Sala de forensia de memoria: uso de Volatility para extraer procesos, credenciales y artefactos de un volcado.
> **EN:** Memory forensics room: using Volatility to extract processes, credentials and artifacts from a dump.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y del volcado de memoria que se va a analizar.

No answer needed

### Task 2: Usuario del volcado / Dump user
**Explicación:** Se identifica el usuario activo o el perfil de usuario asociado al volcado de memoria.

1. charmander999

### Task 3: Fechas y artefactos / Dates and artifacts
**Explicación:** Se localizan fechas y cadenas relevantes dentro de la memoria, entre ellas la marca temporal y el artefacto solicitado.

1. 2020-12-27 22:50:12
2. You_found_me

### Task 4: Flag final / Final flag
**Explicación:** Se recupera la flag o credencial final enterrada en el volcado.

1. forgetmenot

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Usuario del volcado | `charmander999` |
| 3.1 | Marca temporal encontrada | `2020-12-27 22:50:12` |
| 3.2 | Artefacto encontrado | `You_found_me` |
| 4.1 | Flag/credencial final | `forgetmenot` |

---

**Metodología:** Identificación del volcado de memoria, extracción de usuarios y procesos con Volatility, búsqueda de marcas temporales y cadenas relevantes, y recuperación de credenciales o flags mantenidos en la imagen.

### Cadena de ataque / Attack Chain

Volcado de memoria → Volatility → extracción de usuarios → búsqueda de fechas y artefactos → credencial/flag final.

**Learning chain:** Memoria → Volatility → usuarios → artefactos → credencial → flag

*Lección:* Los volcados de memoria conservan usuarios, credenciales y marcas temporales que permiten reconstruir la actividad del sistema.

**MITRE ATT&CK:** T1003 - OS Credential Dumping.

**Fuente:** [TryHackMe - Memory Forensics](https://tryhackme.com/room/memoryforensics)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.