# The Vantara Leak [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF
* **Slug:** `thevantaraleak`
* **Link:** https://tryhackme.com/room/thevantaraleak
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=thevantaraleak` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala **DFIR de Windows** de dificultad Media basada en un **triage KAPE** (`Vantara-Artefacts.zip`). El incidente es una cadena de intrusión del **05-06-2026 (05:35–06:26)**: un documento financiero abre el ataque, un binario de `Downloads` se lanza, `certutil` entrega la segunda etapa, el payload se hace pasar por `svchost` en `%TEMP%`, se crea persistencia como tarea programada, se enumera la confianza de dominios con `nltest`, una cuenta de servicio de dominio (`VFG\svc.***`) se usa para movimiento lateral (Event 4648), se crea una cuenta rogue local `help***$` (SAM), y se prepara un archivo de staging. Se resuelve con **EZ Tools + Timeline Explorer** sobre el triage KAPE.
> **EN:** **Windows DFIR** room of Medium difficulty built on a **KAPE triage** (`Vantara-Artefacts.zip`). The incident is an intrusion chain from **05-06-2026 (05:35–06:26)**: a financial document opens the attack, a binary from Downloads is launched, `certutil` delivers the second stage, the payload masquerades as `svchost` in `%TEMP%`, persistence is created as a scheduled task, domain trust is enumerated with `nltest`, a domain service account (`VFG\svc.***`) is used for lateral movement (Event 4648), a rogue local account `help***$` is created (SAM), and a staging file is prepared. Solved with **EZ Tools + Timeline Explorer** over the KAPE triage.

### Task 1 - Case Briefing

> **ES:** Tarea de briefing (sitio estático). Presenta el caso "The Vantara Leak" (fuga de datos en un entorno corporativo Windows) que se investigará con el triage KAPE descargado. Contiene 1 pregunta de confirmación del briefing: se responde con el propio enunciado de confirmación.
> **EN:** Briefing task (static site). Presents the "The Vantara Leak" case (data leak in a corporate Windows environment) to be investigated with the downloaded KAPE triage. It has 1 briefing confirmation question: answered with the confirmation statement itself.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I have reviewed the case briefing and am ready to begin the investigation. | `I have reviewed the case briefing and am ready to begin the investigation.` |

### Task 2 - The Investigation

> **ES:** Tarea de investigación (máquina virtual) con **12 preguntas** sobre el triage KAPE. Los autores de los walkthroughs enmascaran los valores exactos; donde el valor exacto SÍ se conoce y es seguro, se indica de forma parcial. La convención usada aquí: se muestra el patrón del valor (señalando que la versión pública está enmascarada) y `THM{...redacted...}` para el flag.
> **EN:** Investigation task (VM) with **12 questions** over the KAPE triage. Walkthrough authors mask the exact values; where the exact value IS known and safe, it is shown partially. Convention used here: the value pattern is shown (noting the public version is masked) and `THM{...redacted...}` for the flag.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What executable was launched during the incident from Downloads? | `VPN********.exe` |
| What is the SHA1 of that executable (Amcache)? | `d3c83599…d157` |
| What is the native binary that delivered the second stage? | `cert****.exe` |
| What process did the payload masquerade as? | `svc****.exe` |
| What is the name of the scheduled persistence task? | `Microsoft……Core` |
| What is the full command path of that task? | `…\AppData\Local\Temp\svc*****.exe` |
| What domain trust enumeration tool was used? | `nl****` |
| What domain account was used for lateral movement (Event 4648)? | `VFG\svc.******` |
| What local rogue account was created (SAM)? | `help****$` |
| What financial document was opened during the attack (LNK)? | `Q1_2026_*******_Summary.txt` |
| What is the size in bytes of the staging file (MFT)? | `4**` |
| What is the user-discovery command and its run count (Prefetch RunCount)? | `whoami, 1*` |

> **Nota / Note (Q8):** El evento 4648 (logon explícito) que apunta a movimiento lateral usa la cuenta de dominio **`VFG\svc.***`**; `VFG-CTR-W019\Administrator` es una cuenta **local** que actúa de señuelo (decoy), no es la respuesta.
> **EN (Q8):** The 4648 event (explicit logon) pointing at lateral movement uses the domain account **`VFG\svc.***`**; `VFG-CTR-W019\Administrator` is a **local** account acting as a decoy, not the answer.
> **Nota / Note (Q10/Q11):** El documento financiero abierto por el LNK es `Q1_2026_*******_Summary.txt` y el archivo de staging es `data_backup.zip` en `\Windows\Temp` (creado 06:04:29), de tamaño `4**` bytes.
> **EN (Q10/Q11):** The financial document opened via the LNK is `Q1_2026_*******_Summary.txt` and the staging file is `data_backup.zip` in `\Windows\Temp` (created 06:04:29), `4**` bytes in size.

## Metodología / Methodology

1. **Paso / Step - Preparar el triage:** Descomprimir `Vantara-Artefacts.zip` (triage KAPE: Prefetch, Amcache, MFT, Registro con SAM, LNK, eventos `Security.evtx`, etc.).
2. **Paso / Step - Herramientas EZ Tools:** `PECmd` (Prefetch), `AmcacheParser` (Amcache), `MFTECmd` (MFT) → volcados CSV → abrir en **Timeline Explorer** para correlacionar la línea de tiempo del incidente: **05-06-2026, 05:35–06:26**.
3. **Paso / Step - Q1/Q2 (ejecutable y SHA1):** Triangulando Prefetch + UserAssist + Amcache se identifica el ejecutable lanzado desde `Downloads` (Q1) y su **SHA1** en Amcache (Q2).
4. **Paso / Step - Q3/Q4 (segunda etapa e impostor):** A las 06:01:40 corre `certutil` (binario nativo que entrega la segunda etapa, Q3); a las 06:01:48 aparece el payload en `%TEMP%` disfrazado con nombre de `svchost` (Q4).
5. **Paso / Step - Q5/Q6 (persistencia):** En `System32\Tasks\*.xml` se ve la tarea programada de persistencia (Q5) y su ruta de ejecución completa hacia `…\AppData\Local\Temp\svc*****.exe` (Q6).
6. **Paso / Step - Q7/Q12 (enumeración):** El burst de comandos `whoami`/`net`/`nltest`/`wmic`/`quser` se correlaciona con los RunCount de Prefetch: la herramienta de enumeración de confianza de dominios es `nltest` (Q7) y el comando de descubrimiento de usuario con su RunCount es `whoami, 1*` (Q12).
7. **Paso / Step - Q8 (m. lateral):** En `Security.evtx`, el **EventID 4648** (se intentó iniciar sesión con credenciales explícitas) muestra la cuenta de dominio `VFG\svc.******` usada para movimiento lateral; `VFG-CTR-W019\Administrator` es local (decoy).
8. **Paso / Step - Q9 (cuenta rogue):** En la **SAM** (a través de Registry Explorer sobre el hive del Registro) se detecta la cuenta local rogue `help****$` (RID `0x3F1`).
9. **Paso / Step - Q10/Q11 (documento y staging):** Con `LECmd` (jump lists/LNK) se ve el documento financiero abierto `Q1_2026_*******_Summary.txt` (Q10); con `MFTECmd` se localiza el `data_backup.zip` de staging en `\Windows\Temp` (creado 06:04:29), cuyo tamaño en la MFT da los `4**` bytes (Q11).

### Cadena de ataque / Attack Chain

```
Vantara-Artefacts.zip (triage KAPE)
  -> PECmd (Prefetch) + AmcacheParser (SHA1) + MFTECmd + Registry (SAM) + Security.evtx (4648) + LECmd (LNK)
  -> Timeline Explorer -> incidente 2026-06-05 (05:35 - 06:26)
  -> ejecutable desde Downloads (Q1) -> SHA1 en Amcache (Q2)
  -> certutil 06:01:40 entrega 2a etapa (Q3) -> payload %TEMP% 06:01:48 impostor svchost (Q4)
  -> tarea programada System32\Tasks (Q5) -> ...\AppData\Local\Temp\svc*****.exe (Q6)
  -> nltest enumeracion de confianza de dominios (Q7) -> whoami RunCount (Q12)
  -> Security.evtx EventID 4648 -> VFG\svc.****** (dominio, no la local VFG-CTR-W019\Administrator decoy) (Q8)
  -> SAM -> cuenta rogue help****$ RID 0x3F1 (Q9)
  -> LECmd -> Q1_2026_*******_Summary.txt abierto por LNK (Q10)
  -> MFTECmd -> data_backup.zip en \Windows\Temp (06:04:29) -> tamano 4** bytes (Q11)
```

**Lección:** Un triage **KAPE + EZ Tools + Timeline Explorer** reconstruye la cadena completa del incidente en una sola línea de tiempo: Prefetch y Amcache identifican el binario y su hash, el Registro y Events 4648 cubren la persistencia y el movimiento lateral, y conviene recordar que las cuentas locales (como `VFG-CTR-W019\Administrator`) son señuelos que hay que descartar frente a las cuentas de dominio reales usadas en el ataque.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.