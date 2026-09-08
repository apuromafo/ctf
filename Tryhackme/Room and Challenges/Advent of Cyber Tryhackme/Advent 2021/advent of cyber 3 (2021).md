# Advent of Cyber 3 (2021)

| **Dificultad** | N/A | **Tipo** | CTF (Free Room) | **Slug** | `adventofcyber3` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber3) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2021 | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | idor / cookie / dashboards / lfi / rce / php filter / nosql / mongo / dfir / santa rat / network http dns ftp / nmap / mssql / nfs / windows / dirb / osint / cloud aws s3 / docker / phishing / eicar / yara / oledump / powershell | | **Impacto** | Tercer Advent of Cyber, 24 dias con IDOR, LFI/RCE, NoSQL, DFIR de SantaRat, analisis de red, AWS Cloud, Docker, phishing y malware analysis |

---

**Contexto:** Advent of Cyber 3 (2021). Historias de Grinch Enterprises y el paso de McSkidy por monitorear, explorar y atacar el villano del anio. 24 dias: IDOR en el Inventory Management System, cookies hex/JSON, dashboards admin, LFI con PHP filter y log poisoning (RCE), MongoDB/NoSQL injection, DFIR completo del malware SantaRat (transcripciones, LOLbins, GitHub, uharc), analisis de trafico HTTP/DNS/FTP, Nmap/CVE-2021-42013, MSSQL, NFS, escalada Windows (Iperius), OSINT del operador (Twitter, keybase, Bitcoin), AWS (S3, EC2, Secrets Manager), Docker, phishing, EICAR/YARA, oledump/VBA y logs PowerShell.

---

## Solucionario

### Task 1: Web Exploitation - IDOR (Mischief Managed)

**Explicacion:** Encontrar cuentas y sus posiciones en la company mediante IDOR. Santa = The Boss!, McStocker = Build Manager, el responsable de tampering = Mischief Manager. Al arreglar el Inventory Management System: `THM{AOC_IDOR_2B34BHI3}`. Cookie nueva: `user-auth`; encoding hexadecimal; data en JSON; cookie admin (username=admin) hex: `7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | After finding Santa's account, what is their position in the company? | `The Boss!` |
| 2 | After finding McStocker's account, what is their position in the company? | `Build Manager` |
| 3 | After finding the account responsible for tampering, what is their position in the company? | `Mischief Manager` |
| 4 | What is the received flag when McSkidy fixes the Inventory Management System? | `THM{AOC_IDOR_2B34BHI3}` |
| 5 | What is the name of the new cookie that was created for your account? | `user-auth` |
| 6 | What encoding type was used for the cookie value? | `hexadecimal` |
| 7 | What object format is the data of the cookie stored in? | `JSON` |
| 8 | What is the value of the administrator cookie? (username = admin) | `7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d` |

### Task 2: Web Exploitation - Admin Dashboard

**Explicacion:** Team environment que no responde: HR; con network warning: Application. Enumerar con wordlist la dashboard admin: folder `admin`; default credentials `administrator`; admin panel flag `THM{ADM1N_AC3SS}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What team environment is not responding? | `HR` |
| 2 | What team environment has a network warning? | `Application` |
| 3 | Using a common wordlist for discovering content, enumerate http://MACHINE_IP to find the location of the administrator dashboard. What is the name of the folder? | `admin` |
| 4 | In your web browser, try some default credentials on the newly discovered login form for the "administrator" user. What is the password? | `administrator` |
| 5 | Access the admin panel. What is the value of the flag? | `THM{ADM1N_AC3SS}` |

### Task 3: Web Exploitation - Santa's Gadget Shop (LFI) Part 1

