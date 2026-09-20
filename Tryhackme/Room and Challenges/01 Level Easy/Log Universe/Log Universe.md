# Log Universe

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | loguniverse | [TryHackMe](https://tryhackme.com/room/loguniverse) | 01 Level Easy | THM | logs, Windows Event Logs, Apache, nginx, Tomcat, SQL injection, nikto, análisis de logs | Comprensión del universo de logs (Windows y Linux) y análisis de logs web, de servicios y de ataques |

---

**Contexto:** Sala práctica sobre el universo de logs. Se recorre desde los registros de Windows (IDs de evento, cuentas `Administrator`) hasta logs web de Apache, `nginx` y `Apache Tomcat`, finalizando con el análisis de logs de un ataque (escaneo `nikto`, intentos de SQL injection y desfiguración con una configuración maliciosa).

> **EN:**
> 1. No answer needed
> 2. No answer needed
> 3. No answer needed
> 4. 1. 744
>    2. Administrator
>    3. Adminstrator
>    4. 0x4B666
> 5. 1. 28
>    2. THMjohn-p
>    3. 5678
>    4. nginx
>    5. Apache Tomcat
>    6. 03/27 15:51:56
> 6. 1. 203[.]45[.]78[.]102
>    2. buyer986
>    3. adv8779
>    4. nikto/2.1.5 (OpenVAS)
>    5. 7654
>    6. \x80\x03\x01\x00\x01
>    7. "SELECT.+FROM"
>    8. /etc/httpd/conf.d/malicious.conf
> 7. No answer needed

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta el objetivo de la sala: entender la diversidad de logs generados por los sistemas y aprender a extraer conclusiones de ellos.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Conceptos previos / Background concepts

**Explicación:** Se introducen los fundamentos teóricos necesarios para interpretar después los registros de los distintos sistemas.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 3: Visión general / Overview

**Explicación:** Se ofrece una panorámica de cómo conviven los logs de Windows y Linux en el ecosistema de una organización.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 4: Logs de Windows / Windows logs

**Explicación:** Se analizan los Event Logs de Windows: identificadores de evento, cuentas implicadas (incluida la variante mal escrita `Adminstrator`) y los códigos de estado que delatan actividad relevante.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Código numérico relacionado con el evento analizado / Numeric code related to the analyzed event | `744` |
| 2 | Cuenta implicada en el evento / Account involved in the event | `Administrator` |
| 3 | Variante mal escrita de la cuenta en el log / Misspelled variant of the account in the log | `Adminstrator` |
| 4 | Código hexadecimal asociado al estado del evento / Hexadecimal code associated with the event state | `0x4B666` |

### Task 5: Logs web / Web logs

**Explicación:** Se examinan los registros de los servidores web y aplicaciones: se extrae una flag, se identifican puertos de servicio, se distinguen los servidores (`nginx`, `Apache Tomcat`) y el acto dentro de la aplicación, registrando su momento exacto.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Número identificado en el análisis / Number identified in the analysis | `28` |
| 2 | Flag encontrada en los logs web / Flag found in the web logs | `THMjohn-p` |
| 3 | Puerto de servicio identificado / Identified service port | `5678` |
| 4 | ¿Qué servidor web responde? / Which web server responds? | `nginx` |
| 5 | ¿Qué aplicación/servidor también aparece en los logs? / Which other application/server appears in the logs? | `Apache Tomcat` |
| 6 | ¿Cuándo ocurrió la actividad en la aplicación? / When did the activity happen in the application? | `03/27 15:51:56` |

### Task 6: Logs de ataque / Attack logs

**Explicación:** Se analizan logs de un ataque real: la IP del atacante ofuscada (`203[.]45[.]78[.]102`), las cuentas a las que apuntó, el escáner empleado (`nikto/2.1.5 (OpenVAS)`), intentos de SQL injection y el archivo de configuración malicioso que desfiguró el sitio (`/etc/httpd/conf.d/malicious.conf`).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | IP del atacante (ofuscada) / Attacker IP (obfuscated) | `203[.]45[.]78[.]102` |
| 2 | Cuenta objetivo 1 del ataque / Attack target account 1 | `buyer986` |
| 3 | Cuenta objetivo 2 del ataque / Attack target account 2 | `adv8779` |
| 4 | ¿Qué escáner usó el atacante? / Which scanner did the attacker use? | `nikto/2.1.5 (OpenVAS)` |
| 5 | Puerto atacado / Attacked port | `7654` |
| 6 | Byte inicial de la petición maliciosa / Initial byte of the malicious request | `\x80\x03\x01\x00\x01` |
| 7 | Patrón de SQL injection observado / SQL injection pattern observed | `"SELECT.+FROM"` |
| 8 | ¿Qué archivo de configuración malicioso se detectó? / Which malicious configuration file was detected? | `/etc/httpd/conf.d/malicious.conf` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala consolidando los aprendizajes sobre los distintos formatos y fuentes de logs.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Revisar los Event Logs de Windows filtrando por IDs de evento y cuentas (`Administrator`/`Adminstrator`) y anotar los códigos de estado. Pasar a los logs web: correlacionar servidores (`nginx`, `Apache Tomcat`), puertos y timestamps, y extraer flags embebidas. Para el ataque final, correlacionar la IP ofuscada `203[.]45[.]78[.]102` con el escáner `nikto/2.1.5 (OpenVAS)`, los patrones de peticiones maliciosas (bytes iniciales poco comunes y expresiones como `"SELECT.+FROM"`) y la configuración de desfiguración `/etc/httpd/conf.d/malicious.conf`.

### Cadena de ataque / Attack Chain

Conceptos → Event Logs de Windows (744, 0x4B666) → logs web (nginx, Apache Tomcat) → flags y puertos → logs de ataque → IP ofuscada → nikto (OpenVAS) → SQL injection → desfiguración con malicious.conf

**Learning chain:** Windows logs → 744 → Administrator → 0x4B666 → THMjohn-p → 5678 → nginx → Apache Tomcat → 203[.]45[.]78[.]102 → nikto → SELECT.+FROM → /etc/httpd/conf.d/malicious.conf

**Lección:** *Cada sistema habla un idioma de logs distinto: saber cruzar Event Logs de Windows con logs de `nginx`, `Apache Tomcat` o Apache permite reconstruir un ataque completo — desde el escaneo con `nikto` hasta la inyección SQL y la desfiguración mediante `malicious.conf` — sin necesidad de herramientas avanzadas.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1193 (Spearphishing Attachment), T1005 (Data from Local System), T1083 (File and Directory Discovery), T1491 (Defacement)

**Fuente:** [TryHackMe - Log Universe](https://tryhackme.com/room/loguniverse)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.