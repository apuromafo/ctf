# Advent of Cyber 2024

| **Dificultad** | N/A | **Tipo** | CTF (Free Room) | **Slug** | `adventofcyber2024` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber2024) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | OPSEC / Log Analysis / Atomic Red Team / XXE / Sandboxes / AWS / Shellcodes / GRC / Phishing / Wi-Fi / Web Timing / WebSockets / Certificates / Active Directory / Azure / Prompt Injection / Traffic Analysis / Reverse Engineering / Kubernetes / Hash Cracking / MQTT | | **Impacto** | Write-up completo del Advent of Cyber 2024 (24 días + encuesta final) con todas las respuestas verificadas |

---

**Contexto:** Repositorio de soluciones de la sala del Advent of Cyber 2024 de TryHackMe. El reto se desarrolla en el pueblo ficticio de Wareville durante la "SOC-mas": el villano Mayor Malware sabotea las operaciones de Santa mientras Glitch y McSkidy investigan cada incidente. La sala comprime 24 días de laboratorios (tareas 7-30), cada uno con una temática: OPSEC/OSINT, análisis de logs con SIEM/ELK, Atomic Red Team, XXE, sandboxes, logs AWS, shellcodes, GRC, phishing, ataques Wi-Fi, timing attacks, WebSockets, mal manejo de certificados, Active Directory, Azure, prompt injection, análisis de tráfico, ingeniería inversa, DFIR de Kubernetes, hash cracking y protocolos de comunicación (MQTT), cerrando con una encuesta. Respuestas capturadas línea a línea en el orden original del reto.

El original es 100% en inglés; se mantiene la pregunta y respuesta verbatim y se añaden anotaciones propias en español por día.

---

## Solucionario

### Día 1: OPSEC - Maybe SOC-mas music, he thought, doesn't come from a store?

**Explicación:** Día centrado en OPSEC (Security Operations / Secure Operations) y los errores de higiene que cometen los atacantes: reutilizar cuentas, dejar metadatos identificables en ficheros (exiftool sobre song.mp3), publicar en GitHub o no usar VPN. Sirve para atribuir la identidad digital de "M.M." (Mayor Malware) a partir de los metadatos del mp3, la URL del C2 (papash3ll.thm), su perfil de GitHub y las ramas/issues del repositorio encontrado.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Is there a dedicated Advent of Cyber channel on TryHackMe Discord where users can discuss daily challenges and receive dedicated support? (yes/no) | `yes` |
| 2 | Looks like the song.mp3 file is not what we expected! Run "exiftool song.mp3" in your terminal to find out the author of the song. Who is the author? | `Tyler Ramsbey` |
| 3 | The malicious PowerShell script sends stolen info to a C2 server. What is the URL of this C2 server? | `http://papash3ll.thm/data` |
| 4 | Who is M.M? Maybe his Github profile page would provide clues? | `Mayor Malware` |
| 5 | What is the number of commits on the GitHub repo where the issue was raised? | `1` |

### Día 2: Log Analysis - One man's false positive is another man's potpourri

**Explicación:** Análisis de logs (SIEM) para detectar un ataque de fuerza bruta y la técnica de un atacante encubierto. Se investigan los intentos de login fallidos (cuenta `service_admin`, 6791 intentos), la IP de origen del atacante (Glitch, `10.0.255.1`), su logon exitoso en ADM-01 (Dec 1, 2024 08:54:39.000) y el comando PowerShell ofuscado en Base64 que se decodifica con CyberChef: `Install-WindowsUpdate -AcceptAll -AutoReboot`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 6 | What is the name of the account causing all the failed login attempts? | `service_admin` |
| 7 | How many failed logon attempts were observed? | `6791` |
| 8 | What is the IP address of Glitch? | `10.0.255.1` |
| 9 | When did Glitch successfully logon to ADM-01? Format: MMM D, YYYY HH:MM:SS.SSS | `Dec 1, 2024 08:54:39.000` |
| 10 | What is the decoded command executed by Glitch to fix the systems of Wareville? | `Install-WindowsUpdate -AcceptAll -AutoReboot` |

