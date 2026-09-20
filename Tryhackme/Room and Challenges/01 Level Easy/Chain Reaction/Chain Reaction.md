# Chain Reaction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `chainreaction-bt` | [TryHackMe](https://tryhackme.com/r/room/chainreaction-bt) | Supply Chain Security | THM | npm supply chain, Axios, postinstall, persistence, MITRE | Alto — cadena completa de ataque de supply chain en dependencias npm con persistencia a nivel de sistema |

---

**Contexto:** Chain Reaction explora un escenario de ataque de supply chain completo: un paquete npm aparentemente legítimo (Axios) ha sido comprometido con una dependencia maliciosa que ejecuta código post-instalación, establece persistencia y conecta a un servidor C2. El jugador debe rastrear la cadena de compromiso desde npm hasta la persistencia en el sistema, identificando cada técnica MITRE ATT&CK involucrada.

> **ES:** Análisis de una cadena de suministro npm comprometida: dependencia maliciosa de Axios, script postinstall, strings ofuscadas (XOR), conexión C2, payload Python descargado, persistencia y mapeo MITRE ATT&CK.

> **EN:** Analysis of a compromised npm supply chain: malicious Axios dependency, postinstall script, obfuscated strings (XOR), C2 connection, downloaded Python payload, persistence and MITRE ATT&CK mapping.

## Solucionario

### Task 1: npm Supply Chain Analysis / Análisis de la cadena de suministro npm

**Explicación:** Se inspecciona el proyecto Node comprometido: la versión instalada de Axios, la dependencia sospechosa y el comando que se ejecuta tras la instalación del paquete (hook postinstall).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the version of the installed Axios library? | `1.14.1` |
| 2 | What suspicious package does Axios depend on? | `typing-coreutils@1.6.4` |
| 3 | What command is run after the package installation? | `node postinst.js` |

### Task 2: Payload Analysis / Análisis del payload

**Explicación:** Se deobfuscan los strings del JavaScript malicioso: la clave XOR que protege las cadenas, la URL del servidor C2 y el string que solicita la descarga del payload.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the encryption key for the JS strings? | `OrDeR_7077` |
| 2 | What is the full C2 URL found in the JS file? | `http://sfrquack.thm:8000/1502068` |
| 3 | What string is sent to the C2 to initiate the payload download? | `pypi.org/latest` |

### Task 3: Persistence & MITRE / Persistencia y MITRE

**Explicación:** Se rastrea el payload Python inicial descargado, la línea de comando del proceso en ps aux y la técnica MITRE utilizada para mantener la persistencia, cerrando con el flag descifrado enviado al C2.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What absolute path was the initial Python payload dropped to? | `/tmp/.promise.py` |
| 2 | What is its command line shown by the ps aux command? | `unattended-upgr /home/ubuntu/.local/apt.conf` |
| 3 | What MITRE ATT&CK sub-technique did it use for persistence? | `T1546.004` |
| 4 | What's the decoded flag sent to the C2 after the loop completes? | `THM{audit_your_deps!}` |

---

**Metodología:** Instalación de dependencia npm sospechosa → análisis de `package.json` y scripts postinstall → deobfuscación de JavaScript ofuscado (XOR con clave `OrDeR_7077`) → rastreo de conexión C2 → análisis del payload Python descargado → verificación de persistencia via systemd/apt config → mapeo de técnicas MITRE ATT&CK → obtención del flag final.

**Learning chain:** npm dependency audit → postinstall hook analysis → JS string deobfuscation → C2 infrastructure tracing → payload download chain → Linux persistence mechanisms → MITRE mapping

### Cadena de ataque / Attack Chain

Dependencia npm maliciosa (typing-coreutils) → hook postinstall → ejecución de node postinst.js → deobfuscación XOR → contacto con el C2 → descarga del payload Python → persistencia (T1546.004) → envío del flag.

**Lección:** *Una cadena de suministro comprometida entra cuando se instala una sola dependencia: auditar package-lock, desconfiar de los hooks postinstall y revisar las conexiones salientes convierten a un paquete "legítimo" en un eslabón detectado antes de que la persistencia arraigue.*

**MITRE ATT&CK:** T1195.002 (Supply Chain Compromise: Software Supply Chain), T1059.006 (Python), T1071.001 (Web Protocols), T1546.004 (Unix Shell Configuration Modification)

**Fuente:** [TryHackMe - Chain Reaction](https://tryhackme.com/room/chainreaction-bt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.