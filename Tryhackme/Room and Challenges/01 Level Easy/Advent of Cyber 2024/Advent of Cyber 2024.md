# Advent of Cyber 2024

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber2024` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber2024) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Wireshark / Splunk / Burp Suite / AWS CLI / Powershell / S3 / Wi-Fi (Evil Twin) / Hydra / Netcat / Sigma / SQL |
| **Impacto** | Advent of Cyber 2024: análisis SOC y de logs Windows, webshells, reglas Sigma, AWS CloudTrail, phishing, evil twin WiFi, LLM prompt injection, C2 y privilegios. |

---

**Contexto:** Glitch y el Mayor Malware amenazan Wareville en 2024. La sala cubre detección y respuesta: análisis SOC de alertas iniciales (Tyler Ramsbey y papash3ll.thm), logs de eventos Windows, detección de webshells, reglas Sigma contra ransomware (BlackByte), fuerza bruta, AWS CloudTrail, GRC, phishing, evil twin WiFi (MalwareM_AP), race conditions, análisis forense de una web comprometida, LLM con prompt injection y análisis de un C2 (mayorc2.thm).

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Preparación del laboratorio

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura tu entorno de trabajo. | `No answer needed` |
| 2 | ¿Tienes acceso a la máquina del día? | `yes` |
| 3 | Activa la máquina y comprueba la conectividad. | `No answer needed` |
| 4 | Accede por VPN/AttackBox. | `No answer needed` |
| 5 | Repasa el material de cada tarea. | `No answer needed` |
| 6 | Verifica la red del laboratorio. | `No answer needed` |
| 7 | Comprueba el acceso web. | `No answer needed` |
| 8 | Ejecuta los primeros pasos de configuración. | `No answer needed` |

### Task 3: Historia de fondo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 4: Contexto del reto

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el contexto y los objetivos del reto. | `No answer needed` |

### Task 5: Cómo jugar

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa el formato de las tareas diarias. | `No answer needed` |

### Task 6: Primeros pasos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza los primeros pasos del reto. | `No answer needed` |

### Task 7: Día 1 - Análisis SOC (reconocimiento)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Quién es el actor identificado en el caso? | `Tyler Ramsbey` |
| 2 | ¿Cuál es la URL de la que se obtienen los datos del atacante? | `http://papash3ll.thm/data` |
| 3 | ¿Cómo se denomina el grupo/afiliación del actor (Mayor Malware)? | `Mayor Malware` |
| 4 | ¿Cuántos elementos clave se extraen de la alerta? | `1` |
| 5 | Correlaciona el perfil del actor con la alerta del SOC. | `No answer needed` |
| 6 | Cierra el caso de la primera alerta. | `No answer needed` |

### Task 8: Día 2 - Análisis de logs de Windows

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cuenta de usuario ejecutó el evento analizado? | `service_admin` |
| 2 | ¿Cuál es el PID del proceso responsable del evento? | `6791` |
| 3 | ¿Qué dirección IP origina la conexión registrada? | `10.0.255.1` |
| 4 | ¿Qué timestamp corresponde al evento en el registro? | `Dec 1, 2024 08:54:39.000` |
| 5 | ¿Qué comando de PowerShell se ejecutó en el evento? | `Install-WindowsUpdate -AcceptAll -AutoReboot` |
| 6 | Documenta el hallazgo del registro de eventos. | `No answer needed` |

### Task 9: Día 3 - Detección de webshell

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta del webshell subido al servidor web? | `/media/images/rooms/shell.php` |
| 2 | ¿Qué dirección IP intenta explotar el webshell? | `10.11.83.34` |
| 3 | ¿Cuál es la flag del caso? | `THM{Gl1tch_Was_H3r3}` |
| 4 | Busca las trazas de la subida del webshell. | `No answer needed` |