**Explicacion:** Santa se conecta al shop. Password para account "santa": `cookie`. Flag itinerary: `THM{SANTA_DELIVERS}`. Al deshabilitar el plugin: `THM{NO_MORE_BUTTMAS}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What valid password can you use to access the "santa" account? | `cookie` |
| 2 | What is the flag in Santa's itinerary? | `THM{SANTA_DELIVERS}` |
| 3 | What flag did you get when you disabled the plugin? | `THM{NO_MORE_BUTTMAS}` |

### Task 4: Web Exploitation - LFI / RCE

**Explicacion:** Entry point de la web app: `err`. LFI para leer /etc/flag: `THM{d29e08941cf7fe41df55f1a7da6c4c06}`. PHP filter de index.php: `$flag` = `THM{791d43d46018a0d89361dbf60d5d9eb8}`. Credenciales del login `McSkidy:A0C315Aw3s0m`. Password flag.thm.aoc server: `THM{552f313b52e3c3dbf5257d8c6db7f6f1}`. LFI a RCE via log page (./includes/logs/app_access.log): hostname `lfi-aoc-awesome-59aedca683fff9261263bb084880c965`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Deploy the attached VM and look around. What is the entry point for our web application? | `err` |
| 2 | Use the entry point to perform LFI to read the /etc/flag file. What is the flag? | `THM{d29e08941cf7fe41df55f1a7da6c4c06}` |
| 3 | Use the PHP filter technique to read the source code of the index.php. What is the $flag variable's value? | `THM{791d43d46018a0d89361dbf60d5d9eb8}` |
| 4 | Now that you read the index.php, there is a login credential PHP file's path. Use the PHP filter technique to read its content. What are the username and password? | `McSkidy:A0C315Aw3s0m` |
| 5 | Use the credentials to login into the web application. Help McSkidy to recover the server's password. What is the password of the flag.thm.aoc server? | `THM{552f313b52e3c3dbf5257d8c6db7f6f1}` |
| 6 | The web application logs all users' requests, and only authorized users can read the log file. Use the LFI to gain RCE via the log file page. What is the hostname of the webserver? The log file location is at ./includes/logs/app_access.log. | `lfi-aoc-awesome-59aedca683fff9261263bb084880c965` |

### Task 5: Web Exploitation - NoSQL (MongoDB)

**Explicacion:** Interactuar con MongoDB: flag `THM{8814a5e6662a9763f7df23ee59d944f9}`. Bypass login admin en Grinch Enterprise: `THM{b6b304f5d5834a4d089b570840b467a8}`. Gift search page list guest usernames: `THM{2ec099f2d602cc4968c5267970be1326}`. NoSQLi para mcskidy record: `ID:6184f516ef6da50433f100f4:mcskidy:admin`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Interact with the MongoDB server to find the flag. What is the flag? | `THM{8814a5e6662a9763f7df23ee59d944f9}` |
| 2 | We discussed how to bypass login pages as an admin. Can you log into the application that Grinch Enterprise controls as admin and retrieve the flag? | `THM{b6b304f5d5834a4d089b570840b467a8}` |
| 3 | Once you are logged in, use the gift search page to list all usernames that have guest roles. What is the flag? | `THM{2ec099f2d602cc4968c5267970be1326}` |
| 4 | Use the gift search page to perform NoSQL injection and retrieve the mcskidy record. What is the details record? | `ID:6184f516ef6da50433f100f4:mcskidy:admin` |

### Task 6: DFIR - SantaRat (Part 1)

**Explicacion:** OS Name laptop de Santa: `Microsoft Windows 11 Pro`. Password backdoor: `grinchstolechristmas`. Ruta original del archivo copiado al Desktop: `C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat`. LOLbin usado para encode: `certutil.exe`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What operating system is Santa's laptop running ("OS Name")? | `Microsoft Windows 11 Pro` |
| 2 | What was the password set for the new "backdoor" account? | `grinchstolechristmas` |
| 3 | In one of the transcription logs, the bad actor interacts with the target under the new backdoor user account, and copies a unique file to the Desktop. Before it is copied to the Desktop, what is the full path of the original file? | `C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat` |
| 4 | The actor uses a Living Off The Land binary (LOLbin) to encode this file, and then verifies it succeeded by viewing the output file. What is the name of this LOLbin? | `certutil.exe` |

### Task 7: DFIR - SantaRat (Part 2)

**Explicacion:** Folder que sugiere software publico en plataforma de codigo: `.github`. Folder "Bag of Toys": `bag_of_toys.zip`. Owner del repo SantaRat: `Grinchiest`. Repo pertinente: `operation-bag-of-toys`. Exe que instalo utilidad para exfiltrar la bolsa: `uharc-cmd-install.exe`. Contenido de los archivos maliciosos (coal, mold, etc.): `GRINCHMAS`. Password del archivo original uha: `TheGrinchiestGrinchmasOfAll` (sin crackear). Archivos originales en la bolsa: 228.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Drill down into the folders and see if you can find anything that might indicate how we could better track down what this SantaRat really is. What specific folder name clues us in that this might be publicly accessible software hosted on a code-sharing platform? | `.github` |
| 2 | Additionally, there is a unique folder named "Bag of Toys" on the Desktop! This must be where Santa prepares his collection of toys, and this is certainly sensitive data that the actor could have compromised. What is the name of the file found in this folder? | `bag_of_toys.zip` |
| 3 | What is the name of the user that owns the SantaRat repository? | `Grinchiest` |
| 4 | Explore the other repositories that this user owns. What is the name of the repository that seems especially pertinent to our investigation? | `operation-bag-of-toys` |
| 5 | Read the information presented in this repository. It seems as if the actor has, in fact, compromised and tampered with Santa's bag of toys! You can review the activity in the transcription logs. It looks as if the actor installed a special utility to collect and eventually exfiltrate the bag of toys. What is the name of the executable that installed a unique utility the actor used to collect the bag of toys? | `uharc-cmd-install.exe` |
| 6 | Following this, the actor looks to have removed everything from the bag of toys, and added in new things like coal, mold, worms, and more! What are the contents of these "malicious" files (coal, mold, and all the others)? | `GRINCHMAS` |
| 7 | What is the password to the original bag_of_toys.uha archive? (You do not need to perform any password-cracking or bruteforce attempts) | `TheGrinchiestGrinchmasOfAll` |
| 8 | How many original files were present in Santa's Bag of Toys? | `228` |

### Task 8: Network Analysis - HTTP / DNS / FTP

**Explicacion:** HTTP1 GET: directorio `login`. HTTP2 POST creds: `McSkidy:Christmas2021!`. User-Agent: `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}`. DNS TXT message flag: `THM{dd63a80bf9fdd21aabbf70af7438c257}`. FTP login password: `TryH@ckM3!`. Comando FTP para subir secret.txt (placeholder en original): `STOR` para upload. Contenido de secret.txt: `123^-^321`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | In the HTTP #1 - GET requests section, which directory is found on the web server? | `login` |
| 2 | What is the username and password used in the login page in the HTTP #2 - POST section? | `McSkidy:Christmas2021!` |
| 3 | What is the User-Agent's name that has been sent in HTTP #2 - POST section? | `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}` |
| 4 | In the DNS section, there is a TXT DNS query. What is the flag in the message of that DNS query? | `THM{dd63a80bf9fdd21aabbf70af7438c257}` |
| 5 | In the FTP section, what is the FTP login password? | `TryH@ckM3!` |
| 6 | In the FTP section, what is the FTP command used to upload the secret.txt file? | `STOR` |
| 7 | In the FTP section, what is the content of the secret.txt file? | `123^-^321` |

### Task 9: Network Analysis - Nmap

**Explicacion:** `nmap -sT MACHINE_IP`: puertos abiertos 1-100 = 2; puerto mas pequeno = 22; servicio del puerto mas alto = HTTP; `nmap -sS` mismos resultados = Y; version web server = Apache httpd 2.4.49; CVE resuelto en 2.4.51 = CVE-2021-42013.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Help McSkidy and run nmap -sT MACHINE_IP. How many ports are open between 1 and 100? | `2` |
| 2 | What is the smallest port number that is open? | `22` |
| 3 | What is the service related to the highest port number you found in the first question? | `HTTP` |
| 4 | Now run nmap -sS MACHINE_IP. Did you get the same results? (Y/N) | `Y` |
| 5 | If you want Nmap to detect the version info of the services installed, you can use nmap -sV MACHINE_IP. What is the version number of the web server? | `Apache httpd 2.4.49` |
| 6 | By checking the vulnerabilities related to the installed web server, you learn that there is a critical vulnerability that allows path traversal and remote code execution. Now you can tell McSkidy that Grinch Enterprises used this vulnerability. What is the CVE number of the vulnerability that was solved in version 2.4.51? | `CVE-2021-42013` |

### Task 10: Network Analysis - MSSQL

**Explicacion:** Puerto nuevo en resultados: 20212. Programa escuchando: `telnetd`. Puerto MS SQL Server: `1433`. Prompt de conexion: `1>`. Tabla reindeer id 9 primero nombre: `Rudolph`. Tabla schedule destino Dec 7: `Prague`. Tabla presents cantidad Power Bank: `25000`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the port number that appeared in the results now? | `20212` |
| 2 | What is the name of the program listening on the newly discovered port? | `telnetd` |
| 3 | There is an open port related to MS SQL Server accessible over the network. What is the port number? | `1433` |
| 4 | If the connection is successful, you will get a prompt. What is the prompt that you have received? | `1>` |
| 5 | We can see four columns in the table displayed above: id, first (name), last (name), and nickname. What is the first name of the reindeer of id 9? | `Rudolph` |
| 6 | Check the table schedule. What is the destination of the trip scheduled on December 7? | `Prague` |
| 7 | Check the table presents. What is the quantity available for the present "Power Bank"? | `25000` |

### Task 11: Network Analysis - Linux NFS

**Explicacion:** En el home de grinch hay flag: `THM{YjtKeUy2qT3v5dDH}`. Scan `nmap -Pn` (Windows bloquea ping): 7 TCP ports open. Puerto NFS/mountd: `2049`. Shares encontrados: 4. Shares "everyone": 3. Titulo file 2680-0.txt: `Meditations`. Share con id_rsa: `confidential`. MD5 de id_rsa: `3e2d315a38f377f304f5598dc2f044de`. Username p.....: `pepper`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | There is a flag hidden in the grinch user's home directory. What are its contents? | `THM{YjtKeUy2qT3v5dDH}` |
| 2 | Scan the target server with the IP MACHINE_IP. Remember that MS Windows hosts block pings by default, so we need to add -Pn, for example, nmap -Pn MACHINE_IP for the scan to work correctly. How many TCP ports are open? | `7` |
| 3 | In the scan results you received earlier, you should be able to spot NFS or mountd, depending on whether you used the -sV option with Nmap or not. Which port is detected by Nmap as NFS or using the mountd service? | `2049` |
| 4 | How many shares did you find? | `4` |
| 5 | How many shares show "everyone"? | `3` |
| 6 | What is the title of file 2680-0.txt? | `Meditations` |
| 7 | It seems that Grinch Enterprises has forgotten their SSH keys on our system. One of the shares contains a private key used for SSH authentication (id_rsa). What is the name of the share? | `confidential` |
| 8 | We can calculate the MD5 sum of a file using md5sum FILENAME. What is the MD5 sum of id_rsa? | `3e2d315a38f377f304f5598dc2f044de` |
| 9 | Complete the username: p..... | `pepper` |

### Task 12: DFIR Windows - Escalada

**Explicacion:** OS version: `10.0.17763 N/A Build 17763`. Backup service: `IperiusSvc`. Path del exe: `C:\Program Files (x86)\Iperius Backup\IperiusService.exe`. whoami: `the-grinch-hack\thegrinch`. flag.txt: `THM-736635221`. Donde encontrarlo a las 5:30: `jazzercize`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the OS version? | `10.0.17763 N/A Build 17763` |
| 2 | What backup service did you find running on the system? | `IperiusSvc` |
| 3 | What is the path of the executable for the backup service you have identified? | `C:\Program Files (x86)\Iperius Backup\IperiusService.exe` |
| 4 | Run the whoami command on the connection you have received on your attacking machine. What user do you have? | `the-grinch-hack\thegrinch` |
| 5 | What is the content of the flag.txt file? | `THM-736635221` |
| 6 | The Grinch forgot to delete a file where he kept notes about his schedule! Where can we find him at 5:30? | `jazzercize` |

### Task 13: Web Exploitation - Dirb y Scripts

**Explicacion:** Paginas que encuentra dirb con su wordlist default: 4. Scripts en /home/thegrinch/scripts: 4. Cinco caracteres tras $6$G en el hash de pepper: `ZUP42`. Flag.txt desktop de Grinch: `DI3H4rdIsTheBestX-masMovie!`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How many pages did the dirb scan find with its default wordlist? | `4` |
| 2 | How many scripts do you see in the /home/thegrinch/scripts folder? | `4` |
| 3 | What are the five characters following $6$G in pepper's password hash? | `ZUP42` |
| 4 | What is the content of the flag.txt file on the Grinch's user desktop? | `DI3H4rdIsTheBestX-masMovie!` |

### Task 14: OSINT - El Operador

**Explicacion:** Username operador: `GrinchWho31`; plataforma: Twitter; identificador criptografico: `1GW8QR7CWW3cpvVPGMCF5tZz4j96ncEgrVaR`; plataforma del identificador: keybase.io; bitcoin address: `bc1q5q2w2x6yka5gchr89988p2c8w8nquem6tndw2f`; plataforma donde lo leak: GitHub; email personal: `DonteHeath21@gmail.com`; nombre real: `Donte Heath`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the operator's username? | `GrinchWho31` |
| 2 | What social media platform is the username associated with? | `Twitter` |
| 3 | What is the cryptographic identifier associated with the operator? | `1GW8QR7CWW3cpvVPGMCF5tZz4j96ncEgrVaR` |
| 4 | What platform is the cryptographic identifier associated with? | `keybase.io` |
| 5 | What is the bitcoin address of the operator? | `bc1q5q2w2x6yka5gchr89988p2c8w8nquem6tndw2f` |
| 6 | What platform does the operator leak the bitcoin address on? | `GitHub` |
| 7 | What is the operator's personal email? | `DonteHeath21@gmail.com` |
| 8 | What is the operator's real name? | `Donte Heath` |

### Task 15: Cloud - AWS S3

**Explicacion:** S3 bucket del comunicado HR: `images.bestfestivalcompany.com`. Mensaje flag.txt del bucket: `It's easy to get your elves data when you leave it so easy to find!`. Otro archivo interesante: `wp-backup.zip`. AWS Access Key ID: `AKIAQI52OJVCPZXFYAOI`. AWS Account ID: `019181489476`. Username del access-key: `ElfMcHR@bfc.com`. EC2 instance TAG Name: `HR-Portal`. Database password en Secrets Manager: `Winter2021!`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the name of the S3 Bucket used to host the HR Website announcement? | `images.bestfestivalcompany.com` |
| 2 | What is the message left in the flag.txt object from that bucket? | `It's easy to get your elves data when you leave it so easy to find!` |
| 3 | What other file in that bucket looks interesting to you? | `wp-backup.zip` |
| 4 | What is the AWS Access Key ID in that file? | `AKIAQI52OJVCPZXFYAOI` |
| 5 | What is the AWS Account ID that access-key works for? | `019181489476` |
| 6 | What is the Username for that access-key? | `ElfMcHR@bfc.com` |
| 7 | There is an EC2 Instance in this account. Under the TAGs, what is the Name of the instance? | `HR-Portal` |
| 8 | What is the database password stored in Secrets Manager? | `Winter2021!` |

