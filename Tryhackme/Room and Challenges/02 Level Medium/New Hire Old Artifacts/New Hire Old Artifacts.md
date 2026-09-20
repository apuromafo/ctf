# New Hire Old Artifacts

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Laboratorio DFIR | newhireoldartifacts | https://tryhackme.com/room/newhireoldartifacts | Forense / DFIR (Windows) | TryHackMe | Memoria (Volatility), artefactos Windows, persistencia, defensa | High |

> **Objeto:** Realizar un análisis forense completo de una máquina Windows comprometida: recuperar artefactos de un volcado de memoria con Volatility, identificar malware (NirSoft), persistencia (WMI), políticas de Windows Defender y exfiltración, y responder a las preguntas del caso "New Hire Old Artifacts".

---

**Contexto:**

La sala presenta un caso forense: la máquina de una nueva contratación fue comprometida y se debe reconstruir la cadena de ataque a partir de su volcado de memoria y sus artefactos del sistema. Se usa Volatility para recuperar procesos, archivos borrados del directorio `Temp`, programas y sus extensiones, direcciones IP maliciosas, configuraciones de exclusión de Windows Defender aplicadas por WMI, los hashes de los ejecutables en cuestión y los ejecutables reales (EasyCalc) ocultos en AppData.

> **ES:** Con Volatility se recupera el archivo `11111.exe` de `C:\Users\FINANC~1\AppData\Local\Temp`, se identifica el creador de la herramienta (NirSoft), las extensiones de los archivos (IonicLarge.exe y PalitExplorer.exe), la IP `2[.]56[.]59[.]42`, la política de exclusión de Windows Defender (HKLM\SOFTWARE\Policies\Microsoft\Windows Defender), el comando WMIC con los ThreatID y el ejecutable malicioso en AppData (EasyCalc.exe) con sus DLLs asociadas.

> **EN:** With Volatility the file `11111.exe` is recovered from `C:\Users\FINANC~1\AppData\Local\Temp`, the tool author is identified (NirSoft), the file extensions (IonicLarge.exe and PalitExplorer.exe), the IP `2[.]56[.]59[.]42`, the Windows Defender exclusion policy (HKLM\SOFTWARE\Policies\Microsoft\Windows Defender), the WMIC command with the ThreatIDs and the malicious executable in AppData (EasyCalc.exe) with its associated DLLs.

## Solucionario

### Task 1: Análisis forense / Forensic Analysis
**Explicación:**

