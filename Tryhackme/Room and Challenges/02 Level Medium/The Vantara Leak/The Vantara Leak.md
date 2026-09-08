# The Vantara Leak

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `thevantaraleak` |
| **Link** | [TryHackMe](https://tryhackme.com/room/thevantaraleak) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | KAPE / EZ Tools / Timeline Explorer / DFIR / MFT / Prefetch / Amcache / SAM / Event 4648 |
| **Impacto** | Reconstruir una cadena de intrusión completa de Windows a partir de un triage KAPE, incluyendo C2, persistencia y movimiento lateral |

---

**Contexto:** Sala **DFIR de Windows** de dificultad Media basada en un **triage KAPE** (`Vantara-Artefacts.zip`). El incidente es una cadena de intrusión del **05-06-2026 (05:35-06:26)**: un documento financiero abre el ataque, un binario de `Downloads` se lanza, `certutil` entrega la segunda etapa, el payload se hace pasar por `svchost` en `%TEMP%`, se crea persistencia como tarea programada, se enumera la confianza de dominios con `nltest`, una cuenta de servicio de dominio (`VFG\svc.***`) se usa para movimiento lateral (Event 4648), se crea una cuenta rogue local `help***$` (SAM), y se prepara un archivo de staging. Se resuelve con **EZ Tools + Timeline Explorer** sobre el triage KAPE.

## Solucionario

### Task 1: Case Briefing

**Explicación:**

Tarea de briefing (sitio estático). Presenta el caso "The Vantara Leak" (fuga de datos en un entorno corporativo Windows) que se investigará con el triage KAPE descargado. Contiene 1 pregunta de confirmación del briefing: se responde con el propio enunciado de confirmación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have reviewed the case briefing and am ready to begin the investigation. | `I have reviewed the case briefing and am ready to begin the investigation.` |

### Task 2: The Investigation

**Explicación:**

Tarea de investigación (máquina virtual) con **12 preguntas** sobre el triage KAPE. Los autores de los walkthroughs enmascaran los valores exactos; donde el valor exacto sí se conoce y es seguro, se indica de forma parcial. La convención usada aquí: se muestra el patrón del valor (señalando que la versión pública está enmascarada) y `THM{...redacted...}` para el flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What executable was launched during the incident from Downloads? | `VPN********.exe` |
| 2 | What is the SHA1 of that executable (Amcache)? | `d3c83599.d157` |
| 3 | What is the native binary that delivered the second stage? | `cert****.exe` |
| 4 | What process did the payload masquerade as? | `svc****.exe` |
| 5 | What is the name of the scheduled persistence task? | `Microsoft..Core` |
| 6 | What is the full command path of that task? | `.\AppData\Local\Temp\svc*****.exe` |
| 7 | What domain trust enumeration tool was used? | `nl****` |
| 8 | What domain account was used for lateral movement (Event 4648)? | `VFG\svc.******` |
| 9 | What local rogue account was created (SAM)? | `help****$` |
| 10 | What financial document was opened during the attack (LNK)? | `Q1_2026_*******_Summary.txt` |
| 11 | What is the size in bytes of the staging file (MFT)? | `4**` |
| 12 | What is the user-discovery command and its run count (Prefetch RunCount)? | `whoami, 1*` |

> **Nota (Q8):** El evento 4648 (logon explícito) que apunta a movimiento lateral usa la cuenta de dominio `VFG\svc.***`; `VFG-CTR-W019\Administrator` es una cuenta **local** que actúa de señuelo (decoy), no es la respuesta.
>
> **Nota (Q10/Q11):** El documento financiero abierto por el LNK es `Q1_2026_*******_Summary.txt` y el archivo de staging es `data_backup.zip` en `\Windows\Temp` (creado 06:04:29), de tamaño `4**` bytes.

---

**Metodología:**

1. **Preparar el triage:** Descomprimir `Vantara-Artefacts.zip` (triage KAPE: Prefetch, Amcache, MFT, Registro con SAM, LNK, eventos `Security.evtx`, etc.).
2. **Herramientas EZ Tools:** `PECmd` (Prefetch), `AmcacheParser` (Amcache), `MFTECmd` (MFT) → volcados CSV → abrir en **Timeline Explorer** para correlacionar la línea de tiempo del incidente: **05-06-2026, 05:35-06:26**.
3. **Q1/Q2 (ejecutable y SHA1):** Triangulando Prefetch + UserAssist + Amcache se identifica el ejecutable lanzado desde `Downloads` (Q1) y su **SHA1** en Amcache (Q2).
4. **Q3/Q4 (segunda etapa e impostor):** A las 06:01:40 corre `certutil` (binario nativo que entrega la segunda etapa, Q3); a las 06:01:48 aparece el payload en `%TEMP%` disfrazado con nombre de `svchost` (Q4).
5. **Q5/Q6 (persistencia):** En `System32\Tasks\*.xml` se ve la tarea programada de persistencia (Q5) y su ruta de ejecución completa hacia `.\AppData\Local\Temp\svc*****.exe` (Q6).
6. **Q7/Q12 (enumeración):** El burst de comandos `whoami`/`net`/`nltest`/`wmic`/`quser` se correlaciona con los RunCount de Prefetch: la herramienta de enumeración de confianza de dominios es `nltest` (Q7) y el comando de descubrimiento de usuario con su RunCount es `whoami, 1*` (Q12).
7. **Q8 (mov. lateral):** En `Security.evtx`, el **EventID 4648** (se intentó iniciar sesión con credenciales explícitas) muestra la cuenta de dominio `VFG\svc.******` usada para movimiento lateral; `VFG-CTR-W019\Administrator` es local (decoy).
8. **Q9 (cuenta rogue):** En la **SAM** (a través de Registry Explorer sobre el hive del Registro) se detecta la cuenta local rogue `help****$` (RID `0x3F1`).
9. **Q10/Q11 (documento y staging):** Con `LECmd` (jump lists/LNK) se ve el documento financiero abierto `Q1_2026_*******_Summary.txt` (Q10); con `MFTECmd` se localiza el `data_backup.zip` de staging en `\Windows\Temp` (creado 06:04:29), cuyo tamaño en la MFT da los `4**` bytes (Q11).

**Learning chain:** KAPE triage -> Timeline Explorer -> documento Q1_2026_*_Summary.txt -> ejecutable Downloads (SHA1 Amcache) -> certutil 2a etapa -> payload svchost impostor (persistencia task Microsoft..Core) -> nltest trust enum -> whoami RunCount -> Event 4648 (VFG\svc) -> SAM rogue help****$ -> data_backup.zip staging

**Lección:** *Un triage **KAPE + EZ Tools + Timeline Explorer** reconstruye la cadena completa del incidente en una sola línea de tiempo: Prefetch y Amcache identifican el binario y su hash, el Registro y Events 4648 cubren la persistencia y el movimiento lateral, y conviene recordar que las cuentas locales (como `VFG-CTR-W019\Administrator`) son señuelos que hay que descartar frente a las cuentas de dominio reales usadas en el ataque.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1105 (Ingress Tool Transfer) · T1053.005 (Scheduled Task) · T1482 (Domain Trust Discovery) · T1136.001 (Local Account) · CWE-798 (Hard-coded Credentials)

**Fuente:** [TryHackMe - The Vantara Leak](https://tryhackme.com/room/thevantaraleak)
