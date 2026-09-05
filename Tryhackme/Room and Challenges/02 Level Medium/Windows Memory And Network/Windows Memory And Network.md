# Windows Memory & Network [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough
* **Slug:** `windowsmemoryandnetwork`
* **Link:** https://tryhackme.com/room/windowsmemoryandnetwork
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** TryHackMyOffsecBox/TryHackMe-CN (GitHub/Docusaurus), tryhackme.com/room/windowsmemoryandnetwork

## Solucionario de Tareas / Task Solutions

> **ES:** Sala DFIR (Premium) y última de un set de tres. Analiza el tráfico de red y el comportamiento post-explotación capturado en RAM a partir del mismo volcado `THM-WIN-001_071528_07052025.mem`. Se identifican conexiones activas con `windows.netscan`, el C2 del atacante (10.0.0.129:8081), la persistencia vía carpeta Startup (windows-update.exe escuchando en 4443) y el movimiento lateral vía SSH hacia 192.168.0.30.
> **EN:** A DFIR Premium room and the last of a set of three. It analyzes network traffic and post-exploitation behavior captured in RAM from the same dump `THM-WIN-001_071528_07052025.mem`. Active connections are identified with `windows.netscan`, the attacker's C2 (10.0.0.129:8081), persistence via the Startup folder (windows-update.exe listening on 4443), and lateral movement via SSH to 192.168.0.30.

### Task 1 - Introduction

> **ES:** Objetivos: identificar conexiones de red en el volcado, puertos/endpoints sospechosos, vincular conexiones a procesos, detectar reverse shells e inyecciones de memoria, y trazar la actividad PowerShell/C2.
> **EN:** Objectives: identify network connections in the dump, suspicious ports/endpoints, link connections to processes, detect reverse shells and memory injections, and trace PowerShell/C2 activity.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Click to continue to the room | No answer needed |

### Task 2 - Scenario Information

> **ES:** Mismo incidente THM-0001 en TryHatMe. Host `WIN-001` (Windows 10 22H2, 10.0.19045). Volcado `THM-WIN-001_071528_07052025.dmp` con MD5 `78535fc49ab54fed57919255709ae650`.
> **EN:** Same incident THM-0001 at TryHatMe. Host `WIN-001` (Windows 10 22H2, 10.0.19045). Dump `THM-WIN-001_071528_07052025.dmp` with MD5 `78535fc49ab54fed57919255709ae650`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I went through the case details and am ready to find out more | No answer needed |

### Task 3 - Environment & Setup

> **ES:** Arrancar la VM; el volcado está en `/home/ubuntu` y se analiza con `vol`.
> **EN:** Start the VM; the dump is in `/home/ubuntu` and analyzed with `vol`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Click here if you were able to start your environment | No answer needed |

### Task 4 - Analyzing Active Connections

> **ES:** Se usa `vol -f THM-WIN-001_071528_07052025.mem windows.netscan` para escanear sockets TCP/UDP en memoria (aunque ya estén cerrados). Se detectan: `updater.exe` (PID 10032) conectado a `10.0.0.129:8081` (C2 del atacante) usando el puerto local 55985 con protocolo TCP; `windows-update.exe` (PID 10084) escuchando en el puerto 4443 y con conexión establecida a `10.0.0.129:47982`; y `powershell.exe` (PID 6984) conectándose a `192.168.0.30:22` (movimiento lateral). El orden de establecimiento de las conexiones salientes es: windows-update, updater, powershell.
> **EN:** Use `vol -f THM-WIN-001_071528_07052025.mem windows.netscan` to scan TCP/UDP sockets in memory (even if already closed). Detected: `updater.exe` (PID 10032) connected to `10.0.0.129:8081` (attacker C2) using local port 55985 over TCP; `windows-update.exe` (PID 10084) listening on port 4443 with an established connection to `10.0.0.129:47982`; and `powershell.exe` (PID 6984) connecting to `192.168.0.30:22` (lateral movement). The order in which outbound connections were established is: windows-update, updater, powershell.

