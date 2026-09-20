# Snapped Phish-ing Line

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | SOC / DFIR (Phishing) | snappedphishingline | https://tryhackme.com/room/snappedphishingline | 01 Level Easy | TryHackMe | Análisis de cabeceras de correo, extracción de URLs, hashing SHA256, Timeline | Alto |

---

**Contexto:**
> **ES:** Laboratorio defensivo de análisis de un correo de phishing. Se examinan cabeceras, remitentes, URLs ofuscadas (defanged) y artefactos del mensaje para reconstruir la cadena completa del ataque.
> **EN:** A defensive lab analysing a phishing email. Headers, senders, defanged URLs and message artefacts are examined to rebuild the full attack chain of the email.

## Solucionario

### Task 1: Análisis del correo de phishing / Phishing Email Analysis
**Explicación:**
La tarea recoge todo el análisis forense del correo: remitente, destinatarios, URLs y hashes del archivo adjunto, fechas de envío y entrega, y la flag final del laboratorio.

```
1. 1. William McClean
   2. Accounts.Payable@groupmarketingonline.icu
   3. hxxp[://]kennaroads[.]buzz/data/Update365/office365/40e7baa2f826a57fcf04e5202526f8bd/?email=zoe[.]duncan@swiftspend[.]finance&error
   4. hxxp[://]kennaroads[.]buzz/data/Update365[.]zip
   5. ba3c15267393419eb08c7b2652b8b6b39b406ef300ae8a18fee4d16b19ac9686
   6. 2020-04-08 21:55:50 UTC
   7. 2020-06-25
   8. michael.ascot@swiftspend.finance
   9. m3npat@yandex.com
   10. jamestanner2299@gmail.com
   11. THM{pL4y_w1Th_tH3_URL}
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1.1 | `William McClean` |
| 1.2 | `Accounts.Payable@groupmarketingonline.icu` |
| 1.3 | `hxxp[://]kennaroads[.]buzz/data/Update365/office365/40e7baa2f826a57fcf04e5202526f8bd/?email=zoe[.]duncan@swiftspend[.]finance&error` |
| 1.4 | `hxxp[://]kennaroads[.]buzz/data/Update365[.]zip` |
| 1.5 | `ba3c15267393419eb08c7b2652b8b6b39b406ef300ae8a18fee4d16b19ac9686` |
| 1.6 | `2020-04-08 21:55:50 UTC` |
| 1.7 | `2020-06-25` |
| 1.8 | `michael.ascot@swiftspend.finance` |
| 1.9 | `m3npat@yandex.com` |
| 1.10 | `jamestanner2299@gmail.com` |
| 1.11 | `THM{pL4y_w1Th_tH3_URL}` |

---

**Metodología:**
1. Apertura del correo y análisis de las cabeceras.
2. Identificación del remitente real (`William McClean`) y de la dirección de respuesta falsa `Accounts.Payable@groupmarketingonline.icu`.
3. Extracción y defanging de las URLs maliciosas del cuerpo del mensaje.
4. Cálculo del hash SHA-256 del archivo malicioso.
5. Cruce de fechas de envío y entrega (timeline).
6. Recopilación de todas las direcciones de correo implicadas.

### Cadena de ataque / Attack Chain
Remitente (`Accounts.Payable@groupmarketingonline.icu`) → Enlace malicioso (`hxxp[://]kennaroads[.]buzz/data/Update365/...`) → Payload (`Update365[.]zip`) → Víctimas (`michael.ascot@swiftspend.finance`, etc.) → Flag.

**Learning chain:**
Cabeceras de correo → defanging de URLs → hashing de adjuntos → timeline → correlación de artefactos.

**Lección:** *El análisis manual de cabeceras y la inspección de URLs ofuscadas permiten reconstruir íntegramente una campaña de phishing.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Phishing: Spearphishing Attachment | T1566.001 |
| User Execution: Malicious Link | T1204.001 |
| Phishing: Spearphishing Link | T1566.002 |
| Masquerading | T1036 |

**Fuente:** [TryHackMe - Snapped Phish-ing Line](https://tryhackme.com/room/snappedphishingline)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.