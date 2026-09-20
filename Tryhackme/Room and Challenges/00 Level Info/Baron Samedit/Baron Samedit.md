# Baron Samedit

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `sudovulnssamedit` | [TryHackMe](https://tryhackme.com/room/sudovulnssamedit) | 00 Level Info | TryHackMe | sudo, CVE-2021-3156, heap buffer overflow, desarrollo de exploits | Ejecución de código con privilegios root mediante el desbordamiento de búfer en el heap de sudo (Baron Samedit) |

---

**Contexto:** Sala de prácticas sobre el Baron Samedit (CVE-2021-3156), una vulnerabilidad crítica de desbordamiento de búfer en el heap del binario de sudo que permite a cualquier usuario local elevar privilegios a root. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Pregunta de arranque de la sala, sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Explotación / Exploitation

**Explicación:** Se explota el Baron Samedit (CVE-2021-3156) con el exploit público `sudo-hax-me-a-sandwich`, que desencadena el desbordamiento de búfer del heap de sudo, se obtiene una shell como root y se captura la flag `THM{NmU4OWYwMWJmMjkxMDdiYTU4MWIxNWVk}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `sudo-hax-me-a-sandwich` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{NmU4OWYwMWJmMjkxMDdiYTU4MWIxNWVk}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `sudo-hax-me-a-sandwich` |
| 3 | *(Task 2, Pregunta 2 no especificada en el original)* | `THM{NmU4OWYwMWJmMjkxMDdiYTU4MWIxNWVk}` |

---

**Metodología:** Identificar la vulnerabilidad crítica de sudo CVE-2021-3156 (Baron Samedit) → transferir y compilar el exploit `sudo-hax-me-a-sandwich` → ejecutarlo para desencadenar el heap buffer overflow → obtener una shell como root → capturar la flag.

### Cadena de ataque / Attack Chain

```text
sudo CVE-2021-3156 → exploit sudo-hax-me-a-sandwich → heap buffer overflow → shell como root → flag THM{...}
```

**Learning chain:** Comprensión de la vulnerabilidad de sudo → uso del exploit público → escalada a root → captura de la flag

**Lección:** *Una única vulnerabilidad en el binario setuid de sudo, incluso con años de antigüedad, puede entregar privilegios root completos a cualquier usuario local.*

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1548 (Abuse Elevation Control Mechanism)

**Fuente:** [TryHackMe - Baron Samedit](https://tryhackme.com/room/sudovulnssamedit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.