Se trabaja sobre el volcado de memoria y los artefactos del sistema para reconstruir el ataque. Se recuperan los archivos sospechosos del directorio `Temp`, se identifica la herramienta y su autor, las extensiones de los archivos de malware, la IP del C2, las políticas de Windows Defender manipuladas por WMI, los ThreatIDs añadidos a las exclusiones y los ejecutables y DLLs del programa malicioso.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Ruta del ejecutable recuperado | `C:\Users\FINANC~1\AppData\Local\Temp\11111.exe` |
| 2. Autor de la herramienta | `NirSoft` |
| 3. Extensiones de los archivos | `IonicLarge.exe,PalitExplorer.exe` |
| 4. IP del C2 (ofuscada) | `2[.]56[.]59[.]42` |
| 5. Ruta de la política de Windows Defender | `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender` |
| 6. Ejecutables de la persistencia | `WvmIOrcfsuILdX6SNwIRmGOJ.exe,phcIAmLJMAIMSa9j9MpgJo1m.exe` |
| 7. Comando WMIC de exclusión | `powershell WMIC /NAMESPACE:\\root\Microsoft\Windows\Defender PATH MSFT_MpPreference call Add ThreatIDDefaultAction_Ids=2147737394 ThreatIDDefaultAction_Actions=6 Force=True` |
| 8. ThreatIDs añadidos | `2147735503,2147737010,2147737007,2147737394` |
| 9. Ruta del ejecutable malicioso real | `C:\Users\Finance01\AppData\Roaming\EasyCalc\EasyCalc.exe` |
| 10. DLLs asociadas | `ffmpeg.dll,nw.dll,nw_elf.dll` |
| 11. Task subpregunta | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Ejecutable en Temp | `C:\Users\FINANC~1\AppData\Local\Temp\11111.exe` |
| 2 | Autor de la herramienta | `NirSoft` |
| 3 | Extensiones de los archivos | `IonicLarge.exe,PalitExplorer.exe` |
| 4 | IP del C2 | `2[.]56[.]59[.]42` |
| 5 | Política de Windows Defender | `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender` |
| 6 | Ejecutables de persistencia | `WvmIOrcfsuILdX6SNwIRmGOJ.exe,phcIAmLJMAIMSa9j9MpgJo1m.exe` |
| 7 | Comando WMIC | `powershell WMIC /NAMESPACE:\\root\Microsoft\Windows\Defender PATH MSFT_MpPreference call Add ThreatIDDefaultAction_Ids=2147737394 ThreatIDDefaultAction_Actions=6 Force=True` |
| 8 | ThreatIDs | `2147735503,2147737010,2147737007,2147737394` |
| 9 | Ejecutable malicioso | `C:\Users\Finance01\AppData\Roaming\EasyCalc\EasyCalc.exe` |
| 10 | DLLs | `ffmpeg.dll,nw.dll,nw_elf.dll` |
| 11 | Task subpregunta | `No answer needed` |

---

**Metodología:**

1. Volcado de memoria y análisis con Volatility (procesos, archivos y registry).
2. Recuperación del ejecutable `11111.exe` del directorio `Temp` e identificación de la herramienta (NirSoft).
3. Listado de extensiones de archivos y de la IP de exfiltración/comunicación (`2[.]56[.]59[.]42`).
4. Revisión de políticas de Windows Defender y del comando WMIC de exclusión de ThreatID.
5. Identificación del ejecutable persistente en AppData (`EasyCalc.exe`) y sus DLLs.

### Cadena de ataque / Attack Chain

```
Compromiso inicial: 11111.exe en Temp (herramienta NirSoft)
        |
        v
Ejecución con extensiones IonicLarge.exe / PalitExplorer.exe
        |
        v
Comunicación con C2: 2[.]56[.]59[.]42
        |
        v
Persistencia vía WMI: add ThreatIDDefaultAction_Ids (2147735503, ...)
        |
        v
Exclusión en Windows Defender (HKLM\SOFTWARE\Policies\...\Windows Defender)
        |
        v
Malware residente: EasyCalc.exe + ffmpeg.dll, nw.dll, nw_elf.dll
```

**Learning chain:**

- ¿Cómo se recuperan archivos y procesos de un volcado de memoria con Volatility?
- ¿Qué papel juega NirSoft en la obtención de credenciales/artefactos?
- ¿Cómo se usa WMI para añadir excepciones de ThreatID en Windows Defender?
- ¿Cómo se reconstruye la cadena completa de infección y persistencia?

**Lección:**

*La memoria no miente: cada paso del atacante — descarga, ejecución, comunicación y persistencia — queda registrado en los artefactos, y saber extraerlos con Volatility convierte un volcado en una línea de tiempo completa del incidente.*

**MITRE ATT&CK:**

- T1003 (OS Credential Dumping) — herramientas NirSoft
- T1547.009 (Boot or Logon Autostart Execution: Shortcut Modification)
- T1546 / T1546.003 (Event Triggered Execution: WMI Event Subscription)
- T1562.001 (Impair Defenses: Disable or Modify Tools) — exclusiones Windows Defender
- T1071.001 (Application Layer Protocol: Web) — C2

**Fuente:** [TryHackMe - New Hire Old Artifacts](https://tryhackme.com/room/newhireoldartifacts)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.