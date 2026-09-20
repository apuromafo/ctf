# Linux Memory Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Premium (requiere suscripción) | linuxmemoryanalysis | https://tryhackme.com/room/linuxmemoryanalysis | Forensics / Memoria | Writeup de thmrevenant (GitHub) / systemweakness.com | Volatility 3, imagen de memoria, procesos, netcat, directorio /tmp, binarios ocultos, hash MD5 | Huella de un APT en un servidor Linux comprometido |

> **Objeto:** Examinar la huella de un APT en un servidor Linux comprometido usando Volatility 3 sobre una imagen de memoria: procesos sospechosos, netcat, binarios ocultos y archivos de tmp.

---

**Contexto:** La sala **Linux Memory Analysis** es un laboratorio de forense de memoria (Premium) donde se examina la huella de un APT en un servidor Linux comprometido usando **Volatility 3** sobre una imagen de memoria. Se identifican el hash MD5 de la imagen, el PID del proceso Netcat sospechoso y el nombre del proceso oculto que se ejecuta desde el directorio `tmp`. El resto de tareas queda documentado como pendiente por falta de fuentes públicas accesibles.

## Solucionario

> Room centrada en forense de memoria Linux con Volatility 3 tras un incidente APT en un servidor comprometido.
> Room focused on Linux memory forensics with Volatility 3 after an APT incident on a compromised server.

### Task 5: Hunting for Suspicious Process
**Explicación:**

Sobre la imagen de memoria se verifica el hash MD5 de la imagen investigada y se cazan con Volatility 3 los procesos sospechosos: el proceso Netcat y el proceso oculto que se ejecuta desde el directorio `tmp`.

**¿Cuál es el hash MD5 de la imagen que estamos investigando? / What is the MD5 hash of the image we are investigating?**
`c0fbf40989bda765b8edaa41f72d3ee9`

**¿Cuál es el PID del sospechoso proceso Netcat? / What is the PID of the suspicious Netcat process?**
`15011`

**¿Cuál es el nombre del sospechoso proceso que se ejecuta desde el directorio tmp oculto? / What is the name of the suspicious process running from the hidden tmp directory?**
`.strokes`

Fuente / Source: https://systemweakness.com/linux-memory-analysis-tryhackme-ca62220d0d86 (Aaron)

> **Pendiente:** El resto de tareas (1-4 y las respuestas restantes de tareas posteriores) no están disponibles en fuentes públicas accesibles. Medium/simontaplin/YouTube no documentan el resto de forma extraíble. Agregar cuando se resuelva la room o se disponga de acceso.
> **Pending:** The remaining tasks (1-4 and the rest of later tasks) are not available in accessible public sources. Medium/simontaplin/YouTube do not document the rest extractably. Add once the room is completed or access is available.

*Fuente de respuestas / Answer source: https://systemweakness.com/linux-memory-analysis-tryhackme-ca62220d0d86*

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5.1 | ¿Cuál es el hash MD5 de la imagen que estamos investigando? / What is the MD5 hash of the image we are investigating? | `c0fbf40989bda765b8edaa41f72d3ee9` |
| 5.2 | ¿Cuál es el PID del sospechoso proceso Netcat? / What is the PID of the suspicious Netcat process? | `15011` |
| 5.3 | ¿Cuál es el nombre del sospechoso proceso que se ejecuta desde el directorio tmp oculto? / What is the name of the suspicious process running from the hidden tmp directory? | `.strokes` |

---

**Metodología:** Forense de memoria con Volatility 3: validación de la integridad de la imagen mediante su hash MD5, enumeración de procesos (`linux.pslist` / lineas de proceso) y correlación con directorios inusuales de ejecución (/tmp oculto) para identificar la huella del APT.

**Learning chain:** Imagen de memoria → hash MD5 → proceso Netcat (PID) → proceso oculto en /tmp → huella del APT.

**Lección:** *La memoria de un sistema comprometido conserva la huella del atacante (procesos, conexiones, binarios cargados) incluso cuando los artefactos en disco se han limpiado; Volatility 3 permite volcar esa huella de forma no invasiva.*

**MITRE ATT&CK:** T1055 Process Injection · T1105 Ingress Tool Transfer · T1071.001 Application Layer Protocol · T1036 Masquerading.

**Fuente:** [TryHackMe - Linux Memory Analysis](https://tryhackme.com/room/linuxmemoryanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.