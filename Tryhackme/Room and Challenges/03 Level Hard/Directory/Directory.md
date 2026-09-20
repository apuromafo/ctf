# Directory

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Walkthrough | `directorydfirroom` | https://tryhackme.com/room/directorydfirroom | 03 Level Hard | TryHackMe | Windows / Active Directory / Service Directory (Active Directory Domain Services) / ldapsearch / SAM/SYSTEM dump / secretsdump / reg save | Sala de respuesta a incidentes en Active Directory: analizar una infección que volcó las bases de datos de contraseñas, extraer el SAM y SYSTEM con reg save, volcar los hashes con secretsdump y escalar/validar con El Rastro del robo. |

---

**Contexto:** Sala DFIR orientada a Active Directory. La investigación parte del servicio Directory Services de Windows y de la enumeración del dominio (puertos de AD, usuario del directorio como `directory.thm\larry.doe`), para después responder con un hash de usuario, una contraseña clara (`Password1!`), el comando de volcado del registro usado por el atacante (`reg save` sobre HKLM\SYSTEM y HKLM\SAM) y la flag final del incidente.

> **ES:** "Sala DFIR de Active Directory: enumera el servicio de directorio, extrae SAM y SYSTEM con reg save y resuelve el robo de credenciales."
> **EN:** "Active Directory DFIR room: enumerate the directory service, dump SAM and SYSTEM with reg save and solve the credential theft."

## Solucionario

### Task 1: Investigación del incidente / Incident investigation

**Explicación:** Tarea única con las seis respuestas de la investigación: puertos del entorno de directorio, usuario del dominio, hash de nuestra cuenta, contraseña clara, comando de volcado de SAM/SYSTEM y la flag del incidente. Contenido original de la tarea:

```text
1. 1. 53,80,88,135,139,389,445,464,593,636,3268,3269,5357
   2. directory.thm\larry.doe
   3. 55616532b664cd0b50cda8d4ba469f
   4. Password1!
   5. reg save HKLM\SYSTEM C:\SYSTEM,reg save HKLM\SAM C:\SAM
   6. THM{Ya_G0t_R0aSt3d!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Puertos expuestos por el entorno de Active Directory (lista completa). | `53,80,88,135,139,389,445,464,593,636,3268,3269,5357` |
| 2 | Usuario del dominio (formato dominio\usuario). | `directory.thm\larry.doe` |
| 3 | Hash de la contraseña de usuario extraído. | `55616532b664cd0b50cda8d4ba469f` |
| 4 | Contraseña del usuario en claro. | `Password1!` |
| 5 | Comando empleado para volcar el registro SAM y SYSTEM. | `reg save HKLM\SYSTEM C:\SYSTEM,reg save HKLM\SAM C:\SAM` |
| 6 | Flag del incidente. | `THM{Ya_G0t_R0aSt3d!}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Puertos expuestos por el entorno de Active Directory (lista completa). | `53,80,88,135,139,389,445,464,593,636,3268,3269,5357` |
| 2 | Usuario del dominio (formato dominio\usuario). | `directory.thm\larry.doe` |
| 3 | Hash de la contraseña de usuario extraído. | `55616532b664cd0b50cda8d4ba469f` |
| 4 | Contraseña del usuario en claro. | `Password1!` |
| 5 | Comando empleado para volcar el registro SAM y SYSTEM. | `reg save HKLM\SYSTEM C:\SYSTEM,reg save HKLM\SAM C:\SAM` |
| 6 | Flag del incidente. | `THM{Ya_G0t_R0aSt3d!}` |

---

**Metodología:**
1. Identificar el servicio de Active Directory Domain Services y enumerar los puertos expuestos por el entorno.
2. Enumerar el dominio y localizar la cuenta `directory.thm\larry.doe`.
3. Extraer los hashes (SAM/SYSTEM) y obtener la contraseña en claro `Password1!` (crackeo del hash).
4. Reconstruir el comando del atacante con `reg save` para el volcado de HKLM\SYSTEM y HKLM\SAM.
5. Completar la investigación con la flag del incidente.

### Cadena de ataque / Attack Chain

```text
Recon (puertos AD) -> Directory Services -> dominio directory.thm -> usuario larry.doe -> reg save HKLM\SYSTEM + reg save HKLM\SAM -> hashes -> Password1! -> THM{Ya_G0t_R0aSt3d!}
```

**Learning chain:** `Enumeración de Active Directory -> puertos del dominio -> cuenta directory.thm\larry.doe -> volcado SAM/SYSTEM con reg save -> hash -> Password1! -> flag`

**Lección:** *El volcado de las cuentas de seguridad (SAM/SYSTEM) mediante `reg save` permite a un atacante offline crackear contraseñas; en DFIR hay que buscar artefactos exactamente como el comando `reg save HKLM\SYSTEM C:\SYSTEM,reg save HKLM\SAM C:\SAM`.*

**MITRE ATT&CK:** T1003.001 (OS Credential Dumping: LSASS Memory), T1003.002 (OS Credential Dumping: Security Account Manager), T1078 (Valid Accounts), T1018 (Remote System Discovery)

**Fuente:** [TryHackMe - Directory](https://tryhackme.com/room/directorydfirroom)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.