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

**Explicación:** Presentación de la edición 2023: los Frostlings (humanoides helados) amenazan la Navidad y McGreedy dirige la operación. Combinación de retos SOC, IA, web, AD y forense. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Cómo jugar

**Explicación:** Explicación del formato de la sala: tareas diarias con máquinas desplegables, preguntas con respuestas exactas y seguimiento por la interfaz del evento. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el formato de las tareas diarias. | `No answer needed` |

### Task 3: Configuración del laboratorio

**Explicación:** Se configura el entorno: activar la máquina del día, conectarse por VPN/AttackBox, comprobar el acceso web al laboratorio y verificar la conectividad de red. Tarea de preparación sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura tu entorno de trabajo. | `No answer needed` |
| 2 | Activa la máquina del día. | `No answer needed` |
| 3 | Accede por VPN/AttackBox. | `No answer needed` |
| 4 | Comprueba el acceso web. | `No answer needed` |
| 5 | Ejecuta los primeros pasos de configuración. | `No answer needed` |
| 6 | Verifica la conectividad de red. | `No answer needed` |

### Task 4: Pregunta previa

**Explicación:** Pregunta de confirmación textual para arrancar el evento: la respuesta esperada es `yes`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Estás listo para comenzar el evento? | `yes` |

### Task 5: Historia de fondo

**Explicación:** Narrativa: la "Antarctic Crafts" es un negocio cooperativo navideño cuyos operadores (Tourists, Penguins, etc.) sufren el sabotaje de los Frostlings. Solo lectura de la historia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 6: Contexto del reto

**Explicación:** Repaso del contexto operativo del evento y sus objetivos día a día. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa el contexto y los objetivos del reto. | `No answer needed` |

### Task 7: Día 1 - Análisis inicial (SOC)

**Explicación:** Primer caso SOC: se siguen correos sospechosos en el laboratorio de Investigación. El remitente investigado es `t.mcgreedy@antarcticrafts.thm`, el correo menciona el código `BtY2S02` y apunta al producto/servicio `Purple Snow`. Lección: correlacionar correos con productos internos para localizar el incidente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el correo del remitente que se investiga? | `t.mcgreedy@antarcticrafts.thm` |
| 2 | ¿Qué código/identificador se menciona en el correo analizado? | `BtY2S02` |
| 3 | ¿Cómo se llama el producto/servicio indicado en la pista? | `Purple Snow` |
| 4 | Sigue el hilo del correo para cerrar el caso. | `No answer needed` |

### Task 8: Día 2 - Análisis de tráfico (ping/ICMP)

**Explicación:** Análisis de una captura PCAP con Wireshark: el primer paquete tiene TTL `100`, la primera petición parte de `10.10.1.4` y el protocolo usado en el escaneo inicial es `ICMP`. Lección: los ping sweeps (múltiples ICMP a varios hosts) delatan escaneo de red; el TTL ayuda a identificar el SO.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina del laboratorio. | `No answer needed` |
| 2 | ¿Cuál es el valor TTL del primer paquete analizado? | `100` |
| 3 | ¿Qué dirección IP envía la primera petición detectada? | `10.10.1.4` |
| 4 | ¿Qué protocolo se usa en el escaneo inicial de la captura? | `ICMP` |
| 5 | Analiza el resto de la captura. | `No answer needed` |

### Task 9: Día 3 - Brute force de PIN

**Explicación:** El panel de acceso protegido por PIN tiene un rango reducido y se fuerza con un script/Burp Intruder; la flag es `THM{pin-code-brute-force}`. Lección: los PINs de pocos dígitos sin límite de intentos se agotan en segundos; implementar rate-limiting y bloqueo.

