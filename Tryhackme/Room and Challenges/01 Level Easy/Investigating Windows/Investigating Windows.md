# Investigating Windows

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough / máquina | `investigatingwindows` | [TryHackMe](https://tryhackme.com/room/investigatingwindows) | 01 Level Easy | TryHackMe | Windows Server, logins, eventos, Mimikatz, C2, persistencia, netstat, política de contraseñas | Investigar un Windows comprometido: reconstruir el acceso inicial, los usuarios implicados y la actividad del atacante a partir del sistema. |

---

**Contexto:** Sala de investigación forense sobre un sistema Windows que ha sido comprometido. Se examinan aspectos del sistema operativo en uso, la sesión de usuario, la configuración de red, los usuarios locales, el sistema de archivos, los procesos sospechosos y los mecanismos de persistencia. Las preguntas llevan a identificar un archivo de PowerShell malicioso, un PID concreto, la política de contraseñas, fechas de instalación y acceso, la presencia de herramientas de robo de credenciales como Mimikatz, la IP del atacante y la comunicación de tipo C2. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Recorrer la máquina comprometida: sistema, usuario, red, cuentas, procesos y eventos, identificar el malware y la herramienta de credenciales, la IP de origen y la comunicación hacia el C2.
> **EN:** Walk through the compromised box: system, user, network, accounts, processes and events, identify the malware and the credential tool, the source IP and the C2 communication.

## Solucionario

### Task 1: Sistema operativo / Operating System
**Explicación:** Se identifica la versión concreta de Windows Server que aloja la máquina.

1. Windows Server 2016

### Task 2: Sesión iniciada / Logged-on User
**Explicación:** Se determina la cuenta de usuario con la sesión iniciada en el sistema.

1. Administrator

### Task 3: Fecha y hora de cambio / Last Change Date
**Explicación:** Se obtiene la fecha y hora exactas del último cambio de la contraseña.

1. 03/02/2019 5:48:32 PM

### Task 4: Dirección IP del servidor / Server IP Address
**Explicación:** Se localiza la IP del servidor dentro de la configuración de red.

1. 10.34.2.3

### Task 5: Cuentas de usuario / User Accounts
**Explicación:** Se listan las cuentas de usuario existentes en el sistema.

1. Guest, Jenny

### Task 6: Sistema de archivos / File System
**Explicación:** Se determina qué utilidad de comprobación del sistema de archivos se ha ejecutado.

1. Clean file system

### Task 7: Archivo sospechoso / Suspicious File
**Explicación:** Se identifica un archivo de script que llama la atención durante el análisis.

1. nc.ps1

### Task 8: Proceso en ejecución / Running Process
**Explicación:** Se localiza el PID de un proceso relacionado con la actividad maliciosa.

1. 1348

### Task 9: Política de contraseñas / Password Policy
**Explicación:** Se consulta la política de caducidad de las contraseñas del equipo.

1. Never

### Task 10: Fecha de instalación / Installation Date
**Explicación:** Se averigua cuándo se instaló el sistema operativo en la máquina.

1. 03/02/2019

### Task 11: Último acceso / Last Access Time
**Explicación:** Se registra la hora exacta del último acceso a un elemento relevante del sistema.

1. 03/02/2019 4:04:49 PM

### Task 12: Herramienta de credenciales / Credential Dumping Tool
**Explicación:** Se detecta la herramienta conocida por robar credenciales de memoria presente en el sistema.

1. Mimikatz

### Task 13: IP del atacante / Attacker IP
**Explicación:** Se identifica la dirección IP desde la que se ha producido el ataque.

1. 76.32.97.132

### Task 14: Extensión de archivo / File Extension
**Explicación:** Se determina la extensión utilizada por el archivo malicioso desplegado.

1. .jsp

### Task 15: Puerto de escucha / Listening Port
**Explicación:** Se identifica el puerto usado para la comunicación maliciosa.

1. 1337

### Task 16: Comunicación C2 / C2 Communication
**Explicación:** Se detecta el dominio de control y comando con el que comunicaba el malware.

1. google.com

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Versión del sistema operativo / Operating system version | `Windows Server 2016` |
| 2 | Usuario con sesión iniciada / Logged-on user | `Administrator` |
| 3 | Fecha y hora del último cambio / Last change date | `03/02/2019 5:48:32 PM` |
| 4 | Dirección IP del servidor / Server IP address | `10.34.2.3` |
| 5 | Cuentas de usuario / User accounts | `Guest, Jenny` |
| 6 | Utilidad del sistema de archivos / File system utility | `Clean file system` |
| 7 | Archivo sospechoso / Suspicious file | `nc.ps1` |
| 8 | PID del proceso / Process PID | `1348` |
| 9 | Política de caducidad de contraseñas / Password expiry policy | `Never` |
| 10 | Fecha de instalación / Installation date | `03/02/2019` |
| 11 | Último acceso / Last access | `03/02/2019 4:04:49 PM` |
| 12 | Herramienta de credenciales / Credential tool | `Mimikatz` |
| 13 | IP del atacante / Attacker IP | `76.32.97.132` |
| 14 | Extensión del archivo malicioso / Malicious file extension | `.jsp` |
| 15 | Puerto de escucha / Listening port | `1337` |
| 16 | Dominio C2 / C2 domain | `google.com` |

---

**Metodología:** Examinar el sistema y su configuración (versión, red, cuentas, política), revisar archivos y procesos sospechosos, consultar eventos y fechas de instalación/acceso, detectar herramientas de robo de credenciales y reconstruir la actividad del atacante (IP origen, extensión, puerto y C2).

### Cadena de ataque / Attack Chain

```text
acceso inicial -> usuario Administrator -> despliegue de nc.ps1 y .jsp -> proceso 1348 en puerto 1337 -> Mimikatz -> exfiltración hacia google.com (C2) desde 76.32.97.132
```

**Learning chain:** Windows Server -> logins y eventos -> cuentas y política de contraseñas -> archivos/procesos sospechosos -> robo de credenciales (Mimikatz) -> C2 y exfiltración.

**Lección:** *La investigación de un Windows comprometido es una reconstrucción en capas: sistema, cuentas, procesos, credenciales y C2; cruzar fechas, PIDs y conexiones permite recuperar toda la cadena del ataque.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1003 (OS Credential Dumping), T1078 (Valid Accounts), T1036 (Masquerading), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Investigating Windows](https://tryhackme.com/room/investigatingwindows)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.