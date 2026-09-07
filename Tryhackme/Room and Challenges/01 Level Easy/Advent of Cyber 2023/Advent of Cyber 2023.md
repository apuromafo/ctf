# Advent of Cyber 2023

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber2023` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber2023) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Wireshark / Burp Suite / sqlmap / CyberChef / Nmap / Hydra / Jenkins / Responder / systemd / Inteligencia Artificial (ML) / Sigma |
| **Impacto** | Advent of Cyber 2023: SOC, análisis de tráfico y malware, SQLi, Jenkins, detección con modelos Diamond y Machine Learning, Responder, persistencia systemd y forense digital. |

---

**Contexto:** Los Frostlings amenazan la Navidad de 2023 y McGreedy es el villano de turno. La sala mezcla análisis SOC (emails, ping sweeps, logs web), brute force de PIN, credenciales por defecto, archivos comprimidos con conversión ASCII, análisis de malware descubriendo el C2 (mcgreedysecretc2), una app web vulnerable con inyección SQL y driver ODBC, compromiso de Jenkins, teoría de detección (Diamond Model, threat hunting), varios días de Machine Learning (incluido un OCR de captchas), análisis de logs de aplicación JSON, persistencia con systemd, OSINT del operador @badsecops, y cierra con un ataque Responder en Active Directory y web forense digital.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Cómo jugar

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el formato de las tareas diarias. | `No answer needed` |

### Task 3: Configuración del laboratorio

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura tu entorno de trabajo. | `No answer needed` |
| 2 | Activa la máquina del día. | `No answer needed` |
| 3 | Accede por VPN/AttackBox. | `No answer needed` |
| 4 | Comprueba el acceso web. | `No answer needed` |
| 5 | Ejecuta los primeros pasos de configuración. | `No answer needed` |
| 6 | Verifica la conectividad de red. | `No answer needed` |

### Task 4: Pregunta previa

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Estás listo para comenzar el evento? | `yes` |

### Task 5: Historia de fondo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 6: Contexto del reto

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa el contexto y los objetivos del reto. | `No answer needed` |

### Task 7: Día 1 - Análisis inicial (SOC)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el correo del remitente que se investiga? | `t.mcgreedy@antarcticrafts.thm` |
| 2 | ¿Qué código/identificador se menciona en el correo analizado? | `BtY2S02` |
| 3 | ¿Cómo se llama el producto/servicio indicado en la pista? | `Purple Snow` |
| 4 | Sigue el hilo del correo para cerrar el caso. | `No answer needed` |

### Task 8: Día 2 - Análisis de tráfico (ping/ICMP)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina del laboratorio. | `No answer needed` |
| 2 | ¿Cuál es el valor TTL del primer paquete analizado? | `100` |
| 3 | ¿Qué dirección IP envía la primera petición detectada? | `10.10.1.4` |
| 4 | ¿Qué protocolo se usa en el escaneo inicial de la captura? | `ICMP` |
| 5 | Analiza el resto de la captura. | `No answer needed` |

### Task 9: Día 3 - Brute force de PIN

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto de brute force del código PIN? | `THM{pin-code-brute-force}` |
| 2 | Fuerza el PIN y accede al panel. | `No answer needed` |

### Task 10: Día 4 - Credenciales por defecto

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué credenciales (usuario:contraseña) permiten el acceso inicial? | `isaias:Happiness` |
| 2 | ¿Cuál es la flag de la tarea? | `THM{m3rrY4nt4rct1crAft$}` |
| 3 | Entra en el sistema con las credenciales por defecto. | `No answer needed` |

### Task 11: Día 5 - Archivos comprimidos y ASCII

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántas palabras/entradas contiene el archivo de texto analizado? | `12,704` |
| 2 | ¿Qué herramienta/nombre de backup aparece en la pista? | `BackupMaster3000` |
| 3 | ¿Qué valores hexadecimales se muestran en la primera conversión? | `41 43` |
| 4 | ¿Cuál es la flag del reto? | `THM{0LD_5CH00L_C00L_d00D}` |
| 5 | Convierta los hex y extraiga el mensaje. | `No answer needed` |

### Task 12: Día 6 - Marcas temporales / logs

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de la marca temporal (timestamp) clave del log? | `1397772111` |
| 2 | ¿Cuál es la flag del análisis? | `THM{mchoneybell_is_the_real_star}` |
| 3 | Convierte la marca temporal para confirmar el evento. | `No answer needed` |
| 4 | Continúa con el análisis del archivo. | `No answer needed` |

### Task 13: Día 7 - Análisis de logs web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer valor numérico del análisis de los logs? | `9` |
| 2 | ¿Cuál es el segundo valor numérico del análisis? | `111` |
| 3 | ¿Cuál es el tercer valor (código) del análisis? | `503` |
| 4 | ¿Qué dominio aparece en los logs analizados? | `frostlings.bigbadstash.thm` |
| 5 | ¿Qué dirección IP se identifica como origen del ataque? | `10.10.185.225` |
| 6 | ¿Qué puerto se destaca en la respuesta del servidor? | `1581` |
| 7 | ¿Cuál es la flag del análisis? | `THM{a_gift_for_you_awesome_analyst!}` |
| 8 | Correlaciona los datos del log con las peticiones maliciosas. | `No answer needed` |

### Task 14: Día 8 - Análisis de malware (byte-level)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dominio del C2 se extrae del binario analizado? | `mcgreedysecretc2.thm` |
| 2 | ¿Cómo se llama el ejecutable malicioso identificado? | `JuicyTomaTOY.exe` |
| 3 | ¿Cuál es la flag del análisis a nivel de byte? | `THM{byt3-L3vel_@n4Lys15}` |
| 4 | ¿Cuál es el hash del archivo malicioso? | `39f2dea6ffb43bf80d80f19d122076b3682773c2` |
| 5 | Documenta los indicadores del binario. | `No answer needed` |

### Task 15: Día 9 - C2 y tráfico de malware

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué user-agent utiliza el malware en sus peticiones? | `Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15` |
| 2 | ¿Qué método HTTP se usa para exfiltrar datos al C2? | `POST` |
| 3 | ¿Cuál es la clave/secreto que forma la comunicación con el C2? | `youcanthackthissupersecurec2keys` |
| 4 | ¿A qué URL del C2 envía el malware los datos? | `http://mcgreedysecretc2.thm/reg` |
| 5 | ¿Cuántos registros/peticiones se envian en el flujo analizado? | `15` |
| 6 | ¿Qué tipo de acceso/backdoor solicita el malware? | `shell` |
| 7 | ¿Qué dominio adicional se detecta en el análisis (stash)? | `stash.mcgreedy.thm` |
| 8 | Reconstruye el flujo completo del C2. | `No answer needed` |

