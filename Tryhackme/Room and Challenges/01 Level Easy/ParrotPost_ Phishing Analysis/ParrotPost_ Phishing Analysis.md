# ParrotPost: Phishing Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `parrotpostphishinganalysis` | https://tryhackme.com/room/parrotpostphishinganalysis | 01 Level Easy | TryHackMe | Phishing analysis, email headers, Base64, CSS/JS obfuscation, credential capture, reverse engineering | Compromiso completo de la cadena de phishing: desde el análisis del correo hasta la recuperación de credenciales reales |

---

**Contexto:** ParrotPost Secure Webmail es un servicio que se presenta como profesional y etiquetado como "No te engañes con el phishing – está en todas partes". En ParrotPost tudo está cifrado y protegido. Y tú estás protegido, ¿verdad? ... La interfaz no deja de acceder por web... a menos que consigas desactivar la Protección de Cuenta (Account Protection) de ParrotPost. Una vez desactivada, empiezan a llegar correos maliciosos.

> **ES:** Analiza un correo de phishing paso a paso: revisa las cabeceras para identificar el país del servidor emisor, decodifica un adjunto ofuscado con Base64, explora una página HTML ofuscada con CSS para descubrir una página de login falsa y, finalmente, interactúa con un sitio de phishing para capturar las credenciales y obtener las flags.
> **EN:** Analyze a phishing email step by step: examine the headers to identify the sender's country, decode an obfuscated attachment using Base64, explore a CSS-obfuscated HTML attachment to uncover a fake login page and interact with the phishing site to capture credentials and find the flags.

## Solucionario

### Task 1: Inicio / Getting Started

**Explicación:** Tarea de preparación de la práctica. Se confirma que el estudiante está listo para comenzar el análisis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to proceed with the analysis! | `No answer needed` |

### Task 2: Análisis del correo de phishing / Phishing Email Analysis

**Explicación:** Se inspeccionan las cabeceras del correo recibido (asunto RE: FlyLoas Airways - Compra tu boleto...). El campo `X-Original-Sender: jumbo@bigbang.com` aparece en la fila de la tabla de encabezados, y en la respuesta original de la bandeja el ISP envía un NDR (notificación de fallo de entrega) indicando que el remitente es Latvian LVSTATICIP (Letonia). El remitente responde a `no-reply@postparr0t.thm`. Se identifica el header personalizado (el tercer encabezado del correo) con la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to the IP address, what country is the sending email server associated with? | `Latvia` |
| 2 | If Paul replies to this email, which email address will his reply be sent to? | `no-reply@postparr0t.thm` |
| 3 | What is the value of the custom header in the email? | `THM{y0u_f0und_7h3_h34d3r}` |

### Task 3: Análisis del adjunto / Email Attachment Analysis

**Explicación:** El correo incluye un archivo adjunto malicioso. Se inspecta el contenido y se identifica que está codificado en **base64** (el patrón `UEsDBB...` aparece en varias posiciones del archivo). Para decodificarlo se utiliza la función JavaScript `atob()` que invierte el proceso. Al decodificar el archivo se obtiene el script malicioso completo y, en su interior, la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the encoding used in the obfuscated attachment? | `base64` |
| 2 | What is the JavaScript function used to decode the base64-encoded content? | `atob()` |
| 3 | What is the flag? | `THM{d0ubl3_3nc0d3d}` |

### Task 4: Ofuscación CSS / CSS Obfuscation

**Explicación:** La transición CSS se manipula con `window.location.href` para encadenar estilos legibles con una página web maliciosa. El HTML contiene un `@import` que carga CSS y combina el código Malware con un DOM no malicioso. La página de login se titula **ParrotPost Secure Webmail Login** (visto en la pestaña del navegador). El reverso de CSS Minify es CSS Beautify, herramienta que permite leer el CSS compresado de vuelta a un formato legible.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the delivered HTML attachment's login page title? | `ParrotPost Secure Webmail Login` |
| 2 | What is the reverse of CSS Minify? | `CSS Beautify` |

### Task 5: Ofuscación JavaScript / JavaScript Obfuscation

