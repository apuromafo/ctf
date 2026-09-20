# ItsyBitsy

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `itsybitsy` |
| **Link** | [TryHackMe](https://tryhackme.com/room/itsybitsy) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | BITS Admin / BITS Jobs / Exfiltración de datos / Windows Event Logs / Threat Hunting / Pastebin / C2 Staging | **Impacto** | Investiga el abuso de BITS en un host Windows: se identifican el ID de evento, la IP de C2, la herramienta bitsadmin, el dominio/URL de staging (pastebin.com/yTg0Ah6a), el archivo exfiltrado (secret.txt) y la flag THM |

---

**Contexto:** Sala de threat hunting centrada en el abuso de Windows BITS (Background Intelligent Transfer Service) para exfiltrar datos. El análisis de los logs del host revela el ID/página de eventos (`1482`), la dirección de C2 (`192.166.65.54`), el uso de `bitsadmin`, el alojamiento en `pastebin.com` con el contenido en `pastebin.com/yTg0Ah6a`, el archivo exfiltrado `secret.txt` y finalmente la flag `THM{SECRET__CODE}`.

## Solucionario

### Task 1: Introducción a BITS / Conceps

**Explicación:** Qué es BITS y por qué los adversarios lo abusan (uso legítimo de transferencia en segundo plano de Windows). No se requiere respuesta:

1. No answer needed

### Task 2: Análisis del Abuso de BITS en el Host

**Explicación:** Cadena de detección del uso malicioso de BITS:

2. 1. `1482` — ID del evento/registro que revela la transferencia
   2. `192.166.65.54` — IP del host remoto (C2/staging)
   3. `bitsadmin` — herramienta utilizada para crear el job
   4. `pastebin.com` — dominio de destino del tráfico
   5. `pastebin.com/yTg0Ah6a` — URL completa del alojamiento externo
   6. `secret.txt` — archivo exfiltrado por el job de BITS
   7. `THM{SECRET__CODE}` — flag de la sala

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué ID de evento evidencia la transferencia BITS? | `1482` |
| 2 | ¿Cuál es la IP del host remoto implicado? | `192.166.65.54` |
| 3 | ¿Qué herramienta crea el job de BITS? | `bitsadmin` |
| 4 | ¿Qué dominio recibe el tráfico? | `pastebin.com` |
| 5 | ¿Cuál es la URL completa del alojamiento? | `pastebin.com/yTg0Ah6a` |
| 6 | ¿Qué archivo se exfiltra? | `secret.txt` |
| 7 | ¿Cuál es la flag de la sala? | `THM{SECRET__CODE}` |

---

**Metodología:**
1. Revisar los eventos de Windows relacionados con BITS (`1482`).
2. Identificar la IP remota y la herramienta usada (`bitsadmin`).
3. Correlacionar el destino del tráfico (pastebin.com y su URL).
4. Vincular el archivo exfiltrado (`secret.txt`).
5. Extraer la flag de la sala.

**Learning chain:** evento 1482 → 192.166.65.54 → bitsadmin → pastebin.com → pastebin.com/yTg0Ah6a → secret.txt → `THM{SECRET__CODE}`

**Lección:** *BITS es el "transferidor silencioso" de Windows: al ser un servicio legítimo y en segundo plano, los adversarios lo convierten en un canal de exfiltración y staging difícil de detectar. Conocer sus eventos y artefactos permite cazarlo aunque use dominios públicos como Pastebin.*

**MITRE ATT&CK:** T1197 - BITS Jobs; T1041 - Exfiltration Over C2 Channel; T1048 - Exfiltration Over Alternative Protocol; T1104 - Multi-Stage Channels; T1071.001 - Application Layer Protocol: Web Protocols; T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage (Pastebin)

**Fuente:** [TryHackMe - ItsyBitsy](https://tryhackme.com/room/itsybitsy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.