### Task 16: Día 10 - Aplicación web (SQLi)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué script/página de la aplicación es vulnerable a inyección SQL? | `/giftsearch.php` |
| 2 | ¿Qué driver de base de datos se revela en el error de la consulta? | `ODBC Driver 17 for SQL Server` |
| 3 | ¿Cuál es la primera flag del reto? | `THM{a4ffc901c27fb89efe3c31642ece4447}` |
| 4 | ¿Cuál es la segunda flag del reto? | `THM{b06674fedd8dfc28ca75176d3d51409e}` |
| 5 | ¿Cuál es la tercera flag del reto? | `THM{4cbc043631e322450bc55b42c}` |
| 6 | Explota la inyección para obtener todas las flags. | `No answer needed` |

### Task 17: Día 11 - Integridad de archivos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash de integridad (MD5) del archivo comprobado? | `03E805D8A8C5AA435FB48832DAD620E3` |
| 2 | ¿Cuál es la flag de la tarea? | `THM{XMAS_IS_SAFE}` |
| 3 | Verifica la integridad de los backups con el hash. | `No answer needed` |
| 4 | Termina la comprobación de los archivos. | `No answer needed` |

### Task 18: Día 12 - Jenkins

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto usa el servidor Jenkins? | `8080` |
| 2 | ¿Cuál es el nombre de usuario detectado en el laboratorio? | `13_1n_33` |
| 3 | ¿Cuál es la contraseña del usuario Jenkins? | `ezRo0tW1thoutDiD` |
| 4 | ¿Qué mensaje devuelve Jenkins al intentar ejecutar sudo? | `Sorry, user tracy may not run sudo on Jenkins.` |
| 5 | ¿Cuál es la primera flag del reto? | `Ne3d2SecureTh1sSecureSh31l` |
| 6 | ¿Cuál es la segunda flag del reto? | `FullTrust_has_n0_Place1nS3cur1ty` |
| 7 | Configura un nodo/agente en Jenkins para tener ejecución. | `No answer needed` |

### Task 19: Día 13 - Modelo Diamond y defensa

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modelo de análisis se usa para describir el ataque? | `Diamond Model` |
| 2 | ¿Qué metodología de búsqueda proactiva de amenazas se emplea? | `Threat hunting` |
| 3 | ¿Qué controles de red se recomiendan frente a los Frostlings? | `Firewall and Honeypot` |
| 4 | ¿Qué acción/resultado se asigna a la regla analizada? | `Deny` |
| 5 | ¿Cuál es la flag del reto de defensa? | `THM{P0T$_W@11S_4_S@N7@}` |
| 6 | Dimensiona los controles de la infraestructura. | `No answer needed` |