### Task 16: Container - Docker

**Explicacion:** Listar imagenes locales: `docker images`. Guardar imagen como tar: `docker save`. Archivo con config, tags y layer hashes: `manifest.json`. Token del bonus challenge: `7095b3e9300542edadbc2dd558ac11fa`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What command will list container images stored in your local container registry? | `docker images` |
| 2 | What command will allow you to save a docker image as a tar archive? | `docker save` |
| 3 | What is the name of the file (including file extension) for the configuration, repository tags, and layer hash values stored in a container image? | `manifest.json` |
| 4 | What is the token value you found for the bonus challenge? | `7095b3e9300542edadbc2dd558ac11fa` |

### Task 17: Phishing

**Explicacion:** Email enviado a: `elfmcphearson@tbfc.com`. De (dominio similar): `customerservice@t8fc.info`. Reply-to: `fisher@tempmailz.grinch`. Palabra mal escrita: `stright`. Link a credential harvesting: `https://89xgwsnmo5.grinch/out/fishing/`. Header inusual: `X-GrinchPhish: >;^)`. Attachment: `password-reset-instructions.pdf`. Flag del PDF: `THM{A0C_Thr33_Ph1sh1ng_An4lys!s}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Who was the email sent to? (Answer is the email address) | `elfmcphearson@tbfc.com` |
| 2 | Phishing emails use similar domains of their targets to increase the likelihood the recipient will be tricked into interacting with the email. Who does it say the email was from? (Answer is the email address) | `customerservice@t8fc.info` |
| 3 | Sometimes phishing emails have a different reply-to email address. If this email was replied to, what email address will receive the email response? | `fisher@tempmailz.grinch` |
| 4 | Less sophisticated phishing emails will have typos. What is the misspelled word? | `stright` |
| 5 | The email contains a link that will redirect the recipient to a fraudulent website in an effort to collect credentials. What is the link to the credential harvesting website? | `https://89xgwsnmo5.grinch/out/fishing/` |
| 6 | View the email source code. There is an unusual email header. What is the header and its value? | `X-GrinchPhish: >;^)` |
| 7 | You received other reports of phishing attempts from other colleagues. Some of the other emails contained attachments. Open attachment.txt. What is the name of the attachment? | `password-reset-instructions.pdf` |
| 8 | What is the flag in the PDF file? | `THM{A0C_Thr33_Ph1sh1ng_An4lys!s}` |

