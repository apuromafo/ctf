# Advent of Cyber 2 [2020]

| **Dificultad** | N/A | **Tipo** | CTF (Free Room) | **Slug** | `adventofcyber2` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber2) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2020 | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | cookies / wfuzz / gobuster / xss / zap / wireshark / sniffing / smbclient / enum4linux / escalation / telnet / dirtycow / osint / python / sql / rev / ransomware / lxd | | **Impacto** | Segundo Advent of Cyber con 24 dias cubriendo desde cookies hex/JSON y fuzzing hasta escalada de privilegios, OSINT, reversing, ransomware y lxd |

---

**Contexto:** Segundo Advent of Cyber (2020). Amplia cobertura: cookies de autenticacion (hex/JSON), wfuzz/gobuster fuzzing, XSS (reflected/stored), ZAP scanning, Wireshark/sniffing, SMB/enum4linux, escalation (vertical/sudoers, dirtycow), telnet legacy, OSINT de Rudolph, Python basics, SQL, reversing, ransomware analysis (scheduled tasks/VSS), y escalada con lxd. Room 24 dias.

Notas del entorno (metodologia personal): `- linux server (from ping TTL); - password length > 5, - running php. I found out by request for index.php -> return 200. index.html -> return 440`. Se creo una cuenta `kurohat:12345`. En el dev tool -> cookie:

```
auth:7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a226b75726f686174227d
```

Se supone que es hex/base64 encoded string; se uso CyberChef para entender (resultado: hex que convertido a utf-8 da):

```
{"company":"The Best Festival Company", "username":"kurohat"}
```

El plan es cambiar username a santa: `{"company":"The Best Festival Company", "username":"santa"}` -> hex (CyberChef):

```
7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d
```

Se remueve el cookie value y se remplaza con el de Santa -> F5 (refresh) -> BOOM! somos Santa. Activar cada control para obtener flags. Notas: `SatNav = Satellite navigation`, `never use poor cookie!!!`.

---

## Solucionario

### Dia 1: Cookies y Control de la Navidad

**Explicacion:** Cookie decode: nombre de cookie `auth`, formato hex, dato en JSON. Santa cookie value dada. Al activar cada control se obtiene la flag. Notas: linux server (por ping TTL), password length > 5, running php (index.php -> 200, index.html -> 440). Se creo una cuenta `kurohat:12345`. El valor del cookie de kurohat es `auth:7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a226b75726f686174227d`. Decodificado (hex->utf-8): `{"company":"The Best Festival Company", "username":"kurohat"}`. Se cambia username a santa: `{"company":"The Best Festival Company", "username":"santa"}` -> hex `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d`. Reemplazar cookie y F5 -> acceso como Santa. Activar cada control para flags.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the name of the cookie used for authentication? | `auth` |
| 2 | In what format is the value of this cookie encoded? | `Hexadecimal` |
| 3 | Having decoded the cookie, what format is the data stored in? | `JSON` |
| 4 | What is the value of Santa's cookie? | `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d` |
| 5 | What is the flag you're given when the line is fully active? | `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}` |

### Dia 2: File Upload

**Explicacion:** Parametro para acceder a la page de upload `?id=ODIzODI5MTNiYmYw`; tipo de archivo aceptado Image; directorio `/uploads/`; flag en /var/www/flag.txt `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What string of text needs adding to the URL to get access to the upload page? | `?id=ODIzODI5MTNiYmYw` |
| 2 | What type of file is accepted by the site? | `Image` |
| 3 | In which directory are the uploaded files stored? | `/uploads/` |
| 4 | What is the flag in /var/www/flag.txt? | `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}` |

### Dia 3: Scripting y Fuzzing (wfuzz)

**Explicacion:** Flag general `THM{885ffab980e049847516f9d8fe99ad1a}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the flag? | `THM{885ffab980e049847516f9d8fe99ad1a}` |

### Dia 4: APIs / wfuzz