```python
# idea del ataque: probar cada PIN contra el endpoint
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto de brute force del código PIN? | `THM{pin-code-brute-force}` |
| 2 | Fuerza el PIN y accede al panel. | `No answer needed` |

### Task 10: Día 4 - Credenciales por defecto

**Explicación:** El dispositivo/servicio mantiene las credenciales por defecto `isaias:Happiness`, que permiten entrar; la flag es `THM{m3rrY4nt4rct1crAft$}`. Lección: cambiar siempre las credenciales de fábrica en todos los servicios y dispositivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué credenciales (usuario:contraseña) permiten el acceso inicial? | `isaias:Happiness` |
| 2 | ¿Cuál es la flag de la tarea? | `THM{m3rrY4nt4rct1crAft$}` |
| 3 | Entra en el sistema con las credenciales por defecto. | `No answer needed` |

### Task 11: Día 5 - Archivos comprimidos y ASCII

**Explicación:** Un archivo comprimido protegido (referencia a `BackupMaster3000` en la pista) revela un archivo de texto de `12,704` palabras. El contenido oculto está en hexadecimal: los primeros bytes son `41 43` (que en ASCII son `A` y `C`), y convirtiendo todo el hex a ASCII se obtiene la flag `THM{0LD_5CH00L_C00L_d00D}`. Lección: convertir hex↔ASCII con CyberChef/xxd para recuperar contenido ofuscado.

```bash
xxd -r -p dump.hex
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántas palabras/entradas contiene el archivo de texto analizado? | `12,704` |
| 2 | ¿Qué herramienta/nombre de backup aparece en la pista? | `BackupMaster3000` |
| 3 | ¿Qué valores hexadecimales se muestran en la primera conversión? | `41 43` |
| 4 | ¿Cuál es la flag del reto? | `THM{0LD_5CH00L_C00L_d00D}` |
| 5 | Convierta los hex y extraiga el mensaje. | `No answer needed` |

### Task 12: Día 6 - Marcas temporales / logs

**Explicación:** En el log se identifica la marca temporal (epoch) clave `1397772111`; convirtiéndola a fecha/hora se confirma el evento. La flag del análisis es `THM{mchoneybell_is_the_real_star}`. Lección: los timestamps Unix se convierten con `date -d @1397772111` o CyberChef (From UNIX Timestamp).

```bash
date -d @1397772111
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de la marca temporal (timestamp) clave del log? | `1397772111` |
| 2 | ¿Cuál es la flag del análisis? | `THM{mchoneybell_is_the_real_star}` |
| 3 | Convierte la marca temporal para confirmar el evento. | `No answer needed` |
| 4 | Continúa con el análisis del archivo. | `No answer needed` |

### Task 13: Día 7 - Análisis de logs web

**Explicación:** Análisis de logs Apache: los tres primeros valores numéricos son `9`, `111` y `503` (status code de la petición fallida del atacante). El dominio consultado es `frostlings.bigbadstash.thm`, el origen del ataque es `10.10.185.225`, el puerto destacado en la respuesta es `1581` y la flag es `THM{a_gift_for_you_awesome_analyst!}`. Lección: correlacionar IP de origen, paths, códigos de estado y dominios en logs web.

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

**Explicación:** Análisis bytes del ejecutable `JuicyTomaTOY.exe`: en las cadenas se extrae el dominio del C2 `mcgreedysecretc2.thm`, la flag es `THM{byt3-L3vel_@n4Lys15}` y el hash (SHA1) del binario es `39f2dea6ffb43bf80d80f19d122076b3682773c2`. Lección: strings + hashing sobre la muestra para registrar IoC.

```bash
strings JuicyTomaTOY.exe | grep -iE "http|c2|thm"
sha1sum JuicyTomaTOY.exe
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dominio del C2 se extrae del binario analizado? | `mcgreedysecretc2.thm` |
| 2 | ¿Cómo se llama el ejecutable malicioso identificado? | `JuicyTomaTOY.exe` |
| 3 | ¿Cuál es la flag del análisis a nivel de byte? | `THM{byt3-L3vel_@n4Lys15}` |
| 4 | ¿Cuál es el hash del archivo malicioso? | `39f2dea6ffb43bf80d80f19d122076b3682773c2` |
| 5 | Documenta los indicadores del binario. | `No answer needed` |

### Task 15: Día 9 - C2 y tráfico de malware

**Explicación:** Reconstrucción del tráfico C2: el User-Agent del malware imita Safari (`Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15`), exfiltra datos con `POST`, usa la clave/secreto `youcanthackthissupersecurec2keys` hacia `http://mcgreedysecretc2.thm/reg`, envía `15` registros, solicita una backdoor `shell` y aparece además `stash.mcgreedy.thm`. Lección: identificar UA falsos y endpoints POST para reconstruir el C2.

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

**Explicación:** La aplicación PHP (`/giftsearch.php`) es vulnerable a inyección SQL; el error de la consulta revela el `ODBC Driver 17 for SQL Server` (SQL Server como backend). Enumerando bases/tablas con sqlmap se obtienen tres flags: `THM{a4ffc901c27fb89efe3c31642ece4447}`, `THM{b06674fedd8dfc28ca75176d3d51409e}` y `THM{4cbc043631e322450bc55b42c}`. Lección: los mensajes de error y los drivers delatan el backend y facilitan el ataque.

