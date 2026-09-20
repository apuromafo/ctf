# Advent 2023 [N/A]

| **Dificultad** | Easy | **Tipo** | CTF (Free Room) | **Slug** | `adventofcyber2023` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber2023) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | machine learning / chatbot / log analysis / packet capture / hydra / pin bruteforce / cewl / reverse engineering / memory corruption / pwn / proxy logs / disk forensics / malware analysis / c2 / sql injection / lpe / devsecops jenkins / intrusion detection / diamond model / cnn captcha / silk / network flows / dfir / systemd / ad kerberos netntlm / responder / mobile forensics / forense de disco / telefonía | | **Impacto** | McGreedy y los Frostlings protagonizan 22 bloques que van del análisis de logs, forensia y malware hasta machine learning, SQLi, Jenkins, SiLK y Active Directory |

---

**Contexto:** Advent of Cyber 2023: el villano McGreedy (AntarctiCrafts / Frostlings) ataca la infraestructura de la Best Festival Company. El room `adventofcyber2023` propone 24 días de retos. Este solucionario cubre: historia/introducción (Discord, email de McGreedy, contraseña de la sala del servidor, proyecto secreto Purple Snow), análisis de paquetes, brute force con Hydra (PIN) y CeWL, reversing de firma de backup (DOS), memory corruption (pwn), análisis de logs de proxy (DNS y exfiltración), forensia de disco, análisis de malware (C2 HTTP, minería), SQL injection, escalada de privilegios, Jenkins/DevSecOps, detección de intrusiones (Diamond Model), machine learning (spam, CNN/CAPTCHA), análisis de flujos con SiLK, DFIR de procesos y systemd, compromiso/defensa web (site deface, C2), Active Directory (Kerberos/NetNTLM/Responder) y forensia de teléfono.

---

## Solucionario

### Día 1: Historia e Introducción (Chatbot y Ambientación)

**Explicación:** Preguntas de ambientación de la historia: canal de Discord dedicado de Advent of Cyber (sí), email personal de McGreedy `t.mcgreedy@antarcticrafts.thm`, password de la puerta de la sala del servidor de TI (`BtY2S02`) y el nombre del proyecto secreto de McGreedy: Purple Snow.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Is there a dedicated Advent of Cyber channel on TryHackMe Discord where users can discuss daily challenges and receive dedicated support? (yes/no) | `yes` |
| 2 | What is McGreedy's personal email address? | `t.mcgreedy@antarcticrafts.thm` |
| 3 | What is the password for the IT server room door? | `BtY2S02` |
| 4 | What is the name of McGreedy's secret project? | `Purple Snow` |

### Día 2: Análisis de Paquetes (Log Analysis)

**Explicación:** Análisis de una captura de paquetes: número total de paquetes capturados (100), IP que envió más tráfico (10.10.1.4) y el protocolo más frecuente (ICMP).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How many packets were captured (looking at the PacketNumber)? | `100` |
| 2 | What IP address sent the most amount of traffic during the packet capture? | `10.10.1.4` |
| 3 | What was the most frequent protocol? | `ICMP` |

### Día 3: PIN Brute Force — Hydra y Crunch

**Explicación:** Generación de wordlist con crunch y brute force del sistema de control con Hydra para obtener el código PIN de 4 dígitos y desbloquear la puerta.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Using crunch and hydra, find the PIN code to access the control system and unlock the door. What is the flag? | `THM{pin-code-brute-force}` |

### Día 4: Brute Force Web — CeWL

**Explicación:** Personalización de wordlist con CeWL a partir del contenido del sitio para encontrar la combinación de usuario/contraseña correcta que da acceso al panel.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the correct username and password combination? Format username:password | `isaias:Happiness` |
| 2 | What is the flag? | `THM{m3rrY4nt4rct1crAft$}` |

### Día 5: Reverse Engineering — Backup DOS (Magic Bytes)