### Task 20: Día 14 - Introducción a la IA (Machine Learning)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué rama de la inteligencia artificial se usa para el análisis? | `Machine Learning` |
| 2 | ¿Qué algoritmo evolutivo se menciona en el material? | `Genetic Algorithm` |
| 3 | ¿Qué tipo de aprendizaje entrena con datos etiquetados? | `Supervised Learning` |
| 4 | ¿Qué capa interna de la red procesa las características? | `Hidden Layer` |
| 5 | ¿Qué técnica ajusta los pesos de las capas al entrenar? | `Back-Propagation` |
| 6 | ¿Cuál es la flag del reto de IA? | `THM{Neural.Networks.are.Neat!}` |
| 7 | Ejecuta el modelo de ejemplo en el laboratorio. | `No answer needed` |

### Task 21: Día 15 - Entrenamiento de un modelo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer paso del pipeline de entrenamiento? | `data collection` |
| 2 | ¿Cuál es el segundo paso del pipeline? | `feature engineering` |
| 3 | ¿Qué precisión (accuracy) alcanza el modelo entrenado? | `0.98` |
| 4 | ¿Cuántas épocas/iteraciones se usan en el entrenamiento? | `3` |
| 5 | ¿Qué contraseña predice el modelo para el reto? | `I_Hate_Best_FestiVal` |
| 6 | Entrena y valida el modelo en el laboratorio. | `No answer needed` |

### Task 22: Día 16 - OCR/CAPTCHA con IA

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso extrae las características del texto de la imagen? | `Feature Extraction` |
| 2 | ¿Qué operación filtra/detecta los patrones de la imagen? | `Convolution` |
| 3 | ¿Qué operación reduce la dimensionalidad de la muestra? | `Pooling` |
| 4 | ¿Qué técnica OCR interpreta la salida del texto? | `Attention OCR` |
| 5 | ¿Qué texto (CAPTCHA) resuelve el modelo para acceder? | `ReallyNotGonnaGuessThis` |
| 6 | ¿Cuál es la flag del reto de OCR? | `THM{Captcha.Can't.Hold.Me.Back}` |
| 7 | Resuelve el captcha con el modelo entrenado. | `No answer needed` |

### Task 23: Día 17 - Análisis de logs de aplicación (JSON)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión del servicio aparece en el log JSON analizado? | `3.19.1` |
| 2 | ¿Qué puerto se menciona en la primera entrada del log? | `11774` |
| 3 | ¿Qué timestamp corresponde a la primera conexión? | `2023/12/05T09:33:07.755` |
| 4 | ¿Qué puerto de origen se registra en la entrada analizada? | `49950` |
| 5 | ¿Qué latitud/coordenada se muestra en el registro? | `35.332088` |
| 6 | ¿Qué ID/registro se identifica dentro del log? | `735229` |
| 7 | ¿Qué timestamp corresponde a la segunda conexión del análisis? | `2023/12/08T04:28:44.825` |
| 8 | ¿Qué IP de origen se registra en la primera consulta (defanged)? | `175[.]175[.]173[.]221` |
| 9 | ¿Qué IP de origen se registra en la segunda consulta (defanged)? | `175[.]215[.]236[.]223` |
| 10 | ¿Qué puerto destino se usa en la última entrada del análisis? | `1658` |
| 11 | Correlaciona los eventos del log con la línea temporal del ataque. | `No answer needed` |

### Task 24: Día 18 - Persistencia (systemd)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué unidad de systemd se usa para mantener la persistencia? | `a-unkillable.service` |
| 2 | ¿En qué directorio se instala la unidad de servicio? | `/etc/systemd/system` |
| 3 | ¿Cuántas veces se identifica la ejecución del servicio malicioso? | `4` |
| 4 | Crea y valida la unidad de persistencia en el host. | `No answer needed` |

### Task 25: Día 19 - Malware y comunicación C2

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cadena codificada se encuentra dentro del binario malicioso? | `NEhX4VSrN7sV` |
| 2 | ¿Qué puerto usa el malware para comunicarse con el C2? | `10280` |
| 3 | ¿Cuál es el primer hash (MD5) de la muestra analizada? | `153a5c8efe4aa3be240e5dc645480dee` |
| 4 | ¿Cuál es el segundo hash (SHA256) de la muestra? | `c586e774bb2aa17819d7faae18dad7d1` |
| 5 | ¿Cuál es el dominio del C2 al que conecta (defanged)? | `hxxp[://]mcgreedysecretc2[.]thm` |
| 6 | ¿Cuál es la ruta del payload instalado en el sistema (mysqlserver)? | `/var/tmp/.system-python3.8-Updates/mysqlserver` |
| 7 | Documenta la cadena completa de la infección. | `No answer needed` |

