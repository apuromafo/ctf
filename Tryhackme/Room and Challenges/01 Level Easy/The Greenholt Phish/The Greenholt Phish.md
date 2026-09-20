# The Greenholt Phish

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `thegreenholtphish` | [TryHackMe](https://tryhackme.com/room/thegreenholtphish) | 01 Level Easy | THM | Análisis de email (.msg), phishing, headers DNS | Identificación de campaña de phishing |

---

**Contexto:**

> **ES:** Sala de nivel fácil centrada en el análisis de un correo de phishing (.msg): cabeceras del mensaje, infraestructura del remitente, registros SPF/DMARC y análisis del adjunto malicioso para evidenciar la campaña.
> **EN:** Easy room focused on analyzing a phishing email (.msg): message headers, sender infrastructure, SPF/DMARC records and analysis of the malicious attachment to evidence the campaign.

## Solucionario

### Task 1: Análisis del correo / Email analysis

**Explicación:**

Esta tarea analiza los datos de cabecera y contenido del correo de phishing. Se conserva de forma literal el contenido original:

1. 1. 09674321
   2. Mr. James Jackson
   3. info@mutawamarine.com
   4. info.mutawamarine@mail.com

### Task 2: Infraestructura / Infrastructure

**Explicación:**

Esta tarea identifica la infraestructura de envío del correo. Se conserva de forma literal el contenido original:

2. 1. 192.119.71.157
   2. Hostwinds LLC

### Task 3: Autenticación del correo / Email authentication

**Explicación:**

Esta tarea revisa los registros de autenticación DNS del dominio del remitente. Se conserva de forma literal el contenido original:

3. 1. v=spf1 include:spf.protection.outlook.com -all
   2. v=DMARC1; p=quarantine; fo=1

### Task 4: Adjunto malicioso / Malicious attachment

**Explicación:**

Esta tarea analiza el archivo adjunto del correo y su contenido. Se conserva de forma literal el contenido original:

4. 1. SWT_#09674321____PDF__.CAB
   2. 2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f
   3. 400.26 KB
   4. RAR

### Tabla Unificada de Preguntas y Respuestas

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Número de referencia del correo | `09674321` |
| 2 | Task 1 | Nombre del remitente que se muestra | `Mr. James Jackson` |
| 3 | Task 1 | Dirección de correo del remitente (From) | `info@mutawamarine.com` |
| 4 | Task 1 | Dirección de respuesta (Return-Path) | `info.mutawamarine@mail.com` |
| 5 | Task 2 | Dirección IP del remitente | `192.119.71.157` |
| 6 | Task 2 | Proveedor de alojamiento (hosting) | `Hostwinds LLC` |
| 7 | Task 3 | Registro SPF del dominio | `v=spf1 include:spf.protection.outlook.com -all` |
| 8 | Task 3 | Registro DMARC del dominio | `v=DMARC1; p=quarantine; fo=1` |
| 9 | Task 4 | Nombre del archivo adjunto | `SWT_#09674321____PDF__.CAB` |
| 10 | Task 4 | Hash SHA256 del adjunto | `2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f` |
| 11 | Task 4 | Tamaño del archivo adjunto | `400.26 KB` |
| 12 | Task 4 | Tipo/extensiones del contenido | `RAR` |

---

**Metodología:** 1) Apertura del .msg y extracción de cabeceras; 2) Resolución de la infraestructura del remitente (IP, hosting); 3) Revisión de registros SPF y DMARC; 4) Extracción y hash del adjunto (SHA256) y análisis del contenido extraído.

### Cadena de ataque / Attack Chain

- Recepción del correo de phishing con adjunto .CAB
- Análisis de cabeceras (From/Return-Path) → dominio mutawamarine.com
- Enumeración de IP/hosting → infraestructura del atacante
- Revisión de SPF/DMARC → deficiencias de autenticación
- Extracción del adjunto → hash SHA256 y análisis del contenido

**Learning chain:** Análisis de cabeceras → Revisión de infraestructura → Autenticación de email → Análisis de malware → Reporte forense

**Lección:** *Un correo de phishing se desmonta leyendo sus cabeceras y registros DNS: el dominio, la infraestructura y los fallos de SPF/DMARC evidencian la campaña incluso antes de abrir el adjunto.*

**MITRE ATT&CK:** T1566.001 (Spearphishing Attachment), T1204.002 (User Execution: Malicious File)

**Fuente:** [TryHackMe - The Greenholt Phish](https://tryhackme.com/room/thegreenholtphish)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.