**Explicación:** Reversing de un backup antiguo (DOS): tamaño del archivo AC2023.BAK (12,704 bytes), nombre del programa de backup (BackupMaster3000), firma/correct bytes del file signature para restaurarlo (`41 43`) y la flag al restaurar el backup correctamente.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How large (in bytes) is the AC2023.BAK file? | `12,704` |
| 2 | What is the name of the backup program? | `BackupMaster3000` |
| 3 | What should the correct bytes be in the backup's file signature to restore the backup properly? | `41 43` |
| 4 | What is the flag after restoring the backup successfully? | `THM{0LD_5CH00L_C00L_d00D}` |

### Día 6: Pwn — Memory Corruption

**Explicación:** Día de memory corruption en un juego: con el valor en memoria de la variable `coins`, calcular cuántas monedas habría en el juego (1397772111) y obtener la flag final del nivel.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | If the coins variable had the in-memory value in the image below, how many coins would you have in the game? | `1397772111` |
| 2 | What is the value of the final flag? | `THM{mchoneybell_is_the_real_star}` |

### Día 7: Análisis de Logs de Proxy — Exfiltración

**Explicación:** Análisis de los logs del servidor proxy corporativo: IPs únicas conectadas (9), dominios únicos accedidos por todas las workstations (111), status code de las peticiones al dominio menos accedido (503), dominio sospechoso (frostlings.bigbadstash.thm), IP de origen que lo accedió (10.10.185.225), nº total de peticiones (1581) y la flag oculta tras recuperar los datos exfiltrados.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How many unique IP addresses are connected to the proxy server? | `9` |
| 2 | How many unique domains were accessed by all workstations? | `111` |
| 3 | What status code is generated by the HTTP requests to the least accessed domain? | `503` |
| 4 | Based on the high count of connection attempts, what is the name of the suspicious domain? | `frostlings.bigbadstash.thm` |
| 5 | What is the source IP of the workstation that accessed the malicious domain? | `10.10.185.225` |
| 6 | How many requests were made on the malicious domain in total? | `1581` |
| 7 | Having retrieved the exfiltrated data, what is the hidden flag? | `THM{a_gift_for_you_awesome_analyst!}` |

### Día 8: Forensia de Disco

**Explicación:** Forensia de disco: servidor C2 del malware (`mcgreedysecretc2.thm`), archivo dentro del zip borrado (`JuicyTomaTOY.exe`), flag oculta en uno de los PNG eliminados y el SHA1 de la unidad física/imagen forense (`39f2dea6ffb43bf80d80f19d122076b3682773c2`).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the malware C2 server? | `mcgreedysecretc2.thm` |
| 2 | What is the file inside the deleted zip archive? | `JuicyTomaTOY.exe` |
| 3 | What flag is hidden in one of the deleted PNG files? | `THM{byt3-L3vel_@n4Lys15}` |
| 4 | What is the SHA1 hash of the physical drive and forensic image? | `39f2dea6ffb43bf80d80f19d122076b3682773c2` |

### Día 9: Análisis de Malware — Comunicación C2 HTTP

**Explicación:** Análisis de la muestra maliciosa y su comunicación con el C2: User-Agent usado (Mozilla/5.0 ... Safari/605.1.15), método HTTP para enviar la salida de comandos (POST), clave de cifrado/descifrado de los datos C2 (`youcanthackthissupersecurec2keys`), primera URL HTTP usada (`http://mcgreedysecretc2.thm/reg`), segundos del sleep hardcodeado (15), comando C2 para ejecutar comandos vía cmd.exe (`shell`) y el dominio para descargar otro binario (`stash.mcgreedy.thm`).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What HTTP User-Agent was used by the malware for its connection requests to the C2 server? | `Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15` |
| 2 | What is the HTTP method used to submit the command execution output? | `POST` |
| 3 | What key is used by the malware to encrypt or decrypt the C2 data? | `youcanthackthissupersecurec2keys` |
| 4 | What is the first HTTP URL used by the malware? | `http://mcgreedysecretc2.thm/reg` |
| 5 | How many seconds is the hardcoded value used by the sleep function? | `15` |
| 6 | What is the C2 command the attacker uses to execute commands via cmd.exe? | `shell` |
| 7 | What is the domain used by the malware to download another binary? | `stash.mcgreedy.thm` |

