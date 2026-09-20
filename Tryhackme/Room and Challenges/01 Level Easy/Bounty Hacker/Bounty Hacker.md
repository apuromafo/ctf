# Bounty Hacker

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `bountyhacker` | [TryHackMe](https://tryhackme.com/room/bountyhacker) | 01 Level Easy | TryHackMe | FTP / SSH / force brute / cron / sudo | Compromiso inicial vía FTP y SSH, y escalada a root mediante un script de copia de seguridad ejecutado por cron |

---

**Contexto:** Bounty Hacker es una máquina Linux que expone un servicio FTP y SSH. La sala muestra cómo aprovechar el acceso anónimo al FTP para recuperar archivos que contienen el usuario `lin` y su contraseña, acceder por SSH con ella y, finalmente, abusar de un script de copia de seguridad ejecutado por cron para escalar a root y capturar ambas flags.

> **ES:** Máquina Linux con FTP y SSH. Mediante el FTP se obtienen los archivos `lock.txt` y `task.txt`, con el usuario `lin` y la contraseña `RedDr4gonSynd1cat3`. Con SSH se entra y, abusando del cron, se eleva a root.
> **EN:** A Linux box exposing FTP and SSH. Files `lock.txt` and `task.txt` retrieved via FTP reveal user `lin` and password `RedDr4gonSynd1cat3`. SSH access is gained and a cron job is abused to escalate to root.

## Solucionario

### Task 1: Acceso inicial / Initial access
**Explicación:** El escaneo de puertos identifica el FTP y el SSH. Conectando al FTP de forma anónima se descargan los archivos del servicio, que revelan al usuario `lin` y la contraseña que se usa en el servicio SSH. Se captura el user flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué pregunta de enumeración se plantea? | `No answer needed` |
| ¿Qué pregunta de credenciales se plantea? | `No answer needed` |
| ¿Cuál es el nombre de usuario del servicio FTP? | `lin` |
| ¿Qué servicio corre en el puerto 22? | `SSH` |
| ¿Cuál es la contraseña del usuario? | `RedDr4gonSynd1cat3` |
| ¿Cuál es el user flag? | `THM{CR1M3_SyNd1C4T3}` |

### Task 2: Escalada / Privilege escalation
**Explicación:** Dentro del sistema se observa un script de copia de seguridad en `/opt` que se ejecuta periódicamente mediante cron con privilegios de root. Aprovechando esa ejecución se obtiene una shell como root y se captura el root flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el root flag? | `THM{80UN7Y_h4cK3r}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de enumeración | `No answer needed` |
| 2 | Pregunta de credenciales | `No answer needed` |
| 3 | Usuario del servicio FTP | `lin` |
| 4 | Servicio del puerto 22 | `SSH` |
| 5 | Contraseña del usuario | `RedDr4gonSynd1cat3` |
| 6 | User flag | `THM{CR1M3_SyNd1C4T3}` |
| 7 | Root flag | `THM{80UN7Y_h4cK3r}` |

---

**Metodología:** Se escanea la máquina y se identifica el FTP anónimo. Se descargan los archivos del FTP (`lock.txt` y `task.txt`), que revelan las credenciales `lin:RedDr4gonSynd1cat3`. Con ellas se establece una sesión SSH. Enumerando el sistema se encuentra un script de backup ejecutado por cron como root; se modifica o se abusa de su ejecución para obtener una shell como root, con la que se captura el root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> FTP anónimo -> descargar lock.txt/task.txt -> lin:RedDr4gonSynd1cat3 -> SSH -> enum -> script de backup en /opt ejecutado por cron -> shell root -> root flag
```

**Learning chain:** port scanning --> anonymous FTP --> file retrieval --> credential disclosure --> SSH access --> cron job enumeration --> backup script abuse --> root shell --> root flag

**Lección:** *Los servicios expuestos de forma anónima (FTP) y los scripts de sistema ejecutados por cron con privilegios elevados son vectores clásicos de acceso inicial y escalada.*

**MITRE ATT&CK:** T1048 (Exfiltration Over Alternative Protocol) – acceso a FTP, T1078 (Valid Accounts), T1021.004 (Remote Services: SSH), T1053.003 (Scheduled Task/Job: Cron), T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Bounty Hacker](https://tryhackme.com/room/bountyhacker)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.