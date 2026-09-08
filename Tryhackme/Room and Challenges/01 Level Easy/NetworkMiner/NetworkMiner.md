# NetworkMiner

| **Dificultad** | Easy |
| **Tipo** | Análisis forense de red (laboratorio) |
| **Slug** | `networkminer` |
| **Link** | [TryHackMe](https://tryhackme.com/room/networkminer) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | NetworkMiner / pcap / análisis forense / NTLMv2 / SMB / credenciales / OSINT desde capturas / Wireshark |
| **Impacto** | Sala dedicada a NetworkMiner, un analizador de tráfico de red pasivo y de código abierto para forense de red: permite extraer credenciales (incluyendo hashes NTLMv2), identificar hosts y sus sistemas operativos, geolocalizar direcciones IP, listar servicios y versiones, e inspeccionar el contenido de capturas pcap en busca de archivos, correos y actividad maliciosa. |

---

**Contexto:** La sala enseña NetworkMiner, una herramienta de análisis de tráfico de red pasivo (código abierto) que se usa para tareas de forense y respuesta a incidentes. En la primera fase práctica se analiza una captura (`mx-3`): se cuentan los paquetes (460), se cruzan direcciones MAC frente a IPs (2 IPs comparten la MAC de 145.253.2.203), se filtra el tráfico de un origen concreto (72 paquetes de 65.208.228.223), se identifica el servidor web del puerto 80 (Apache) y, en la pestaña de credenciales, se extraen el usuario SMB `#B\Administrator` y el hash NTLMv2 completo. En la segunda práctica (`mx-4`) se identifican el sistema operativo (CentOS), el nombre de la empresa propietaria (Password-Ned AB), una IP de servidor (80.239.178.187) y un puerto (36255), la visita a Facebook y un correo electrónico (branson@sandsite.org). Luego se estudian las versiones de protocolos de una tercera captura (2.7, 1.6, 1.6). Finalmente, en `mx-6` se trabaja sobre una captura de un equipo Windows NT 4 (192 paquetes, puerto 20769, host 2AD77400), se listan los hosts detectados (2), se identifica el dispositivo de red ASIX, el móvil Lumia 535, la IP 50.22.95.9 y, en la pestaña de respuestas de credenciales de correo, la contraseña spring2015 y el servidor pop.gmx.com.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación de la sala: NetworkMiner es una herramienta de análisis de red pasivo, gratuita y de código abierto, orientada al forense de red y a la respuesta a incidentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el resumen de la sala. | `No answer needed` |

### Task 2: Primeros pasos con la herramienta

**Explicación:** Se descargan los archivos de captura (pcaps) que se usarán a lo largo de la sala y se abre NetworkMiner para familiarizarse con sus pestañas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descarga los archivos de la sala y abre NetworkMiner. | `No answer needed` |

### Task 3: Usando NetworkMiner

**Explicación:** Revisión de las distintas pestañas de NetworkMiner (Hosts, Files, Credentials, Messages, Images, Parameters, DNS, etc.) y de cómo cargar capturas pcap para su análisis pasivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora las pestañas de la interfaz y carga las capturas pcap de la sala. | `No answer needed` |

### Task 4: Análisis de la captura mx-3

**Explicación:** Con la captura `mx-3.pcap` cargada se responden las primeras preguntas: el total de paquetes es `460`. Cruzando la pestaña de frames por dirección MAC se ve que `2` direcciones IP comparten la misma MAC que `145.253.2.203`. Del análisis de IPs se extrae que `65.208.228.223` origina `72` paquetes. En la pestaña de servicios se identifica que el servidor del puerto 80 es `Apache`. La información más valiosa está en la pestaña de credenciales: el usuario del sector SMB es `#B\Administrator` y el hash capturado del protocolo de autenticación es el siguiente hash `$NETNTLMv2$...`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos paquetes hay en la captura? | `460` |
| 2 | En la captura, ¿cuántas direcciones IP tienen la misma dirección MAC que 145.253.2.203? | `2` |
| 3 | ¿Cuántos paquetes se originan desde 65.208.228.223? | `72` |
| 4 | ¿Qué servicio web corre en el puerto 80? | `Apache` |
| 5 | ¿Cuál es el nombre de usuario en la sección "SMB Credentials"? | `#B\Administrator` |
| 6 | ¿Qué valor de hash NTLMv2 capturamos? | `$NETNTLMv2$#B$136B077D942D9A63$FBFF3C253926907AAAAD670A9037F2A5$01010000000000000094D71AE38CD60170A8D571127AE49E00000000020004003300420001001E003000310035003600360053002D00570049004E00310036002D004900520004001E0074006800720065006500620065006500730063006F002E0063006F006D0003003E003000310035003600360073002D00770069006E00310036002D00690072002E0074006800720065006500620065006500730063006F002E0063006F006D0005001E0074006800720065006500620065006500730063006F002E0063006F006D00070008000094D71AE38CD601060004000200000008003000300000000000000000000000003000009050B30CECBEBD73F501D6A2B88286851A6E84DDFAE1211D512A6A5A72594D340A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E00360036002E0033003600000000000000000000000000` |

### Task 5: Análisis de la captura mx-4

**Explicación:** En `mx-4.pcap` se identifican el sistema operativo del host `145.253.2.203` (`CentOS`), el nombre de la empresa propietaria del dominio o servidor (`Password-Ned AB`), la IP `80.239.178.187`, el puerto `36255`, el sitio visitado (`Facebook`) y una dirección de correo electrónico presente en la captura (`branson@sandsite.org`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué sistema operativo corre en 145.253.2.203? | `CentOS` |
| 2 | ¿Cuál es el nombre de la empresa propietaria del dominio observado? | `Password-Ned AB` |
| 3 | ¿Cuál es la dirección IP del servidor detectado? | `80.239.178.187` |
| 4 | ¿Qué puerto abre ese servidor? | `36255` |
| 5 | ¿Qué popular sitio web fue visitado desde esa máquina? | `Facebook` |
| 6 | ¿Qué dirección de correo electrónico aparece en la captura? | `branson@sandsite.org` |

### Task 6: Analizando versiones de protocolos (mx-5)

**Explicación:** En la captura `mx-5.pcap` se analizan las versiones de los protocolos de red detectados por NetworkMiner en la pestaña de servicios: los valores de versión responsables de las conexiones son `2.7`, `1.6` y `1.6`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión tiene el primer servicio de red detectado en la captura? | `2.7` |
| 2 | ¿Qué versión tiene el segundo servicio de red detectado en la captura? | `1.6` |
| 3 | ¿Qué versión tiene el tercer servicio de red detectado en la captura? | `1.6` |

### Task 7: Análisis de la captura mx-6

**Explicación:** En `mx-6.pcap` se trabaja sobre un equipo Windows: el sistema operativo detectado es `Windows - Windows NT 4`, la captura contiene `192` paquetes y destaca el puerto `20769` con el host `2AD77400`. NetworkMiner detecta `2` hosts en la captura, identifica un dispositivo de red cuyo sistema operativo es `ASIX`, un terminal móvil `Lumia 535`, la IP `50.22.95.9` y, en la sección de credenciales de correo, la contraseña `spring2015` asociada al servidor de correo `pop.gmx.com`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué sistema operativo corre en el host capturado? | `Windows - Windows NT 4` |
| 2 | ¿Cuántos paquetes tiene la captura? | `192` |
| 3 | ¿Qué puerto queda abierto y capturado en el tráfico? | `20769` |
| 4 | ¿Cuál es el nombre del host detectado? | `2AD77400` |
| 5 | ¿Cuántos hosts detecta NetworkMiner en esta captura? | `2` |
| 6 | ¿Qué sistema operativo corre el dispositivo de red ASIX? | `ASIX` |
| 7 | ¿Qué dispositivo móvil aparece en la captura? | `Lumia 535` |
| 8 | ¿Cuál es la dirección IP del equipo Windows? | `50.22.95.9` |
| 9 | ¿Qué contraseña de correo aparece capturada? | `spring2015` |
| 10 | ¿Qué servidor de correo aparece en la captura de credenciales? | `pop.gmx.com` |

### Task 8: Conclusión

**Explicación:** Repaso final de la potencia de NetworkMiner para el análisis pasivo de pcap y su papel en el forense de red y la respuesta a incidentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Buen trabajo! Has completado la sala. | `No answer needed` |

---

**Metodología:** Carga pasiva de cada pcap en NetworkMiner y respuesta guiada a partir de sus pestañas: pestaña general para conteos de frames y paquetes, pestaña "Frames"/filtro por MAC para cruzar IPs contra direcciones MAC, pestaña "Hosts"/"Services" para sistemas operativos, IPs, puertos y versiones, pestaña "Credentials" para extraer usuarios SMB, hashes NTLMv2 y contraseñas de correo, y pestaña de hosts para identificar dispositivos de red y móviles.
**Learning chain:** descargar y abrir el pcap → explorar pestañas de NetworkMiner (Hosts, Services, Credentials, Messages) → correlacionar MAC/IP → extraer credenciales y hashes → identificar hosts, SO, empresas y servicios → responder las preguntas de cada práctica.
**MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web), T1046 (Network Service Discovery), T1033 (System Owner/User Discovery), T1555 (Credentials from Password Stores), T1021.002 (Remote Services: SMB/Windows Admin Shares)
**Fuente:** [TryHackMe - NetworkMiner](https://tryhackme.com/room/networkminer)