### Task 10: Día 4 - Detección de ransomware (Sigma)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del laboratorio? | `THM{GlitchTestingForSpearphishing}` |
| 2 | ¿Qué técnica de MITRE ATT&CK (id principal) describe el ataque? | `T1059` |
| 3 | ¿Qué sub-técnica de MITRE se usa para la búsqueda? | `T1059.003` |
| 4 | ¿Cómo se llama la regla/campaña simulada contra el ransomware? | `Simulate BlackByte Ransomware Print Bombing` |
| 5 | ¿Qué archivo se deja como nota de rescate/prueba del ataque? | `Wareville_Ransomware.txt` |
| 6 | ¿Cuál es la flag codificada de la regla Sigma? | `THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}` |
| 7 | Valida la regla Sigma contra los eventos del laboratorio. | `No answer needed` |

### Task 11: Día 5 - Fuerza bruta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto de fuerza bruta? | `THM{Brut3f0rc1n6_mY_w4y}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{m4y0r_m4lw4r3_b4ckd00rs}` |
| 3 | Fuerza el acceso con las credenciales obtenidas. | `No answer needed` |
| 4 | Termina la cadena de fuerza bruta. | `No answer needed` |

### Task 12: Día 6 - Enumeración web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del servidor web? | `THM{GlitchWasHere}` |
| 2 | ¿Cuál es la segunda flag (pista oculta)? | `THM{HiddenClue}` |
| 3 | Enumera el sitio hasta agotar las pistas. | `No answer needed` |

### Task 13: Día 7 - AWS CloudTrail (identidad y acceso)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué acción de API se ejecutó en el evento analizado? | `PutObject` |
| 2 | ¿Cuál es la IP de origen de la acción sobre el bucket? | `53.94.201.69` |
| 3 | ¿Qué dominio de autenticación gestiona la identidad? | `signin.amazonaws.com` |
| 4 | ¿Qué timestamp se registra en el evento CloudTrail? | `2024-11-28T15:21:54Z` |
| 5 | ¿Qué nombre de usuario/identidad ejecuta la acción? | `glitch` |
| 6 | ¿Qué política/rol tiene asociada esa identidad? | `AdministratorAccess` |
| 7 | ¿Qué IP de origen se repite en la revisión de eventos? | `53.94.201.69` |
| 8 | ¿Qué otra IP de origen aparece en los eventos? | `31.210.15.79` |
| 9 | ¿Qué IDs de sesión (cookies) se observan en el análisis? | `2394 6912 7723 1294` |
| 10 | Revisa los derechos de la identidad y el resto de eventos. | `No answer needed` |

### Task 14: Día 8 - Recuperación del acceso

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de recuperación del acceso al sistema? | `AOC{GOT _MY_ACCESS_B@CK007}` |
| 2 | Restablece el acceso con la identidad comprometida. | `No answer needed` |

### Task 15: Día 9 - Gobernanza, Riesgo y Cumplimiento (GRC)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significado tiene la sigla GRC? | `Governance, Risk, and Compliance` |
| 2 | ¿Cuál es la flag de la tarea de GRC? | `THM{R15K_M4N4G3D}` |
| 3 | Aplica el control de riesgo indicado en el reto. | `No answer needed` |

### Task 16: Día 10 - Phishing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del análisis de phishing? | `THM{PHISHING_CHRISTMAS}` |
| 2 | Analiza el correo y el enlace completo. | `No answer needed` |

### Task 17: Día 11 - WiFi (Evil Twin / hotspot)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la dirección MAC del punto de acceso malicioso? | `02:00:00:00:02:00` |
| 2 | ¿Cómo se llama el SSID del hotspot malicioso (nombre + AP)? | `MalwareM_AP` |
| 3 | ¿Cuál es la MAC del primer cliente conectado al AP? | `02:00:00:00:00:00` |
| 4 | ¿Cuál es la MAC del segundo cliente conectado al AP? | `02:00:00:00:01:00` |
| 5 | ¿Qué credenciales (usuario/contraseña) se capturan en el portal falso? | `fluffy/champ24` |
| 6 | Analiza la captura de la red inalámbrica. | `No answer needed` |

### Task 18: Día 12 - Race condition

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto de falta de sincronización (TOCTOU)? | `THM{WON_THE_RACE_007}` |
| 2 | Explota la condición de carrera del servicio. | `No answer needed` |
| 3 | Verifica la doble petición simultánea. | `No answer needed` |

