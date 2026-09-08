# Windows Threat Detection 3

| **Dificultad** | Medium |
| **Tipo** | Walkthrough (Premium) |
| **Slug** | `windowsthreatdetection3` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsthreatdetection3) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias (simontaplin.net) |
| **Componentes** | malware C2 / backdoor user / servicios / scheduled tasks / persistencia / Sysmon |
| **Impacto** | Detectar Command and Control (C2) y cómo los hackers mantienen acceso a una máquina Windows: malware C2, backdoors, servicios, tareas programadas y persistencia |

---

**Contexto:** Tercera sala de la serie de detección de amenazas en Windows. Enfoque en C2, backdoor users, servicios, scheduled tasks y persistencia. Se analizan los artefactos de Sysmon (descarga de archivos, procesos, eventos de login) y se ejecutan los malware Troy, Odin y Kitten para obtener las flags.

## Solucionario

### Tarea 1: C2 Malware

**Explicación:**

El archivo sospechoso que descargó el usuario es `URGENT!.zip`. Los atacantes escondieron el malware C2 en `C:\Users\Administrator\AppData\Roaming\update.exe`. El dominio del servidor de Command and Control es `route.m365officesync.workers.dev`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which suspicious archive did the user download? | `URGENT!.zip` |
| 2 | Where did the attackers hide the C2 malware file? | `C:\Users\Administrator\AppData\Roaming\update.exe` |
| 3 | What is the domain of the Command and Control server? | `route.m365officesync.workers.dev` |

### Tarea 2: Backdoor User

**Explicación:**

Revisando la secuencia de eventos de login (Sysmon), hay `6` intentos de inicio de sesión previos antes del acceso del atacante. Tras el acceso exitoso, el atacante creó el usuario backdoor `support` y lo añadió al grupo privilegiado `Administrators`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Number of prior login attempts before the attacker's access (per room sequence). | `6` |
| 2 | After the successful login, which backdoor user did the attacker create? | `support` |
| 3 | Which privileged group was the backdoor user added to? | `Administrators` |

### Tarea 3: Service & Scheduled Task Persistence

**Explicación:**

El servicio de Windows creado para persistir el malware Nessie es `Data Protection Service`. La tarea programada creada para persistir el malware Troy es `AmazonSync`. La flag que se obtiene tras encontrar y ejecutar el malware Troy es `THM{c2_is_on_schedule!}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which Windows service was created to persist the Nessie malware? | `Data Protection Service` |
| 2 | Which scheduled task was created to persist the Troy malware? | `AmazonSync` |
| 3 | What flag do you get after finding and running the Troy malware? | `THM{c2_is_on_schedule!}` |

### Tarea 4: Additional Malware (Odin & Kitten)

**Explicación:**

La imagen del proceso padre del malware "Odin" es `c:\windows\explorer.exe`. La última línea que genera el malware "Odin" es `Done doing bad stuff!`. La flag que se obtiene tras encontrar y ejecutar el malware "Kitten" es `THM{persisting_in_basket!}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the parent process image of the "Odin" malware? | `c:\windows\explorer.exe` |
| 2 | What is the last line that the "Odin" malware outputs? | `Done doing bad stuff!` |
| 3 | What flag do you get after finding and running the "Kitten" malware? | `THM{persisting_in_basket!}` |

### Tarea 5: Theory

**Explicación:**

La mayor amenaza para la mayoría de redes corporativas Windows es `Ransomware`. La etapa en la que es mejor detectar y detener el ataque es `Initial Access`, cuantos antes se detenga mejor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the biggest threat to most corporate Windows networks? | `Ransomware` |
| 2 | At which stage is it best to detect and stop the attack (e.g. Exfiltration)? | `Initial Access` |

---

**Metodología:**

1. Rastrear la descarga del archivo sospechoso (`URGENT!.zip`) y la ubicación del malware C2 en `AppData\Roaming\update.exe`; identificar el dominio C2 en los logs de red.
2. Revisar los eventos de login en Sysmon: contar los intentos previos (6) y detectar la creación del usuario backdoor `support` y su adición a `Administrators`.
3. Buscar servicios y tareas programadas recién creadas (persistencia): `Data Protection Service` (Nessie) y `AmazonSync` (Troy); ejecutar Troy para obtener la flag.
4. Analizar Odin (proceso padre explorer.exe) y Kitten; ejecutarlos para capturar la última línea y la flag de persistencia.
5. Concluir con la teoría sobre la mayor amenaza (ransomware) y la etapa de detección óptima (Initial Access).

**Learning chain:** Sysmon network logs -> URGENT!.zip -> C2 route.m365officesync.workers.dev -> login events (6 intentos) -> backdoor user support -> Administrators -> scheduled task AmazonSync (Troy) -> THM{c2_is_on_schedule!} -> Odin (explorer.exe / Done doing bad stuff!) -> Kitten -> THM{persisting_in_basket!} -> teoría: ransomware + Initial Access

**Lección:** *La persistencia en Windows se consigue mediante backdoors (usuarios, servicios, tareas programadas) y el C2 se mantiene vía scripts/workers de nube; detectarlo en las primeras fases (Initial Access) es clave para contener la cadena antes de que el ransomware se despliegue.*

**MITRE ATT&CK:** T1071 (C2) · T1136.001 (Create Account: Local Account) · T1543.003 (Create or Modify System Process: Windows Service) · T1053.005 (Scheduled Task) · T1547 (Boot or Logon Autostart Execution) · CWE-732 (Incorrect Permission Assignment)

**Fuente:** [TryHackMe - Windows Threat Detection 3](https://tryhackme.com/room/windowsthreatdetection3)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