**Explicación:** El contenido del HTML tiene una capa de JavaScript ofuscada que contiene una función que envía el formulario de login a un servidor externo. La URL de captura de credenciales es `http://evilparrot.thm:8080/cred-capture.php`. El método de redirección post-captura es `window.location.href`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the URL that receives the login request when the login form is submitted? | `http://evilparrot.thm:8080/cred-capture.php` |
| 2 | What is the JavaScript method used to redirect users to the phish page? | `window.location.href` |

### Task 6: Análisis del sitio de phishing / Phishing Site Analysis

**Explicación:** Se accede al servidor de captura de credenciales y se envía un par de credenciales falsas al endpoint `/cred-capture.php`. Al verificar el archivo `/creds.txt` se obtiene la primera flag de esta fase. En el contenido del mismo archivo aparece también la contraseña real de Chris Smith. Finalmente, se accede a la URL del servidor de phishing para completar la práctica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag you receive after sending fake credentials to the /cred-capture.php endpoint? | `THM{c4p7ur3d_y0ur_cr3d5}` |
| 2 | What is the path on the web server hosting the log of captured credentials? | `/creds.txt` |
| 3 | Based on the log, what is Chris Smith's password? | `FlyL1ke!A~Bird` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la práctica. Se confirma que el estudiante ha completado el análisis completo de la cadena de phishing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed / Finalizar | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to proceed with the analysis! | `No answer needed` |
| 2 | According to the IP address, what country is the sending email server associated with? | `Latvia` |
| 3 | If Paul replies to this email, which email address will his reply be sent to? | `no-reply@postparr0t.thm` |
| 4 | What is the value of the custom header in the email? | `THM{y0u_f0und_7h3_h34d3r}` |
| 5 | What is the name of the encoding used in the obfuscated attachment? | `base64` |
| 6 | What is the JavaScript function used to decode the base64-encoded content? | `atob()` |
| 7 | What is the flag? | `THM{d0ubl3_3nc0d3d}` |
| 8 | What is the delivered HTML attachment's login page title? | `ParrotPost Secure Webmail Login` |
| 9 | What is the reverse of CSS Minify? | `CSS Beautify` |
| 10 | What is the URL that receives the login request when the login form is submitted? | `http://evilparrot.thm:8080/cred-capture.php` |
| 11 | What is the JavaScript method used to redirect users to the phish page? | `window.location.href` |
| 12 | What is the flag you receive after sending fake credentials to the /cred-capture.php endpoint? | `THM{c4p7ur3d_y0ur_cr3d5}` |
| 13 | What is the path on the web server hosting the log of captured credentials? | `/creds.txt` |
| 14 | Based on the log, what is Chris Smith's password? | `FlyL1ke!A~Bird` |
| 15 | Click me to proceed / Finalizar | `No answer needed` |

---

**Metodología:** Análisis de phishing multietapa: inspección de cabeceras de correo para geolocalizar el servidor emisor y extraer headers customizados, decodificación de adjuntos ofuscados en base64 con `atob()`, inspección de HTML/CSS y JavaScript ofuscado para identificar la URL de captura y, finalmente, explotación del sitio de phishing enviando credenciales falsas y extracción de las reales del log del servidor.

### Cadena de ataque / Attack Chain

```text
Correo de phishing (Latvia) -> cabeceras (no-reply@postparr0t.thm, X-custom-header) -> adjunto base64 -> atob() -> HTML ofuscado -> CSS Beautify -> login falso (ParrotPost Secure Webmail Login) -> cred-capture.php -> /creds.txt -> flag + credenciales reales
```

**Learning chain:** phishing email analysis → IP geolocation → custom email headers → Base64 decoding (atob()) → CSS obfuscation → JavaScript obfuscation → credential capture (POST to /cred-capture.php) → log file extraction → real credentials

**Lección:** *Un análisis completo de phishing debe recorrer la cadena entera: cabeceras del correo → adjunto → código cliente → servidor de captura. Solo al final se obtiene la evidencia completa: la flag del atacante y las credenciales robadas.*

**MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Attachment), T1059.007 (JavaScript), T1539 (Steal Web Session Cookie)

**Fuente:** [TryHackMe - ParrotPost: Phishing Analysis](https://tryhackme.com/room/parrotpostphishinganalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.