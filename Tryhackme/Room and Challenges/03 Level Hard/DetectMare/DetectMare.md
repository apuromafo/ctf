# DetectMare [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF
* **Slug:** `detectmare`
* **Link:** https://tryhackme.com/room/detectmare
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=detectmare` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de **Detection Engineering** de dificultad Hard con enfoque **Detection-as-Code + Splunk**. El cliente es el **Meridian Defense Research Institute** y el adversario es **APT21**. Tras leer el briefing (TSS Operations Hub), el objetivo es escribir y afinar **5 detecciones** (PR#1–PR#5) contra el índice Splunk `index="dac_lab"` (All time) siguiendo el pipeline DaC: sintaxis Sigma → convertidor a SPL → validación de entorno → test automatizado de Red Team → merge/approve → flag de la PR.
> **EN:** **Detection Engineering** room of Hard difficulty with a **Detection-as-Code + Splunk** focus. The client is the **Meridian Defense Research Institute** and the adversary is **APT21**. After reading the briefing (TSS Operations Hub), the goal is to write and tune **5 detections** (PR#1–PR#5) against the Splunk index `index="dac_lab"` (All time) following the DaC pipeline: Sigma syntax → SPL converter → environment validation → automated Red Team test → merge/approve → PR flag.

### Task 1 - Case Briefing

> **ES:** Tarea de briefing (sitio estático). Presenta el caso del **Meridian Defense Research Institute** y al adversario **APT21** (campaña de spearphishing de macros → NetTraveler → credenciales en memoria → movimiento lateral con hashes → exfiltración). Indica que el entorno es Splunk (`index="dac_lab"`, All time) y el portal DaC del laboratorio. 1 pregunta de confirmación: se responde con el enunciado de confirmación.
> **EN:** Briefing task (static site). Presents the **Meridian Defense Research Institute** case and adversary **APT21** (macro spearphishing → NetTraveler → credentials in memory → lateral movement with hashes → exfiltration). Notes the environment is Splunk (`index="dac_lab"`, All time) and the lab DaC portal. 1 confirmation question: answered with the confirmation statement.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I have reviewed the case briefing and am ready to begin the investigation. | `I have reviewed the case briefing and am ready to begin the investigation.` |

### Task 2 - Tuning Detections

> **ES:** Tarea de investigación con **10 preguntas**: 5 flags de las 5 "Pull Requests" de detección y 5 respuestas de investigación. Los flags solo aparecen publicados en screenshots (los autores no los transcriben); se indica el formato esperado de cada uno. El resto de respuestas SÍ son valores estáticos publicados.
> **EN:** Investigation task with **10 questions**: 5 flags from the 5 detection "Pull Requests" and 5 investigation answers. The flags are only published as screenshots (authors do not transcribe them); the expected format of each is noted. The rest of the answers ARE static published values.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the doc file opened by the infected user? | `Hypersonic_Test_Schedule_2025.docm` |
| What is the PR#1 flag? | `THM{...redacted...}` |
| What is the filename of the internal tool that may cause false positives in PR#2 if not properly filtered? | `researchdeploy.exe` |
| What is the PR#2 flag? | `THM{...redacted...}` |
| What is the username that the attacker used to execute the LSASS dump? | `m.okafor` |
| What is the PR#3 flag? | `THM{...redacted...}` |
| When did the pass-the-hash authentication happen? (MM/DD/YYYY HH:MM:SS.mmm AM/PM) | `3/11/2025 10:40:00.000 AM` |
| What is the PR#4 flag? | `THM{...redacted...}` |
| In which folder should an attacker place a malicious binary to make it look like a legitimate backup routine? | `D:\Backups\nightly` |
| What is the PR#5 flag? | `THM{...redacted...}` |

> **Nota / Note:** Formato esperado de los flags (vistos solo en screenshot): PR#1 `THM{OfFicE_…}`, PR#2 `THM{sIgNeD…}`, PR#3 `THM{D…}`, PR#4 `THM{P…}`, PR#5 `THM{A…}`. Se documenta el método para reclamar cada PR; el literal exacto no está transcrito públicamente.
> **EN:** Expected flag formats (seen only in screenshots): PR#1 `THM{OfFicE_…}`, PR#2 `THM{sIgNeD…}`, PR#3 `THM{D…}`, PR#4 `THM{P…}`, PR#5 `THM{A…}`. The method to claim each PR is documented; the exact literal is not publicly transcribed.

## Metodología / Methodology

1. **Paso / Step - Briefing (TSS Operations Hub):** Leer el caso Meridian Defense / APT21. Cadena del adversario: **spearphishing `.docm` → payload loaders (NetTraveler) → credenciales en memoria → lateral movement con hashes → staging/exfiltración con ZIP cifrado**.
2. **Paso / Step - Entorno:** Splunk con `index="dac_lab"` (rango All time) para validar, y el portal DaC del laboratorio (`LAB_WEB_URL.p.thmlabs.com/dac-site`) donde viven los 5 PRs y su `README.md`.
3. **Paso / Step - Pipeline DaC de cada PR:** Sigma Syntax → Converter (a SPL) → Environment Validation → Automated Red Team Test. El gate exige **TP > 0 y FP = 0** para poder mergear/approve y obtener la flag de la PR. Se repite para PR#1–PR#5.
4. **Paso / Step - PR#1 (spearphishing):** Sigma anclado a Word (proceso WINWORD) abriendo el documento `Hypersonic_Test_Schedule_2025.docm` → confirma la Q1 (doc abierto por el usuario infectado). Ajustar con el `EventCode`/`EventID` correcto y filtros `and not` del entorno → approve → flag `THM{OfFicE_…}`.
5. **Paso / Step - PR#2 (proxy execution):** Detección sobre ejecución vía `rundll32` con `researchdeploy.exe` y contexto SOLIDWORKS. La herramienta interna **`researchdeploy.exe`** genera falsos positivos si no se filtra → se excluye con `and not` conservando los TPs → flag `THM{sIgNeD…}`.
6. **Paso / Step - PR#3 (LSASS dump):** Correlación de `comsvcs.dll` (o `WerFault`/`vaultagent`) con el usuario **`m.okafor`** que ejecutó el volcado de LSASS. La búsqueda `user=m.okafor` en el índice da la Q5. Ajustes de eventos → flag `THM{D…}`.
7. **Paso / Step - PR#4 (pass-the-hash):** Evento **4624 con LogonType 3 (red) + autenticación NTLM**, correlacionado con el **7045** (servicio) → autenticación PtH en **`3/11/2025 10:40:00.000 AM`** (Q7). Filtros de eventos del entorno → flag `THM{P…}`.
8. **Paso / Step - PR#5 (staging/backup):** Detección de compresión de archivos (`7z`/`Compress-Archive`, `researchbackup`, `autobackup`) en un directorio de backup legítimo: la carpeta donde un atacante escondería el binario es **`D:\Backups\nightly`** (Q9). Tuneo del filtro → flag `THM{A…}`.

### Cadena de ataque / Attack Chain

```
Briefing TSS Operations Hub (cliente: Meridian Defense Research Institute; adversario: APT21)
  -> cadena APT21: .docm -> NetTraveler -> creds en memoria -> movimiento lateral con hashes -> ZIP cifrado
  -> portal DaC LAB_WEB_URL.p.thmlabs.com/dac-site -> 5 PRs + README.md
  -> pipeline DaC: Sigma Syntax -> Converter (SPL) -> Environment Validation -> Automated Red Team Test
  -> reglas en Splunk index="dac_lab" (All time), TP > 0 y FP = 0
  -> PR#1 spearphishing -> WINWORD/Hypersonic_Test_Schedule_2025.docm -> Q1 -> THM{OfFicE_...}
  -> PR#2 proxy execution -> rundll32 + researchdeploy.exe + SOLIDWORKS (FP interno excluido) -> THM{sIgNeD...}
  -> PR#3 LSASS dump -> comsvcs/WerFault/vaultagent + m.okafor -> Q5 -> THM{D...}
  -> PR#4 PtH -> 4624 LogonType3 NTLM + 7045 -> 3/11/2025 10:40:00.000 AM -> THM{P...}
  -> PR#5 staging -> 7z/Compress-Archive/researchbackup/autobackup + D:\Backups\nightly -> THM{A...}
  -> mergear/approve cada PR -> flag de cada PR
```

**Lección:** Detection-as-Code valida la regla de extremo a extremo: cada PR pasa por conversión Sigma→SPL, validación de entorno y un test automatizado de Red Team antes de aprobarse, y los falsos positivos se cierran con filtros de entorno (`and not` sobre herramientas internas legítimas) manteniendo los verdaderos positivos intactos.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.