### Día 3: Log Analysis (ELK) - Even if I wanted to go, their vulnerabilities wouldn't allow it.

**Explicación:** Operación Blue (análisis defensivo con ELK/Kibana sobre el índice `frostypines-resorts`) y Operación Red (recreación del ataque). Un atacante subió una web shell por subida de ficheros sin restringir en la web de Frosty Pines Resorts (RCE vía unrestricted file upload); el fichero se guardó en `/media/images/rooms/shell.php` y fue invocado desde la IP `10.11.83.34`. Con la shell (`ls`, `cat`) se recupera la flag `THM{Gl1tch_Was_H3r3}`. Se emplea KQL y la vista Discover de Kibana filtrando entre el 3 de octubre de 2024, 11:30-12:00.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 11 | BLUE: Where was the web shell uploaded to? | `/media/images/rooms/shell.php` |
| 12 | BLUE: What IP address accessed the web shell? | `10.11.83.34` |
| 13 | RED: What is the contents of the flag.txt? | `THM{Gl1tch_Was_H3r3}` |

### Día 4: Atomic Red Team - I'm all atomic inside!

**Explicación:** Uso del framework Atomic Red Team e Invoke-AtomicTest para emular ataques. Primero se emula T1566.001 (Spearphishing Attachment) ejecutando `Invoke-AtomicTest T1566.001 -TestNumbers 1`, se revisan los artefactos (PhishingAttachment.xlsm y su .txt en `%temp%`) y los eventos Sysmon (Event ID 1 y 11) para obtener la primera flag. Después se emula T1059.003 (Windows Command Shell) con `Invoke-AtomicTest T1059.003 -TestNumbers 4`, cuyo test es "Simulate BlackByte Ransomware Print Bombing", que crea `Wareville_Ransomware.txt` en `C:\Tools\AtomicRedTeam\atomics\t1059.003\src\`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 14 | What was the flag found in the .txt file that is found in the same directory as the PhishingAttachment.xslm artefact? | `THM{GlitchTestingForSpearphishing}` |
| 15 | What ATT&CK technique ID would be our point of interest? | `T1059` |
| 16 | What ATT&CK subtechnique ID focuses on the Windows Command Shell? | `T1059.003` |
| 17 | What is the name of the Atomic Test to be simulated? | `Simulate BlackByte Ransomware Print Bombing` |
| 18 | What is the name of the file used in the test? | `Wareville_Ransomware.txt` |
| 19 | What is the flag found from this Atomic Test? | `THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}` |

### Día 5: XXE - SOC-mas XX-what-ee?

**Explicación:** Introducción a XML External Entity (XXE). El atacante inserta una entidad externa en un documento XML para leer ficheros locales o hacer SSRF. En el laboratorio se recorre un sitio de "wishes" (deseos) navegando por los deseos; la fuerza bruta/Timing sobre el mismo revela `THM{Brut3f0rc1n6_mY_w4y}` y la inspección de una posible prueba de sabotaje revela `THM{m4y0r_m4lw4r3_b4ckd00rs}`. Herramientas típicas: Burp Suite; mitigación: deshabilitar external entity loading y validar entradas.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 20 | What is the flag discovered after navigating through the wishes? | `THM{Brut3f0rc1n6_mY_w4y}` |
| 21 | What is the flag seen on the possible proof of sabotage? | `THM{m4y0r_m4lw4r3_b4ckd00rs}` |

### Día 6: Sandboxes - If I can't find a nice malware to use, I'm not going.

**Explicación:** Análisis de malware en sandbox (FlareVM). Mayor Malware usa técnicas anti-sandbox (consulta la clave de registro `HKLM\Software\Microsoft\Windows\CurrentVersion` en busca de `ProgramFilesDir`) que se detectan con una regla YARA y un EDR custom ("Jingle Bells.ps1"); al detectarse, el EDR muestra la primera flag. Para evadir, el malware ofusca la consulta en Base64; con FLOSS (floss.exe sobre MerryChristmas.exe) se extraen las cadenas ofuscadas guardadas en malstrings.txt con la segunda flag. También se usan reglas YARA sobre logs Sysmon y EventRecordID.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 22 | What is the flag displayed in the popup window after the EDR detects the malware? | `THM{GlitchWasHere}` |
| 23 | What is the flag found in the malstrings.txt document after running floss.exe, and opening the file in a text editor? | `THM{HiddenClue}` |

### Día 7: AWS Log Analysis - CloudTrail / S3

**Explicación:** Análisis de logs de AWS (CloudTrail) tras un incidente en la nube. Se investigan las acciones del usuario `glitch` sobre un bucket S3 (ListObject y PutObject), la IP de origen 53.94.201.69, el evento ConsoleLogin generado por `signin.amazonaws.com` el 2024-11-28T15:21:54Z, y la creación del usuario anómalo por `mcskidy` con la política `AdministratorAccess`. Con los datos se atribuye la IP habitual de Mayor Malware (53.94.201.69), la IP real de McSkidy (31.210.15.79) y el número de cuenta bancaria de Mayor Malware: 2394 6912 7723 1294.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 24 | What is the other activity made by the user glitch aside from the ListObject action? | `PutObject` |
| 25 | What is the source IP related to the S3 bucket activities of the user glitch? | `53.94.201.69` |
| 26 | Based on the eventSource field, what AWS service generates the ConsoleLogin event? | `signin.amazonaws.com` |
| 27 | When did the anomalous user trigger the ConsoleLogin event? | `2024-11-28T15:21:54Z` |
| 28 | What was the name of the user that was created by the mcskidy user? | `glitch` |
| 29 | What type of access was assigned to the anomalous user? | `AdministratorAccess` |
| 30 | Which IP does Mayor Malware typically use to log into AWS? | `53.94.201.69` |
| 31 | What is McSkidy's actual IP address? | `31.210.15.79` |
| 32 | What is the bank account number owned by Mayor Malware? | `2394 6912 7723 1294` |

### Día 8: Shellcodes - Shellcodes of the world, unite!

**Explicación:** Introducción a shellcodes: generación de payloads de reverse shell y su ejecución en un entorno Windows (digital vault) usando herramientas como msfvenom, con técnicas de inyección y evasión. Al conseguir la reverse shell con `nc` en el puerto 4444, la flag aparece en `C:\Users\glitch\Desktop\flag.txt` (se lee con `type`); puede tardar alrededor de un minuto en aparecer.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 33 | What is the flag value once Glitch gets reverse shell on the digital vault using port 4444? Note: The flag may take around a minute to appear in the C:\Users\glitch\Desktop directory. You can view the content of the flag by using the command type C:\Users\glitch\Desktop\flag.txt. | `AOC{GOT _MY_ACCESS_B@CK007}` |

### Día 9: GRC y Evaluación de Riesgos / Risk Assessment

**Explicación:** Gobierno, Riesgo y Cumplimiento (Governance, Risk and Compliance): procesos con los que la organización evalúa y mitiga riesgos (por ejemplo el ransomware) equilibrando seguridad, disponibilidad y coste. Tras realizar la evaluación de riesgo del reto se obtiene la flag.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 34 | What does GRC stand for? | `Governance, Risk, and Compliance` |
| 35 | What is the flag you receive after performing the risk assessment? | `THM{R15K_M4N4G3D}` |

### Día 10: Phishing - SOC-mas Phishing

**Explicación:** Análisis de un ataque de phishing y del artefacto entregado al usuario. Tras ejecutar el documento malicioso (que devuelve una reverse shell) se consigue acceso al equipo de la víctima y se lee la flag de `flag.txt` en el escritorio de la cuenta Administrator.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 36 | What is the flag value inside the flag.txt file that’s located on the Administrator’s desktop? | `THM{PHISHING_CHRISTMAS}` |

### Día 11: Wi-Fi Attacks - WPA / PSK

**Explicación:** Auditoría inalámbrica: se monitoriza el tráfico Wi-Fi (modo monitor), se identifican las BSSID/SSID (interfaz propia `02:00:00:00:02:00`, AP `MalwareM_AP` con BSSID `02:00:00:00:00:00` y cliente conectado `02:00:00:00:01:00`), se captura el handshake WPA y se crackea el PSK (fluffy/champ24) para acceder a la red del AP de Mayor Malware.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 37 | What is the BSSID of our wireless interface? | `02:00:00:00:02:00` |
| 38 | What is the SSID and BSSID of the access point? Format: SSID, BSSID | `MalwareM_AP, 02:00:00:00:00:00` |
| 39 | What is the BSSID of the wireless interface that is already connected to the access point? | `02:00:00:00:01:00` |
| 40 | What is the PSK after performing the WPA cracking attack? | `fluffy/champ24` |

### Día 12: Web Timing Attacks - If I can’t steal their money, I’ll steal their joy!

**Explicación:** Ataques de timing/race condition en aplicaciones web: se explota la ventana de tiempo entre comprobación de estado y transferencia para transferir más de $2000 desde la cuenta de Glitch y completar la condición de carrera. La flag confirma "haber ganado la carrera".

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 41 | What is the flag value after transferring over $2000 from Glitch's account? | `THM{WON_THE_RACE_007}` |

### Día 13: WebSockets - It came without buffering! It came without lag!

**Explicación:** Comunicación bidireccional por WebSocket (a diferencia de HTTP, la conexión permanece abierta). Con Burp Suite (Intruder/Repeater) se manipulan mensajes WebSocket para modificar datos o elevar privilegios (débil autenticación, message tampering, CSWSH). Se obtienen dos flags (Flag1 y Flag2).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 42 | What is the value of Flag1? | `THM{dude_where_is_my_car}` |
| 43 | What is the value of Flag2? | `THM{my_name_is_malware._mayor_malware}` |

### Día 14: Certificate Mismanagement - Gift Scheduler

**Explicación:** Mala gestión de certificados: la página "Gift Scheduler" usa un certificado autofirmado o firmado por la CA "THM" (emisor). Revisando el histórico HTTP (POST requests) se recupera la contraseña del usuario `snowballelf` (c4rrotn0s3); con las credenciales de cualquier elfo (elf) se accede a la página de scheduling (flag AoC-3lf0nth3Sh3lf); reutilizando la contraseña se obtiene la cuenta de Marta May Ware (H0llyJ0llySOCMAS!) y con ella la consola administrativa (flag AoC-h0wt0ru1nG1ftD4y) que cancela el G-Day.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 44 | What is the name of the CA that has signed the Gift Scheduler certificate? | `THM` |
| 45 | Look inside the POST requests in the HTTP history. What is the password for the snowballelf account? | `c4rrotn0s3` |
| 46 | Use the credentials for any of the elves to authenticate to the Gift Scheduler website. What is the flag shown on the elves’ scheduling page? | `THM{AoC-3lf0nth3Sh3lf}` |
| 47 | What is the password for Marta May Ware’s account? | `H0llyJ0llySOCMAS!` |
| 48 | Mayor Malware finally succeeded in his evil intent: with Marta May Ware’s username and password, he can finally access the administrative console for the Gift Scheduler. G-Day is cancelled! What is the flag shown on the admin page? | `THM{AoC-h0wt0ru1nG1ftD4y}` |

### Día 15: Active Directory - Glitch_Malware

**Explicación:**
Hunt en Active Directory: se revisa el historial de PowerShell del Administrador (`Get-ADUser -Filter * -Properties MemberOf | Select-Object Name`) para enumerar usuarios, el log de Windows PowerShell (Application and Services Logs) donde se recupera la contraseña fijada a Glitch_Malware (SuperSecretP@ssw0rd!), el GPO instalado de persistencia ("Malicious GPO - Glitch_Malware Persistence"), el último login de Glitch_Malware (07/11/2024) y el Event ID 4624 de logon.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 49 | On what day was Glitch_Malware last logged in? | `07/11/2024` |
| 50 | What event ID shows the login of the Glitch_Malware user? | `4624` |
| 51 | Read the PowerShell history of the Administrator account. What was the command that was used to enumerate Active Directory users? | `Get-ADUser -Filter * -Properties MemberOf \| Select-Object Name` |
| 52 | Look in the PowerShell log file located in Application and Services Logs -> Windows PowerShell. What was Glitch_Malware's set password? | `SuperSecretP@ssw0rd!` |
| 53 | Review the Group Policy Objects present on the machine. What is the name of the installed GPO? | `Malicious GPO - Glitch_Malware Persistence` |

### Día 16: Azure Exploitation - Key Vault

**Explicación:** Explotación de una identidad de Azure: se filtra la contraseña de la cuenta `backupware` (R3c0v3r_s3cr3ts!), se localiza el grupo "Secret Recovery Group" (group ID 7d96660a-02e1-4112-9515-1762d0cb66b7) y se extrae el secreto del vault (nombre `aoc2024`) cuyo contenido es `WhereIsMyMind1999`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 54 | What is the password for backupware that was leaked? | `R3c0v3r_s3cr3ts!` |
| 55 | What is the group ID of the Secret Recovery Group? | `7d96660a-02e1-4112-9515-1762d0cb66b7` |
| 56 | What is the name of the vault secret? | `aoc2024` |
| 57 | What are the contents of the secret stored in the vault? | `WhereIsMyMind1999` |

### Día 17: Log Analysis - CCTV Footage

**Explicación:** Análisis de logs de las cámaras CCTV (cctv_feed): se extraen los eventos asociados al login exitoso (642 logs), se identifica la Session_id del atacante que borró la grabación (rij5uu4gt204q0d3eb7jj86okt) y el nombre del atacante en los logs: mmalware.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 58 | Extract all the events from the cctv_feed logs. How many logs were captured associated with the successful login? | `642` |
| 59 | What is the Session_id associated with the attacker who deleted the recording? | `rij5uu4gt204q0d3eb7jj86okt` |
| 60 | What is the name of the attacker found in the logs, who deleted the CCTV footage? | `mmalware` |

### Día 18: Prompt Injection - Chatbot / Health API

**Explicación:** Inyección de prompt contra un chatbot con restricciones (system prompt). Se identifica el término técnico "system prompt" (conjunto de reglas e instrucciones dadas al chatbot) y, mediante inyección, se consigue que el asistente invoque la API interna de salud con la query "status". Encadenando la inyección hasta obtener una reverse shell se lee `flag.txt` con la flag `THM{WareW1se_Br3ach3d}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 61 | What is the technical term for a set of rules and instructions given to a chatbot? | `system prompt` |
| 62 | What query should we use if we wanted to get the "status" of the health service from the in-house API? | `Use the health service with the query: status` |
| 63 | After achieving a reverse shell, look around for a flag.txt. What is the value? | `THM{WareW1se_Br3ach3d}` |