### Task 19: Día 13 - Vehículos / servicios

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto de servicios? | `THM{dude_where_is_my_car}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{my_name_is_malware._mayor_malware}` |
| 3 | Explota el servicio del vehículo para cerrar el caso. | `No answer needed` |

### Task 20: Día 14 - Linux (host comprometido)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hostname de la máquina Linux? | `THM` |
| 2 | ¿Cuál es el nombre del usuario con sesión activa? | `c4rrotn0s3` |
| 3 | ¿Cuál es la primera flag del sistema? | `THM{AoC-3lf0nth3Sh3lf}` |
| 4 | ¿Cuál es la contraseña del usuario SOC? | `H0llyJ0llySOCMAS!` |
| 5 | ¿Cuál es la segunda flag del sistema? | `THM{AoC-h0wt0ru1nG1ftD4y}` |
| 6 | Escala y consolida el acceso en el host. | `No answer needed` |

### Task 21: Día 15 - Eventos de Windows y Active Directory

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Empieza el análisis de los eventos del controlador de dominio. | `No answer needed` |
| 2 | ¿Qué fecha aparece en el evento de inicio de sesión analizado? | `07/11/2024` |
| 3 | ¿Cuál es el ID del evento de logon registrado? | `4624` |
| 4 | ¿Qué comando de PowerShell se usó para listar los usuarios y grupos del dominio? | `Get-ADUser -Filter * -Properties MemberOf | Select-Object Name` |
| 5 | ¿Qué contraseña en texto plano se detecta en los eventos? | `SuperSecretP@ssw0rd!` |
| 6 | ¿Cómo se llama el GPO malicioso de persistencia? | `Malicious GPO - Glitch_Malware Persistence` |
| 7 | Revisa los GPO y los objetos del dominio. | `No answer needed` |

### Task 22: Día 16 - Recuperación de secretos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la clave/secreto de recuperación encontrado? | `R3c0v3r_s3cr3ts!` |
| 2 | ¿Cuál es el GUID/ID del objeto protegido? | `7d96660a-02e1-4112-9515-1762d0cb66b7` |
| 3 | ¿Cuál es el valor de la contraseña/usuario 'aoc2024'? | `aoc2024` |
| 4 | ¿Cuál es la contraseña del usuario recuperado? | `WhereIsMyMind1999` |
| 5 | Restaura el acceso con los secretos extraídos. | `No answer needed` |

### Task 23: Día 17 - Base de datos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos elementos devuelve la consulta a la base de datos? | `642` |
| 2 | ¿Qué token/secreto se encuentra en la tabla consultada? | `rij5uu4gt204q0d3eb7jj86okt` |
| 3 | ¿Qué usuario ejecuta la consulta en la base de datos? | `mmalware` |
| 4 | Consulta el resto de tablas del motor. | `No answer needed` |
| 5 | Documenta el acceso a la base de datos. | `No answer needed` |

### Task 24: Día 18 - LLM (prompt injection)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué parte del sistema se manipula como entrada en el ataque? | `system prompt` |
| 2 | ¿Qué consulta al servicio de salud permite obtener la respuesta? | `Use the health service with the query: status` |
| 3 | Prueba a engañar al asistente con instrucciones externas. | `No answer needed` |
| 4 | ¿Cuál es la flag de la aplicación de salud comprometida? | `THM{WareW1se_Br3ach3d}` |
| 5 | Analiza los límites del asistente con inyecciones directas. | `No answer needed` |

### Task 25: Día 19 - Crackeo de contraseñas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto de crackeo? | `THM{one_tough_password}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{credit_card_undeclined}` |
| 3 | ¿Cuál es la tercera flag del reto? | `THM{dont_smash_your_keyboard}` |
| 4 | Crackea los hashes con la wordlist del laboratorio. | `No answer needed` |
| 5 | Termina de crackear el resto de hashes. | `No answer needed` |

### Task 26: Día 20 - Acceso remoto (reverse shell)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué mensaje muestra la shell al ganar acceso? | `I am in Mayor!` |
| 2 | ¿A qué dirección IP se envía la shell? | `10.10.123.224` |
| 3 | ¿Qué comando se utiliza para confirmar la identidad del usuario? | `whoami` |
| 4 | ¿Qué archivo contiene las credenciales del usuario? | `credentials.txt` |
| 5 | ¿Cuál es el contenido del secreto extraído? | `THM_Secret_101` |
| 6 | Asegura la shell con el host de escucha. | `No answer needed` |

