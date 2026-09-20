# Phishing Analysis Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `phishinganalysisfundamentals` | [TryHackMe](https://tryhackme.com/room/phishinganalysisfundamentals) | 01 Level Easy | THM | Phishing, Cabeceras de correo, SMTP/IMAP/POP3, ARIN, Adjuntos PDF, Business Email Compromise | Análisis de emails de phishing |

---

**Contexto:** Laboratorio guiado que enseña a analizar emails de phishing: historia del phishing, protocolos y puertos de correo (SMTP/IMAP/POP3), lectura de cabeceras (Return-Path), búsqueda de IPs en ARIN y análisis de adjuntos y emails maliciosos reales hasta identificar Business Email Compromise.

> **ES:** Aprende paso a paso a desmenuzar un email de phishing: cabeceras, protocolos de correo, origen de la IP del remitente y adjuntos maliciosos, con casos prácticos reales.
> **EN:** Learn step by step to break down a phishing email: headers, mail protocols, sender IP origin and malicious attachments, using real practical cases.

## Solucionario

### Task 1: Proceso de análisis de phishing / Phishing Analysis Process

**Explicación:** Presenta la metodología general para analizar un email de phishing: recopilar el mensaje, examinar cabeceras, enlaces y adjuntos, y registrar indicadores de compromiso (IoCs).

1. No answer needed

### Task 2: Breve historia del phishing / A Brief History

**Explicación:** Sitúa el origen del phishing en la década de 1970, cuando comenzaron a usarse técnicas de ingeniería social para extraer datos y credenciales de los usuarios.

2. 1970s

### Task 3: Emails y el modelo TCP/IP / Emails and the TCP/IP Model

**Explicación:** Explica cómo viaja el correo por la red usando SMTP (puerto 587 para el envío) y cómo los clientes leen los mensajes mediante IMAP (993) o POP3 (995).

3. 1. 587
   2. 993
   3. 995

### Task 4: Cabeceras de email / Email Headers

**Explicación:** Muestra cómo inspeccionar las cabeceras: la cabecera Return-Path registra la dirección de retorno y, con la IP de origen, se consulta http://www.arin.net para obtener los detalles del propietario de la IP.

4. 1. Return-Path
   2. http://www.arin.net

### Task 5: Analiza un email / Analyse an Email

**Explicación:** Plantea el análisis de un email de phishing con adjunto PDF. El adjunto Payment-updateid.pdf resulta benigno y arroja la bandera THM{BENIGN_PDF_ATTACHMENT}.

5. 1. https://i.imgur.com/LSWOtDI.png
   2. Payment-updateid.pdf
   3. THM{BENIGN_PDF_ATTACHMENT}

### Task 6: Analiza varios emails / Analyse Multiple Emails

**Explicación:** Aplica el análisis sobre un email que suplanta a Home Depot desde support@teckbe.com, con asunto de pedido y una URL maliciosa ofuscada (hxxp[://]t[.]teckbe[.]com) para evitar su clic accidental.

6. 1. Home Depot
   2. support@teckbe.com
   3. Order Placed : Your Order ID OD2321657089291 Placed Successfully
   4. hxxp[://]t[.]teckbe[.]com

### Task 7: Más ataques de phishing / More Phishing Attacks

**Explicación:** Cubre otras variantes de phishing empleadas como vector de ataque, destacando el Business Email Compromise (BEC) como una de las formas más comunes.

7. Business Email Compromise

| Pregunta | Respuesta |
|---|---|
| T1: Tarea introductoria sin respuesta | `No answer needed` |
| ¿En qué década se originó el phishing como técnica de ingeniería social? | `1970s` |
| ¿Qué puerto usa SMTP para el envío (submission) de correo? | `587` |
| ¿Qué puerto usa IMAP para la lectura de correo? | `993` |
| ¿Qué puerto usa POP3 para la lectura de correo? | `995` |
| ¿Qué cabecera registra la dirección de retorno del email? | `Return-Path` |
| ¿Qué URL se usa para consultar los detalles de la IP de origen? | `http://www.arin.net` |
| ¿Cuál es la URL de la imagen del email analizado? | `https://i.imgur.com/LSWOtDI.png` |
| ¿Cuál es el nombre del archivo adjunto del email? | `Payment-updateid.pdf` |
| ¿Cuál es la bandera del adjunto analizado? | `THM{BENIGN_PDF_ATTACHMENT}` |
| ¿Qué empresa es la víctima del email de phishing? | `Home Depot` |
| ¿Cuál es la dirección del remitente del email? | `support@teckbe.com` |
| ¿Cuál es el asunto del email de phishing? | `Order Placed : Your Order ID OD2321657089291 Placed Successfully` |
| ¿A qué URL intenta dirigir al usuario el email malicioso? | `hxxp[://]t[.]teckbe[.]com` |
| ¿Qué forma de phishing es otro vector de ataque común? | `Business Email Compromise` |

---

**Metodología:** Análisis pasivo de cabeceras de correo, verificación de IPs con ARIN, inspección de adjuntos en un entorno aislado y correlación de indicadores de compromiso (IoCs) propios de campañas de phishing y BEC.

### Cadena de ataque / Attack Chain
Reconocimiento del remitente y del dominio (Return-Path, From) -> Análisis de cabeceras y puertos/protocolos implicados -> Búsqueda de la IP de origen en ARIN -> Inspección del adjunto PDF -> Identificación del email suplantado (Home Depot) y de su URL maliciosa -> Clasificación del ataque como BEC y generación de IoCs.

**Learning chain:** Puertos SMTP/IMAP/POP3, estructura y lectura de cabeceras de correo, consultas WHOIS/ARIN, análisis de adjuntos y reconocimiento de variantes de phishing (spearphishing, BEC).

**Lección:** *El phishing se combate analizando la anatomía del email (cabeceras, origen del remitente y adjuntos), no solo el mensaje visible al usuario.*

**MITRE ATT&CK:** T1566 Phishing, T1566.001 Spearphishing Attachment, T1566.002 Spearphishing Link, T1598.003 Phishing for Information.

**Fuente:** [TryHackMe - Phishing Analysis Fundamentals](https://tryhackme.com/room/phishinganalysisfundamentals)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.