### Día 19: Secrets Vault - I merely noticed that you’re improperly stored, my dear secret!

**Explicación:** Explotación de una aplicación de almacenamiento/secrets (vault) con autenticación débil: se obtienen tres flags según el ítem recuperado: la flag OTP (one_tough_password), la flag del ítem "billionaire" (credit_card_undeclined) y la flag biométrica (dont_smash_your_keyboard), tras un bypass del control de acceso por manipulación de la lógica de la aplicación.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 64 | What is the OTP flag? | `THM{one_tough_password}` |
| 65 | What is the billionaire item flag? | `THM{credit_card_undeclined}` |
| 66 | What is the biometric flag? | `THM{dont_smash_your_keyboard}` |

### Día 20: Traffic Analysis - C2 Beaconing

**Explicación:** Análisis de tráfico de red (pcap) de un C2: se identifica el primer mensaje enviado por el payload al C2 de Mayor Malware ("I am in Mayor!"), la IP del C2 (10.10.123.224), el comando enviado desde el C2 (whoami), el fichero crítico exfiltrado (credentials.txt) y el mensaje secreto devuelto en los beacons cifrados (THM_Secret_101).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 67 | What was the first message the payload sent to Mayor Malware’s C2? | `I am in Mayor!` |
| 68 | What was the IP address of the C2 server? | `10.10.123.224` |
| 69 | What was the command sent by the C2 server to the target machine? | `whoami` |
| 70 | What was the filename of the critical file exfiltrated by the C2 server? | `credentials.txt` |
| 71 | What secret message was sent back to the C2 in an encrypted format through beacons? | `THM_Secret_101` |

