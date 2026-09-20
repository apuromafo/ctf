# Squid Game

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | squidgameroom | https://tryhackme.com/room/squidgameroom | 03 Level Hard | TryHackMe | oletools / olevba / msoffcrypto / strings / VBA macros / Cobalt Strike / rundll32 / PowerShell | Análisis forense de cinco documentos maliciosos (maldocs) con macros VBA que descargan ejecutables y DLL, encapsulan Cobalt Strike y despliegan agentes contra sistemas Windows. |

---

**Contexto:** El room Squid Game es un ejercicio de análisis de malware en el que se presentan cinco documentos de Office maliciosos (uno por cada "attacker"). En todos se repite el mismo patrón de macro: objetos COM (ShellBrowserWindow), descarga de ejecutables o DLLs desde dominios C2, reinserción en `%ProgramData%` o `TEMP` y ejecución con `rundll32.exe`/`certutil`/VBS. El análisis mezcla extracción de cadenas, inspección de streams OLE (números y tamaños de los bloques que contienen macros), descifrado de contenido ofuscado (reversión de strings, XOR y base64) y, en el último reto, la identificación completa de una implantación Cobalt Strike (IP, puerto, user-agent, ruta del shellcode y APIs importadas).

> **ES:** Sala de análisis de malware con cinco maldocs cuyas macros VBA descargan payloads, con confusión base64/XOR y una implantación final de Cobalt Strike.
> **EN:** Malware-analysis room with five maldocs whose VBA macros drop payloads, with base64/XOR obfuscation and a final Cobalt Strike implant.

## Solucionario

### Task 1: The Invitation / La invitación
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accept the invitation? (Yes/No) | `Yes` |

### Task 2: Attacker 1 / Atacante 1
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the malicious C2 domain you found in the maldoc where an executable download was attempted? | `fpetraardella.band/xap_102b-AZ1/704e.php?l=litten4.gas` |
| 2 | What executable file is the maldoc trying to drop? | `QdZGP.exe` |
| 3 | In what folder is it dropping the malicious executable? (hint: %Folder%) | `%ProgramData%` |
| 4 | Provide the name of the COM object the maldoc is trying to access. | `ShellBrowserWindow` |
| 5 | Include the malicious IP and the php extension found in the maldoc. (Format: IP/name.php) | `176.32.35.16/704e.php` |
| 6 | Find the phone number in the maldoc. (Answer format: xxx-xxx-xxxx) | `213-446-1757` |
| 7 | Doing some static analysis, provide the type of maldoc this is under the keyword "AutoOpen". | `AutoExec` |
| 8 | Provide the subject for this maldoc. (make sure to remove the extra whitespace) | `West Virginia Samanta` |
| 9 | Provide the time when this document was last saved. (Format: YEAR-MONTH-DAY XX:XX:XX) | `2019-02-07 23:45:30` |
| 10 | Provide the stream number that contains a macro. | `8` |
| 11 | Provide the name of the stream that contains a macro. | `ThisDocument` |

### Task 3: Attacker 2 / Atacante 2
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the streams (numbers) that contain macros. | `12, 13, 14, 16` |
| 2 | Provide the size (bytes) of the compiled code for the second stream that contains a macro. | `13867` |
| 3 | Provide the largest number of bytes found while analyzing the streams. | `63641` |
| 4 | Find the command located in the 'fun' field (make sure to reverse the string). | `cmd /k cscript.exe C:\ProgramData\pin.vbs` |
| 5 | Provide the first domain found in the maldoc. | `priyacareers.com/u9hDQN9Yy7g/pt.html` |
| 6 | Provide the second domain found in the maldoc. | `perfectdemos.com/Gv1iNAuMKZ/pt.html` |
| 7 | Provide the name of the first malicious DLL it retrieves from the C2 server. | `www1.dll` |
| 8 | How many DLLs does the maldoc retrieve from the domains? | `5` |
| 9 | Provide the path of where the malicious DLLs are getting dropped onto? | `C:\ProgramData` |
| 10 | What program is it using to run DLLs? | `rundll32.exe` |
| 11 | How many seconds does the function in the maldoc sleep for to fully execute the malicious DLLs? | `15` |
| 12 | Under what stream did the main malicious script use to retrieve DLLs from the C2 domains? (Provide the name of the stream). | `Macros/Form/o` |

