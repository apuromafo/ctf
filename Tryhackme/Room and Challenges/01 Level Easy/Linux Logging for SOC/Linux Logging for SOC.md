# Linux Logging for SOC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | linuxloggingforsoc | [TryHackMe](https://tryhackme.com/room/linuxloggingforsoc) | 01 Level Easy | THM | journald, rsyslog, ntp, auth.log, execve, naabu, escaneo de red, Ubuntu | Fundamentos del logging en Linux para un SOC: recolección, fuentes de log, auditoría y detección de actividad maliciosa |

---

**Contexto:** Sala que enseña a un analista SOC los fundamentos del registro de eventos en Linux: fuentes de configuración de tiempo (NTP), logs de autenticación, auditoría del kernel (`execve`), versionado de paquetes y detección de escaneos de red con herramientas como `naabu`.

> **EN:**
> 1. No answer needed
> 2. 1. ntp.ubuntu.com
>    2. Becoming mindful.
> 3. 1. 10.14.94.82
>    2. xerxes
> 4. 1. 6.0-28ubuntu4.1
>    2. THM{note_to_remember}
> 5. 1. execve
>    2. Nay
> 6. 1. 08/13/25 18:36:54
>    2. naabu_2.3.5_linux_amd64.zip
>    3. 192.168.50.0/24
> 7. No answer needed

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta el objetivo de la sala: entender qué registra Linux, dónde se guardan esos logs y cómo un SOC los utiliza para detectar actividad maliciosa.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Sincronización de tiempo / Time synchronization

**Explicación:** La sincronización de tiempo vía NTP es crítica para correlacionar logs. Se identifica la fuente de tiempo automática del sistema (provisión automática de la máquina y la forma en que se autoconfigura).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué servidor NTP se usa por defecto? / Which NTP server is used by default? | `ntp.ubuntu.com` |
| 2 | ¿Qué frase describe el estado del servicio? / What phrase describes the service state? | `Becoming mindful.` |

### Task 3: Logs de autenticación / Authentication logs

**Explicación:** Se analizan los logs de autenticación del sistema, aislados por IP de origen y usuario implicado, para detectar accesos no autorizados.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué IP aparece en los intentos de autenticación? / Which IP appears in the authentication attempts? | `10.14.94.82` |
| 2 | ¿Qué usuario está implicado? / Which user is involved? | `xerxes` |

### Task 4: Versiones y auditoría / Versions and auditing

**Explicación:** Se identifica la versión exacta del kernel o paquetes instalados para conocer las CVE aplicables y se localiza una flag oculta en la configuración de auditoría del sistema.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuál es la versión identificada? / Which version is identified? | `6.0-28ubuntu4.1` |
| 2 | ¿Qué flag se encuentra? / What flag is found? | `THM{note_to_remember}` |

### Task 5: Auditoría del kernel / Kernel auditing

**Explicación:** Se revisan los registros de auditoría del kernel (`auditd`). El campo `execve` registra la ejecución de procesos y se determina si el sistema cuenta con la configuración de auditoría adecuada.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué tipo de evento registra la ejecución de comandos? / What event type records command execution? | `execve` |
| 2 | ¿El audit está habilitado de la forma esperada? / Is auditing enabled as expected? | `Nay` |

### Task 6: Detección de escaneos / Scanning detection

**Explicación:** Se detecta actividad de reconocimiento ofensivo: un escaneo de red lanzado con una herramienta recién descargada (`naabu`) desde el rango `192.168.50.0/24`, con su timestamps exacto.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuándo se inició el escaneo? / When did the scan start? | `08/13/25 18:36:54` |
| 2 | ¿Qué herramienta se descargó para escanear? / Which tool was downloaded to scan? | `naabu_2.3.5_linux_amd64.zip` |
| 3 | ¿Qué rango de red se escaneó? / Which network range was scanned? | `192.168.50.0/24` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala: se repasa cómo la correcta recolección y análisis de los logs de Linux permite a un SOC reconstruir y detectar la actividad maliciosa.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Verificar la configuración NTP (`ntpd`/`chrony`) para garantizar timestamps fiables en la correlación. Revisar los logs de autenticación y filtrar por IP y usuario. Comprobar las versiones del kernel y paquetes instalados. Examinar los registros de `auditd`, centrándose en los eventos `execve` que capturan la ejecución de procesos y binarios. Por último, correlacionar descargas recientes (como `naabu_2.3.5_linux_amd64.zip`) con conexiones salientes para detectar escaneos activos contra `192.168.50.0/24`.

### Cadena de ataque / Attack Chain

Sincronización NTP → logs de autenticación → identificación de usuario sospechoso → versionado de paquetes → auditoría del kernel (execve) → descarga de `naabu` → escaneo de `192.168.50.0/24` → detección temprana por el SOC

**Learning chain:** NTP → auth logs → 10.14.94.82 → xerxes → kernel version → execve → naabu_2.3.5 → 192.168.50.0/24

**Lección:** *Para un SOC, la fiabilidad del análisis depende de registros bien configurados: la sincronización NTP y la auditoría del kernel (`execve`) convierten logs aparentemente triviales en la cadena de evidencias que delata un escaneo o una intrusión.*

**MITRE ATT&CK:** T1059.004 (Unix Shell), T1046 (Network Service Discovery), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Linux Logging for SOC](https://tryhackme.com/room/linuxloggingforsoc)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.