# Advent of Cyber 1 [2019]

| **Dificultad** | N/A | **Tipo** | CTF (Free Room) | **Slug** | `25daysofchristmas` | | **Link** | [TryHackMe](https://tryhackme.com/room/25daysofchristmas) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2019 | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | web recon / cookie manipulation / nmap / suid / metasploit / osint / reversing / sql injection / pwn | | **Impacto** | Primer Advent of Cyber, 25 dias de retos que cubren desde cookies de autenticacion y web recon hasta escalada de privilegios, reversing y SQLi |

---

**Contexto:** Primer Advent of Cyber de TryHackMe (2019), con 25 dias de retos de dificultad creciente. Cubre: manipulacion de cookies de autenticacion, fuzzing de paginas ocultas, cracking de passwords, nmap, SUID privilege escalation, Metasploit, OSINT, reversing (Ghidra/radare), SQL injection, y varios CTF de maquinas. Los 25 dias abarcan toda la cadena: recon, explotacion web, escalada de privilegios y forensics.

---

## Solucionario

### Dia 1: Web Recon y Cookies de Autenticacion

**Explicacion:** Analisis web inicial: identificar la cookie usada para autenticacion y decodificarla. La cookie es `authid` y tiene una parte fija `v4er9ll1ss`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the name of the cookie used for authentication? | `authid` |
| 2 | If you decode the cookie, what is the value of the fixed part of the cookie? | `v4er9ll1ss` |

### Dia 2: Fuzzing Web y Enumeracion

**Explicacion:** Tras acceder a la cuenta del usuario `mcinventory`, se identifica una request y se descubre una pagina oculta `/sysadmin` con password `defaultpass`. Ademas hay que llevar Eggnog al 'partay'.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | After accessing his account, what did the user mcinventory request? | `firewall` |
| 2 | What is the path of the hidden page? | `/sysadmin` |
| 3 | What is the password you found? | `defaultpass` |
| 4 | What do you have to take to the 'partay'? | `Eggnog` |

### Dia 3: Analisis de Paquetes (Wireshark)

**Explicacion:** Analisis de pcap en Wireshark. Se identifica la destination IP en el paquete 998 y el item en la Christmas list.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Whats the destination IP on packet number 998? | `63.32.89.195` |
| 2 | What item is on the Christmas list? | `ps4` |

### Dia 4: Cracking de Passwords

**Explicacion:** Cracking de la password del usuario buddy con un hash tool. La password es `rainbow`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Crack buddy's password! | `rainbow` |

### Dia 5: Linux Basics - Archivos y Permisos

**Explicacion:** Enumeracion de archivos en el home directory. Hay 8 archivos visibles; file5 contiene `recipes`, file6 contiene la string 'password', un archivo tiene la IP `10.0.0.05`, y hay 3 usuarios que pueden loguear. El sha1 de file8 es `fa67ee594358d83becdd2cb6c466b25320fd2835`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How many visible files are there in the home directory(excluding ./ and ../)? | `8` |
| 2 | What is the content of file5? | `recipes` |
| 3 | Which file contains the string 'password'? | `file6` |
| 4 | What is the IP address in a file in the home folder? | `10.0.0.05` |
| 5 | How many users can log into the machine? | `3` |
| 6 | What is the sha1 hash of file8? | `fa67ee594358d83becdd2cb6c466b25320fd2835` |

### Dia 6: Linux - Password Hash Extraction

**Explicacion:** Extraccion del hash de mcsysadmin: `$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/` (hash sha512crypt).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is mcsysadmin's password hash? | `$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/` |

### Dia 7: OSINT - Instagram

**Explicacion:** OSINT sobre Lola en Instagram: su cumpleanos es December 29, 1900; ocupacion Santa's Helper; hace iPhone X; empezo fotografia 23/10/2014; tiene a ada lovelace en su web page.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019) | `December 29, 1900` |
| 2 | What is Lola's current occupation? | `Santa's Helper` |
| 3 | What phone does Lola make? | `iPhone X` |
| 4 | What date did Lola first start her photography? Format: dd/mm/yyyy | `23/10/2014` |
| 5 | What famous woman does Lola have on her web page? | `ada lovelace` |

### Dia 8: Analisis de Trafico DNS

**Explicacion:** Analisis de captura DNS: datos exfiltrados via DNS `Candy Cane Serial Number 8491`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What data was exfiltrated via DNS? | `Candy Cane Serial Number 8491` |

### Dia 9: OSINT - Twitter

**Explicacion:** OSINT en Twitter: Little Timmy queria ser PenTester.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What did Little Timmy want to be for Christmas? | `PenTester` |

### Dia 10: Steganografia

**Explicacion:** Steganografia: lo oculto dentro del archivo es `RFC527`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What was hidden within the file? | `RFC527` |

### Dia 11: Escaneo de Puertos

**Explicacion:** Nmap: 3 TCP ports bajo 1000 abiertos; OS Linux; SSH version 7.4; file accesible en el server `interesting.file`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How many TCP ports under 1000 are open? | `3` |
| 2 | What is the name of the OS of the host? | `Linux` |
| 3 | What version of SSH is running? | `7.4` |
| 4 | What is the name of the file that is accessible on the server you found running? | `interesting.file` |
| 5 | What port is SSH running on? | `65534` |

### Dia 12: Escalada de Privilegios - SUID

**Explicacion:** Encontrar y ejecutar un archivo como igor (flag1) y luego explotar un SUID para ser root (flag2).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Find and run a file as igor. Read the file /home/igor/flag1.txt | `THM{d3f0708bdd9accda7f937d013eaf2cd8}` |
| 2 | Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file? | `THM{8c8211826239d849fa8d6df03749c3a2}` |

### Dia 13: Analisis de Malware - Binarios

**Explicacion:** Analisis de binario: valor de la flag `sCrIPtKiDd`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the value of the flag? | `sCrIPtKiDd` |

### Dia 14: Metasploit

**Explicacion:** Compromiso del web server usando Metasploit (flag1) y luego acceso al sistema principal con la password SSH de Santa `rudolphrednosedreindeer`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Compromise the web server using Metasploit. What is flag1? | `THM{3ad96bb13ec963a5ca4cb99302b37e12}` |
| 2 | Now you've compromised the web server, get onto the main system. What is Santa's SSH password? | `rudolphrednosedreindeer` |

### Dia 15: Scripting Python

**Explicacion:** Scripting: linea 148 de la naughty list es Melisa Vanhoose; linea 52 de la nice list es Lindsey Gaffney.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Who is on line 148 of the naughty list? | `Melisa Vanhoose` |
| 2 | Who is on line 52 of the nice list? | `Lindsey Gaffney` |

### Dia 16: SQL Injection

**Explicacion:** SQLi en el login y enumeracion de base de datos: password en creds.txt `securepassword123`; file en puerto 21 `file.txt`; password tras enumerar la db `bestpassword`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the password inside the creds.txt file? | `securepassword123` |
| 2 | What is the name of the file running on port 21? | `file.txt` |
| 3 | What is the password after enumerating the database? | `bestpassword` |

### Dia 17: Reversing (Linux)

**Explicacion:** Reversing de binarios: md5 de note1 `24cf615e2a4f42718f2ff36b35614f8f`; elf Bob se reunio con Alice en Santa's Grotto; decrypt de note2 flag `THM{ed9ccb6802c5d0f905ea747a310bba23}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the md5 hashsum of the encrypted note1 file? | `24cf615e2a4f42718f2ff36b35614f8f` |
| 2 | Where was elf Bob told to meet Alice? | `Santa's Grotto` |
| 3 | Decrypt note2 and obtain the flag! | `THM{ed9ccb6802c5d0f905ea747a310bba23}` |

### Dia 18: Web Exploitation - Hidden Directory

**Explicacion:** Hidden directory `/retro`; acceso inicial y lectura de user.txt y root.txt (optional). Flags: user `THM{HACK_PLAYER_ONE}`, root `THM{COIN_OPERATED_EXPLOITATION}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | A web server is running on the target. What is the hidden directory which the website lives on? | `/retro` |
| 2 | Gain initial access and read the contents of user.txt | `THM{HACK_PLAYER_ONE}` |
| 3 | [Optional] Elevate privileges and read the content of root.txt | `THM{COIN_OPERATED_EXPLOITATION}` |

### Dia 19: Enum4linux / Samba (ZIP)

**Explicacion:** Enumeracion de shares/Samba. Se extraen 50 archivos; 3 contienen Version: 1.1 en metadata; la flag dL6w.txt es la file con password. Archivo `employee_names.txt` y contenido `mcchef`; Charlie reserva Hawaii; pass `password1`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the name of the file you found? | `employee_names.txt` |
| 2 | What is in the file? | `mcchef` |
| 3 | What is Charlie going to book a holiday to? | `Hawaii` |
| 4 | Read /etc/shadow and crack Charlies password. | `password1` |
| 5 | What is flag1.txt? | `THM{4ea2adf842713ad3ce0c1f05ef12256d}` |
| 6 | How many files did you extract(excluding all the .zip files) | `50` |
| 7 | How many files contain Version: 1.1 in their metadata? | `3` |
| 8 | Which file contains the password? | `dL6w.txt` |

### Dia 20: Hydra - Brute Force

**Explicacion:** Hydra bruteforce de molly web password (flag1) y SSH password (flag2). Flags: `THM{2673a7dd116de68e85c48ec0b1f2612e}` y `THM{c8eeb0468febbadea859baeb33b2541b}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH) | `THM{2673a7dd116de68e85c48ec0b1f2612e}` |
| 2 | Use Hydra to bruteforce molly's SSH password. What is flag 2? | `THM{c8eeb0468febbadea859baeb33b2541b}` |