### Día 10: SQL Injection

**Explicación:** Explotación del formulario de búsqueda de regalos vulnerable (`/giftsearch.php`): análisis del mensaje de error SQL (ODBC Driver 17 for SQL Server), inyección de la condición 1=1 para listar todos los resultados (último resultado del listado = flag), flag en la nota que dejó Gr33dstr en el sistema y flag de la homepage tras restaurar el sitio.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Manually navigate the defaced website to find the vulnerable search form. What is the first webpage you come across that contains the gift-finding feature? | `/giftsearch.php` |
| 2 | Analyze the SQL error message that is returned. What ODBC Driver is being used in the back end of the website? | `ODBC Driver 17 for SQL Server` |
| 3 | Inject the 1=1 condition into the Gift Search form. What is the last result returned in the database? | `THM{a4ffc901c27fb89efe3c31642ece4447}` |
| 4 | What flag is in the note file Gr33dstr left behind on the system? | `THM{b06674fedd8dfc28ca75176d3d51409e}` |
| 5 | What is the flag you receive on the homepage after restoring the website? | `THM{4cbc043631e322450bc55b42c}` |

### Día 11: Escalada de Privilegios (LPE)

**Explicación:** Escalada de privilegios en el host comprometido vía SQLi: hash del usuario vulnerable (`03E805D8A8C5AA435FB48832DAD620E3`) y flag en el Desktop del Administrador (`THM{XMAS_IS_SAFE}`).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the hash of the vulnerable user? | `03E805D8A8C5AA435FB48832DAD620E3` |
| 2 | What is the content of flag.txt on the Administrator Desktop? | `THM{XMAS_IS_SAFE}` |

### Día 12: DevSecOps — Jenkins

**Explicación:** Enumeración/explotación del entorno Jenkins: puerto por defecto (8080), password del usuario tracy (`13_1n_33`) y las flags de root, SSH y Jenkins obtenidas al escalar en el nodo.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the default port for Jenkins? | `8080` |
| 2 | What is the password of the user tracy? | `13_1n_33` |
| 3 | What's the root flag? | `ezRo0tW1thoutDiD` |
| 4 | What's the SSH flag? | `Ne3d2SecureTh1sSecureSh31l` |
| 5 | What's the Jenkins flag? | `FullTrust_has_n0_Place1nS3cur1ty` |

### Día 13: Detección de Intrusiones (Diamond Model)

**Explicación:** Análisis del breach y estrategias de defensa: modelo de seguridad usado (Diamond Model), capacidad defensiva de búsqueda activa (Threat hunting), los dos focos principales de infraestructura (Firewall and Honeypot), comando de firewall para bloquear tráfico (Deny) y la flag escondida en una de las historias.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Which security model is being used to analyse the breach and defence strategies? | `Diamond Model` |
| 2 | Which defence capability is used to actively search for signs of malicious activity? | `Threat hunting` |
| 3 | What are our main two infrastructure focuses? (Answer format: answer1 and answer2) | `Firewall and Honeypot` |
| 4 | Which firewall command is used to block traffic? | `Deny` |
| 5 | There is a flag in one of the stories. Can you find it? | `THM{P0T$_W@11S_4_S@N7@}` |

### Día 14: Machine Learning (Introducción)