**Explicacion:** Usando wfuzz para el parametro "breed" de `http://shibes.xyz/api.php` con la wordlist "big.txt": `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`. GoBuster contra la maquina desplegada (no shibes.xyz) encuentra `site-log.php`. Fuzz del parametro date en ese archivo -> flag `THM{D4t3_AP1}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory) | `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ` |
| 2 | Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there? | `site-log.php` |
| 3 | Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post? | `THM{D4t3_AP1}` |

### Dia 5: Web Hacking (Brute Force)

**Explicacion:** Santa's secret login panel sin directory brute forcing: `/santapanel`. Entries en la gift database: 22. Paul pidio Github Ownership. Flag `thmfox{All_I_Want_for_Christmas_Is_You}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Without using directory brute forcing, what's Santa's secret login panel? | `/santapanel` |
| 2 | How many entries are there in the gift database? | `22` |
| 3 | What did Paul ask for? | `Github Ownership` |
| 4 | What is the flag? | `thmfox{All_I_Want_for_Christmas_Is_You}` |

### Dia 6: XSS

**Explicacion:** Password de admin `EhCNSWzzFP6sc7gB`; tipo de vuln usada Stored cross-site scripting; query string abusable para reflected XSS `q`; ZAP scan: 2 XSS alerts.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is admin's password? | `EhCNSWzzFP6sc7gB` |
| 2 | What vulnerability type was used to exploit the application? | `Stored cross-site scripting` |
| 3 | What query string can be abused to craft a reflected XSS? | `q` |
| 4 | Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan? | `2` |

### Dia 7: Sniffing (Wireshark)

**Explicacion:** Pcap1: IP que inicia ICMP/ping `10.11.3.2`; filtro HTTP GET `http.request.method == GET`; articulo que visito 10.10.67.199 `reindeer-of-the-week`. Pcap2: FTP leaked password `plaintext_password_fiasco`; protocolo encriptado SSH.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping? | `10.11.3.2` |
| 2 | If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use? | `http.request.method == GET` |
| 3 | Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited? | `reindeer-of-the-week` |
| 4 | Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process? | `plaintext_password_fiasco` |
| 5 | Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted? | `SSH` |

### Dia 8: Fuzzing / Yara

**Explicacion:** Whislist de Elf McSkidy que reemplazara a Elf McEager: Rubber ducky. Snort fue creado en 1998.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is on Elf McSkidy's wishlist that will be used to replace Elf McEager? | `Rubber ducky` |
| 2 | When was Snort created? | `1998` |

### Dia 9: Nmap / FTP

**Explicacion:** Nmap en MACHINE_IP: puertos 80,2222,3389 (ascending). Distro Linux: Ubuntu. NSE HTTP-TITLE: Blog. FTP anonymous: directorio `public`; script `backup.sh`; peli Polar Express; re-upload script malicioso -> root flag `THM{even_you_can_be_santa}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Using Nmap on MACHINE_IP , what are the port numbers of the three services running? (Please provide your answer in ascending order/lowest -> highest, separated by a comma) | `80,2222,3389` |
| 2 | Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running? | `Ubuntu` |
| 3 | Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for? | `Blog` |
| 4 | Question 1: Name the directory on the FTP server that has data accessible by the "anonymous" user | `public` |
| 5 | Question 2: What script gets executed within this directory? | `backup.sh` |
| 6 | Question 3: What movie did Santa have on his Christmas shopping list? | `The Polar Express` |
| 7 | Question 4: Re-upload this script to contain malicious data (just like we did in section 9.6). Output the contents of /root/flag.txt! | `THM{even_you_can_be_santa}` |

### Dia 10: Samba / SMB

**Explicacion:** enum4linux: 3 users en Samba; 4 shares; share sin password `tbfc-santa`; directorio que dejo ElfMcSkidy `jingle-tunes`. Tipo de escalada con user account como admin: Vertical. Archivo con usuarios sudo: sudoers. Contenido /root/flag.txt: `thm{2fb10afe933296592}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Question 1 Using enum4linux, how many users are there on the Samba server (MACHINE_IP)? | `3` |
| 2 | Question 2 Now how many "shares" are there on the Samba server? | `4` |
| 3 | Question 3 Use smbclient to try to login to the shares on the Samba server (MACHINE_IP). What share doesn't require a password? | `tbfc-santa` |
| 4 | Question 4 Log in to this share, what directory did ElfMcSkidy leave for Santa? | `jingle-tunes` |
| 5 | What type of privilege escalation involves using a user account to execute commands as an administrator? | `Vertical` |
| 6 | What is the name of the file that contains a list of users who are a part of the sudo group? | `sudoers` |
| 7 | What are the contents of the file located at /root/flag.txt? | `thm{2fb10afe933296592}` |