### Task 4: Attacker 3 / Atacante 3
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the executable name being downloaded. | `1.exe` |
| 2 | What program is used to run the executable? | `Certutil` |
| 3 | Provide the malicious URI included in the maldoc that was used to download the binary (without http/https). | `8cfayv.com/bolb/jaent.php?l=liut6.cab` |
| 4 | What folder does the binary gets dropped in? | `ProgramData` |
| 5 | Which stream executes the binary that was downloaded? | `A3` |

### Task 5: Attacker 4 / Atacante 4
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the first decoded string found in this maldoc. | `MSXML2.XMLHTTP` |
| 2 | Provide the name of the binary being dropped. | `DYIATHUQLCW.exe` |
| 3 | Provide the folder where the binary is being dropped to. | `TEMP` |
| 4 | Provide the name of the second binary. | `bin.exe` |
| 5 | Provide the full URI from which the second binary was downloaded (exclude http/https). | `gv-roth.de/js/bin.exe` |

### Task 6: Attacker 5 / Atacante 5
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the caption you found in the maldoc? | `CobaltStrikeIsEverywhere` |
| 2 | What is the XOR decimal value found in the decoded-base64 script? | `35` |
| 3 | Provide the C2 IP address of the Cobalt Strike server. | `176.103.56.89` |
| 4 | Provide the full user-agent found. | `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)` |
| 5 | Provide the path value for the Cobalt Strike shellcode. | `/SjMR` |
| 6 | Provide the port number of the Cobalt Strike C2 Server. | `8080` |
| 7 | Provide the first two APIs found. | `LoadLibraryA, InternetOpenA` |

### Preguntas y Respuestas / Questions and Answers

| # | Task | Pregunta | Respuesta |
|---|---|---|---|
| 1 | Task 1 | Accept the invitation? (Yes/No) | `Yes` |
| 2 | Task 2 | What is the malicious C2 domain you found in the maldoc where an executable download was attempted? | `fpetraardella.band/xap_102b-AZ1/704e.php?l=litten4.gas` |
| 3 | Task 2 | What executable file is the maldoc trying to drop? | `QdZGP.exe` |
| 4 | Task 2 | In what folder is it dropping the malicious executable? (hint: %Folder%) | `%ProgramData%` |
| 5 | Task 2 | Provide the name of the COM object the maldoc is trying to access. | `ShellBrowserWindow` |
| 6 | Task 2 | Include the malicious IP and the php extension found in the maldoc. (Format: IP/name.php) | `176.32.35.16/704e.php` |
| 7 | Task 2 | Find the phone number in the maldoc. (Answer format: xxx-xxx-xxxx) | `213-446-1757` |
| 8 | Task 2 | Doing some static analysis, provide the type of maldoc this is under the keyword "AutoOpen". | `AutoExec` |
| 9 | Task 2 | Provide the subject for this maldoc. (make sure to remove the extra whitespace) | `West Virginia Samanta` |
| 10 | Task 2 | Provide the time when this document was last saved. (Format: YEAR-MONTH-DAY XX:XX:XX) | `2019-02-07 23:45:30` |
| 11 | Task 2 | Provide the stream number that contains a macro. | `8` |
| 12 | Task 2 | Provide the name of the stream that contains a macro. | `ThisDocument` |
| 13 | Task 3 | Provide the streams (numbers) that contain macros. | `12, 13, 14, 16` |
| 14 | Task 3 | Provide the size (bytes) of the compiled code for the second stream that contains a macro. | `13867` |
| 15 | Task 3 | Provide the largest number of bytes found while analyzing the streams. | `63641` |
| 16 | Task 3 | Find the command located in the 'fun' field (make sure to reverse the string). | `cmd /k cscript.exe C:\ProgramData\pin.vbs` |
| 17 | Task 3 | Provide the first domain found in the maldoc. | `priyacareers.com/u9hDQN9Yy7g/pt.html` |
| 18 | Task 3 | Provide the second domain found in the maldoc. | `perfectdemos.com/Gv1iNAuMKZ/pt.html` |
| 19 | Task 3 | Provide the name of the first malicious DLL it retrieves from the C2 server. | `www1.dll` |
| 20 | Task 3 | How many DLLs does the maldoc retrieve from the domains? | `5` |
| 21 | Task 3 | Provide the path of where the malicious DLLs are getting dropped onto? | `C:\ProgramData` |
| 22 | Task 3 | What program is it using to run DLLs? | `rundll32.exe` |
| 23 | Task 3 | How many seconds does the function in the maldoc sleep for to fully execute the malicious DLLs? | `15` |
| 24 | Task 3 | Under what stream did the main malicious script use to retrieve DLLs from the C2 domains? (Provide the name of the stream). | `Macros/Form/o` |
| 25 | Task 4 | Provide the executable name being downloaded. | `1.exe` |
| 26 | Task 4 | What program is used to run the executable? | `Certutil` |
| 27 | Task 4 | Provide the malicious URI included in the maldoc that was used to download the binary (without http/https). | `8cfayv.com/bolb/jaent.php?l=liut6.cab` |
| 28 | Task 4 | What folder does the binary gets dropped in? | `ProgramData` |
| 29 | Task 4 | Which stream executes the binary that was downloaded? | `A3` |
| 30 | Task 5 | Provide the first decoded string found in this maldoc. | `MSXML2.XMLHTTP` |
| 31 | Task 5 | Provide the name of the binary being dropped. | `DYIATHUQLCW.exe` |
| 32 | Task 5 | Provide the folder where the binary is being dropped to. | `TEMP` |
| 33 | Task 5 | Provide the name of the second binary. | `bin.exe` |
| 34 | Task 5 | Provide the full URI from which the second binary was downloaded (exclude http/https). | `gv-roth.de/js/bin.exe` |
| 35 | Task 6 | What is the caption you found in the maldoc? | `CobaltStrikeIsEverywhere` |
| 36 | Task 6 | What is the XOR decimal value found in the decoded-base64 script? | `35` |
| 37 | Task 6 | Provide the C2 IP address of the Cobalt Strike server. | `176.103.56.89` |
| 38 | Task 6 | Provide the full user-agent found. | `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)` |
| 39 | Task 6 | Provide the path value for the Cobalt Strike shellcode. | `/SjMR` |
| 40 | Task 6 | Provide the port number of the Cobalt Strike C2 Server. | `8080` |
| 41 | Task 6 | Provide the first two APIs found. | `LoadLibraryA, InternetOpenA` |

