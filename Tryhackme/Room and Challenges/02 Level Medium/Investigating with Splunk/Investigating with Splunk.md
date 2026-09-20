# Investigating with Splunk

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `investigatingwithsplunk` |
| **Link** | [TryHackMe](https://tryhackme.com/room/investigatingwithsplunk) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Splunk / Incident Response / Windows Event Logs / Registry / WMIC / net user / Defanging IOCs (URL C2) | **Impacto** | Investiga con Splunk un incidente en el host WORKSTATION6: creación de usuario persistente (A1berto), ejecución vía WMIC, exfiltración por PowerShell y red de mando y control, hasta recuperar el IOC C2 defanged |

---

**Contexto:** Sala práctica de investigación forense con Splunk sobre el host `WORKSTATION6`. A través de los logs de Windows se reconstruye el incidente: un evento inicial (`12256`), la creación del usuario `A1berto` (clave de registro `HKLM\SAM\SAM\Domains\Account\Users\Names\A1berto`), el uso de `WMIC.exe` con `net user /add A1berto paw0rd1`, la conexión de red, el proceso `James.browne`, el evento `79` y finalmente el IOC de C2 defanged: `hxxp[://]10[.]10[.]10[.]5/news[.]php`.

## Solucionario

### Task 1: Investiga el Incidente (Splunk sobre WORKSTATION6)

**Explicación:** Investigación completa del incidente consultando los índices de Splunk del host comprometido. Se responden las 9 preguntas de la cadena de eventos:

1. 1. `12256` — valor inicial/localización del primer evento relevante de la investigación
   2. `A1berto` — usuario creado por el atacante
   3. `HKLM\SAM\SAM\Domains\Account\Users\Names\A1berto` — ruta del registro donde queda persistido el usuario
   4. `Alberto` — valor asociado a la cuenta creada
   5. `C:\windows\System32\Wbem\WMIC.exe" /node:WORKSTATION6 process call create "net user /add A1berto paw0rd1` — comando WMIC de creación del usuario
   6. `0` — código/valor devuelto por la ejecución
   7. `James.browne` — proceso/entidad implicado en la cadena
   8. `79` — evento/hito posterior de la investigación
   9. `hxxp[://]10[.]10[.]10[.]5/news[.]php` — IOC de C2 (defanged)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del primer evento relevante de la investigación? | `12256` |
| 2 | ¿Qué usuario creó el atacante? | `A1berto` |
| 3 | ¿En qué ruta del registro queda persistido el usuario? | `HKLM\SAM\SAM\Domains\Account\Users\Names\A1berto` |
| 4 | ¿Qué nombre/valor usa la cuenta creada? | `Alberto` |
| 5 | ¿Qué comando ejecutó WMIC para crear al usuario? | `C:\windows\System32\Wbem\WMIC.exe" /node:WORKSTATION6 process call create "net user /add A1berto paw0rd1` |
| 6 | ¿Qué código devolvió la ejecución? | `0` |
| 7 | ¿Qué proceso/entidad aparece en la cadena del evento? | `James.browne` |
| 8 | ¿Cuál es el siguiente evento/hito de la investigación? | `79` |
| 9 | ¿Cuál es el IOC de C2 (defanged)? | `hxxp[://]10[.]10[.]10[.]5/news[.]php` |

---

**Metodología:**
1. Consultar los eventos de Splunk del host WORKSTATION6.
2. Localizar el primer hito de la cadena (`12256`).
3. Seguir la creación del usuario `A1berto` y su persistencia en registro.
4. Reconstruir el comando WMIC de creación de cuenta.
5. Continuar la cadena de eventos hasta el proceso `James.browne` y el evento `79`.
6. Recuperar y defangear el IOC de C2 (`hxxp[://]10[.]10[.]10[.]5/news[.]php`).

**Learning chain:** WORKSTATION6 → 12256 → A1berto → HKLM\SAM\...\A1berto → Alberto → WMIC /net user → 0 → James.browne → 79 → C2 `hxxp[://]10[.]10[.]10[.]5/news[.]php`

**Lección:** *Splunk convierte el ruido de eventos en una línea de tiempo investigable: cada respuesta es un eslabón (evento → usuario → registro → comando → red) y el último eslabón, el C2 defanged, es el artefacto que permite pivoteo, blocking y atribución.*

**MITRE ATT&CK:** T1136.001 - Create Account: Local Account (net user /add); T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys; T1047 - Windows Management Instrumentation (WMIC); T1059.001 - Command and Scripting Interpreter: PowerShell; T1071.001 - Application Layer Protocol: Web Protocols (C2 news.php); T1016 - System Network Configuration Discovery

**Fuente:** [TryHackMe - Investigating with Splunk](https://tryhackme.com/room/investigatingwithsplunk)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.