### Dia 21: Cookies y SQLi

**Explicacion:** Admin authid cookie `2564799a4e6689972f6d9e1c7b406f87065cbf65`; user.txt `5W7WkjxBWwhe3RNsWJ3Q`; SSH en 4567; sam flag1 `THM{dec4389bc09669650f3479334532aeab}`; cronjob flag2 `THM{b27d33705f97ba2e1f444ec2da5f5f61}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the admin's authid cookie value? | `2564799a4e6689972f6d9e1c7b406f87065cbf65` |
| 2 | What are the contents of the user.txt file? | `5W7WkjxBWwhe3RNsWJ3Q` |
| 3 | What port is SSH running on? | `4567` |
| 4 | Crack sam's password and read flag1.txt | `THM{dec4389bc09669650f3479334532aeab}` |
| 5 | Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2? | `THM{b27d33705f97ba2e1f444ec2da5f5f61}` |

### Dia 22: Reversing (Ghidra)

**Explicacion:** Reversing de un binario con Ghidra: valores de registros y variables en instrucciones movl/imull.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the value of local_ch when its corresponding movl instruction is called(first if multiple)? | `1` |
| 2 | What is the value of eax when the imull instruction is called? | `6` |
| 3 | What is the value of local_4h before eax is set to 0? | `6` |
| 4 | what is the value of local_8h before the end of the main function? | `9` |
| 5 | What is the value of local_4h before the end of the main function? | `2` |

### Dia 23: SQL Injection

**Explicacion:** SQLi en el parámetro `log_email`; email de Santa `bigman@shefesh.com`; password `saltnpepper`; estacion Waterloo; flag de LapLANd shell `THM{SHELLS_IN_MY_EGGNOG}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Which field is SQL injectable? Use the input name used in the HTML code. | `log_email` |
| 2 | What is Santa Claus' email address? | `bigman@shefesh.com` |
| 3 | What is Santa Claus' plaintext password? | `saltnpepper` |
| 4 | Santa has a secret! Which station is he meeting Mrs Mistletoe in? | `Waterloo` |
| 5 | Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/ | `THM{SHELLS_IN_MY_EGGNOG}` |

