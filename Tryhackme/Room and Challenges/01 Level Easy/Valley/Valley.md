# Valley

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `valley` | [TryHackMe](https://tryhackme.com/room/valley) | 01 Level Easy | THM | Enumeración web, revisión de código fuente, credenciales hardcodeadas, FTP, análisis de PCAP, reutilización de contraseñas, escalada de privilegios, Python library hijacking, cron | Resolución completa del reto |

---

**Contexto:** Reto Linux y web que encadena varias debilidades pequeñas: una zona de desarrollo expuesta, credenciales hardcodeadas en JavaScript del lado cliente, acceso FTP con credenciales reutilizadas, capturas de paquetes (PCAP) con credenciales reutilizadas, reutilización débil de contraseñas entre servicios y usuarios locales, y un cron de root que ejecuta Python. La escalada final explota un archivo de la librería Python (/usr/lib/python3.8/base64.py) escribible que root importa posteriormente (Python library hijacking), culminando en una bash SUID.

> **ES:** Box CTF: enumeración web → zona de desarrollo expuesta → credenciales hardcodeadas en JavaScript → FTP con credenciales reutilizadas → análisis de PCAP → SSH valleyDev → pcap pistas → binario valleyAuthenticator → clave liberty123 → su valley → biblioteca Python escribible → cron de root → hijacking de base64.py → bash SUID → root flag.
> **EN:** CTF box: web enumeration → exposed dev area → credentials hardcoded in client-side JavaScript → FTP with reused credentials → PCAP analysis → SSH valleyDev → pcap clues → valleyAuthenticator binary → liberty123 key → su valley → writable Python library → root cron → base64.py hijacking → SUID bash → root flag.

## Solucionario

### Task 1: Compromete la máquina / Compromise the machine

**Explicación:** Se enumeran los puertos (22 SSH, 80 HTTP, 37370 FTP), se descubre la zona de desarrollo web, se recuperan credenciales hardcodeadas en JavaScript y se usa FTP con credenciales reutilizadas. Un análisis de capturas de paquetes (PCAP) expone credenciales de SSH; con valleDev se obtiene el user flag. El binario /home/valleyAuthenticator revela la clave liberty123, permitiendo su valley. El cron de root `python3 /photos/script/photosEncrypt.py` importa /usr/lib/python3.8/base64.py, que se modifica (hijacking) para que root genere una bash con SUID y así obtener el root flag. El contenido original del reto, conservado íntegramente, es el siguiente:

1. `THM{k@l1_1n_th3_v@lley}`
2. `THM{v@lley_0f_th3_sh@d0w_0f_pr1v3sc}`

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the user flag? | `THM{k@l1_1n_th3_v@lley}` |
| 2 | What is the root flag? | `THM{v@lley_0f_th3_sh@d0w_0f_pr1v3sc}` |

---

**Metodología:** nmap (22/80/37370) → descubrimiento de /pricing, /gallery y /static → credenciales hardcodeadas en JS → FTP con credenciales reutilizadas → descarga y análisis de PCAP → credenciales de SSH → acceso como valleyDev → user flag → enumeración de /home (valleyAuthenticator) → strings del binario → liberty123 → su valley → análisis del cron de root → modificación de /usr/lib/python3.8/base64.py → ejecución de photosEncrypt.py por cron → bash SUID → root flag.

### Cadena de ataque / Attack Chain

Enumeración web (dev area) → credenciales hardcodeadas (JavaScript) → FTP (credenciales reutilizadas) → análisis de PCAP → SSH valleyDev → user.txt → binario valleyAuthenticator → liberty123 → su valley → cron root (photosEncrypt.py) → hijacking de base64.py → bash SUID (/tmp/bash -p) → root flag

**Learning chain:** Web enumeration → source code review → hardcoded credentials → FTP → PCAP analysis → credential reuse → SSH → user flag → binary analysis (strings) → lateral move → writable Python library → cron job → library hijacking → SUID bash → root flag

**Lección:** *Las pistas están repartidas en sitios insospechados (JS, FTP, capturas de red) y la reutilización de contraseñas permite ir encadenando accesos; una carpeta de librería Python escribible combinada con un cron de root convierte un simple archivo modificable en la puerta hacia root.*

**MITRE ATT&CK:** T1592 (Gather Victim Host Information), T1087 (Account Discovery), T1078 (Valid Accounts), T1110.001 (Password Guessing), T1555 (Credentials from Password Stores), T1572 (Protocol Tunneling), T1053.003 (Cron), T1574 (Hijack Execution Flow), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Valley](https://tryhackme.com/room/valley)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.