# Forgotten Implant
| **Dificultad** | Medium |
| **Tipo** | CTF (C2 / Red Team) |
| **Slug** | `forgottenimplant` |
| **Link** | [TryHackMe](https://tryhackme.com/room/forgottenimplant) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `forgottenimplant` + walkthrough oficial de Ingo Kleiber y walkthroughs públicos) |
| **Componentes** | Linux, Command & Control (C2), implant, Wireshark, HTTP, Base64, JSON, python-http-server/Flask, jq, phpMyAdmin 4.8.1, LFI/RCE, sudo, PHP, escalada de privilegios |
| **Impacto** | Room CTF con casi nula superficie de ataque: se debe descubrir y hablar el protocolo de un implant C2 "olvidado" que beaconiza hacia el atacante, reconstruir su protocolo (HTTP/Base64/JSON), usarlo para ganar acceso inicial, moverse lateralmente con credenciales almacenadas y escalar a root vía phpMyAdmin y sudo/PHP. |
---
**Contexto:** "Forgotten Implant" es una room tipo CTF en la que la máquina víctima **no expone puertos**, por lo que el escaneo tradicional no revela nada y hay que cambiar de enfoque: asumir que un **implant C2 olvidado** ya está ejecutándose dentro y que intenta *beaconizar* hacia el exterior. Se monitoriza el tráfico con **Wireshark**, se descubre una petición HTTP con un objeto **JSON** codificado en **Base64**, se reconstruye el protocolo cliente-servidor, se levanta una interfaz C2 en Python para hablar con el implant, se obtiene ejecución de comandos, se reutilizan credenciales almacenadas para movimiento lateral y se escala a `root` explotando **phpMyAdmin 4.8.1** (RCE) y **sudo + PHP**.
*EN: "Forgotten Implant" is a CTF-style room where the victim machine **exposes no ports**, so a traditional scan reveals nothing and the approach must change: assume a **forgotten C2 implant** is already running inside and beaconing out. Traffic is monitored with **Wireshark**, an HTTP request carrying a **Base64**-encoded **JSON** object is found, the client-server protocol is reverse engineered, a Python C2 interface is built to talk to the implant, command execution is obtained, stored credentials are reused for lateral movement and privilege is escalated to `root` by exploiting **phpMyAdmin 4.8.1** (RCE) and **sudo + PHP**.*
## Solucionario
### Task 1: Forgotten Implant
**Explicación:** El reconocimiento inicial no muestra puertos abiertos; el indicio está en el tráfico de red saliente del implant hacia el atacante. Se captura con Wireshark/tcpdump una petición HTTP a un servidor controlado, cuyo cuerpo es un **JSON en Base64** con información del host y del último *job* a ejecutar:
```json
{
  "time": "2022-07-14T22:23:01.173978",
  "systeminfo": { "os": "Linux", "hostname": "forgottenimplant" },
  "latest_job": { "job_id": 0, "cmd": "whoami" },
  "success": false
}
```
Comandos habituales:
```bash
rustscan -a <IP> --ulimit 5000 --timeout 5000
# capturar el beacon y decodificar el Base64 (CyberChef / base64 -d) -> JSON con jq
```
El implant habla con un servidor C2 que hay que **suplantar**: se levanta un endpoint HTTP (por ejemplo `python -m http.server`, Flask o `socat`) que devuelva los *jobs* en el formato esperado (JSON/base64) y así se logra **ejecución de comandos** en la víctima. Con una reverse shell se obtiene el **user flag**. A continuación se localizan credenciales almacenadas en archivos de la aplicación (p. ej. `products.py` con usuario/clave de MySQL) que permiten **movimiento lateral**, se explota **phpMyAdmin 4.8.1** para RCE y, con `sudo` sobre PHP, se **escala a root** para leer el flag final (`/root/.root.txt`).
*EN: Initial reconnaissance shows no open ports; the clue lies in the implant's outbound traffic toward the attacker. Wireshark/tcpdump captures an HTTP request to an attacker-controlled server whose body is a **Base64 JSON** with host info and the latest job. The implant talks to a C2 server that must be **impersonated**: an HTTP endpoint is stood up to return jobs in the expected format and **command execution** is achieved. A reverse shell yields the **user flag**. Stored app credentials (e.g. `products.py` with a MySQL user/password) are found for **lateral movement**, **phpMyAdmin 4.8.1** is exploited for RCE and, via `sudo` on PHP, privilege is **escalated to root** to read the final flag.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{902e8e8b1f49dfeb678e419935be23ef}` |
| 2 | What is the root flag? | `THM{7762118e4a93b277cb2fb221745d2cf1}` |
---
**Metodología:** Reconocimiento sin resultados (sin puertos) → captura de tráfico (Wireshark/tcpdump) → identificación del beacon HTTP → decodificación Base64/JSON → ingeniería inversa del protocolo C2 → implementación de un servidor C2 en Python → ejecución de comandos / reverse shell → user flag → recolección de credenciales almacenadas → movimiento lateral → exploit phpMyAdmin 4.8.1 (RCE) → escalada con sudo/PHP → root flag.
**Learning chain:** entender un C2 por dentro (beacon HTTP/Base64/JSON) → suplantar el servidor → convertir el implant en foothold → reutilizar credenciales → RCE en phpMyAdmin → privesc con sudo.
**Lección:** *Un implant "olvidado" que sigue llamando a casa es una puerta abierta: el tráfico de red es evidencia y vector; conocer el protocolo del C2 permite controlar al propio implante, y las credenciales almacenadas convierten un foothold en compromiso total.*
**MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web Protocols), T1041 (Exfiltration Over C2 Channel), T1059 (Command and Scripting Interpreter), T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts), T1548.003 (Sudo and Sudo Caching), T1505.003 (Web Shell).
**Fuente:** [TryHackMe - Forgotten Implant](https://tryhackme.com/room/forgottenimplant)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