```bash
sqlmap -u "http://MACHINE_IP/giftsearch.php?gift=abc" --dbms=mssql --dbs --batch
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué script/página de la aplicación es vulnerable a inyección SQL? | `/giftsearch.php` |
| 2 | ¿Qué driver de base de datos se revela en el error de la consulta? | `ODBC Driver 17 for SQL Server` |
| 3 | ¿Cuál es la primera flag del reto? | `THM{a4ffc901c27fb89efe3c31642ece4447}` |
| 4 | ¿Cuál es la segunda flag del reto? | `THM{b06674fedd8dfc28ca75176d3d51409e}` |
| 5 | ¿Cuál es la tercera flag del reto? | `THM{4cbc043631e322450bc55b42c}` |
| 6 | Explota la inyección para obtener todas las flags. | `No answer needed` |

### Task 17: Día 11 - Integridad de archivos

**Explicación:** Verificación de integridad de backups: el hash MD5 de referencia del archivo es `03E805D8A8C5AA435FB48832DAD620E3` y la flag es `THM{XMAS_IS_SAFE}`. Comparando los hashes calculados con los de referencia se confirma que los backups no fueron manipulados. Lección: usar hashes (FIM) para detectar modificaciones no autorizadas.

```powershell
Get-FileHash -Algorithm MD5 archivo.ps1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash de integridad (MD5) del archivo comprobado? | `03E805D8A8C5AA435FB48832DAD620E3` |
| 2 | ¿Cuál es la flag de la tarea? | `THM{XMAS_IS_SAFE}` |
| 3 | Verifica la integridad de los backups con el hash. | `No answer needed` |
| 4 | Termina la comprobación de los archivos. | `No answer needed` |

### Task 18: Día 12 - Jenkins

**Explicación:** Jenkins corre en `8080`. Se entra como el usuario `13_1n_33` con contraseña `ezRo0tW1thoutDiD`; intentando `sudo` devuelve `Sorry, user tracy may not run sudo on Jenkins.`. Configurando un nodo/agente se consigue ejecución de comandos: las flags son `Ne3d2SecureTh1sSecureSh31l` y `FullTrust_has_n0_Place1nS3cur1ty`. Lección: Jenkins mal configurado (agentes libres, credenciales débiles) da RCE.

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

**Explicación:** Teoría de detección: se describe el ataque con el `Diamond Model` (adversario, infraestructura, capacidad, víctima) y se aplica `Threat hunting` para buscarlo proactivamente. Los controles de red recomendados son `Firewall and Honeypot`; la acción asignada a la regla analizada es `Deny`; la flag es `THM{P0T$_W@11S_4_S@N7@}`. Lección: modelar el ataque para diseñar detección y controles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modelo de análisis se usa para describir el ataque? | `Diamond Model` |
| 2 | ¿Qué metodología de búsqueda proactiva de amenazas se emplea? | `Threat hunting` |
| 3 | ¿Qué controles de red se recomiendan frente a los Frostlings? | `Firewall and Honeypot` |
| 4 | ¿Qué acción/resultado se asigna a la regla analizada? | `Deny` |
| 5 | ¿Cuál es la flag del reto de defensa? | `THM{P0T$_W@11S_4_S@N7@}` |
| 6 | Dimensiona los controles de la infraestructura. | `No answer needed` |

### Task 20: Día 14 - Introducción a la IA (Machine Learning)

**Explicación:** Conceptos de inteligencia artificial: la rama usada es `Machine Learning`, el algoritmo evolutivo mencionado es el `Genetic Algorithm`, el aprendizaje con datos etiquetados es `Supervised Learning`, la capa interna que procesa características es la `Hidden Layer`, y la técnica que ajusta pesos es `Back-Propagation`. La flag es `THM{Neural.Networks.are.Neat!}`. Lección: entender los bloques de las redes neuronales para aplicarlos a seguridad.

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

**Explicación:** Pipeline de ML: el primer paso es `data collection` y el segundo `feature engineering`; el modelo entrenado (con `3` épocas) alcanza `0.98` de precisión, y la contraseña que predice para el reto es `I_Hate_Best_FestiVal`. Lección: un modelo entrenado sobre una distribución de contraseñas puede adivinarlas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer paso del pipeline de entrenamiento? | `data collection` |
| 2 | ¿Cuál es el segundo paso del pipeline? | `feature engineering` |
| 3 | ¿Qué precisión (accuracy) alcanza el modelo entrenado? | `0.98` |
| 4 | ¿Cuántas épocas/iteraciones se usan en el entrenamiento? | `3` |
| 5 | ¿Qué contraseña predice el modelo para el reto? | `I_Hate_Best_FestiVal` |
| 6 | Entrena y valida el modelo en el laboratorio. | `No answer needed` |