### Dia 11: Metasploit / Escalada

**Explicacion:** Version web server `9.0.17`; CVE Meterpreter `CVE-2019-0232`; flag1 `thm{whacking_all_the_elves}`. Protocolo legacy telnet; credencial `clauschristmas`; distro Ubuntu 12.04; "quien llego primero": grinch; dirtycow: `gcc -pthread dirty.c -o dirty -lcrypt`; nuevo user `firefart`; MD5 output `8b16f00dd3b51efadb02c1df7f8427cc`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the version number of the web server? | `9.0.17` |
| 2 | What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX) | `CVE-2019-0232` |
| 3 | What are the contents of flag1.txt | `thm{whacking_all_the_elves}` |
| 4 | What old, deprecated protocol and service is running? | `telnet` |
| 5 | What credential was left for you? | `clauschristmas` |
| 6 | What distribution of Linux and version number is this server running? | `Ubuntu 12.04` |
| 7 | Who got here first? | `grinch` |
| 8 | What is the verbatim syntax you can use to compile, taken from the real C source code comments? | `gcc -pthread dirty.c -o dirty -lcrypt` |
| 9 | What "new" username was created, with the default operations of the real C source code? | `firefart` |
| 10 | What is the MD5 hash output? | `8b16f00dd3b51efadb02c1df7f8427cc` |

### Dia 12: OSINT

**Explicacion:** OSINT de Rudolph. URL comentarios Reddit: `https://www.reddit.com/user/IGuidetheClaus2020/comments`; nacio en Chicago; Robert -> last name May; otra plataforma Twitter; username `IGuideClaus2020`; show favorito Bachelorette; parade en Chicago; foto en 41.891815, -87.624277; flag `{FLAG}ALWAYSCHECKTHEEXIFD4T4`; password pwned `spygame`; street numbers del hotel 540.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What URL will take me directly to Rudolph's Reddit comment history? | `https://www.reddit.com/user/IGuidetheClaus2020/comments` |
| 2 | According to Rudolph, where was he born? | `Chicago` |
| 3 | Rudolph mentions Robert. Can you use Google to tell me Robert's last name? | `May` |
| 4 | On what other social media platform might Rudolph have an account? | `Twitter` |
| 5 | What is Rudolph's username on that platform? | `IGuideClaus2020` |
| 6 | What appears to be Rudolph's favorite TV show right now? | `Bachelorette` |
| 7 | Based on Rudolph's post history, he took part in a parade. Where did the parade take place? | `Chicago` |
| 8 | Okay, you found the city, but where specifically was one of the photos taken? | `41.891815, -87.624277` |
| 9 | Did you find a flag too? | `{FLAG}ALWAYSCHECKTHEEXIFD4T4` |
| 10 | Has Rudolph been pwned? What password of his appeared in a breach? | `spygame` |
| 11 | Based on all the information gathered. It's likely that Rudolph is in the Windy City and is staying in a hotel on Magnificent Mile. What are the street numbers of the hotel address? | `540` |

### Dia 13: Python Basics

**Explicacion:** `True + True` = 2; db para instalar librerias de otros = PyPi; `bool("False")` = True; libreria para descargar HTML de una web = Requests; output del codigo Question 5 = [1, 2, 3, 6]; la causa = Pass by reference.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What's the output of True + True? | `2` |
| 2 | What's the database for installing other peoples libraries called? | `PyPi` |
| 3 | What is the output of bool("False")? | `True` |
| 4 | What library lets us download the HTML of a webpage? | `Requests` |
| 5 | What is the output of the program provided in "Code to analyse for Question 5" in today's material? | `[1, 2, 3, 6]` |
| 6 | What causes the previous task to output that? | `Pass by reference` |

