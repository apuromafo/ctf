# Blaster

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|
| Easy | challenge | `blaster` | [TryHackMe](https://tryhackme.com/room/blaster) | 01 Level Easy | TryHackMe | IIS / CVE-2019-1388 / UAC bypass / Metasploit | Explotación de un servidor Windows con IIS mediante el CVE de UAC y persistencia con Meterpreter |

---

**Contexto:** Blaster es una máquina Windows que ejecuta IIS en un servidor. La sala guía desde la enumeración web y el descubrimiento de credenciales en un blog hasta la explotación de una conocida vulnerabilidad de UAC (CVE-2019-1388) para elevar a SYSTEM. Finalmente se muestra cómo migrar la sesión a Meterpreter y establecer persistencia en el sistema.

> **ES:** Servidor Windows con IIS que esconde credenciales en su blog. Entrando por el usuario `wade` se explota el CVE-2019-1388 (UAC) para elevar a `nt authority\system`, migrar a Meterpreter y dejar persistencia.
> **EN:** A Windows IIS box hiding credentials on its blog. Logging in as user `wade` allows exploiting CVE-2019-1388 (UAC) to escalate to `nt authority\system`, migrate to Meterpreter and establish persistence.

## Solucionario

### Task 1: Introducción / Intro
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| Pregunta introductoria de la sala | `No answer needed` |

### Task 2: Enumeración y acceso inicial / Enumeration and initial access
**Explicación:** El escaneo inicial muestra el servidor `IIS Windows Server` con dos puertos abiertos. En el servidor web se encuentra el directorio `/retro` con un blog. El blog revela el nombre de usuario `wade` y, tras fuerza bruta, la contraseña `parzival`. Con estas credenciales se entra y se obtiene el user flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuántos puertos están abiertos en la máquina? | `2` |
| ¿Qué servidor web está ejecutando la máquina? | `IIS Windows Server` |
| ¿Cuál es el nombre del directorio disponible en el servidor web? | `/retro` |
| ¿Cuál es el nombre de usuario identificado? | `wade` |
| ¿Cuál es la contraseña? | `parzival` |
| ¿Cuál es el user flag? | `THM{HACK_PLAYER_ONE}` |

### Task 3: Explotación del CVE / Exploitation (CVE)
**Explicación:** Se localiza el binario vulnerable `hhupd` y se explota el CVE-2019-1388, una vulnerabilidad de UAC que permite elevar privilegios a `nt authority\system` abriendo el diálogo de elevación y ayudando a un binario firmado. Con ello se captura el root flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el CVE de la vulnerabilidad UAC? | `CVE-2019-1388` |
| ¿Cuál es la ruta/nombre del archivo vulnerable? | `hhupd` |
| ¿Qué pregunta de explotación se plantea? | `No answer needed` |
| ¿Bajo qué usuario se eleva el proceso? | `nt authority\system` |
| ¿Cuál es el root flag? | `THM{COIN_OPERATED_EXPLOITATION}` |

### Task 4: Persistencia / Persistence
**Explicación:** Con Metasploit se convierte la sesión en Meterpreter, se migra el proceso y se comprueba el número de sesiones del sistema. A continuación se lanza el módulo de persistencia con el comando `run persistence -X` para mantener el acceso.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué pregunta de migración se plantea? | `No answer needed` |
| ¿Cuántas sesiones/vistas se obtienen en la configuración del Meterpreter? | `2` |
| ¿Qué pregunta de configuración se plantea? | `No answer needed` |
| ¿Qué pregunta de configuración se plantea? | `No answer needed` |
| ¿Qué pregunta de configuración se plantea? | `No answer needed` |
| ¿Qué comando lanza la persistencia en el sistema? | `run persistence -X` |
| ¿Qué pregunta de cierre se plantea? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta introductoria de la sala | `No answer needed` |
| 2 | Número de puertos abiertos | `2` |
| 3 | Servidor web de la máquina | `IIS Windows Server` |
| 4 | Directorio disponible en el servidor web | `/retro` |
| 5 | Nombre de usuario identificado | `wade` |
| 6 | Contraseña del usuario | `parzival` |
| 7 | User flag | `THM{HACK_PLAYER_ONE}` |
| 8 | CVE de la vulnerabilidad UAC | `CVE-2019-1388` |
| 9 | Archivo vulnerable | `hhupd` |
| 10 | Pregunta de explotación | `No answer needed` |
| 11 | Usuario del proceso elevado | `nt authority\system` |
| 12 | Root flag | `THM{COIN_OPERATED_EXPLOITATION}` |
| 13 | Pregunta de migración | `No answer needed` |
| 14 | Sesiones/vistas del Meterpreter | `2` |
| 15 | Pregunta de configuración | `No answer needed` |
| 16 | Pregunta de configuración | `No answer needed` |
| 17 | Pregunta de configuración | `No answer needed` |
| 18 | Comando de persistencia | `run persistence -X` |
| 19 | Pregunta de cierre | `No answer needed` |

---

**Metodología:** Se comienza con un escaneo de puertos que revela el servidor `IIS Windows Server` y el directorio `/retro` en la web. La lectura del blog proporciona al usuario `wade` y su contraseña `parzival`, con la que se entra y se captura el user flag. Para la escalada se explota el CVE-2019-1388, una vulnerabilidad de UAC en el binario `hhupd`, obteniendo una shell como `nt authority\system` y el root flag. Finalmente se usa Metasploit para migrar la sesión a Meterpreter y ejecutar `run persistence -X` y asegurar la persistencia.

### Cadena de ataque / Attack Chain

```text
nmap -> 2 puertos / IIS Windows Server -> /retro -> wade:parzival -> user flag -> CVE-2019-1388 -> hhupd -> nt authority\system -> root flag -> Meterpreter -> run persistence -X
```

**Learning chain:** nmap scanning --> web enumeration --> credential discovery --> user flag --> UAC bypass (CVE-2019-1388) --> SYSTEM privileges --> root flag --> Meterpreter migration --> persistence (run persistence -X)

**Lección:** *Las vulnerabilidades de UAC en binarios de confianza permiten elevar a SYSTEM sin credenciales adicionales; una vez comprometido el sistema, la persistencia es clave para mantener el acceso.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1548.002 (Abuse Elevation Control Mechanism: Bypass User Account Control), T1134 (Access Token Manipulation), T1547 (Boot or Logon Autostart Execution)

**Fuente:** [TryHackMe - Blaster](https://tryhackme.com/room/blaster)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.