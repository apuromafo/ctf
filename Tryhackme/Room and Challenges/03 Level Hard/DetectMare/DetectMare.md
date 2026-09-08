# DetectMare

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `detectmare` |
| **Link** | [TryHackMe](https://tryhackme.com/room/detectmare) |
| **Sección** | 03 Level Hard |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=detectmare` + websearch de walkthroughs) |
| **Componentes** | Splunk / Sigma / SPL / Detection-as-Code / NetTraveler / rundll32 / LSASS / pass-the-hash / 7-Zip |
| **Impacto** | Sala de Detection Engineering: escribir, afinar y aprobar 5 detecciones (PR#1–PR#5) Sigma-to-SPL contra `index="dac_lab"` para detectar la cadena completa del adversario APT21. |

---

**Contexto:** Sala de **Detection Engineering** de dificultad Hard con enfoque **Detection-as-Code + Splunk**. El cliente es el **Meridian Defense Research Institute** y el adversario es **APT21**. Tras leer el briefing (TSS Operations Hub), el objetivo es escribir y afinar **5 detecciones** (PR#1–PR#5) contra el índice Splunk `index="dac_lab"` (All time) siguiendo el pipeline DaC: sintaxis Sigma → convertidor a SPL → validación de entorno → test automatizado de Red Team → merge/approve → flag de la PR.

## Solucionario

### Task 1: Case Briefing

**Explicación:** El briefing (sitio estático del TSS Operations Hub) presenta al cliente **Meridian Defense Research Institute** y al adversario **APT21**, cuya cadena de ataque es spearphishing de macro `.docm` → payload loaders (NetTraveler) → credenciales en memoria → movimiento lateral con hashes → staging/exfiltración con ZIP cifrado. Indica que el entorno de validación es Splunk (`index="dac_lab"`, All time) y que el portal DaC del laboratorio vive en `LAB_WEB_URL.p.thmlabs.com/dac-site`. La única pregunta es de confirmación y se responde con el propio enunciado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have reviewed the case briefing and am ready to begin the investigation. | `I have reviewed the case briefing and am ready to begin the investigation.` |

### Task 2: Tuning Detections

**Explicación:** La tarea tiene 10 preguntas (5 flags + 5 respuestas de investigación). Para cada Pull Request el pipeline es: **Sigma Syntax → Converter (a SPL) → Environment Validation → Automated Red Team Test**, y el gate exige TP > 0 y FP = 0 para poder mergear/aprobar la PR.

- **PR#1 (spearphishing):** regla anclada al proceso WINWORD de Word abriendo el documento `Hypersonic_Test_Schedule_2025.docm` (responde la Q1).
- **PR#2 (proxy execution):** ejecución vía `rundll32` con contexto SOLIDWORKS; la herramienta interna `researchdeploy.exe` genera falsos positivos si no se filtra con `and not`.
- **PR#3 (LSASS dump):** correlación de `comsvcs.dll` (o `WerFault`/`vaultagent`) con el usuario `m.okafor` que lanzó el volcado (Q5).
- **PR#4 (pass-the-hash):** evento 4624 con LogonType 3 (red) + NTLM, correlacionado con el 7045 (creación de servicio); la autenticación PtH ocurrió el `3/11/2025 10:40:00.000 AM` (Q7).
- **PR#5 (staging/backup):** compresión de archivos (`7z`/`Compress-Archive`, `researchbackup`, `autobackup`); la carpeta donde un atacante escondería el binario para aparentar un backup legítimo es `D:\Backups\nightly` (Q9).

```bash
# búsquedas clave en Splunk
index="dac_lab" user=m.okafor        # LSASS dump / Q5
index="dac_lab" EventID=4624 LogonType=3 NTLM   # pass-the-hash / Q7
index="dac_lab" WINWORD "Hypersonic_Test_Schedule_2025.docm"  # Q1
```

Los flags de las PRs solo aparecen publicados en screenshots (los autores no los transcriben); su formato esperado es: PR#1 `THM{OfFicE_…}`, PR#2 `THM{sIgNeD…}`, PR#3 `THM{D…}`, PR#4 `THM{P…}`, PR#5 `THM{A…}`. Se documenta el método para reclamar cada PR, no el flag exacto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the doc file opened by the infected user? | `Hypersonic_Test_Schedule_2025.docm` |
| 2 | What is the PR#1 flag? | `THM{...redacted...}` |
| 3 | What is the filename of the internal tool that may cause false positives in PR#2 if not properly filtered? | `researchdeploy.exe` |
| 4 | What is the PR#2 flag? | `THM{...redacted...}` |
| 5 | What is the username that the attacker used to execute the LSASS dump? | `m.okafor` |
| 6 | What is the PR#3 flag? | `THM{...redacted...}` |
| 7 | When did the pass-the-hash authentication happen? (MM/DD/YYYY HH:MM:SS.mmm AM/PM) | `3/11/2025 10:40:00.000 AM` |
| 8 | What is the PR#4 flag? | `THM{...redacted...}` |
| 9 | In which folder should an attacker place a malicious binary to make it look like a legitimate backup routine? | `D:\Backups\nightly` |
| 10 | What is the PR#5 flag? | `THM{...redacted...}` |

---

**Metodología:**
1. **Briefing (TSS Operations Hub):** leer el caso Meridian Defense / APT21. Cadena del adversario: spearphishing `.docm` → payload loaders (NetTraveler) → credenciales en memoria → movimiento lateral con hashes → staging/exfiltración con ZIP cifrado.
2. **Entorno:** Splunk con `index="dac_lab"` (rango All time) para validar, y el portal DaC del laboratorio (`LAB_WEB_URL.p.thmlabs.com/dac-site`) donde viven los 5 PRs y su `README.md`.
3. **Pipeline DaC de cada PR:** Sigma Syntax → Converter (a SPL) → Environment Validation → Automated Red Team Test. El gate exige TP > 0 y FP = 0 para poder mergear/approve y obtener la flag de la PR. Se repite para PR#1–PR#5.
4. **PR#1 (spearphishing):** Sigma anclado a Word (proceso WINWORD) abriendo `Hypersonic_Test_Schedule_2025.docm` → confirma la Q1 (doc abierto por el usuario infectado). Ajustar con el `EventCode`/`EventID` correcto y filtros `and not` del entorno → approve → flag.
5. **PR#2 (proxy execution):** detección de ejecución vía `rundll32` con `researchdeploy.exe` y contexto SOLIDWORKS. La herramienta interna **`researchdeploy.exe`** genera falsos positivos si no se filtra → se excluye con `and not` conservando los TPs → flag.
6. **PR#3 (LSASS dump):** correlación de `comsvcs.dll` (o `WerFault`/`vaultagent`) con el usuario **`m.okafor`** que ejecutó el volcado de LSASS; la búsqueda `user=m.okafor` en el índice da la Q5. Ajustes de eventos → flag.
7. **PR#4 (pass-the-hash):** evento 4624 con LogonType 3 (red) + autenticación NTLM, correlacionado con el 7045 (servicio) → autenticación PtH en `3/11/2025 10:40:00.000 AM` (Q7). Filtros de eventos del entorno → flag.
8. **PR#5 (staging/backup):** detección de compresión de archivos (`7z`/`Compress-Archive`, `researchbackup`, `autobackup`) en un directorio de backup legítimo: la carpeta donde un atacante escondería el binario es **`D:\Backups\nightly`** (Q9). Tuneo del filtro → flag.
9. **Nota sobre los flags:** el literal exacto de cada PR solo aparece publicado en screenshots (los autores no lo transcriben); formato esperado visto en capturas: PR#1 `THM{OfFicE_…}`, PR#2 `THM{sIgNeD…}`, PR#3 `THM{D…}`, PR#4 `THM{P…}`, PR#5 `THM{A…}`. Se documenta el método para reclamar cada PR, no el flag exacto.

**Learning chain:** `Briefing TSS Operations Hub → cadena APT21 (.docm → NetTraveler → creds en memoria → lateral movement → ZIP cifrado) → portal DaC (LAB_WEB_URL.p.thmlabs.com/dac-site) → pipeline Sigma→SPL→validación→Red Team → Splunk index="dac_lab" (TP>0, FP=0) → PR#1 spearphishing → PR#2 proxy execution → PR#3 LSASS dump → PR#4 Pass-the-Hash → PR#5 staging/backup → merge/approve → flag PR`

**MITRE ATT&CK:** T1566 (Phishing), T1059 (Command and Scripting Interpreter), T1003 (OS Credential Dumping), T1550 (Use Alternate Authentication Material), T1021 (Remote Services), T1560 (Archive Collected Data)

**Fuente:** [TryHackMe - DetectMare](https://tryhackme.com/room/detectmare)