### Task 26: Día 20 - OSINT (operador malicioso)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cuenta de Twitter del operador se identifica en la investigación? | `@badsecops` |
| 2 | ¿Qué puerto usa el panel de control al que conecta el operador? | `9081` |
| 3 | ¿Qué servidor web responde en ese puerto? | `Apache` |
| 4 | ¿Qué mensaje/motivo se muestra en el panel del operador? | `FROSTLINGS RULE` |
| 5 | ¿Cuál es el hash que identifica la muestra del panel? | `986b7407` |
| 6 | Sigue el rastro del panel de control. | `No answer needed` |
| 7 | Cierra la investigación OSINT del operador. | `No answer needed` |

### Task 27: Día 21 - Reconocimiento del sistema comprometido

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión de kernel ejecuta el sistema AWS comprometido? | `5.4.0-1029-aws` |
| 2 | ¿Cuál es el hash SHA256 del parche/candidato analizado? | `90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7` |
| 3 | Verifica el plano de actualización del sistema. | `No answer needed` |

### Task 28: Día 22 - Teoría y evaluación de amenazas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Según el análisis, ¿el agente 31001 está presente en el host? | `nay` |
| 2 | ¿Qué versión de protocolo/servicio se menciona en la evaluación? | `1.1` |
| 3 | ¿Qué usuario aparece asociado a las credenciales comprometidas? | `mcgreedy` |
| 4 | ¿Cuál es la primera flag de la tarea? | `THM{EXPLOITED_31001}` |
| 5 | ¿Cuál es la segunda flag de la tarea? | `THM{AGENT_REMOVED_1001}` |
| 6 | Documenta la evaluación de la amenaza. | `No answer needed` |

### Task 29: Día 23 - Responder / Active Directory

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué kerberos/protocolo de autenticación usa el ataque en el dominio? | `Kerberos` |
| 2 | ¿Qué tipo de hash captura la herramienta durante la autenticación? | `NetNTLM` |
| 3 | ¿Qué herramienta se usa para capturar los hashes en la red? | `Responder` |
| 4 | ¿Cuál es la contraseña descifrada a partir del hash capturado? | `GreedyGrabber1@` |
| 5 | ¿Cuál es la flag del ataque al dominio? | `THM{Greedy.Greedy.McNot.So.Great.Stealy}` |
| 6 | Demuestra el acceso con las credenciales obtenidas. | `No answer needed` |

### Task 30: Día 24 - Forense digital

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del caso forense? | `THM{DIGITAL_FORENSICS}` |
| 2 | ¿Cómo se llama el investigador principal del caso? | `Detective Carrot-Nose` |
| 3 | ¿Qué contraseña se requiere para el siguiente paso del caso? | `chee7AQu` |
| 4 | Analiza las evidencias del caso con la herramienta forense. | `No answer needed` |

### Task 31: Flag final

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del episodio final? | `THM{YouMeddlingKids}` |

### Task 32: Encuesta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Responde a la encuesta de cierre del evento. | `No answer needed` |

### Task 33: Confirmación de la encuesta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por participar. Introduce la flag de confirmación. | `THM{SurveyComplete_and_HolidaysSaved}` |

---

**Metodología:** Los días SOC analizan correos, ping sweeps y logs web hasta llegar al C2 del malware (mcgreedysecretc2.thm). La fase ofensiva usa brute force de PIN, credenciales por defecto, archivos comprimidos con ASCII, una app PHP con inyección SQL sobre SQL Server y el compromiso de Jenkins para ejecutar comandos. La parte analítica explica Diamond Model, threat hunting, Machine Learning (incluido OCR/CAPTCHA) y análisis de logs JSON. Finalmente se cubre persistencia con systemd, OSINT del operador @badsecops, un ataque Responder contra NetNTLM/Kerberos y un caso de forense digital.

**Learning chain:** análisis SOC → ping sweep/ICMP → brute force → credenciales por defecto → ASCII/zipcrypto → timestamps → logs web → análisis de malware → C2 → SQLi → integridad → Jenkins → Diamond Model → ML → entrenamiento → OCR → logs JSON → systemd → C2 avanzado → OSINT → kernel/FIM → evaluación de amenazas → Responder → forense digital.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1566 (Phishing), T1555 (Credentials from Password Stores), T1059 (Command and Scripting Interpreter), T1547 (Boot or Logon Autostart Execution), T1105 (Ingress Tool Transfer), T1021 (Remote Services), T1558 (Steal or Forge Kerberos Tickets)

**Fuente:** [TryHackMe - Advent of Cyber 2023](https://tryhackme.com/room/adventofcyber2023)