### Día 21: Reverse Engineering - WarevilleApp.exe

**Explicación:** Ingeniería inversa del binario WarevilleApp.exe: la función que descarga y ejecuta ficheros es `DownloadAndExecuteFile`; al ejecutar la app descarga otro binario a Downloads (`explorer.exe`) desde el dominio `mayorc2.thm`; el binario stage 2 empaqueta los datos del equipo en `CollectedFiles.zip` y los sube al C2 `anonymousc2.thm`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 72 | What is the function name that downloads and executes files in the WarevilleApp.exe? | `DownloadAndExecuteFile` |
| 73 | Once you execute the WarevilleApp.exe, it downloads another binary to the Downloads folder. What is the name of the binary? | `explorer.exe` |
| 74 | What domain name is the one from where the file is downloaded after running WarevilleApp.exe? | `mayorc2.thm` |
| 75 | The stage 2 binary is executed automatically and creates a zip file comprising the victim's computer data; what is the name of the zip file? | `CollectedFiles.zip` |
| 76 | What is the name of the C2 server where the stage 2 binary tries to upload files? | `anonymousc2.thm` |

### Día 22: Kubernetes DFIR - Docker Registry

**Explicación:** DFIR en Kubernetes/Docker: se encuentra la web shell usada por Mayor Malware (shelly.php), el fichero leído del pod (db.php), la herramienta buscada para conexión remota (nc), la IP inesperada conectada al docker registry (10.10.130.253), el primer acceso desde esa IP (29/Oct/2024:10:06:33 +0000), el push de la imagen maliciosa (29/Oct/2024:12:34:28 +0000) y el valor del secreto "pull-creds" con credenciales del registry.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 77 | What is the name of the webshell that was used by Mayor Malware? | `shelly.php` |
| 78 | What file did Mayor Malware read from the pod? | `db.php` |
| 79 | What tool did Mayor Malware search for that could be used to create a remote connection from the pod? | `nc` |
| 80 | What IP connected to the docker registry that was unexpected? | `10.10.130.253` |
| 81 | At what time is the first connection made from this IP to the docker registry? | `29/Oct/2024:10:06:33 +0000` |
| 82 | At what time is the updated malicious image pushed to the registry? | `29/Oct/2024:12:34:28 +0000` |
| 83 | What is the value stored in the "pull-creds" secret? | `{"auths":{"http://docker-registry.nicetown.loc:5000":{"username":"mr.nice","password":"Mr.N4ughty","auth":"bXIubmljZTpNci5ONHVnaHR5"}}}` |

