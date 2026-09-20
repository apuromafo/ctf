# Friday Overtime
| **Dificultad** | Medium |
| **Tipo** | Walkthrough (Blue Team / Threat Intel) |
| **Slug** | `fridayovertime` |
| **Link** | [TryHackMe](https://tryhackme.com/room/fridayovertime) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `fridayovertime` + walkthroughs públicos: Slade Venter, KimbakiS, vnelai) |
| **Componentes** | Malware analysis, Threat Intelligence, VirusTotal, CyberChef (Defang), DocIntel, hashing (SHA1/MD5), MITRE ATT&CK, MgBot, APT Daggerfly/Evasive Panda (BRONZE HIGHLAND), iOS/Android spyware |
| **Impacto** | Análisis de una muestra DLL (`pRsm.dll`) reportada como posible intrusión: se verifica su hash, se atribuye al framework **MgBot**, se mapea a MITRE ATT&CK (T1123 Audio Capture), se defangan IOCs (URL de descarga y C2) y se pivota por OSINT hasta un spyware de Android de la familia SpyAgent que comparte la misma infraestructura. |
---
**Contexto:** Es viernes por la tarde en *PandaProbe Intelligence* cuando **SwiftSpend Finance** abre un ticket urgente reportando DLLs sospechosas. Como único analista en turno hay que descargar los adjuntos, examinarlos en un entorno controlado y determinar si constituyen una intrusión dirigida o una falsa alarma. El engagement implica verificar hashes de archivos, correlacionar con frameworks conocidos (**MgBot**), identificar el mapeo **MITRE ATT&CK**, enriquecer IOCs con **VirusTotal** y **CyberChef** y confirmar el alcance de un posible compromiso (incluida la actividad de spyware en Android).
*EN: It's late Friday at *PandaProbe Intelligence* when **SwiftSpend Finance** opens a high-priority ticket reporting suspicious DLLs. As the only analyst on shift, the attachments must be downloaded, examined in a controlled environment and triaged to decide whether it indicates a targeted intrusion or a false alarm. The engagement involves verifying file hashes, correlating with known frameworks (**MgBot**), identifying the **MITRE ATT&CK** mapping, enriching IOCs with **VirusTotal** and **CyberChef**, and confirming the scope of potential compromise (including Android spyware activity).*
## Solucionario
### Task 1: Friday Overtime
**Explicación:** Investigación CTI/malware:
1. **Origen de la muestra.** En el portal **DocIntel** el campo *Reporter* del ticket identifica quién compartió las muestras: **SwiftSpend Finance** a través de **Oliver Bennett**. Esto establece la custodia y la prioridad de triaje.
2. **Verificación de hashes.** Se calcula el **SHA1** de `pRsm.dll` dentro de `samples.zip`:
```bash
unzip samples.zip
sha1sum pRsm.dll
# 9d1ecbbe8637fed0d89fca1af35ea821277ad2e8
```
Al subir el hash a **VirusTotal** aparecen múltiples detecciones etiquetadas como **MgBot**, un framework modular de espionaje.
3. **Atribución.** `pRsm.dll` es un *plugin* del framework **MgBot** (APT **Daggerfly** / **Evasive Panda** / **BRONZE HIGHLAND**); su función es **capturar audio** (micrófono), lo que se corresponde con la técnica **T1123 – Audio Capture**.
4. **Defang de IOCs con CyberChef.**
   - URL de descarga maliciosa (vista por primera vez el **2020-11-02**): `hxxp[://]update[.]browser[.]qq[.]com/qmbs/QQ/QQUrlMgr_QQ88_4296[.]exe`
   - IP del servidor C&C (detectada el **2020-09-14**): `122[.]10[.]90[.]12`
5. **Pivote OSINT/Android.** La misma infraestructura C2 se asocia a un spyware de Android de la familia **SpyAgent**, cuyo hash se pide en la última pregunta.
*EN: CTI/malware investigation: the sample origin (SwiftSpend Finance / Oliver Bennett via DocIntel), SHA1 verification of `pRsm.dll` (VirusTotal flags it as MgBot), attribution (MgBot plugin of Daggerfly/Evasive Panda performing audio capture → T1123), CyberChef defanging of the download URL and C2 IP, and the OSINT pivot to Android SpyAgent spyware sharing the same C2 infrastructure.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who shared the malware samples? | `Oliver Bennett` |
| 2 | What is the SHA1 hash of the file "pRsm.dll" inside samples.zip? | `9d1ecbbe8637fed0d89fca1af35ea821277ad2e8` |
| 3 | Which malware framework utilizes these DLLs as add-on modules? | `MgBot` |
| 4 | Which MITRE ATT&CK Technique is linked to using pRsm.dll in this malware framework? | `T1123` |
| 5 | What is the CyberChef defanged URL of the malicious download location first seen on 2020-11-02? | `hxxp[://]update[.]browser[.]qq[.]com/qmbs/QQ/QQUrlMgr_QQ88_4296[.]exe` |
| 6 | What is the CyberChef defanged IP address of the C&C server first detected on 2020-09-14 using these modules? | `122[.]10[.]90[.]12` |
| 7 | What is the hash of the spyagent family spyware hosted on the same IP targeting Android devices on November 16, 2022? | `951F41930489A8BFE963FCED5D8DFD79` |
---
**Metodología:** Triage del ticket (DocIntel) → descarga y aislado de muestras → hashing (SHA1) e integridad → enriquecimiento en VirusTotal → atribución a framework/APT → mapeo MITRE ATT&CK → defang de IOCs con CyberChef → pivote OSINT a infraestructura compartida (Android).
**Learning chain:** validar muestras → atribuir a un framework (MgBot) → entender la técnica (audio capture) → documentar IOCs defanged → ampliar el alcance a otras plataformas (Android/SpyAgent).
**Lección:** *El triaje de malware es un ejercicio de correlación: un hash bien calculado lleva a la atribución, la atribución a la técnica y la técnica al IOC; defangar los IOCs permite compartirlos sin propagar el riesgo y el pivote OSINT revela el alcance real de la campaña.*
**MITRE ATT&CK:** T1123 (Audio Capture), T1071.001 (Application Layer Protocol: Web Protocols), T1583.001 (Acquire Infrastructure: Domains), T1583.003 (Acquire Infrastructure: Virtual Private Server), T1027 (Obfuscated Files or Information), T1105 (Ingress Tool Transfer).
**Fuente:** [TryHackMe - Friday Overtime](https://tryhackme.com/room/fridayovertime)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
