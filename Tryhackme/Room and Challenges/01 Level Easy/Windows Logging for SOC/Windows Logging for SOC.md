# Windows Logging for SOC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `windowsloggingforsoc` | [TryHackMe](https://tryhackme.com/room/windowsloggingforsoc) | 01 Level Easy | TryHackMe | Event Viewer / Security logs / Sysmon / PowerShell History / Event IDs 4624-4625 / 4720 / 4732 / SOC | Análisis de logs y eventos de Windows (Security, Sysmon, PowerShell history) para detección de compromisos en labores de SOC |

---

**Contexto:** Sala del nivel SOC 1 que enseña a usar los registros nativos de Windows para detectar amenazas. Se analiza el archivo `Practice-Security.evtx` (brute force, RDP, creación de usuarios maliciosos), el archivo `Practice-Sysmon.evtx` (descarga de malware, persistencia y C2) y el historial de PowerShell del administrador para reconstruir el compromiso de la máquina THM-PC.

> **ES:** La sala parte de una máquina comprometida (THM-PC) y enseña a triar los logs de Windows: Security (4624/4625, 4720/4732), Sysmon (creación de archivos, red, DNS) e historial de PowerShell, para identificar el ataque completo.
> **EN:** This room uses a compromised host (THM-PC) and teaches triaging Windows logs: Security (4624/4625, 4720/4732), Sysmon (file creation, network, DNS) and PowerShell history, to reconstruct the full attack.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¡Listo para continuar! | `No answer needed` |

### Task 2: Qué se registra / What Is Logged
**Explicación:** Se aprende a distinguir los registros de Windows y los Event IDs clave. Un inicio de sesión correcto en el visor de eventos se identifica con el log `Security` y el Event ID `4624`. Contenido original de la sala (verbatim): `Security / 4624`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Mirando la última captura, ¿qué Event ID describe un inicio de sesión correcto? (Formato: LogSource / ID, p. ej. Application / 8194) | `Security / 4624` |

### Task 3: Registro de seguridad: autenticación / Security Log: Authentication
**Explicación:** Abriendo `Practice-Security.evtx` y filtrando por Event ID 4625 contra THM-PC se identifica la IP que realizó el brute force y, tras el 4624, al usuario comprometido y el Logon ID del RDP malicioso (Logon Type 10). Contenido original de la sala (verbatim): `10.10.53.248`, `Administrator`, `0x183C36D`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Abre el archivo "Practice-Security.evtx" del escritorio de la VM. ¿Qué IP realizó un brute force de THM-PC? | `10.10.53.248` |
| ¿Qué usuario ha sido comprometido como resultado del ataque? | `Administrator` |
| ¿Cuál fue el Logon ID del login RDP malicioso? Nota: el login que buscas tiene Logon Type 10. | `0x183C36D` |

### Task 4: Registro de seguridad: auditoría / Security Log: Auditing
**Explicación:** Continuando con `Practice-Security.evtx`, filtros por el Event ID 4720 (usuario creado) y 4732 (usuario añadido a un grupo) revelan la creación de la cuenta backdoor `svc_sysrestore` y su inclusión en los grupos privilegiados Backups Operators y Remote Desktop Users. Contenido original de la sala (verbatim): `svc_sysrestore`, `Backup Operators, Remote Desktop Users`, `Yea`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué usuario fue creado por el atacante poco después del login RDP? | `svc_sysrestore` |
| ¿A qué dos grupos privilegiados se añadió el usuario backdoor? (Respuesta en orden alfabético) | `Backup Operators, Remote Desktop Users` |
| ¿Es un evento raro para THM-PC? (Yea/Nay) | `Yea` |

### Task 5: Sysmon: malware / Sysmon: Malware
**Explicación:** Se trabaja con `Practice-Sysmon.evtx` para identificar la descarga del malware: `Google Chrome` es el proceso que descargó el binario, cuya ruta es `C:\Users\sarah.miller\Downloads\ckjg.exe`, y el Event ID 15 de Sysmon revela la URL de descarga. Contenido original de la sala (verbatim): `Google Chrome`, `C:\Users\sarah.miller\Downloads\ckjg.exe`, `http://gettsveriff.com/bgj3/ckjg.exe`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué proceso descargó el malware? | `Google Chrome` |
| ¿Cuál es la ruta completa del malware en Downloads? | `C:\Users\sarah.miller\Downloads\ckjg.exe` |
| ¿De qué URL se descargó el archivo? Nota: ¡Usa otros eventos de Sysmon para averiguarlo! | `http://gettsveriff.com/bgj3/ckjg.exe` |