```
vol -f THM-WIN-001_071528_07052025.mem windows.netscan > netscan.txt
cat netscan.txt | grep LISTENING
vol -f THM-WIN-001_071528_07052025.mem windows.netstat
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the remote source port number used in the connection between 192.168.1.192 and 10.0.0.129:8081? | `8081` |
| Which internal IP address received a connection on port 22 from the compromised host? | `192.168.0.30` |
| What is the exact timestamp when the connection from the IP addresses in question 1 was established? | `THM{...redacted...}` |
| What is the local port used by the system to initiate the SSH connection to 192.168.0.30? | `THM{...redacted...}` |
| What is the protocol used in the connection from 192.168.1.192:55985 to 10.0.0.129:8081? | `TCP` |
| What is the order in which the potential malicious processes established outbound connections? | `windows-update, updater, powershell` |

### Task 5 - Investigating Remote Access and C2 Communications

> **ES:** Profundiza en la comunicación con la infraestructura del atacante. `updater.exe` mantiene la sesión C2 hacia `10.0.0.129:8081`; `windows-update.exe` (persistido en la carpeta Startup) actúa como listener en `4443` para recibir instrucciones/payloads. Se compara con `windows.netstat` para validar qué conexiones seguían activas en el momento de la captura.
> **EN:** Dives deeper into communication with the attacker's infrastructure. `updater.exe` maintains the C2 session to `10.0.0.129:8081`; `windows-update.exe` (persisted in the Startup folder) acts as a listener on `4443` to receive instructions/payloads. `windows.netstat` is compared to validate which connections were still active at capture time.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue with the analysis of the C2 communications | `THM{...redacted...}` |

### Task 6 - Post-Exploitation Communication

> **ES:** Se rastrea la comunicación post-explotación: `powershell.exe` (PID 6984) conecta a `192.168.0.30:22`, indicando movimiento lateral hacia el siguiente objetivo interno mediante SSH. Se correlaciona la cadena de procesos con las conexiones de red para cerrar la línea de tiempo del ataque.
> **EN:** Post-exploitation communication is traced: `powershell.exe` (PID 6984) connects to `192.168.0.30:22`, indicating lateral movement to the next internal target via SSH. The process chain is correlated with the network connections to close the attack timeline.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue with the post-exploitation analysis | `THM{...redacted...}` |

### Task 7 - Putting it All Together

> **ES:** Se combina la información de las salas anteriores (procesos y actividad de usuario) con las conexiones de red para reconstruir la cadena completa: macro → pdfupdater → windows-update (C2 10.0.0.129:8081/4443) → powershell (SSH a 192.168.0.30).
> **EN:** Information from the previous rooms (processes and user activity) is combined with network connections to reconstruct the full chain: macro → pdfupdater → windows-update (C2 10.0.0.129:8081/4443) → powershell (SSH to 192.168.0.30).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue with the full reconstruction | `THM{...redacted...}` |

### Task 8 - Conclusion

> **ES:** Cierre de la sala y del módulo de análisis de memoria: la red y el comportamiento post-explotación quedan capturados en RAM y se reconstruyen con Volatility 3.
> **EN:** Closing of the room and of the memory analysis module: network and post-exploitation behavior are captured in RAM and reconstructed with Volatility 3.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Click to complete the room | No answer needed |

## Metodología / Methodology

1. **Paso / Step - Escaneo de red:** Ejecuta `windows.netscan` para enumerar sockets TCP/UDP en memoria aunque estén cerrados.
2. **Paso / Step - Filtrar listening:** Con `grep LISTENING` identifica puertos no estándar; `windows-update.exe` escucha en el 4443 (anómalo).
3. **Paso / Step - Identificar C2:** Observa `updater.exe` con conexión ESTABLISHED hacia `10.0.0.129:8081` (puerto local 55985, protocolo TCP) = infraestructura del atacante.
4. **Paso / Step - Movimiento lateral:** Detecta `powershell.exe` conectándose a `192.168.0.30:22` (SSH), el siguiente objetivo interno.
5. **Paso / Step - Orden de las conexiones:** Ordena por timestamp de creación: windows-update (07:13:35), updater, powershell (07:15:15).
6. **Paso / Step - Validación cruzada:** Usa `windows.netstat` para confirmar qué conexiones seguían activas en la captura.
7. **Paso / Step - Correlación:** Une procesos, actividad de usuario y red para reconstruir la cadena completa del ataque.

### Cadena de ataque / Attack Chain

```
cv-resume-test.docm ──> pdfupdater.exe ──> windows-update.exe ──> updater.exe
                                   │  persistencia (Startup)           │ C2
                                   │  escucha 4443                     ▼
                                   └──────────────────────> 10.0.0.129:8081 (atacante)
                                                                        │
                                                            powershell.exe
                                                                        │ SSH :22
                                                                        ▼
                                                                192.168.0.30 (siguiente objetivo)
```

**Lección:** El tráfico C2, la persistencia (Startup) y el movimiento lateral dejan huellas fiables en RAM que `windows.netscan`/`windows.netstat` permiten recuperar y vincular a procesos concretos, cerrando la línea de tiempo del incidente sin depender de capturas de red en vivo.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