### Día 23: Hash Cracking - Passwords y PDF

**Explicación:** Cracking de hashes y documentos protegidos: se crackea el hash de `hash1.txt` (contraseña fluffycat12) y se fuerza/procesa el fichero `private.pdf` para leer la flag de su cabecera (THM{do_not_GET_CAUGHT}). Herramientas típicas: Hashcat/John the Ripper y (para el PDF) john/pdf2john.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 84 | Crack the hash value stored in hash1.txt. What was the password? | `fluffycat12` |
| 85 | What is the flag at the top of the private.pdf file? | `THM{do_not_GET_CAUGHT}` |

### Día 24: Communication Protocols - MQTT

**Explicación:** Análisis de protocolos de comunicación IoT (MQTT): inspeccionando el tráfico MQTT se localizan los comandos maliciosos y la flag del día.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 86 | What is the flag? | `THM{Ligh75on-day54ved}` |

### Encuesta final / Final Survey

**Explicación:** Para cerrar la sala, la encuesta final entrega la flag de confirmación del reto completo.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 87 | What is the flag you get at the end of the survey? | `THM{we_will_be_back_in_2025}` |

---

**Metodología:**

1. OPSEC y atribución de la identidad del atacante via metadatos y OSINT (Día 1).

2. Análisis de logs (SIEM/ELK, KQL, Event Viewer, Sysmon, CloudTrail) para reconstruir la cadena de ataque (Días 2, 3, 7, 17).

