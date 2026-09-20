# Android Analysis

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `androidanalysis` |
| **Link** | [TryHackMe](https://tryhackme.com/room/androidanalysis) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Análisis de APK, app espía `com.sneakcam.capture`, exfiltración, easyupload.io, MediaFire |
| **Impacto** | Identificación de malware de cámara y de la infraestructura de exfiltración de datos |

---

**Contexto:** Análisis de una aplicación Android de tipo espía (cámara) y de su componente de exfiltración de datos. Las respuestas revelan el paquete malicioso `com.sneakcam.capture`, un *intent* oculto con la flag `FLAG{MSG_HIDDEN_INTENT}`, datos de exfiltración hacia `easyupload.io` y `MediaFire`, y un segundo paquete `com.data.exfiltool` con la flag `FLAG{INSIDER_ACCESS_42X9}`. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Análisis de la aplicación Android / Android App Analysis

**Explicación:** Se inspecciona el APK malicioso, se localizan los paquetes `com.sneakcam.capture` y `com.data.exfiltool`, se recuperan las flags de los *intents* ocultos y se identifican los endpoints de subida (`easyupload.io`, `MediaFire`) y el correo de exfiltración (`ghost123@tutanota.com`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |
| 3 | *(Pregunta 3 no especificada en el original)* | `ABC123456789` |
| 4 | *(Pregunta 4 no especificada en el original)* | `com.sneakcam.capture` |
| 5 | *(Pregunta 5 no especificada en el original)* | `No answer needed` |
| 6 | *(Pregunta 6 no especificada en el original)* | `FLAG{MSG_HIDDEN_INTENT}` |
| 7 | *(Pregunta 6 no especificada en el original)* | `+14155550011` |
| 8 | *(Pregunta 6 no especificada en el original)* | `Encrypted User` |
| 9 | *(Pregunta 6 no especificada en el original)* | `https://easyupload.io` |
| 10 | *(Pregunta 6 no especificada en el original)* | `Pixel_6_User` |
| 11 | *(Pregunta 7 no especificada en el original)* | `com.data.exfiltool` |
| 12 | *(Pregunta 7 no especificada en el original)* | `MediaFire` |
| 13 | *(Pregunta 7 no especificada en el original)* | `ghost123@tutanota.com` |
| 14 | *(Pregunta 7 no especificada en el original)* | `FLAG{INSIDER_ACCESS_42X9}` |
| 15 | *(Pregunta 8 no especificada en el original)* | `No answer needed` |
| 16 | *(Pregunta 9 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |
| 3 | *(Pregunta 3 no especificada en el original)* | `ABC123456789` |
| 4 | *(Pregunta 4 no especificada en el original)* | `com.sneakcam.capture` |
| 5 | *(Pregunta 5 no especificada en el original)* | `No answer needed` |
| 6 | *(Pregunta 6 no especificada en el original)* | `FLAG{MSG_HIDDEN_INTENT}` |
| 7 | *(Pregunta 6 no especificada en el original)* | `+14155550011` |
| 8 | *(Pregunta 6 no especificada en el original)* | `Encrypted User` |
| 9 | *(Pregunta 6 no especificada en el original)* | `https://easyupload.io` |
| 10 | *(Pregunta 6 no especificada en el original)* | `Pixel_6_User` |
| 11 | *(Pregunta 7 no especificada en el original)* | `com.data.exfiltool` |
| 12 | *(Pregunta 7 no especificada en el original)* | `MediaFire` |
| 13 | *(Pregunta 7 no especificada en el original)* | `ghost123@tutanota.com` |
| 14 | *(Pregunta 7 no especificada en el original)* | `FLAG{INSIDER_ACCESS_42X9}` |
| 15 | *(Pregunta 8 no especificada en el original)* | `No answer needed` |
| 16 | *(Pregunta 9 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Análisis estático/dinámico del APK → localización de paquetes y *intents* ocultos → extracción de flags → identificación de la infraestructura de exfiltración (servicios de subida, correo, número de teléfono).

**Learning chain:** Decompilación del APK → análisis de manifest → *intents* ocultos → correlación con endpoints de exfiltración → obtención de flags

**Lección:** *El análisis de manifiestos, *intents* y recursos de un APK revela la lógica de exfiltración y permite cerrar el círculo entre el malware móvil y su infraestructura de comandos y entrega de datos.*

**MITRE ATT&CK:** T1418 (Exfiltration Over Alternative Protocol), T1515 (Hidden Intent), T1407 (Download New Code at Runtime)

**Fuente:** [TryHackMe - Android Analysis](https://tryhackme.com/room/androidanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.