**Explicación:** Fundamentos de IA/ML aplicados a seguridad: término para AI/ML que enseña a las máquinas cómo piensan los humanos o funciona la naturaleza (Machine Learning), estructura ML que imita la selección natural (Genetic Algorithm), estilo de aprendizaje con datos etiquetados (Supervised Learning), capa intermedia de una red neuronal (Hidden Layer), proceso de feedback (Back-Propagation) y la flag de la predicción con más del 90% de precisión.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the other term given for Artificial Intelligence or the subset of AI meant to teach computers how humans think or nature works? | `Machine Learning` |
| 2 | What ML structure aims to mimic the process of natural selection and evolution? | `Genetic Algorithm` |
| 3 | What is the name of the learning style that makes use of labelled data to train an ML structure? | `Supervised Learning` |
| 4 | What is the name of the layer between the Input and Output layers of a Neural Network? | `Hidden Layer` |
| 5 | What is the name of the process used to provide feedback to the Neural Network on how close its prediction was? | `Back-Propagation` |
| 6 | What is the value of the flag you received after achieving more than 90% accuracy on your submitted predictions? | `THM{Neural.Networks.are.Neat!}` |

### Día 15: Machine Learning — Pipeline y Spam

**Explicación:** Aplicación práctica del pipeline de ML para detectar spam: primer paso clave (data collection), feature engineering, promedio ponderado de precisión de detección de spam (0.98), nº de emails de test marcados como spam (3) y el código secreto en uno de esos emails (`I_Hate_Best_FestiVal`).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the key first step in the Machine Learning pipeline? | `data collection` |
| 2 | Which data preprocessing feature is used to create new features or modify existing ones to improve model performance? | `feature engineering` |
| 3 | During the data splitting step, 20% of the dataset was split for testing. What is the percentage weightage avg of precision of spam detection? | `0.98` |
| 4 | How many of the test emails are marked as spam? | `3` |
| 5 | One of the emails that is detected as spam contains a secret code. What is the code? | `I_Hate_Best_FestiVal` |

### Día 16: CNN y CAPTCHA

**Explicación:** Redes convolucionales para romper CAPTCHAs: proceso clave de entrenamiento cubierto por una CNN (Feature Extraction), proceso usado para extraer las features (Convolution), proceso que reduce las features (Pooling), CNN lista para usar (Attention OCR), password que McGreedy puso en el portal HQ Admin (`ReallyNotGonnaGuessThis`) y la flag al autenticarse.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What key process of training a neural network is taken care of by using a CNN? | `Feature Extraction` |
| 2 | What is the name of the process used in the CNN to extract the features? | `Convolution` |
| 3 | What is the name of the process used to reduce the features down? | `Pooling` |
| 4 | What off-the-shelf CNN did we use to train a CAPTCHA-cracking OCR model? | `Attention OCR` |
| 5 | What is the password that McGreedy set on the HQ Admin portal? | `ReallyNotGonnaGuessThis` |
| 6 | What is the value of the flag that you receive when you successfully authenticate to the HQ Admin portal? | `THM{Captcha.Can't.Hold.Me.Back}` |

### Día 17: Análisis de Tráfico — SiLK

**Explicación:** Análisis de flujos de red con SiLK: versión instalada (3.19.1), tamaño de los flows en los records (11774), sTime del sexto record, puerto destino del sexto record UDP (49950), % de records del dport 53 (35.332088), bytes transmitidos por el top talker (735229), sTime del primer DNS a puerto 53, IP controlada por el C2 (defanged) y la supuesta IP del flood attacker, además del nº de records SYN (1658).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Which version of SiLK is installed on the VM? | `3.19.1` |
| 2 | What is the size of the flows in the count records? | `11774` |
| 3 | What is the start time (sTime) of the sixth record in the file? | `2023/12/05T09:33:07.755` |
| 4 | What is the destination port of the sixth UDP record? | `49950` |
| 5 | What is the record value (%) of the dport 53? | `35.332088` |
| 6 | What is the number of bytes transmitted by the top talker on the network? | `735229` |
| 7 | What is the sTime value of the first DNS record going to port 53? | `2023/12/08T04:28:44.825` |
| 8 | What is the IP address of the host that the C2 potentially controls? (In defanged format: 123[.]456[.]789[.]0 ) | `175[.]175[.]173[.]221` |
| 9 | Which IP address is suspected to be the flood attacker? (In defanged format: 123[.]456[.]789[.]0 ) | `175[.]215[.]236[.]223` |
| 10 | What is the sent SYN packet's number of records? | `1658` |