### Task 18: Malware Analysis - EICAR y YARA

**Explicacion:** `strings` de testfile: `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`. File type: `EICAR virus test files`. Primer visto en la web: `2005-10-17 22:03:48`. Clasificacion de Microsoft: `Virus:DOS/EICAR_Test_File`. Primeros dos nombres del file: `ducklin.htm or ducklin-html.htm`. Maximo caracteres: `128`. Operador booleano para que la regla siga hitting: `or`. Opcion para metadata: `-m`. Seccion con autor: `metadata`. Opcion para reglas sin hit: `-n`. Rerun con -c: `0`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Open the terminal and navigate to the file on the desktop named 'testfile'. Using the 'strings' command, check the strings in the file. There is only a single line of output to the 'strings' command. What is the output? | `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*` |
| 2 | Check the file type of 'testfile' using the 'file' command. What is the file type? | `EICAR virus test files` |
| 3 | Calculate the file's hash and search for it on VirusTotal. When was the file first seen in the wild? | `2005-10-17 22:03:48` |
| 4 | On VirusTotal's detection tab, what is the classification assigned to the file by Microsoft? | `Virus:DOS/EICAR_Test_File` |
| 5 | Go to this link to learn more about this file and what it is used for. What were the first two names of this file? | `ducklin.htm or ducklin-html.htm` |
| 6 | The file has 68 characters in the start known as the known string. It can be appended with whitespace characters upto a limited number of characters. What is the maximum number of total characters that can be in the file? | `128` |
| 7 | We changed the text in the string $a as shown in the eicaryara rule we wrote, from X5O to X50, that is, we replaced the letter O with the number 0. The condition for the Yara rule is $a and $b and $c and $d. If we are to only make a change to the first boolean operator in this condition, what boolean operator shall we replace the 'and' with, in order for the rule to still hit the file? | `or` |
| 8 | What option is used in the Yara command in order to list down the metadata of the rules that are a hit to a file? | `-m` |
| 9 | What section contains information about the author of the Yara rule? | `metadata` |
| 10 | What option is used to print only rules that did not hit? | `-n` |
| 11 | Change the Yara rule value for the $a string to X50. Rerun the command, but this time with the -c option. What is the result? | `0` |