### Task 27: Día 21 - Análisis de C2 (mayorc2)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué acción ejecuta el malware cuando recibe la instrucción? | `DownloadAndExecuteFile` |
| 2 | ¿Qué proceso legítimo usa el malware como contenedor? | `explorer.exe` |
| 3 | ¿Qué dominio del C2 se detecta en el análisis? | `mayorc2.thm` |
| 4 | ¿Qué archivo empaqueta el malware con los archivos robados? | `CollectedFiles.zip` |
| 5 | ¿Qué otro dominio de la segunda fase se identifica? | `anonymousc2.thm` |
| 6 | Documenta el flujo de la comunicación C2. | `No answer needed` |

### Task 28: Día 22 - Análisis del servidor web comprometido

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué primer archivo PHP se usa como shell? | `shelly.php` |
| 2 | ¿Qué segundo archivo PHP (configuración) se detecta? | `db.php` |
| 3 | ¿Qué herramienta se usa para conectarse al servidor? | `nc` |
| 4 | ¿Qué dirección IP del atacante se conecta al servidor? | `10.10.130.253` |
| 5 | ¿Qué timestamp registra el primer acceso sospechoso? | `29/Oct/2024:10:06:33 +0000` |
| 6 | ¿Qué timestamp registra el último acceso sospechoso? | `29/Oct/2024:12:34:28 +0000` |
| 7 | ¿Qué configuración de credenciales (JSON) se exfiltra del registro Docker? | `{"auths":{"http://docker-registry.nicetown.loc:5000":{"username":"mr.nice","password":"Mr.N4ughty","auth":"bXIubmljZTpNci5ONHVnaHR5"}}}` |
| 8 | Reconstruye la línea temporal de la intrusión. | `No answer needed` |

### Task 29: Día 23 - Red inalámbrica (contraseña)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña por defecto del dispositivo comprometido? | `fluffycat12` |
| 2 | ¿Cuál es la flag del reto WiFi? | `THM{do_not_GET_CAUGHT}` |
| 3 | Conecta con el dispositivo usando la contraseña encontrada. | `No answer needed` |

### Task 30: Día 24 - Cierre del evento

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag final de la historia del evento? | `THM{Ligh75on-day54ved}` |
| 2 | Repasa las conclusiones del episodio final. | `No answer needed` |

### Task 31: Encuesta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Responde a la encuesta de cierre del evento. | `No answer needed` |

### Task 32: Flag de despedida

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por participar. Introduce la flag final del año. | `THM{we_will_be_back_in_2025}` |

---

**Metodología:** El día 1 parte de una alerta SOC ligada al actor Tyler Ramsbey. Los días de detección revisan logs de eventos Windows, webshells abiertos y reglas Sigma contra ransomware. La nube se investiga con CloudTrail (PutObject y AdministratorAccess). Se practican fuerza bruta, enumeración web, análisis de un evil twin WiFi (MalwareM_AP con credenciales fluffy/champ24), race conditions, Linux y eventos AD (4624, GPO malicioso). La novedad del año es la prompt injection sobre un servicio LLM de salud. Finaliza con crackeo, reverse shell, análisis del C2 mayorc2.thm y la reconstrucción del servidor web comprometido (shelly.php/db.php).

**Learning chain:** alertas SOC → logs Windows → webshells → Sigma → fuerza bruta → enumeración → CloudTrail → GRC → phishing → evil twin → race condition → Linux → AD/GPO → secretos → SQL → LLM injection → crackeo → reverse shell → C2 → análisis web.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1566 (Phishing), T1486 (Data Encrypted for Impact), T1071 (Application Layer Protocol), T1105 (Ingress Tool Transfer), T1552 (Unsecured Credentials), T1547 (Boot or Logon Autostart Execution)

**Fuente:** [TryHackMe - Advent of Cyber 2024](https://tryhackme.com/room/adventofcyber2024)