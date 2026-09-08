# Splunk 2

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `splunk2gcd5` |
| **Link** | [TryHackMe](https://tryhackme.com/room/splunk2gcd5) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Splunk / SIEM / investigation / threat hunting / BOTS |
| **Impacto** | Investigar un incidente en la plataforma Splunk BOTS para seguir la cadena de ataque |

---

**Contexto:** Sala de investigación con Splunk (BOTS): analizar logs de una red comprometida para reconstruir la cadena de ataque, mover lateralmente y obtener indicadores y flags.

## Solucionario

### Task 1: Investigation

**Explicación:**

Introducción a la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: Investigation

**Explicación:**

Introducción a la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 3: Web Investigation

**Explicación:**

Investigación web: el dominio atacante es `www.berkbeer.com`; la ruta del recurso (CEO) es `/images/ceoberk.png`; el CEO es **Martin Berk**; los correos de los CEO son `mberk@berkbeer.com` y `hbernhard@berkbeer.com`; el documento subido es `Saccharomyces_cerevisiae_patent.docx`; y el correo del usuario relacionado es `ambersthebest@yeastiebeastie.com`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Attacker domain) | `1. www.berkbeer.com` |
| 2 | (Resource path) | `2. /images/ceoberk.png` |
| 3 | (CEO) | `3. Martin Berk` |
| 4 | (Email 1) | `4. mberk@berkbeer.com` |
| 5 | (Email 2) | `5. hbernhard@berkbeer.com` |
| 6 | (Uploaded document) | `6. Saccharomyces_cerevisiae_patent.docx` |
| 7 | (Related email) | `7. ambersthebest@yeastiebeastie.com` |

### Task 4: Web Investigation Part 2

**Explicación:**

La versión del servidor web es `7.0.4`; las IPs implicadas son `52.42.208.228` y `45.77.65.211`; el archivo PHP vulnerable es `/member.php`; la técnica de inyección SQL es `updatexml`; el timestamp del ataque es `1502408189`; y el usuario relacionado es `kIagerfield`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Server version) | `1. 7.0.4` |
| 2 | (IP 1) | `2. 52.42.208.228` |
| 3 | (IP 2) | `3. 45.77.65.211` |
| 4 | (PHP file) | `4. /member.php` |
| 5 | (SQL technique) | `5. updatexml` |
| 6 | (Timestamp) | `6. 1502408189` |
| 7 | (User) | `7. kIagerfield` |

### Task 5: Malware Investigation

**Explicación:**

Investigación de malware: el archivo cifrado es `Frothly_marketing_campaign_Q317.pptx.crypt`; el archivo de guiones (script) es `S07E02`; el fabricante del dispositivo USB es **Alcor Micro Corp.**; el lenguaje de programación usado (por el malware) es **Perl**; la fecha es `2017-01-17`; y los dominios C2 son `eidk.duckdns.org` y `eidk.hopto.org`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Encrypted file) | `1. Frothly_marketing_campaign_Q317.pptx.crypt` |
| 2 | (Script file) | `2. S07E02` |
| 3 | (USB manufacturer) | `3. Alcor Micro Corp.` |
| 4 | (Language) | `4. Perl` |
| 5 | (Date) | `5. 2017-01-17` |
| 6 | (C2 domain 1) | `6. eidk.duckdns.org` |
| 7 | (C2 domain 2) | `7. eidk.hopto.org` |

### Task 6: Phishing Investigation

**Explicación:**

Investigación de phishing: el archivo adjunto es `invoice.zip`; el número de factura es `912345678`; el país del certificado es `C = US`; el documento HWP adjunto es `나는_데이비드를_사랑한다.hwp`; el empleado implicado es **Ryan Kovar**; el nombre del reto (challenge) es **CyberEastEgg**; y el archivo PHP de carga es `process.php`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Attachment) | `1. invoice.zip` |
| 2 | (Invoice number) | `2. 912345678` |
| 3 | (Certificate country) | `3. C = US` |
| 4 | (HWP document) | `4. 나는_데이비드를_사랑한다.hwp` |
| 5 | (Employee) | `5. Ryan Kovar` |
| 6 | (Challenge) | `6. CyberEastEgg` |
| 7 | (Upload PHP) | `7. process.php` |

### Task 7: Conclusion

**Explicación:**

Cierre de la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusion) | `No answer needed` |

---

**Metodología:**

1. Investigar el tráfico web (dominios, rutas, correos, documentos subidos) y la técnica de inyección SQL (`updatexml`).
2. Analizar artefactos de malware (archivos cifrados, USB, lenguaje, fechas, dominios C2).
3. Investigar phishing (adjuntos, certificados, documentos HWP, procesos de carga).

**Learning chain:** web logs -> SQLi (updatexml) -> attacker domain -> malware (USB/language/C2) -> phishing (invoice/HWP) -> incident reconstruction

**Lección:** *La correlación de logs web, de malware y de phishing en Splunk permite reconstruir la cadena completa del ataque y extraer indicadores y flags.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1059 (Command interpreter) · T1566 (Phishing) · T1041 (Exfiltration Over C2) · T1203 (Exploitation for Client Execution)

**Fuente:** [TryHackMe - Splunk 2](https://tryhackme.com/room/splunk2gcd5)