### Task 19: Malware Analysis - Exfiltracion Email

**Explicacion:** Username del script decodificado: `Grinch.Enterprises.2021@gmail.com`; mailbox password: `S@ntai$comingt0t0wn`; subject: `Christmas Wishlist`; puerto de exfiltracion: `587`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the username (email address of Grinch Enterprises) from the decoded script? | `Grinch.Enterprises.2021@gmail.com` |
| 2 | What is the mailbox password you found? | `S@ntai$comingt0t0wn` |
| 3 | What is the subject of the email? | `Christmas Wishlist` |
| 4 | What port is the script using to exfiltrate data from the North Pole? | `587` |

### Task 20: Malware Analysis - OLE/VBA (oledump)

**Explicacion:** Flag en documento de Grinch (usando `oledump.py -s {stream number} -d`): `YouFoundGrinchCookie`. Segunda flag en la maquina: `S@nt@c1Au$IsrEAl`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the flag hidden found in the document that Grinch Enterprises left behind? (Hint: use the following command oledump.py -s {stream number} -d, the answer will be in the caption). | `YouFoundGrinchCookie` |
| 2 | There is still a second flag somewhere... can you find it on the machine? | `S@nt@c1Au$IsrEAl` |

### Task 21: DFIR - PowerShell Logs