### Task 22: Día 16 - OCR/CAPTCHA con IA

**Explicación:** Redes convolucionales para OCR: `Feature Extraction` extrae las características, `Convolution` detecta patrones, `Pooling` reduce la dimensionalidad y `Attention OCR` interpreta el texto de salida. El CAPTCHA que resuelve el modelo es `ReallyNotGonnaGuessThis` y la flag es `THM{Captcha.Can't.Hold.Me.Back}`. Lección: el OCR con CNN automatiza la resolución de CAPTCHAs.

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

**Explicación:** Análisis de logs JSON de una aplicación: versión del servicio `3.19.1`; primera conexión puerto `11774` con timestamp `2023/12/05T09:33:07.755` y puerto de origen `49950`; latitud `35.332088`; ID del registro `735229`; segunda conexión con timestamp `2023/12/08T04:28:44.825`; IPs de origen (defanged) `175[.]175[.]173[.]221` y `175[.]215[.]236[.]223`; último puerto destino `1658`. Lección: los logs JSON estructurados permiten correlacionar eventos y IPs para reconstruir la línea temporal.

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

**Explicación:** Persistencia en Linux vía systemd: la unidad usada es `a-unkillable.service`, instalada en `/etc/systemd/system`, y se confirma `4` ejecuciones del servicio malicioso en los logs/reinicios. Lección: las unidades systemd (`systemctl`) son un mecanismo de persistencia que hay que revisar y matar.