### Dia 24: Base de Datos / ELK

**Explicacion:** Password en la db `9Qs58Ol3AXkMWLxiEyUyyf`; contenido de /root.txt `someELKfun`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Find the password in the database | `9Qs58Ol3AXkMWLxiEyUyyf` |
| 2 | Read the contents of the /root.txt file | `someELKfun` |

---

**Metodologia:**

1. Web recon: cookies y fuzzing de rutas

2. Wireshark/pcap analysis

3. Password cracking (hashcat/john)

4. Linux basics y enumeracion de archivos

5. OSINT (Instagram y Twitter)

6. Steganografia

7. Escaneo NMAP y service enumeration

8. SUID privilege escalation

9. Metasploit exploitation

10. Scripting python

11. SQL injection

12. Reversing (Ghidra/radare)

13. Hydra brute force (web y SSH)

14. Cronjob escalation

15. Windows exploitation y ELK

**Learning chain:** Web Recon -> Cookies -> Fuzzing -> Wireshark -> Cracking -> Linux -> OSINT -> Stego -> Nmap -> SUID -> Metasploit -> Python -> SQLi -> Reversing -> Hydra -> Cron -> Windows/ELK

**Leccion:** *El Advent of Cyber 2019 establecio la base de todo el ecosistema AoC: mezcla equilibrada de fundamentos (recon, cracking, nmap, scripting) con explotacion real (Metasploit, SUID, SQLi, reversing) distribuida en 25 dias progresivos.*

**MITRE ATT&CK:**

- T1046 - Network Service Discovery

- T1110 - Brute Force

- T1548 - Abuse Elevation Control Mechanism

- T1190 - Exploit Public-Facing Application

- T1059 - Command and Scripting Interpreter

- T1557 - Adversary-in-the-Middle

- T1027 - Obfuscated Files or Information

**Fuente:** [TryHackMe - Advent of Cyber 1 [2019]](https://tryhackme.com/room/25daysofchristmas)