**Explicacion:** Comando ejecutado como Elf McNealy para agregar user: `Invoke-Nightmare`. Usuario que ejecuto el PS para enviar password.txt: `adm1n`. IP y puerto remoto: `10.10.148.96,4321`. Encryption key: `j3pn50vkw21hhurbqmxjlpmo9doiukyb`. App de borrado: `sdelete.exe`. Fecha/timestamp de borrado: `11/11/2021 7:29:27 PM`. Contenido de password.txt: `Mission Control: letitsnowletitsnowletitsnow`. Otro user: `emily`; NTLM hash: `8af326aa4850225b75c592d4ce19ccf5`; password: `1234567890`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What command was executed as Elf McNealy to add a new user to the machine? | `Invoke-Nightmare` |
| 2 | What user executed the PowerShell file to send the password.txt file from the administrator's desktop to a remote server? | `adm1n` |
| 3 | What was the IP address of the remote server? What was the port used for the remote connection? (format: IP,Port) | `10.10.148.96,4321` |
| 4 | What was the encryption key used to encrypt the contents of the text file sent to the remote server? | `j3pn50vkw21hhurbqmxjlpmo9doiukyb` |
| 5 | What application was used to delete the password.txt file? | `sdelete.exe` |
| 6 | What is the date and timestamp the logs show that password.txt was deleted? (format: MM/DD/YYYY H:MM:SS PM) | `11/11/2021 7:29:27 PM` |
| 7 | What were the contents of the deleted password.txt file? | `Mission Control: letitsnowletitsnowletitsnow` |
| 8 | What is the username of the other user on the system? | `emily` |
| 9 | What is the NTLM hash of this user? | `8af326aa4850225b75c592d4ce19ccf5` |
| 10 | What is the password for this user? | `1234567890` |

