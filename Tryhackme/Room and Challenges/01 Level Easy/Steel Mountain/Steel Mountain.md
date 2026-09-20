# Steel Mountain

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `steelmountain` | [TryHackMe](https://tryhackme.com/room/steelmountain) | 01 Level Easy | TryHackMe | Rejetto HTTP File Server, CVE-2014-6287, Metasploit, Windows, PowerShell, rutas sin comillas | Compromiso total de un Windows mediante explotación de Rejetto HFS y escalada de privilegios a SYSTEM |

---

**Contexto:** Sala que compromete una máquina Windows a través del servidor web Rejetto HTTP File Server (HFS) vulnerable a CVE-2014-6287. Tras obtener la flag inicial, se escala a SYSTEM abusando del servicio `AdvancedSystemCareService9` con ruta sin comillas. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Windows exponiendo Rejetto HFS en el puerto 8080. Se explota CVE-2014-6287 con Metasploit, se captura la flag `b04763b6fcf51fcd7c13abc7db4fd365`, se enumera con `powershell -c "Get-Service"` y se escala a SYSTEM por el servicio `AdvancedSystemCareService9`, capturando la flag final `9af5f314f57607c00fd09803a587db80`.
> **EN:** A Windows box exposing Rejetto HFS on port 8080. CVE-2014-6287 is exploited with Metasploit, flag `b04763b6fcf51fcd7c13abc7db4fd365` is captured, services are enumerated with `powershell -c "Get-Service"` and privilege escalation to SYSTEM is achieved through the unquoted service `AdvancedSystemCareService9`, capturing the final flag `9af5f314f57607c00fd09803a587db80`.

## Solucionario

### Task 1: Reconocimiento inicial / Initial Recon

**Explicación:** Se identifica al empleado del mes de la máquina, dato de partida de la sala. Todo el contenido original se conserva verbatim:

1. Bill Harper

### Task 2: Acceso inicial / Initial Access

**Explicación:** Se enumera el servidor web Rejetto HTTP File Server en el puerto 8080, se identifica la vulnerabilidad CVE-2014-6287 y se captura la flag del acceso inicial tras explotarla. Todo el contenido original se conserva verbatim:

2. 1. 8080
   2. Rejetto HTTP File Server
   3. 2014-6287
   4. b04763b6fcf51fcd7c13abc7db4fd365

### Task 3: Escalada de privilegios / Privilege Escalation

**Explicación:** Se abusa del servicio vulnerable `AdvancedSystemCareService9` para escalar privilegios y se captura la flag final de la máquina. Todo el contenido original se conserva verbatim:

3. 1. No answer needed
   2. AdvancedSystemCareService9
   3. No answer needed
   4. 9af5f314f57607c00fd09803a587db80

### Task 4: Explotación y enumeración / Exploitation & Enumeration

**Explicación:** Se utiliza el comando `powershell -c "Get-Service"` para enumerar los servicios del sistema durante la fase de explotación. Todo el contenido original se conserva verbatim:

4. 1. No answer needed
   2. powershell -c "Get-Service"
   3. No answer needed

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Quién es el empleado del mes? / Who is the employee of the month? | `Bill Harper` |
| 2 | Puerto del servidor web / Port of the web server | `8080` |
| 3 | Nombre del servidor web / Name of the web server | `Rejetto HTTP File Server` |
| 4 | CVE de la vulnerabilidad / Vulnerability CVE | `2014-6287` |
| 5 | Flag del acceso inicial / Initial access flag | `b04763b6fcf51fcd7c13abc7db4fd365` |
| 6 | Pregunta informativa de la escalada / Escalation informational question | `No answer needed` |
| 7 | Nombre del servicio vulnerable / Name of the vulnerable service | `AdvancedSystemCareService9` |
| 8 | Pregunta informativa de la escalada / Escalation informational question | `No answer needed` |
| 9 | Flag final de la máquina / Final machine flag | `9af5f314f57607c00fd09803a587db80` |
| 10 | Pregunta informativa de la enum / Enum informational question | `No answer needed` |
| 11 | Comando de enumeración de servicios / Command to enumerate services | `powershell -c "Get-Service"` |
| 12 | Pregunta informativa de la enum / Enum informational question | `No answer needed` |

---

**Metodología:** Escaneo de la máquina → identificación de Rejetto HTTP File Server en el puerto 8080 → explotación de CVE-2014-6287 con Metasploit → obtención de shell y flag inicial → enumeración de servicios con PowerShell → abuso de la ruta sin comillas de `AdvancedSystemCareService9` → escalada a SYSTEM → flag final.

### Cadena de ataque / Attack Chain

```text
nmap -> puerto 8080 -> Rejetto HTTP File Server -> CVE-2014-6287 -> exploit -> shell -> flag b04763b6fcf51fcd7c13abc7db4fd365 -> powershell -c "Get-Service" -> AdvancedSystemCareService9 (ruta sin comillas) -> escalada a SYSTEM -> flag 9af5f314f57607c00fd09803a587db80
```

**Learning chain:** port scanning --> Rejetto HFS --> CVE-2014-6287 --> Metasploit exploit --> initial shell --> initial flag --> service enumeration via PowerShell --> unquoted service path --> privilege escalation to SYSTEM --> final flag

**Lección:** *El servidor Rejetto HFS vulnerable a CVE-2014-6287 y los servicios Windows con rutas sin comillas son vectores clásicos para obtener ejecución remota y escalar a SYSTEM.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1210 (Exploitation of Remote Services), T1059.001 (Command and Scripting Interpreter: PowerShell), T1574.009 (Hijack Execution Flow: Path Interception by Unquoted Path), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Steel Mountain](https://tryhackme.com/room/steelmountain)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.