3. Emulación de ataques con Atomic Red Team y detección con reglas YARA/Sigma (Días 4, 6).

4. Explotación web: XXE, timing/race condition, WebSockets, IDOR/certificados y prompt injection (Días 5, 12, 13, 14, 18).

5. Red team en infraestructura: shellcodes, Wi-Fi/WPA, Active Directory y Azure (Días 8, 11, 15, 16).

6. DFIR y malware: sandboxes, tráfico C2, ingeniería inversa y Kubernetes (Días 6, 20, 21, 22).

7. Cracking de hashes/PDF y análisis de protocolos IoT (Días 23, 24), cerrando con GRC y la encuesta (Días 9, 25).

**Learning chain:** OPSEC -> Log Analysis -> Atomic Red Team -> XXE -> Sandboxes -> AWS -> Shellcodes -> GRC -> Phishing -> Wi-Fi -> Web Timing -> WebSockets -> Certificates -> Active Directory -> Azure -> Prompt Injection -> Traffic Analysis -> Reverse Engineering -> Kubernetes DFIR -> Hash Cracking -> MQTT

**Lección:** *El Advent of Cyber 2024 entrelaza blue team (SIEM/ELK, Sysmon, GRC, DFIR) con red team (web, Wi-Fi, AD, Azure, Kubernetes) alrededor de una única historia (Wareville/SOC-mas), mostrando que el análisis forense y la detección son tan ofensivos como la explotación.* 