### Task 22: Encuesta Final

**Explicacion:** Encuesta 5 min: https://forms.gle/ET6KY5dwcBumsqNv8. Flag de agradecimiento `thm{thank_you_2021}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Please help us improve by answering this 5 minute survey! | `thm{thank_you_2021}` |

---

**Metodologia:**

1. IDOR enumeration de IDs de usuario

2. Cookie manipulation (hex/JSON) y bypass de admin login

3. LFI con PHP filters y log poisoning para RCE

4. NoSQL injection (MongoDB) y bypass de login

5. DFIR completo del malware SantaRat (LOLbins, GitHub, transcripciones, uharc)

6. Analisis de pcap (HTTP, DNS, FTP)

7. Nmap, CVE-2021-42013, MSSQL, NFS, escalada Windows

8. OSINT del operador (Twitter, keybase.io, GitHub, bitcoin)

9. Cloud AWS (S3 buckets, EC2, Secrets Manager)

10. Docker container analysis

11. Phishing analysis, EICAR/YARA rules, oledump/VBA, PowerShell logs

**Learning chain:** IDOR -> Cookies -> LFI -> RCE -> NoSQL -> DFIR SantaRat -> Network (HTTP/DNS/FTP) -> Nmap -> MSSQL -> NFS -> Windows Escalation -> OSINT -> AWS -> Docker -> Phishing -> Malware/YARA -> oledump -> PowerShell logs

**Leccion:** *El AoC 2021 levanto el nivel con DFIR profundo y cadenas de ataque multicapa, demostrando que un mismo reto puede combinar analisis defensivo (logs, malware) con ofensivo (LFI a RCE, NoSQLi, credenciales en la nube).*

**MITRE ATT&CK:**

- T1190 - Exploit Public-Facing Application

- T1059 - Command and Scripting Interpreter

- T1005 - Data from Local System

- T1048 - Exfiltration Over Alternative Protocol

- T1552 - Unsecured Credentials

- T1204 - User Execution

- T1105 - Ingress Tool Transfer

- T1548 - Abuse Elevation Control Mechanism

**Fuente:** [TryHackMe - Advent of Cyber 3 (2021)](https://tryhackme.com/room/adventofcyber3)