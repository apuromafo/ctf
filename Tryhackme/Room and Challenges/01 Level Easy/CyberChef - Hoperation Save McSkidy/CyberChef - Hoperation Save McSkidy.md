# CyberChef - Hoperation Save McSkidy

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Medium | walkthrough | `encoding-decoding-aoc2025-s1a4z7x0c3` | [TryHackMe](https://tryhackme.com/r/room/encoding-decoding-aoc2025-s1a4z7x0c3) | Advent of Cyber 2025 | THM | CyberChef, encoding/decoding, passwords, locks | N/A |

> **Objeto:** Recuperar el objeto codificado resolviendo los cinco candillos protegidos por contraseñas usando las operaciones de decodificación de CyberChef.

---

**Contexto:** En esta sala del Advent of Cyber 2025 (Día 17), el equipo de McSkidy necesita recuperar un objeto codificado mediante una serie de candillos protegidos por contraseñas. Cada lock requiere decodificar la información con las operaciones adecuadas en CyberChef para avanzar hasta el flag final.

> **ES:** En esta sala del Advent of Cyber 2025 (Día 17), el equipo de McSkidy necesita recuperar un objeto codificado mediante una serie de candillos protegidos por contraseñas. Cada lock requiere decodificar la información con las operaciones adecuadas en CyberChef para avanzar hasta el flag final.
> **EN:** In this Advent of Cyber 2025 room (Day 17), McSkidy's team needs to recover an encoded object protected by a series of password-protected locks. Each lock requires decoding the information with the right CyberChef operations to advance to the final flag.

## Solucionario

### Task 1: Day 17 - CyberChef
**Explicación:** Resolución de los cinco candillos aplicando la operación de decodificación adecuada en CyberChef para cada contraseña hasta recuperar el flag final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password for the first lock? | `Iamsofluffy` |
| 2 | What is the password for the second lock? | `Itoldyoutochangeit!` |
| 3 | What is the password for the third lock? | `BugsBunny` |
| 4 | What is the password for the fourth lock? | `passw0rd1` |
| 5 | What is the password for the fifth lock? | `51rBr34chBl0ck3r` |
| 6 | What is the retrieved flag? | `THM{M3D13V4L_D3C0D3R_4D3P7}` |

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | What is the password for the first lock? | `Iamsofluffy` |
| 1.2 | What is the password for the second lock? | `Itoldyoutochangeit!` |
| 1.3 | What is the password for the third lock? | `BugsBunny` |
| 1.4 | What is the password for the fourth lock? | `passw0rd1` |
| 1.5 | What is the password for the fifth lock? | `51rBr34chBl0ck3r` |
| 1.6 | What is the retrieved flag? | `THM{M3D13V4L_D3C0D3R_4D3P7}` |

---

**Metodología:** Se utilizaron operaciones de decodificación en CyberChef (Base64, ROT13, Hex, Binary, etc.) para descifrar cada contraseña de los candillos, aplicando el pie de claves correctamente hasta obtener la contraseña final y el flag.

### Cadena de ataque / Attack Chain

Análisis del formato de cada candillo → selección de la operación de CyberChef adecuada → decodificación de la contraseña → apertura del lock → flag final.

**Learning chain:** encoding → decoding → CyberChef operations → password cracking → flag extraction

*Lección:* Las operaciones de decodificación combinadas de CyberChef permiten recuperar secretos protegidos por capas de codificación sucesivas.

**MITRE ATT&CK:** N/A.

**Fuente:** [TryHackMe - CyberChef - Hoperation Save McSkidy](https://tryhackme.com/room/encoding-decoding-aoc2025-s1a4z7x0c3)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.