### Día 18: DFIR de Procesos — Minero (systemd)

**Explicación:** DFIR de un sistema infectado con un minero: servicio que respawna el proceso (`a-unkillable.service`), path desde el que se ejecutaba (`/etc/systemd/system`), cuándo se muestra el mensaje de burla (opción 4), password expuesta en el bash history (`NEhX4VSrN7sV`), PID del minero (10280) y sus MD5, MD5 de mysqlserver, URL sospechosa defanged (`hxxp[://]mcgreedysecretc2[.]thm`) y la ubicación donde se drops el proceso mysqlserver.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the name of the service that respawns the process after killing it? | `a-unkillable.service` |
| 2 | What is the path from where the process and service were running? | `/etc/systemd/system` |
| 3 | The malware prints a taunting message. When is the message shown? Choose from the options below. | `4` |
| 4 | What is the exposed password that we find from the bash history output? | `NEhX4VSrN7sV` |
| 5 | What is the PID of the miner process that we find? | `10280` |
| 6 | What is the MD5 hash of the miner process? | `153a5c8efe4aa3be240e5dc645480dee` |
| 7 | What is the MD5 hash of the mysqlserver process? | `c586e774bb2aa17819d7faae18dad7d1` |
| 8 | Use the command strings extracted/miner.<PID from question 2>.0x400000 | grep http://. What is the suspicious URL? (Fully defang the URL using CyberChef) | `hxxp[://]mcgreedysecretc2[.]thm` |
| 9 | After reading the elfie file, what location is the mysqlserver process dropped in on the file system? | `/var/tmp/.system-python3.8-Updates/mysqlserver` |

### Día 19: Compromiso Web y C2

**Explicación:** Investigación del site calendario defaceado y del panel C2: handle del developer responsable de los merge changes (`@badsecops`), puerto del server del site (9081), server web malicioso (Apache), mensaje de los Frostlings (FROSTLINGS RULE), commit ID del código original (986b7407), kernel del nodo Jenkins (5.4.0-1029-aws), valor de secret.key, si SSRF carga solo recursos externos (nay), versión C2 (1.1), usuario del panel C2 (mcgreedy) y las flags de acceso al panel y de detener la exfiltración.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the handle of the developer responsible for the merge changes? | `@badsecops` |
| 2 | What port is the defaced calendar site server running on? | `9081` |
| 3 | What server is the malicious server running on? | `Apache` |
| 4 | What message did the Frostlings leave on the defaced site? | `FROSTLINGS RULE` |
| 5 | What is the commit ID of the original code for the Advent Calendar site? | `986b7407` |
| 6 | What Linux kernel version is the Jenkins node? | `5.4.0-1029-aws` |
| 7 | What value is found from /var/lib/jenkins/secret.key? | `90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7` |
| 8 | Is SSRF the process in which the attacker tricks the server into loading only external resources (yea/nay)? | `nay` |
| 9 | What is the C2 version? | `1.1` |
| 10 | What is the username for accessing the C2 panel? | `mcgreedy` |
| 11 | What is the flag value after accessing the C2 panel? | `THM{EXPLOITED_31001}` |
| 12 | What is the flag value after stopping the data exfiltration from the McSkidy computer? | `THM{AGENT_REMOVED_1001}` |

### Día 20: Active Directory — Kerberos, NetNTLM y Responder

**Explicación:** Ataques de autenticación en Active Directory: protocolo AD basado en tickets (Kerberos), protocolo AD que usa el hash NTLM (NetNTLM), herramienta que intercepta estos challenges de autenticación (Responder), password del Administrator (`GreedyGrabber1@`) y la flag en su Desktop.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the name of the AD authentication protocol that makes use of tickets? | `Kerberos` |
| 2 | What is the name of the AD authentication protocol that makes use of the NTLM hash? | `NetNTLM` |
| 3 | What is the name of the tool that can intercept these authentication challenges? | `Responder` |
| 4 | What is the password that McGreedy set for the Administrator account? | `GreedyGrabber1@` |
| 5 | What is the value of the flag that is placed on the Administrator's desktop? | `THM{Greedy.Greedy.McNot.So.Great.Stealy}` |