### Dia 14: Web APIs y Keys

**Explicacion:** Puerto web server 80; directorio API sin tools `/api/`; Santa now Winter Wonderland, Hyde Park, London; API key correcta (odd 0-100) `57`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the port number for the web server? | `80` |
| 2 | Without using enumerations tools such as Dirbuster, what is the directory for the API? (without the API key) | `/api/` |
| 3 | Where is Santa right now? | `Winter Wonderland, Hyde Park, London` |
| 4 | Find out the correct API key. Remember, this is an odd number between 0-100. After too many attempts, Santa's Sled will block you. | `57` |

### Dia 15: Reversing (Ghidra)

**Explicacion:** Reversing de binario: local_ch = 1; eax imull = 6; local_4h antes de eax=0 = 6.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the value of local_ch when its corresponding movl instruction is called (first if multiple)? | `1` |
| 2 | What is the value of eax when the imull instruction is called? | `6` |
| 3 | What is the value of local_4h before eax is set to 0? | `6` |

### Dia 16: SQL Injection 2

**Explicacion:** Password de Santa `santapassword321`; flag al loguear `thm{046af}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is Santa's password? | `santapassword321` |
| 2 | Now that you've retrieved this password, try to login...What is the flag? | `thm{046af}` |

### Dia 17: Passwords

**Explicacion:** Password de Santa `Be good for goodness sake!`; challenge flag `THM{EVERYONE_GETS_PRESENTS}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is Santa's password? | `Be good for goodness sake!` |
| 2 | What is the challenge flag? | `THM{EVERYONE_GETS_PRESENTS}` |

### Dia 18: Forensics de Sistema

**Explicacion:** Elf 1 quiere 2 front teeth (archivo oculto en Documents). Elf 2: pelicula Scrooged (folder oculto desktop). Elf 3: folder oculto 3lfthr3e; primer file tiene 9999 words; palabras en index 551 y 6991: Red Ryder; Elf 3 quiere Red Ryder BB Gun.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want? | `2 front teeth` |
| 2 | Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants? | `Scrooged` |
| 3 | Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while) | `3lfthr3e` |
| 4 | How many words does the first file contain? | `9999` |
| 5 | What 2 words are at index 551 and 6991 in the first file? | `Red Ryder` |
| 6 | This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer) | `Red Ryder BB Gun` |

### Dia 19: Hash / Malware Analysis

