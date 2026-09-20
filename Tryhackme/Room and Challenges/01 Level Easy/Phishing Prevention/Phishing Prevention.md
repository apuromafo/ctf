# Phishing Prevention

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `phishingprevention` | [TryHackMe](https://tryhackme.com/room/phishingprevention) | 01 Level Easy | THM | SPF/DKIM/DMARC, Análisis de cabeceras, Respuestas SMTP, MIME/base64, Sandboxing | Prevención y mitigación de phishing |

---

**Contexto:** Laboratorio centrado en la prevención del phishing: controles de seguridad del correo (SPF, DKIM y DMARC), verificación de firmas y políticas, cifrado, análisis de cabeceras y respuestas SMTP, inspección de adjuntos codificados en base64 y sandboxing de archivos sospechosos.

> **ES:** Aprende a prevenir el phishing verificando controles como SPF/DKIM/DMARC, analizando respuestas SMTP y cabeceras de correo, y aislando adjuntos sospechosos en un sandbox.
> **EN:** Learn to prevent phishing by verifying controls such as SPF/DKIM/DMARC, analyzing SMTP responses and email headers, and isolating suspicious attachments in a sandbox.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introduce la problemática del phishing y el objetivo del lab: prevenir, detectar y mitigar emails maliciosos mediante controles técnicos y análisis.

1. No answer needed

### Task 2: Controles de seguridad del correo / Email Security Controls

**Explicación:** Presenta los controles de seguridad del correo y su uso: en este bloque se verifica el registro SPF del dominio y la bandera (flag) asociada al chequeo.

2. 1. 3
   2. Flag

### Task 3: Verificación de firmas / Signature Verification

**Explicación:** Al comprobar un email firmado, se observa que la verificación de firma falla: el encabezado muestra que la comprobación DKIM no se ha completado correctamente.

3. no key for signature

### Task 4: Política DMARC / DMARC Policy

**Explicación:** Revisa la política DMARC publicada por el dominio emisor y determina el tratamiento que debe darse a los correos que no superen las verificaciones, expresado en el campo de política.

4. p=reject

### Task 5: Cifrado del correo / Email Encryption

**Explicación:** Aborda la protección del contenido y de la comunicación: el cifrado garantiza que los mensajes y datos adjuntos no sean legibles por terceros.

5. Encryption

### Task 6: Análisis de respuestas SMTP / SMTP Response Analysis

**Explicación:** Analiza una sesión SMTP real de un email de phishing (bounce-back): se examina el campo del encabezado que registra el código de respuesta, el código 553 y su mensaje de error asociado.

6. 1. smtp.response.code
   2. 19
   3. 553
   4. Requested action not taken: mailbox name not allowed (553)
   5. 6

### Task 7: Análisis del adjunto / Attachment Analysis

**Explicación:** Descompone el adjunto document.zip del email: su tamaño, el nombre del archivo adjunto, la IP de origen del remitente, el cliente de correo usado y la codificación base64 del contenido.

7. 1. 512
   2. document.zip
   3. 212.253.25.152
   4. Microsoft Outlook Express 6.00.2600.0000
   5. base64

### Task 8: Sandboxing / Sandboxing

**Explicación:** Define la técnica de ejecutar archivos sospechosos (como el adjunto del phishing) en un entorno aislado y controlado para analizar su comportamiento sin riesgo para la organización.

8. Sandboxing

### Task 9: Cierre / Conclusion

**Explicación:** Cierra el lab con un resumen de las mejores prácticas de prevención frente al phishing.

9. No answer needed

| Pregunta | Respuesta |
|---|---|
| T1: Tarea introductoria sin respuesta | `No answer needed` |
| ¿Cuántos controles de seguridad del correo se verifican en este bloque? | `3` |
| ¿Qué campo se usa como bandera/flag en el chequeo SPF? | `Flag` |
| ¿Qué muestra el email cuando falla la verificación de la firma? | `no key for signature` |
| ¿Qué política DMARC publica el dominio emisor? | `p=reject` |
| ¿Qué mecanismo protege el contenido del correo? | `Encryption` |
| ¿Qué campo del encabezado refleja el código de respuesta SMTP? | `smtp.response.code` |
| ¿Qué valor numérico acompaña al campo smtp.response.code? | `19` |
| ¿Cuál es el código de respuesta SMTP devuelto? | `553` |
| ¿Qué mensaje de error SMTP acompaña al código 553? | `Requested action not taken: mailbox name not allowed (553)` |
| ¿Cuántos valores/pasos registra la sesión SMTP analizada? | `6` |
| ¿Cuál es el tamaño del adjunto del email? | `512` |
| ¿Cuál es el nombre del archivo adjunto? | `document.zip` |
| ¿Cuál es la IP de origen del email? | `212.253.25.152` |
| ¿Qué cliente de correo se utilizó para enviar el email? | `Microsoft Outlook Express 6.00.2600.0000` |
| ¿Qué codificación se aplica al contenido adjunto? | `base64` |
| ¿Cómo se denomina la ejecución aislada de archivos sospechosos para su análisis? | `Sandboxing` |
| T9: Tarea de cierre sin respuesta | `No answer needed` |

---

**Metodología:** Verificación de la autenticación del correo (SPF/DKIM/DMARC), análisis de cabeceras y sesiones SMTP, inspección de adjuntos y su codificación (MIME/base64) y ejecución de archivos sospechosos en un entorno aislado (sandbox).

### Cadena de ataque / Attack Chain
Recepción de un email de phishing con dominio falso (verificación SPF/DMARC fallida) -> Entrega de un adjunto malicioso (document.zip) con codificación base64 -> Respuesta SMTP del servidor que descarta el mensaje (553) -> Análisis en sandbox del adjunto para extraer IoCs -> Bloqueo y prevención mediante controles de correo y filtrado.

**Learning chain:** SPF, DKIM y DMARC, lectura de cabeceras y respuestas SMTP, análisis MIME/base64 de adjuntos y sandboxing de muestras maliciosas.

**Lección:** *La prevención del phishing se apoya en la verificación técnica del correo (SPF/DKIM/DMARC) y en el análisis aislado de adjuntos antes de que alcancen al usuario.*

**MITRE ATT&CK:** T1566 Phishing, T1566.001 Spearphishing Attachment, T1204.002 User Execution (Malicious File).

**Fuente:** [TryHackMe - Phishing Prevention](https://tryhackme.com/room/phishingprevention)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.