### Día 21: Forense Móvil y Desenlace

**Explicación:** Forensia del teléfono de Tracy: flag en una de las fotos (`THM{DIGITAL_FORENSICS}`), nombre con el que Tracy guarda el número de Detective Frost-eau (Detective Carrot-Nose), password en un SMS con Van Sprinkles (`chee7AQu`) y la flag final de la historia.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | One of the photos contains a flag. What is it? | `THM{DIGITAL_FORENSICS}` |
| 2 | What name does Tracy use to save Detective Frost-eau's phone number? | `Detective Carrot-Nose` |
| 3 | One SMS exchanged with Van Sprinkles contains a password. What is it? | `chee7AQu` |
| 4 | What is the final flag? | `THM{YouMeddlingKids}` |

### Día 22: Encuesta Final

**Explicación:** Encuesta de cierre del evento; al completarla se obtiene la flag de agradecimiento.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What flag did you get after completing the survey? | `THM{SurveyComplete_and_HolidaysSaved}` |

---

**Metodología:**

1. Ambientación y OSINT básico de la historia (Discord, emails, proyecto secreto)
2. Análisis de capturas de paquetes (PacketNumber, IPs y protocolos)
3. Generación de wordlists con crunch/CeWL y brute force con Hydra (PIN y login web)
4. Reversing de backups DOS y corrección de magic bytes
5. Memory corruption (pwn) y manipulación de variables en memoria
6. Análisis de logs de proxy (DNS, dominios, exfiltración)
7. Forensia de disco (zip/PNG borrados, SHA1 de imagen forense)
8. Análisis de malware: C2 HTTP, claves de cifrado, sleep y descarga de binarios
9. SQL injection (Gift Search, 1=1, ODBC) y escalada de privilegios
10. Enumeración/explotación de Jenkins (8080, secret.key, kernel)
11. Detección de intrusiones (Diamond Model, threat hunting, firewall/honeypot)
12. Machine Learning: fundamentos, pipeline, spam y CNN/CAPTCHA
13. Análisis de flujos con SiLK (records, puertos, top talker, SYN)
14. DFIR de procesos: systemd, bash history, MD5 y drops paths
15. Compromiso web (deface), client-side validation bypass y panel C2
16. Active Directory: Kerberos/NetNTLM con Responder y acceso administrativo
17. Forense de telefonía móvil y encuesta final

**Learning chain:** Historia/Ambientación -> Packet Analysis -> Hydra/Crunch -> CeWL -> Reversing Backup -> Memory Corruption -> Proxy Logs -> Disk Forensics -> Malware C2 -> SQLi -> LPE -> Jenkins -> Intrusion Detection -> ML -> CNN/CAPTCHA -> SiLK -> DFIR Miner -> Web/C2 -> Active Directory -> Mobile Forensics

**Lección:** *El AoC 2023 demostró que la seguridad moderna combina análisis defensivo (logs, flujos, forensia, DFIR) con inteligencia artificial (ML/CNN) y ofensiva clásica (SQLi, LPE, Kerberos), siempre alrededor de una historia de ataque corporativo.*

**MITRE ATT&CK:**

- T1059 - Command and Scripting Interpreter

- T1110 - Brute Force

- T1190 - Exploit Public-Facing Application

- T1068 - Exploitation for Privilege Escalation

- T1005 - Data from Local System

- T1041 - Exfiltration Over C2 Channel

- T1071 - Application Layer Protocol

- T1543 - Create or Modify System Process

- T1027 - Obfuscated Files or Information

- T1558 - Steal or Forge Kerberos Tickets

**Fuente:** [TryHackMe - Advent 2023 [N/A]](https://tryhackme.com/room/adventofcyber2023)


---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.