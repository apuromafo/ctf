# PS Eclipse

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | DFIR / Análisis de amenazas | pseclipse | https://tryhackme.com/room/pseclipse | 02 Level Medium | TryHackMe | PowerShell, Persistencia (schtasks), C2 (ngrok), DFIR | Compromiso de credenciales / persistencia en el sistema |

---

**Contexto:** La sala **PS Eclipse** es un ejercicio de forense digital (DFIR) sobre una máquina Windows comprometida por un artefacto malicioso en PowerShell. Se investiga el ejecutable de la amenaza (`OUTSTANDING_GUTTER.exe`), los endpoints de C2 alojados en ngrok, el proceso lanzador (`powershell.exe`), la tarea programada que garantiza la persistencia, la cuenta objetivo (`NT AUTHORITY\SYSTEM`), los scripts ofuscados (`script.ps1`, `BlackSun.ps1`) y los archivos dejados tras la intrusión.

## Solucionario

### Task 1: Investigación DFIR del artefacto PowerShell / DFIR investigation of the PowerShell artifact
**Explicación:**

La secuencia de respuestas reconstruye toda la cadena de infección: el binario inicial (`OUTSTANDING_GUTTER.exe`), su C2 (ngrok, ofuscado como `hxxp[://]`), el proceso padre `powershell.exe`, la tarea programada de persistencia con su comando `schtasks` (trigger por evento `EventID=777` como `SYSTEM`), el segundo endpoint de C2, los scripts `script.ps1` y `BlackSun.ps1`, y los artefactos finales en el sistema (README y `blacksun.jpg`).

```
1. OUTSTANDING_GUTTER.exe
2. hxxp[://]886e-181-215-214-32[.]ngrok[.]io
3. C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
4. "C:\Windows\system32\schtasks.exe" /Create /TN OUTSTANDING_GUTTER.exe /TR C:\Windows\Temp\COUTSTANDING_GUTTER.exe /SC ONEVENT /EC Application /MO *[System/EventID=777] /RU SYSTEM /f
5. NT AUTHORITY\SYSTEM;"C:\Windows\system32\schtasks.exe" /Run /TN OUTSTANDING_GUTTER.exe
6. hxxp[://]9030-181-215-214-32[.]ngrok[.]io
7. script.ps1
8. BlackSun.ps1
9. C:\Users\keegan\Downloads\vasg6b0wmw029hd\BlackSun_README.txt
10. C:\Users\Public\Pictures\blacksun.jpg
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué binario inicia la infección? | `OUTSTANDING_GUTTER.exe` |
| 2 | ¿Qué endpoint de C2 se usa en la descarga? | `hxxp[://]886e-181-215-214-32[.]ngrok[.]io` |
| 3 | ¿Qué proceso lanza el artefacto? | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` |
| 4 | ¿Qué comando de persistencia se usa? | `"C:\Windows\system32\schtasks.exe" /Create /TN OUTSTANDING_GUTTER.exe /TR C:\Windows\Temp\COUTSTANDING_GUTTER.exe /SC ONEVENT /EC Application /MO *[System/EventID=777] /RU SYSTEM /f` |
| 5 | ¿Qué cuenta y comando ejecutan la tarea? | `NT AUTHORITY\SYSTEM;"C:\Windows\system32\schtasks.exe" /Run /TN OUTSTANDING_GUTTER.exe` |
| 6 | ¿Qué segundo endpoint de C2 aparece? | `hxxp[://]9030-181-215-214-32[.]ngrok[.]io` |
| 7 | ¿Qué script se ejecuta en el sistema? | `script.ps1` |
| 8 | ¿Qué script tiene relación con BlackSun? | `BlackSun.ps1` |
| 9 | ¿Qué artefacto se encuentra en Downloads? | `C:\Users\keegan\Downloads\vasg6b0wmw029hd\BlackSun_README.txt` |
| 10 | ¿Qué imagen deja la amenaza? | `C:\Users\Public\Pictures\blacksun.jpg` |

---

**Metodología:** Análisis forense de la máquina Windows: correlación de procesos y línea de comandos, extracción de C2 (ngrok), auditoría de tareas programadas (schtasks) y localización de artefactos maliciosos en el sistema.

### Cadena de ataque / Attack Chain

```
OUTSTANDING_GUTTER.exe (descarga vía ngrok C2)
        │
        ▼
powershell.exe lanza script.ps1
        │
        ▼
Persistencia: schtasks /Create (EventID=777, SYSTEM)
        │
        ▼
BlackSun.ps1 + descarga de segundo C2
        │
        ▼
Artefactos finales (README + blacksun.jpg)
```

**Learning chain:** Binario inicial → C2 (ngrok) → PowerShell → persistencia (schtasks) → scripts → artefactos.

**Lección:** *Los troyanos en PowerShell casi siempre incluyen persistencia maliciosa y C2 legítimo (ngrok); un DFIR debe correlacionar la línea de comandos de `schtasks` con los scripts y binarios que la acompañan.*

**MITRE ATT&CK:** T1059.001 Command and Scripting Interpreter (PowerShell) · T1053.005 Scheduled Task · T1105 Ingress Tool Transfer · T1071.001 Application Layer Protocol (C2).

**Fuente:** [TryHackMe - PS Eclipse](https://tryhackme.com/room/pseclipse)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.