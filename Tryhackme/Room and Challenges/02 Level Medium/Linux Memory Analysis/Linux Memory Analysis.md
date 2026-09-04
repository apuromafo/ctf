# Linux Memory Analysis [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `linuxmemoryanalysis`
* **Link:** https://tryhackme.com/room/linuxmemoryanalysis
* **Objeto:** Examinar la huella de un APT en un servidor Linux comprometido usando Volatility 3 sobre una imagen de memoria: procesos sospechosos, netcat, binarios ocultos y archivos de tmp.

---

## Solucionario de Tareas / Task Solutions

> Room centrada en forense de memoria Linux con Volatility 3 tras un incidente APT en un servidor comprometido.
> Room focused on Linux memory forensics with Volatility 3 after an APT incident on a compromised server.

### Tarea 5 / Task 5 — Hunting for Suspicious Process

**¿Cuál es el hash MD5 de la imagen que estamos investigando? / What is the MD5 hash of the image we are investigating?**
`c0fbf40989bda765b8edaa41f72d3ee9`

**¿Cuál es el PID del sospechoso proceso Netcat? / What is the PID of the suspicious Netcat process?**
`15011`

**¿Cuál es el nombre del sospechoso proceso que se ejecuta desde el directorio tmp oculto? / What is the name of the suspicious process running from the hidden tmp directory?**
`.strokes`

Fuente / Source: https://systemweakness.com/linux-memory-analysis-tryhackme-ca62220d0d86 (Aaron)

---

> **Pendiente:** El resto de tareas (1-4 y las respuestas restantes de tareas posteriores) no están disponibles en fuentes públicas accesibles. Medium/simontaplin/YouTube no documentan el resto de forma extraíble. Agregar cuando se resuelva la room o se disponga de acceso.
> **Pending:** The remaining tasks (1-4 and the rest of later tasks) are not available in accessible public sources. Medium/simontaplin/YouTube do not document the rest extractably. Add once the room is completed or access is available.

*Fuente de respuestas / Answer source: https://systemweakness.com/linux-memory-analysis-tryhackme-ca62220d0d86*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
