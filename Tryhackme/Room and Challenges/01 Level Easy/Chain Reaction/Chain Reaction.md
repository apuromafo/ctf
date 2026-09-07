# Chain Reaction

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `chainreaction-bt` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/chainreaction-bt) |
| **Sección** | Supply Chain Security |
| **Fuente** | THM |
| **Componentes** | npm supply chain, Axios, postinstall, persistence, MITRE |
| **Impacto** | Alto — cadena completa de ataque de supply chain en dependencias npm con persistencia a nivel de sistema |

---

**Contexto:** Chain Reaction explora un escenario de ataque de supply chain completo: un paquete npm aparentemente legítimo (Axios) ha sido comprometido con una dependencia maliciosa que ejecuta código post-instalación, establece persistencia y conecta a un servidor C2. El jugador debe rastrear la cadena de compromiso desde npm hasta la persistencia en el sistema, identificando cada técnica MITRE ATT&CK involucrada.

## Solucionario

### Task 1: npm Supply Chain Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the version of the installed Axios library? | `1.14.1` |
| 2 | What suspicious package does Axios depend on? | `typing-coreutils@1.6.4` |
| 3 | What command is run after the package installation? | `node postinst.js` |

### Task 2: Payload Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the encryption key for the JS strings? | `OrDeR_7077` |
| 2 | What is the full C2 URL found in the JS file? | `http://sfrquack.thm:8000/1502068` |
| 3 | What string is sent to the C2 to initiate the payload download? | `pypi.org/latest` |

### Task 3: Persistence & MITRE

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What absolute path was the initial Python payload dropped to? | `/tmp/.promise.py` |
| 2 | What is its command line shown by the ps aux command? | `unattended-upgr /home/ubuntu/.local/apt.conf` |
| 3 | What MITRE ATT&CK sub-technique did it use for persistence? | `T1546.004` |
| 4 | What's the decoded flag sent to the C2 after the loop completes? | `THM{audit_your_deps!}` |

---

**Metodología:** Instalación de dependencia npm sospechosa → análisis de `package.json` y scripts postinstall → deobfuscación de JavaScript ofuscado (XOR con clave `OrDeR_7077`) → rastreo de conexión C2 → análisis del payload Python descargado → verificación de persistencia via systemd/apt config → mapeo de técnicas MITRE ATT&CK → obtención del flag final.
**Learning chain:** npm dependency audit → postinstall hook analysis → JS string deobfuscation → C2 infrastructure tracing → payload download chain → Linux persistence mechanisms → MITRE mapping
**MITRE ATT&CK:** T1195.002 (Supply Chain Compromise: Software Supply Chain), T1059.006 (Python), T1071.001 (Web Protocols), T1546.004 (Unix Shell Configuration Modification)
**Fuente:** [TryHackMe - Chain Reaction](https://tryhackme.com/r/room/chainreaction-bt)