**Explicacion:** Hash de db.exe `596690FFC54AB6101932856E6A78E3A1`; hash del misterioso executable `5F037501FB542AD2D9B06EB12AED09F0`; flag oculta con Strings `THM{f6187e6cbeb1214139ef313e108cb6f9}`; flag del connector `THM{3088731ddc7b9fdeccaed982b07c297c}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Read the contents of the text file within the Documents folder. What is the file hash for db.exe? | `596690FFC54AB6101932856E6A78E3A1` |
| 2 | What is the file hash of the mysterious executable within the Documents folder? | `5F037501FB542AD2D9B06EB12AED09F0` |
| 3 | Using Strings find the hidden flag within the executable? | `THM{f6187e6cbeb1214139ef313e108cb6f9}` |
| 4 | What is the flag that is displayed when you run the database connector file? | `THM{3088731ddc7b9fdeccaed982b07c297c}` |

### Dia 20: KeePass / CyberChef

**Explicacion:** Password KeePass `thegrinchwashere`; encoding Base64; decoded Elf Server `sn0wM4n!`; decoded ElfMail `ic3Skating!`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the password to the KeePass database? | `thegrinchwashere` |
| 2 | What is the encoding method listed as the 'Matching ops'? | `Base64` |
| 3 | What is the decoded password value of the Elf Server? | `sn0wM4n!` |
| 4 | What is the decoded password value for ElfMail? | `ic3Skating!` |

### Dia 21: Ransomware

**Explicacion:** Ransomware: decrypted bitcoin plain text `nomorebestfestivalcompany`; file extension `.grinch`; scheduled task `opidsfsdf`; exe en `C:\users\administrator\desktop\opidsfsdf.exe`; VSS task ShadowCopyVolumeID `7a9eea15-0000-0000-0000-010000000000`; hidden folder Confidential; restored password `m33pa55w0rdIZseecure!`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value? | `nomorebestfestivalcompany` |
| 2 | At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files? | `.grinch` |
| 3 | What is the name of the suspicious scheduled task? | `opidsfsdf` |
| 4 | Inspect the properties of the scheduled task. What is the location of the executable that is run at login? | `C:\users\administrator\desktop\opidsfsdf.exe` |
| 5 | There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID? | `7a9eea15-0000-0000-0000-010000000000` |
| 6 | Assign the hidden partition a letter. What is the name of the hidden folder? | `Confidential` |
| 7 | Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file? | `m33pa55w0rdIZseecure!` |

### Dia 22: Web Exploitation (TRON)

**Explicacion:** Scan machine: puertos 80, 65000; hidden website title Light Cycle; hidden php `uploads.php`; hidden dir `grid`; web.txt flag `THM{ENTER_THE_GRID}`; credenciales `tron:IFightForTheUsers`; database name tron; cracked password `@computer@`; user.txt `THM{IDENTITY_DISC_RECOGNISED}`; grupo lxd; root.txt `THM{FLYNN_LIVES}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Scan the machine. What ports are open? | `80, 65000` |
| 2 | What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step. | `Light Cycle` |
| 3 | What is the name of the hidden php page? | `uploads.php` |
| 4 | What is the name of the hidden directory where file uploads are saved? | `grid` |
| 5 | What is the value of the web.txt flag? | `THM{ENTER_THE_GRID}` |
| 6 | Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password | `tron:IFightForTheUsers` |
| 7 | Access the database and discover the encrypted credentials. What is the name of the database you find these in? | `tron` |
| 8 | Crack the password. What is it? | `@computer@` |
| 9 | What is the value of the user.txt flag? | `THM{IDENTITY_DISC_RECOGNISED}` |
| 10 | Check the user's groups. Which group can be leveraged to escalate privileges? | `lxd` |
| 11 | What is the value of the root.txt flag? | `THM{FLYNN_LIVES}` |

### Dia 23: Encuesta Final

**Explicacion:** Encuesta 5 min: https://forms.gle/iixyNWzyZupumsPN7. Flag de agradecimiento `thm{thank_you_2020}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Please help us improve by answer this 5 minute survey! | `thm{thank_you_2020}` |

---

**Metodologia:**

1. Recon basico (TTL, servicios, PHP)

2. Cookie manipulation (hex/JSON) con CyberChef

3. wfuzz + gobuster fuzzing de APIs y parametros

4. XSS (stored/reflected) y ZAP scanning

5. Wireshark/sniffing de pcap (HTTP, FTP, ICMP)

6. enum4linux + smbclient (SMB/shares)

7. Escalada vertical, sudoers, dirtycow (telnet legacy)

8. Metasploit (CVE-2019-0232) y Meterpreter

9. OSINT de Rudolph (Reddit, Twitter, EXIF, haveibeenpwned)

10. Python basics y reversing (Ghidra)

11. SQLi, ransomware analysis (scheduled tasks, VSS), KeePass/CyberChef

12. Escalada con lxd

**Learning chain:** Recon -> Cookies -> Fuzzing -> XSS -> Sniffing -> SMB -> Escalada -> Metasploit -> OSINT -> Python -> Reversing -> SQLi -> Ransomware -> lxd

**Leccion:** *El AoC 2020 profundizo en los conceptos web y de red del anio anterior, agregando OSINT, reversing y analisis de ransomware, pero manteniendo el espiritu de aprender haciendo.*

**MITRE ATT&CK:**

- T1110 - Brute Force

- T1190 - Exploit Public-Facing Application

- T1059 - Command and Scripting Interpreter

- T1068 - Exploitation for Privilege Escalation

- T1203 - Exploitation for Client Execution

- T1040 - Network Sniffing

- T1555 - Credentials from Password Stores

- T1486 - Data Encrypted for Impact

**Fuente:** [TryHackMe - Advent of Cyber 2 [2020]](https://tryhackme.com/room/adventofcyber2)