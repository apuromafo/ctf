# Blue

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `blue` | [TryHackMe](https://tryhackme.com/room/blue) | 01 Level Easy | TryHackMe | EternalBlue / ms17-010 / Metasploit / SAM / Windows | Compromiso total de un Windows 7 vulnerable a EternalBlue (MS17-010) y extracción de credenciales y flags del sistema |

---

**Contexto:** Blue es la clásica máquina Windows 7 vulnerable a EternalBlue (MS17-010). La sala guía desde el escaneo inicial y la confirmación del puerto SMB vulnerable, pasando por la explotación con Metasploit, hasta la migración a Meterpreter y el volcado de la base de datos SAM para recuperar credenciales y las tres flags del sistema.

> **ES:** Máquina Windows 7 con EternalBlue. Tras el escaneo se explota el módulo `ms17_010_eternalblue`, se migra una shell a Meterpreter y se vuelca la SAM para obtener las credenciales `Jon:alqfna22` y las flags.
> **EN:** A Windows 7 box vulnerable to EternalBlue. After scanning, the `ms17_010_eternalblue` module is fired, the shell is upgraded to Meterpreter and the SAM database is dumped to recover the `Jon:alqfna22` credentials and the flags.

## Solucionario

### Task 1: Reconocimiento / Recon
**Explicación:** El escaneo de la máquina revela tres puertos abiertos con score mayor que 1000, destacando el puerto SMB. La vulnerabilidad que se va a explotar es EternalBlue, MS17-010.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué pregunta de reconocimiento se plantea? | `No answer needed` |
| ¿Cuántos puertos están abiertos con un score mayor que 1000? | `3` |
| ¿Cuál es el nombre de la vulnerabilidad? | `ms17-010` |

### Task 2: Explotación / Exploitation
**Explicación:** En Metasploit se usa el módulo `exploit/windows/smb/ms17_010_eternalblue`, configurando la opción `RHOSTS` con la dirección IP de la máquina víctima. Tras ejecutar el exploit se obtiene una shell inversa.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué pregunta del exploit se plantea? | `No answer needed` |
| ¿Qué módulo de exploit se usa para EternalBlue? | `exploit/windows/smb/ms17_010_eternalblue` |
| ¿Qué opción se configura con la IP de la víctima? | `RHOSTS` |
| ¿Qué pregunta de configuración se plantea? | `No answer needed` |
| ¿Qué pregunta de configuración se plantea? | `No answer needed` |

### Task 3: Migración a Meterpreter / Shell upgrade
**Explicación:** Con una shell de baja interacción se lanza el módulo post `post/multi/manage/shell_to_meterpreter`, configurando la opción `SESSION` con el identificador de la sesión de la shell. A continuación se migra el proceso del Meterpreter a un proceso estable.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué módulo se usa para migrar la shell a Meterpreter? | `post/multi/manage/shell_to_meterpreter` |
| ¿Qué opción se configura con el id de la sesión? | `SESSION` |
| ¿Qué pregunta de migración se plantea? | `No answer needed` |
| ¿Qué pregunta de migración se plantea? | `No answer needed` |
| ¿Qué pregunta de migración se plantea? | `No answer needed` |
| ¿Qué pregunta de migración se plantea? | `No answer needed` |
| ¿Qué pregunta de migración se plantea? | `No answer needed` |
| ¿Qué pregunta de migración se plantea? | `No answer needed` |

### Task 4: Usuario y contraseña / User and password
**Explicación:** Volcando la base de datos SAM con `hashdump` se recuperan los hashes de los usuarios. Cracking de los hashes revela el usuario `Jon` y su contraseña `alqfna22`.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el nombre del usuario del sistema? | `Jon` |
| ¿Cuál es la contraseña del usuario? | `alqfna22` |

### Task 5: Flags
**Explicación:** Durante la fase de post-explotación se localizan las tres flags del sistema: la flag de acceso a la máquina, la flag de la base de datos SAM y la flag de los documentos del administrador.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| Flag de acceso a la máquina | `flag{access_the_machine}` |
| Flag de acceso elevado SAM | `flag{sam_database_elevated_access}` |
| Flag de documentos del administrador | `flag{admin_documents_can_be_valuable}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de reconocimiento | `No answer needed` |
| 2 | Puertos abiertos con score > 1000 | `3` |
| 3 | Nombre de la vulnerabilidad | `ms17-010` |
| 4 | Pregunta del exploit | `No answer needed` |
| 5 | Módulo de exploit EternalBlue | `exploit/windows/smb/ms17_010_eternalblue` |
| 6 | Opción con la IP de la víctima | `RHOSTS` |
| 7 | Pregunta de configuración | `No answer needed` |
| 8 | Pregunta de configuración | `No answer needed` |
| 9 | Módulo para migrar a Meterpreter | `post/multi/manage/shell_to_meterpreter` |
| 10 | Opción con el id de sesión | `SESSION` |
| 11 | Pregunta de migración | `No answer needed` |
| 12 | Pregunta de migración | `No answer needed` |
| 13 | Pregunta de migración | `No answer needed` |
| 14 | Pregunta de migración | `No answer needed` |
| 15 | Pregunta de migración | `No answer needed` |
| 16 | Pregunta de migración | `No answer needed` |
| 17 | Usuario del sistema | `Jon` |
| 18 | Contraseña del usuario | `alqfna22` |
| 19 | Flag de acceso a la máquina | `flag{access_the_machine}` |
| 20 | Flag SAM | `flag{sam_database_elevated_access}` |
| 21 | Flag documentos del administrador | `flag{admin_documents_can_be_valuable}` |

---

**Metodología:** Se realiza un escaneo de puertos y se confirma la presencia de SMB con la vulnerabilidad MS17-010. En Metasploit se lanza el módulo `exploit/windows/smb/ms17_010_eternalblue` con `RHOSTS` apuntando a la víctima, obteniendo una shell. La shell se migra a Meterpreter con `post/multi/manage/shell_to_meterpreter` (opción `SESSION`) para poder volcar la base de datos SAM con `hashdump`. Crackeando los hashes se obtienen las credenciales `Jon:alqfna22`. Por último se recorren los directorios del sistema y del administrador para capturar las tres flags.

### Cadena de ataque / Attack Chain

```text
nmap -> SMB abierto -> ms17-010 -> searchsploit/msf -> exploit/windows/smb/ms17_010_eternalblue -> RHOSTS -> shell -> post/multi/manage/shell_to_meterpreter -> SESSION -> hashdump -> Jon:alqfna22 -> flags (access_the_machine, sam_database_elevated_access, admin_documents_can_be_valuable)
```

**Learning chain:** port scanning --> SMB enumeration --> EternalBlue module --> RHOSTS --> initial shell --> shell_to_meterpreter --> SESSION --> hashdump --> credential cracking --> three flags

**Lección:** *EternalBlue (MS17-010) sigue siendo uno de los exploits más relevantes sobre SMB; el volcado de la SAM y el crackeo de hashes permiten recuperar credenciales y acceder a toda la información del sistema.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1210 (Exploitation of Remote Services), T1003.001 (OS Credential Dumping: LSASS), T1003.002 (OS Credential Dumping: Security Account Manager), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Blue](https://tryhackme.com/room/blue)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.