---

**Metodología:**
1. Aceptar la invitación y abrir los cinco documentos de Office disponibles en el entorno.
2. Extraer cadenas y metadatos de cada maldoc (olevba/strings): dominios C2, nombres de ejecutables, carpetas de caída (`%ProgramData%`, `TEMP`), objetos COM y metadatos como subject y fecha de guardado.
3. Analizar los streams OLE para localizar los que contienen macros: número y nombre del stream, tamaño del código compilado y el mayor bloque de bytes.
4. Revertir cadenas y campos ofuscados (como el campo 'fun') para recuperar el comando real (cmd/cscript), los dominios de phishing y el reapunte a DLLs por `rundll32.exe`.
5. En el Attacker 5, descifrar el script base64 con XOR (decimal 35) para recuperar la configuración completa del Cobalt Strike: IP, puerto 8080, user-agent, ruta del shellcode y las dos APIs iniciales (`LoadLibraryA, InternetOpenA`).

### Cadena de ataque / Attack Chain

```text
Aceptar invitación -> Análisis estático de cadenas y metadatos -> Streams OLE (macros) -> Reversión de campos ofuscados -> Descifrado base64/XOR -> Configuración Cobalt Strike
```

**Learning chain:**
`maldoc → macros VBA → streams OLE → cadenas C2 → ejecutables/DLLs → rundll32/certutil → confusión base64/XOR → Cobalt Strike`

**Lección:** *Las macros de Office son la puerta de entrada del phishing: entre cadenas ofuscadas, streams OLE y confusión base64/XOR se esconde toda la infraestructura C2.*

**MITRE ATT&CK:**
T1204 (User Execution), T1566 (Phishing), T1059 (Command and Scripting Interpreter), T1105 (Ingress Tool Transfer), T1218 (System Binary Proxy Execution), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Squid Game](https://tryhackme.com/room/squidgameroom)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.