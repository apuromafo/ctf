# LocalPotato

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `localpotato` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/localpotato) |
| **Sección** | 02 Level Medium |
| **Fuente** | THM |
| **Componentes** | NTLM, CVE-2023-21746, LocalPotato, StorSvc, DLL hijacking, SprintCSP, msbuild, xp_cmdshell |
| **Impacto** | Escalada de privilegios local (LPE) a SYSTEM mediante NTLM local authentication abuse + hijacking de DLL de StorSvc |

---

**Contexto:** Sala que cubre la vulnerabilidad LocalPotato (CVE-2023-21746), un fallo en la autenticación NTLM local que permite a un atacante con una cuenta de bajos privilegios escribir archivos arbitrarios con privilegios de SYSTEM. Se combina con el abuso del servicio StorSvc (hijacking de la DLL SprintCSP.dll) para ejecutar comandos como SYSTEM y obtener una consola administrativa.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine to follow along. | `No answer needed` |

### Task 2: NTLM Authentication Refresher

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; read the packet exchange (Type 1/2/3). | `No answer needed` |

### Task 3: LocalPotato

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; understand the local NTLM authentication flaw. | `No answer needed` |

### Task 4: Abusing StorSvc to Execute Commands

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; compile the SprintCSP.dll payload with msbuild. | `No answer needed` |

### Task 5: Elevating our Privileges

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Elevate your privileges on the system to get an administrative console. What is the value of the flag in C:\users\administrator\desktop\flag.txt? | `THM{local_potatoes_best_potatoes}` |

### Task 6: Detection/Mitigation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; review YARA and SIGMA rules for LocalPotato and SprintCSP hijacking. | `No answer needed` |

### Task 7: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required. | `No answer needed` |

---

**Metodología:** Se despliega la máquina Windows y se accede por RDP (_user_ / _Password123_). Tras repasar la autenticación NTLM (mensajes Type 1, Type 2 y Type 3), se compila la DLL maliciosa `SprintCSP.dll` con msbuild a partir del proyecto SprintCSP, cuyo entry point ejecuta `cmd.exe /C net localgroup administrators user /add`. Se dejan `LocalPotato.exe`, `RpcClient.exe` y `SprintCSP.dll` en el escritorio y se lanza la cadena de exploit: LocalPotato abusa de la autenticación NTLM local para conseguir una conexión con privilegios del proceso engañado y, mediante el vector de StorSvc, se escribe la DLL en el PATH para lograr ejecución como SYSTEM. El usuario queda miembro de administradores y se lee la flag en `C:\users\administrator\desktop\flag.txt`.

**Learning chain:** RDP access → NTLM refresher (Type 1/2/3) → LocalPotato NTLM local auth abuse → arbitrary file write as SYSTEM → StorSvc DLL hijacking (SprintCSP.dll) → cmd as SYSTEM → add user to administrators → administrative console → flag capture

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1574.001 (DLL Search Order Hijacking), T1543 (Create or Modify System Process), T1078 (Valid Accounts), T1134 (Access Token Manipulation)

**Fuente:** [TryHackMe - LocalPotato](https://tryhackme.com/r/room/localpotato)
