# Snort Challenge - Live Attacks
| **Dificultad** | Medium |
| **Tipo** | Challenge / Walkthrough |
| **Slug** | `snortchallengeliveattacks` |
| **Link** | [TryHackMe](https://tryhackme.com/room/snortchallengeliveattacks) |
| **Sección** | Blue Team / Network Security / IDS-IPS |
| **Fuente** | TryHackMe |
| **Componentes** | Snort, IDS, detección de ataques, SSH, Metasploit, reglas Snort, tráfico en vivo |
| **Impacto** | Aplicación práctica de Snort para detectar ataques en vivo: fuerza bruta SSH y una reverse shell de Metasploit, identificando protocolos, puertos y escribiendo reglas de detección. |
---
**Contexto:** Reto práctico de Snort centrado en la detección de ataques en tiempo real ("live attacks"). Los escenarios incluyen una campaña de fuerza bruta contra SSH y la ejecución de un payload de Metasploit que establece una reverse shell. El objetivo es identificar el protocolo/puerto del ataque, escribir reglas Snort que lo detecten y extraer las flags asociadas a cada escenario.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación del escenario de ataques en vivo y de la metodología de trabajo con Snort. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: SSH Brute Force / Fuerza bruta SSH
**Explicación:** Detección de un ataque de fuerza bruta contra SSH. Se identifica el protocolo y puerto objetivo (`SSH`, `TCP/22`) y se escribe la regla Snort correspondiente para alertar ante los múltiples intentos de conexión. La flag confirma la detección.
- Protocolo: `SSH`
- Puerto: `TCP/22`
- Flag: `THM{81b7fef657f8aaa6e4e200d616738254}`
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag del escenario de fuerza bruta. | `THM{81b7fef657f8aaa6e4e200d616738254}` |
| 2. What protocol was targeted by the brute force attack? | `SSH` |
| 3. What port was targeted? | `TCP/22` |
### Task 3: Metasploit Reverse Shell / Reverse Shell de Metasploit
**Explicación:** Detección de una reverse shell generada por Metasploit. Se identifica el puerto de la conexión (`tcp/4444`, puerto por defecto de `meterpreter`/handler) y la herramienta utilizada (`Metasploit`), escribiendo la regla Snort para detectar el patrón de la conexión saliente. La flag confirma la detección.
- Puerto: `tcp/4444`
- Herramienta: `Metasploit`
- Flag: `THM{0ead8c494861079b1b74ec2380d2cd24}`
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag del escenario de reverse shell. | `THM{0ead8c494861079b1b74ec2380d2cd24}` |
| 2. What port was used by the reverse shell? | `tcp/4444` |
| 3. What tool generated the reverse shell? | `Metasploit` |
---
**Metodología:** Inspeccionar el tráfico de red con Snort → identificar el patrón del ataque (protocolo, puerto, payload) → escribir la regla de detección → validar la alerta → extraer la flag.
### Cadena de ataque / Attack Chain
```
Fuerza bruta SSH (TCP/22) -> acceso -> Metasploit payload -> reverse shell (tcp/4444) -> detección con reglas Snort
```
**Learning chain:** análisis de tráfico en vivo → identificación de ataques → escritura de reglas → validación de alertas.
**Lección:** *La detección en vivo exige reconocer patrones de ataque (fuerza bruta, reverse shells) y traducirlos a reglas Snort eficaces y de bajo ruido.*
**MITRE ATT&CK:** T1110 (Brute Force), T1021.004 (Remote Services: SSH), T1059 (Command and Scripting Interpreter), T1071 (Application Layer Protocol).
**Fuente:** [TryHackMe - Snort Challenge - Live Attacks](https://tryhackme.com/room/snortchallengeliveattacks)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
