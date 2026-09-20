# OWASP Top 10 2025: Insecure Data Handling

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `owasptopten2025three` | https://tryhackme.com/room/owasptopten2025three | 01 Level Easy | TryHackMe | OWASP Top 10 2025, A04 Cryptographic Failures, A05 SSTI (Server-Side Template Injection), A08 Insecure Deserialization | Compromiso de confidencialidad e integridad de datos al manipular inputs de aplicación inseguros |

---

<div align="center">
<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/61a7523c029d1c004fac97b3-1763120602843" width="250" alt="OWASP Top 10 2025: Insecure Data Handling">
</div>

> Learn about A04, A05, and A08 as they relate to insecure data handling.

> **ES:** Este módulo del OWASP Top 10 2025 profundiza en tres riesgos relacionados con el manejo inseguro de datos: fallos criptográficos (A04), inyección de plantillas del servidor (SSTI, A05) y fallos de integridad de software o datos con deserialización insegura (A08). Se practican sobre una aplicación web vulnerable interactiva.
> **EN:** This OWASP Top 10 2025 module covers A04, A05, and A08 as they relate to insecure data handling: cryptographic failures, Server-Side Template Injection (SSTI) and software/data integrity failures with insecure deserialization. They are practiced on a deliberately vulnerable web application.

**Room Link:** [https://tryhackme.com/room/owasptopten2025three](https://tryhackme.com/room/owasptopten2025three)

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación del módulo: se anuncia el alcance (A04, A05 y A08) dentro del estándar de seguridad web OWASP Top 10 2025. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Proceed / Proceder | `No answer needed` |

### Task 2: A04 - Fallos Criptográficos / Cryptographic Failures

**Explicación:** Se explota un fallo criptográfico en la aplicación. Tras acceder a notitas encriptadas, se descifran las notas cifradas. Avanzar por las historias/pasos requeridos por la tarea permite llegar hasta una de las notas que contiene la flag. La respuesta, en formato de flag, se obtiene al inspeccionar el contenido de la nota cifrada que revela la vulnerabilidad de manejo criptográfico débil.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Decrypt the encrypted notes. One of them contains a flag value. | `THM{WEAK_CRYPTO_FLAG}` |

### Task 3: A05 - Inyección / Injection (SSTI)

**Explicación:** La aplicación es vulnerable a Server-Side Template Injection (SSTI): los inputs del usuario se insertan directamente en la plantilla del servidor y se evalúan. Mediante payloads de inyección de plantillas se ejecutan operaciones de lectura de ficheros del servidor para obtener el contenido de `flag.txt`, donde reside la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Perform an SSTI attack to read the contents of flag.txt. | `THM{SSTI_FLAG_OBTAINED}` |

### Task 4: A08 - Fallos de Integridad / Deserialización Insegura

**Explicación:** La aplicación serializa datos generados por el usuario y los deserializa del lado del servidor sin validar su origen ni contenido, lo que permite a un atacante manipular el objeto serializado para alterar el flujo de la aplicación. Se modifica la clave de acceso de un objeto serializado y, tras manipular el estado del objeto, el servidor ejecuta la acción deseada y expone el contenido de `flag.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the contents of flag.txt? | `THM{INSECURE_DESERIALIZATION}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Proceed / Proceder | `No answer needed` |
| 2 | Decrypt the encrypted notes. One of them contains a flag value. | `THM{WEAK_CRYPTO_FLAG}` |
| 3 | Perform an SSTI attack to read the contents of flag.txt. | `THM{SSTI_FLAG_OBTAINED}` |
| 4 | What are the contents of flag.txt? | `THM{INSECURE_DESERIALIZATION}` |

---

**Metodología:** Análisis interactivo de una aplicación vulnerable siguiendo el OWASP Top 10 2025: uso de criptografía/debilidades de cifrado (A04), exploits de inyección de plantillas del lado del servidor con lectura de archivos (A05) y manipulación de objetos serializados en el lado del servidor para alterar el flujo de la aplicación (A08).

### Cadena de ataque / Attack Chain

```text
A04: upload/descifrado de notas encriptadas -> THM{WEAK_CRYPTO_FLAG}
A05: payload SSTI {{...}} -> lectura flag.txt -> THM{SSTI_FLAG_OBTAINED}
A08: manipulación de objeto serializado -> deserialización insegura -> flag.txt -> THM{INSECURE_DESERIALIZATION}
```

**Learning chain:** OWASP Top 10 2025 → cryptographic failures (A04) → Server-Side Template Injection (A05) → insecure deserialization (A08) → flag.txt reading

**Lección:** *El manejo inseguro de datos no es una sola vulnerabilidad, sino un racimo: cifrado débil, evaluación de plantillas sin sanitizar y deserialización de objetos no confiables permiten leer ficheros y alterar el estado de la aplicación sin pasar por controles de seguridad.*

**MITRE ATT&CK:** T1204/No aplica directamente; mapeo educativo a OWASP A04:2021 (Cryptographic Failures), A05:2025 (SSTI), A08:2025 (Insecure Deserialization)

**Fuente:** [TryHackMe - OWASP Top 10 2025: Insecure Data Handling](https://tryhackme.com/room/owasptopten2025three)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.