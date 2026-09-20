# SigHunt
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `sighunt` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sighunt) |
| **Sección** | Blue Team / Threat Hunting / Detection Engineering |
| **Fuente** | TryHackMe |
| **Componentes** | Sigma, Sysmon, Windows Event Logs, Threat Hunting, Detection Rules, EVTX |
| **Impacto** | Caza proactiva de amenazas aplicando reglas Sigma sobre telemetría de Windows (Sysmon/EVTX) para detectar actividad maliciosa y responder a los retos de la sala. |
---
**Contexto:** SigHuntes una room de threat hunting centrada en el uso de **Sigma** como lenguaje para describir detecciones. A lo largo de la sala se analizan artefactos de Windows (Sysmon, eventos de proceso, red, servicios y persistencia) y se construyen/consultan reglas Sigma para cazar comportamientos sospechosos. El objetivo es desarrollar el pensamiento de detección: pasar de la telemetría cruda a una hipótesis de ataque verificable.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de la sala y de los objetivos de threat hunting con Sigma. No requiere la resolución de ninguna pregunta técnica, únicamente introducir el escenario de caza y preparar el entorno de trabajo (logs de Sysmon/EVTX y editor de reglas).
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas técnicas). | `No answer needed` |
### Task 2: Hunting Challenges / Retos de caza
**Explicación:** Batería de retos donde se analiza la telemetría disponible y se responden preguntas concretas sobre la actividad capturada. Cada respuesta es una flag con formato `THM{...}` correspondiente a un hallazgo de hunting: campaña de phishing basada en `mshta`, uso de certificados (certs) para evasión, ejecución de `netcat`, enumeración con PowerShell (`p0wp0wp0w3rup`), servicios con privilegios excesivos, ejecución oculta en `runonce`, recolección y compresión con `7z`, descarga vía `curl` en Windows y una flag final del reto de hunting.
- Campaña de phishing con `mshta`: `THM{ph1sh1ng_msht4_101}`
- Uso de certificados / LOLBins firmados: `THM{n0t_just_4_c3rts}`
- Netcat clásico: `THM{cl4ss1c_n3tc4t_r3vs}`
- Enumeración PowerShell: `THM{p0wp0wp0w3rup_3num}`
- Servicio con privilegios excesivos: `THM{ov3rpr1v1l3g3d_s3rv1c3}`
- Persistencia/ejecución oculta en runonce: `THM{h1d3_m3_1n_run0nc3}`
- Recolección y empaquetado con 7-Zip: `THM{c0ll3ct1ng_7z_ftw}`
- Descarga con curl en Windows: `THM{cUrling_0n_w1nd0ws}`
- Flag final del reto de hunting: `THM{huntm3_pl34s3}`
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag del reto de phishing con `mshta`. | `THM{ph1sh1ng_msht4_101}` |
| 2. Flag del reto de certificados. | `THM{n0t_just_4_c3rts}` |
| 3. Flag del reto de netcat. | `THM{cl4ss1c_n3tc4t_r3vs}` |
| 4. Flag del reto de enumeración PowerShell. | `THM{p0wp0wp0w3rup_3num}` |
| 5. Flag del reto de servicio con privilegios. | `THM{ov3rpr1v1l3g3d_s3rv1c3}` |
| 6. Flag del reto de ejecución en runonce. | `THM{h1d3_m3_1n_run0nc3}` |
| 7. Flag del reto de recolección con 7z. | `THM{c0ll3ct1ng_7z_ftw}` |
| 8. Flag del reto de descarga con curl. | `THM{cUrling_0n_w1nd0ws}` |
| 9. Flag final del reto de hunting. | `THM{huntm3_pl34s3}` |
---
**Metodología:** Identificar la fuente de telemetría (Sysmon/EVTX) → formular la hipótesis de ataque → buscar los indicadores (procesos, líneas de comando, red, servicios, persistencia) → crear/consultar la regla Sigma correspondiente → validar el hallazgo y extraer la flag.
### Cadena de ataque / Attack Chain
```
Phishing (mshta) -> ejecución de LOLBins -> enumeración (PowerShell) -> persistencia (runonce/servicio) -> recolección y empaquetado (7z) -> exfiltración/descarga (curl/netcat)
```
**Learning chain:** telemetría cruda → hipótesis de caza → consulta de reglas Sigma → detección de TTPs → extracción de evidencias.
**Lección:** *La caza de amenazas consiste en convertir telemetría en hipótesis verificables; Sigma aporta un lenguaje común y portable para describir esas detecciones y reutilizarlas entre distintos SIEM/EDR.*
**MITRE ATT&CK:** T1566 (Phishing), T1218.005 (Mshta), T1059.001 (PowerShell), T1059.003 (Windows Command Shell), T1547.001 (Registry Run Keys / Startup Folder), T1543.003 (Windows Service), T1560.001 (Archive Collected Data), T1105 (Ingress Tool Transfer).
**Fuente:** [TryHackMe - SigHunt](https://tryhackme.com/room/sighunt)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