**MITRE ATT&CK:**

- T1592 / T1593 - Gather Victim Host Information / Search Open Websites/Domains (Día 1, OPSEC/OSINT)
- T1110 - Brute Force (Días 2, 11 y 12, fuerza bruta y timing)
- T1505.003 - Web Shell (Día 3)
- T1566.001 - Spearphishing Attachment (Días 4 y 10)
- T1059.003 - Command and Scripting Interpreter: Windows Command Shell (Día 4)
- T1190 - Exploit Public-Facing Application (Días 5, 12 y 13)
- T1497 - Virtualization/Sandbox Evasion (Día 6)
- T1078 - Valid Accounts (Días 7, 15, 16 y 19)
- T1530 - Data from Cloud Storage (Día 7)
- T1105 - Ingress Tool Transfer (Días 20 y 21)
- T1573 / T1071.001 - Encrypted Channel / Web Service C2 (Día 20)
- T1027 - Obfuscated Files or Information (Días 6 y 21)
- T1578.001 - Modify Cloud Compute/Storage Infrastructure (Día 22)
- T1558 / T1110.002 - Steal or Forge Kerberos Tickets / Password Cracking (Días 23)

**Fuente:** [TryHackMe - Advent of Cyber 2024](https://tryhackme.com/room/adventofcyber2024)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.