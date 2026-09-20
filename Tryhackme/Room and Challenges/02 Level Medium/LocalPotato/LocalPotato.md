# LocalPotato

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | walkthrough | localpotato | https://tryhackme.com/r/room/localpotato | 02 Level Medium | THM | NTLM, CVE-2023-21746, LocalPotato, StorSvc, DLL hijacking, SprintCSP, msbuild, xp_cmdshell | Escalada de privilegios local (LPE) a SYSTEM mediante NTLM local authentication abuse + hijacking de DLL de StorSvc |

---

**Contexto:** Sala que cubre la vulnerabilidad LocalPotato (CVE-2023-21746), un fallo en la autenticación NTLM local que permite a un atacante con una cuenta de bajos privilegios escribir archivos arbitrarios con privilegios de SYSTEM. Se combina con el abuso del servicio StorSvc (hijacking de la DLL SprintCSP.dll) para ejecutar comandos como SYSTEM y obtener una consola administrativa.

## Solucionario

### Task 1: Introduction
**Explicación:**

Se presenta la sala y su objetivo: explotar CVE-2023-21746 (LocalPotato) para escalar privilegios en un host Windows.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine to follow along. | `No answer needed` |

### Task 2: NTLM Authentication Refresher
**Explicación:**

Repaso de la autenticación NTLM y del intercambio de mensajes Type 1/2/3, base para entender el fallo de autenticación local NTLM (LOCAL NTLM authentication) que explota LocalPotato.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; read the packet exchange (Type 1/2/3). | `No answer needed` |

### Task 3: LocalPotato
**Explicación:**

Se explica la vulnerabilidad CVE-2023-21746: al forzar autenticación NTLM local se consigue la conexión con los privilegios del proceso engañado y se escribe un archivo arbitrario con privilegios de SYSTEM.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; understand the local NTLM authentication flaw. | `No answer needed` |

### Task 4: Abusing StorSvc to Execute Commands
**Explicación:**

Se compila `SprintCSP.dll` con msbuild a partir del proyecto SprintCSP; su entry point ejecuta `cmd.exe /C net localgroup administrators user /add`. El vector de StorSvc escribe la DLL en el PATH con privilegios de SYSTEM.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; compile the SprintCSP.dll payload with msbuild. | `No answer needed` |

### Task 5: Elevating our Privileges
**Explicación:**

Se monta la cadena de exploit: `LocalPotato.exe`, `RpcClient.exe` y `SprintCSP.dll` quedan en el escritorio; LocalPotato abusa de la autenticación NTLM local y, mediante StorSvc, se consigue ejecución como SYSTEM que añade `user` a administradores y permite leer la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Elevate your privileges on the system to get an administrative console. What is the value of the flag in C:\users\administrator\desktop\flag.txt? | `THM{local_potatoes_best_potatoes}` |

### Task 6: Detection/Mitigation
**Explicación:**

Revisión de reglas YARA y SIGMA para detectar LocalPotato y el hijacking de SprintCSP, junto con la mitigación del fallo de autenticación NTLM local (MFA en en escenarios locales y comprobación de uniones insidiosas / mensajes de autenticación locales).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required; review YARA and SIGMA rules for LocalPotato and SprintCSP hijacking. | `No answer needed` |

### Task 7: Conclusion
**Explicación:**

Cierre de la sala resumiendo el ataque completo y las medidas defensivas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required. | `No answer needed` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Deploy the machine to follow along. | `No answer needed` |
| 2.1 | No answer required; read the packet exchange (Type 1/2/3). | `No answer needed` |
| 3.1 | No answer required; understand the local NTLM authentication flaw. | `No answer needed` |
| 4.1 | No answer required; compile the SprintCSP.dll payload with msbuild. | `No answer needed` |
| 5.1 | Elevate your privileges on the system to get an administrative console. What is the value of the flag in C:\users\administrator\desktop\flag.txt? | `THM{local_potatoes_best_potatoes}` |
| 6.1 | No answer required; review YARA and SIGMA rules for LocalPotato and SprintCSP hijacking. | `No answer needed` |
| 7.1 | No answer required. | `No answer needed` |

---

**Metodología:** Se despliega la máquina Windows y se accede por RDP (_user_ / _Password123_). Tras repasar la autenticación NTLM (mensajes Type 1, Type 2 y Type 3), se compila la DLL maliciosa `SprintCSP.dll` con msbuild a partir del proyecto SprintCSP, cuyo entry point ejecuta `cmd.exe /C net localgroup administrators user /add`. Se dejan `LocalPotato.exe`, `RpcClient.exe` y `SprintCSP.dll` en el escritorio y se lanza la cadena de exploit: LocalPotato abusa de la autenticación NTLM local para conseguir una conexión con privilegios del proceso engañado y, mediante el vector de StorSvc, se escribe la DLL en el PATH para lograr ejecución como SYSTEM. El usuario queda miembro de administradores y se lee la flag en `C:\users\administrator\desktop\flag.txt`.

**Learning chain:** RDP access → NTLM refresher (Type 1/2/3) → LocalPotato NTLM local auth abuse → arbitrary file write as SYSTEM → StorSvc DLL hijacking (SprintCSP.dll) → cmd as SYSTEM → add user to administrators → administrative console → flag capture

**Lección:** *Un fallo de autenticación local NTLM se convierte en escalada a SYSTEM solo cuando se encadena con un vector de escritura de archivos (StorSvc) que permite ejecutar un payload como servicio del sistema.*

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1574.001 (DLL Search Order Hijacking), T1543 (Create or Modify System Process), T1078 (Valid Accounts), T1134 (Access Token Manipulation)

**Fuente:** [TryHackMe - LocalPotato](https://tryhackme.com/r/room/localpotato)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.