### Task 6: Sysmon: archivos y red / Sysmon: Files and Network
**Explicación:** Se rastrea la persistencia del malware y su C2. El archivo de persistencia creado en Startup es `DeleteApp.url`, el servidor de mando y control al que se conecta es `193.46.217.4:7777` y el dominio asociado es `hkfasfsafg.click`. Contenido original de la sala (verbatim): `C:\Users\sarah.miller\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\DeleteApp.url`, `193.46.217.4:7777`, `hkfasfsafg.click`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué archivo creó el malware descargado para persistir en el host? | `C:\Users\sarah.miller\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\DeleteApp.url` |
| ¿A qué servidor de Comando y Control se conectó el malware? (Formato IP:Puerto) | `193.46.217.4:7777` |
| Por último, ¿qué dominio corresponde a la IP maliciosa? | `hkfasfsafg.click` |

### Task 7: Registro de PowerShell / PowerShell Logging
**Explicación:** Se revisa el historial de PowerShell de otros usuarios locales. El primer comando ejecutado por el Administrador fue `Get-ComputerInfo` el `May 18, 2025`, y en el historial de otro usuario se encuentra la flag `THM{it_was_me!}`. Contenido original de la sala (verbatim): `Get-ComputerInfo`, `May 18, 2025`, `THM{it_was_me!}`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Revisa el historial de PS del Administrador en la VM adjunta. ¿Qué comando de PowerShell se ejecutó primero? | `Get-ComputerInfo` |
| ¿Cuándo ejecutó el Administrador el primer comando de PS? | `May 18, 2025` |
| ¿Puedes encontrar la flag almacenada en el historial de PS? (Formato: THM{...}) Nota: ¡Revisa también el historial de otros usuarios locales! | `THM{it_was_me!}` |

### Task 8: Conclusión / Conclusion
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para seguir? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Listo para continuar! | `No answer needed` |
| 2 | Event ID de un inicio de sesión correcto | `Security / 4624` |
| 3 | IP que realizó el brute force de THM-PC | `10.10.53.248` |
| 4 | Usuario comprometido tras el ataque | `Administrator` |
| 5 | Logon ID del login RDP malicioso | `0x183C36D` |
| 6 | Usuario backdoor creado por el atacante | `svc_sysrestore` |
| 7 | Grupos privilegiados del usuario backdoor | `Backup Operators, Remote Desktop Users` |
| 8 | ¿Evento raro para THM-PC? | `Yea` |
| 9 | Proceso que descargó el malware | `Google Chrome` |
| 10 | Ruta completa del malware en Downloads | `C:\Users\sarah.miller\Downloads\ckjg.exe` |
| 11 | URL de descarga del malware | `http://gettsveriff.com/bgj3/ckjg.exe` |
| 12 | Archivo de persistencia en Startup | `C:\Users\sarah.miller\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\DeleteApp.url` |
| 13 | Servidor C2 al que se conectó el malware | `193.46.217.4:7777` |
| 14 | Dominio de la IP maliciosa | `hkfasfsafg.click` |
| 15 | Primer comando PS del Administrador | `Get-ComputerInfo` |
| 16 | Fecha del primer comando PS | `May 18, 2025` |
| 17 | Flag en el historial de PowerShell | `THM{it_was_me!}` |
| 18 | ¿Preparado para seguir? | `No answer needed` |

---

**Metodología:** Se trían los registros de la máquina comprometida con el Visor de Eventos: filtros por Event ID 4625 (fallos de autenticación) para detectar el brute force de THM-PC, Event ID 4624 con Logon Type 10 para el RDP malicioso, Event ID 4720/4732 para la creación de la cuenta backdoor, eventos de Sysmon (descarga, persistencia y conexiones de red) para el malware y, por último, el historial de PowerShell para localizar la flag.

### Cadena de ataque / Attack Chain

```text
Brute force RDP (10.10.53.248) -> 4624 Logon Type 10 (0x183C36D, Administrator) -> 4720 cuenta svc_sysrestore -> 4732 Backup Operators / Remote Desktop Users -> ckjg.exe descargado por Google Chrome -> persistencia DeleteApp.url (Startup) -> C2 193.46.217.4:7777 (hkfasfsafg.click) -> PS history Get-ComputerInfo (May 18, 2025) -> THM{it_was_me!}
```

**Learning chain:** Windows logging basics --> Event Viewer --> Security log (4625 brute force, 4624 RDP) --> account creation (4720/4732) --> Sysmon (file creation, network, DNS) --> persistence (Startup) --> C2 traffic --> PowerShell History --> SOC triage --> flag

**Lección:** *El registro de eventos de Windows (Security, Sysmon y PSHistory) es la fuente principal del SOC para reconstruir un compromiso: correlacionar 4625/4624, la creación de cuentas y la telemetría de red permite detectar brute force, persistencia y C2.*

**MITRE ATT&CK:** T1078 (Valid Accounts) / T1136 (Create Account)

**Fuente:** [TryHackMe - Windows Logging for SOC](https://tryhackme.com/room/windowsloggingforsoc)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.