```bash
systemctl status a-unkillable.service
cat /etc/systemd/system/a-unkillable.service
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué unidad de systemd se usa para mantener la persistencia? | `a-unkillable.service` |
| 2 | ¿En qué directorio se instala la unidad de servicio? | `/etc/systemd/system` |
| 3 | ¿Cuántas veces se identifica la ejecución del servicio malicioso? | `4` |
| 4 | Crea y valida la unidad de persistencia en el host. | `No answer needed` |

### Task 25: Día 19 - Malware y comunicación C2

**Explicación:** Análisis avanzado de la muestra maliciosa: cadena codificada `NEhX4VSrN7sV`, puerto de comunicación con el C2 `10280`, hashes MD5 `153a5c8efe4aa3be240e5dc645480dee` y SHA256 `c586e774bb2aa17819d7faae18dad7d1`, dominio del C2 `hxxp[://]mcgreedysecretc2[.]thm` y el payload instalado en `/var/tmp/.system-python3.8-Updates/mysqlserver`. Lección: combinar hashes, strings y rutas de drop para documentar la infección.

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

**Explicación:** OSINT sobre el operador del ataque: la cuenta de Twitter es `@badsecops`, conecta a un panel de control en el puerto `9081` servido por `Apache`, que muestra el mensaje `FROSTLINGS RULE`; la muestra del panel se identifica con el hash `986b7407`. Lección: pivotar desde IoC de red hacia quién opera la infraestructura.

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

**Explicación:** Reconocimiento del host AWS comprometido: el kernel es `5.4.0-1029-aws` y el hash SHA256 del parche/candidato de actualización es `90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7`. Lección: conocer la versión de kernel y planificar parcheado para reducir vulnerabilidades (FIM/gestión de cambios).

```bash
uname -a
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión de kernel ejecuta el sistema AWS comprometido? | `5.4.0-1029-aws` |
| 2 | ¿Cuál es el hash SHA256 del parche/candidato analizado? | `90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7` |
| 3 | Verifica el plano de actualización del sistema. | `No answer needed` |

### Task 28: Día 22 - Teoría y evaluación de amenazas

**Explicación:** Evaluación de la amenaza: el agente `31001` no se encuentra presente en el host (`nay`); el protocolo/servicio evaluado es `1.1`; el usuario asociado a credenciales comprometidas es `mcgreedy`. Las flags son `THM{EXPLOITED_31001}` y `THM{AGENT_REMOVED_1001}`. Lección: verificar presencia de agentes/implantaciones y documentar cada hallazgo en la evaluación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Según el análisis, ¿el agente 31001 está presente en el host? | `nay` |
| 2 | ¿Qué versión de protocolo/servicio se menciona en la evaluación? | `1.1` |
| 3 | ¿Qué usuario aparece asociado a las credenciales comprometidas? | `mcgreedy` |
| 4 | ¿Cuál es la primera flag de la tarea? | `THM{EXPLOITED_31001}` |
| 5 | ¿Cuál es la segunda flag de la tarea? | `THM{AGENT_REMOVED_1001}` |
| 6 | Documenta la evaluación de la amenaza. | `No answer needed` |

### Task 29: Día 23 - Responder / Active Directory

**Explicación:** Ataque de envenenamiento en AD: el protocolo de autenticación kerberos/NTLM envenenado captura hashes `NetNTLMv2`. Con `Responder` se envenenan las consultas y con hashcat/john se crackea: contraseña `GreedyGrabber1@` y flag `THM{Greedy.Greedy.McNot.So.Great.Stealy}`. Lección: Responder captura retos NetNTLM en redes sin SMB firmado; crackear el hash otorga credenciales del dominio.

```bash
sudo responder -I eth0
hashcat -m 5600 hash.txt rockyou.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué kerberos/protocolo de autenticación usa el ataque en el dominio? | `Kerberos` |
| 2 | ¿Qué tipo de hash captura la herramienta durante la autenticación? | `NetNTLM` |
| 3 | ¿Qué herramienta se usa para capturar los hashes en la red? | `Responder` |
| 4 | ¿Cuál es la contraseña descifrada a partir del hash capturado? | `GreedyGrabber1@` |
| 5 | ¿Cuál es la flag del ataque al dominio? | `THM{Greedy.Greedy.McNot.So.Great.Stealy}` |
| 6 | Demuestra el acceso con las credenciales obtenidas. | `No answer needed` |

### Task 30: Día 24 - Forense digital

**Explicación:** Caso forense final (mitología filatélica/honoraria de Evidence.tsv de constelación): la flag del caso es `THM{DIGITAL_FORENSICS}`, el investigador principal es `Detective Carrot-Nose` y la contraseña para avanzar al siguiente paso es `chee7AQu`. Lección: seguir el caso paso a paso con las evidencias recopiladas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del caso forense? | `THM{DIGITAL_FORENSICS}` |
| 2 | ¿Cómo se llama el investigador principal del caso? | `Detective Carrot-Nose` |
| 3 | ¿Qué contraseña se requiere para el siguiente paso del caso? | `chee7AQu` |
| 4 | Analiza las evidencias del caso con la herramienta forense. | `No answer needed` |

### Task 31: Flag final

**Explicación:** Episodio final que cierra la trama de los Frostlings y McGreedy; la flag es `THM{YouMeddlingKids}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del episodio final? | `THM{YouMeddlingKids}` |

### Task 32: Encuesta

**Explicación:** Encuesta de cierre del evento para valorar la experiencia del Advent of Cyber 2023.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Responde a la encuesta de cierre del evento. | `No answer needed` |

### Task 33: Confirmación de la encuesta

**Explicación:** Tras completar la encuesta, la flag de confirmación es `THM{SurveyComplete_and_HolidaysSaved}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por participar. Introduce la flag de confirmación. | `THM{SurveyComplete_and_HolidaysSaved}` |

---

**Metodología:** Los días SOC analizan correos, ping sweeps y logs web hasta llegar al C2 del malware (mcgreedysecretc2.thm). La fase ofensiva usa brute force de PIN, credenciales por defecto, archivos comprimidos con ASCII, una app PHP con inyección SQL sobre SQL Server y el compromiso de Jenkins para ejecutar comandos. La parte analítica explica Diamond Model, threat hunting, Machine Learning (incluido OCR/CAPTCHA) y análisis de logs JSON. Finalmente se cubre persistencia con systemd, OSINT del operador @badsecops, un ataque Responder contra NetNTLM/Kerberos y un caso de forense digital.

**Learning chain:** análisis SOC → ping sweep/ICMP → brute force → credenciales por defecto → ASCII/zipcrypto → timestamps → logs web → análisis de malware → C2 → SQLi → integridad → Jenkins → Diamond Model → ML → entrenamiento → OCR → logs JSON → systemd → C2 avanzado → OSINT → kernel/FIM → evaluación de amenazas → Responder → forense digital.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1566 (Phishing), T1555 (Credentials from Password Stores), T1059 (Command and Scripting Interpreter), T1547 (Boot or Logon Autostart Execution), T1105 (Ingress Tool Transfer), T1021 (Remote Services), T1558 (Steal or Forge Kerberos Tickets)

**Fuente:** [TryHackMe - Advent of Cyber 2023](https://tryhackme.com/room/adventofcyber2023)