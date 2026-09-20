# Eviction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `eviction` | [TryHackMe - Eviction](https://tryhackme.com/room/eviction) | `01 Level Easy` | THM | MITRE ATT&CK, ATT&CK Navigator, APT, threat intelligence, SOC | Defensive — análisis de TTPs de un APT con ATT&CK Navigator |

> **Objeto:** Utilizar el MITRE ATT&CK Navigator sobre la capa de un actor APT para identificar las TTPs de la intrusión a E-Corp y saber si el grupo ya ha comprometido la red.

---

**Contexto:** La sala Eviction forma parte del módulo Cyber Defense Frameworks del path SOC Level 1. La analista Sunny, en E-Corp, recibe un informe de inteligencia sobre el grupo APT28 y debe usar el MITRE ATT&CK Navigator para identificar las TTPs del actor a lo largo de todo el ciclo de ataque: reconocimiento, desarrollo de recursos, ejecución, persistencia, evasión, descubrimiento, movimiento lateral, recolección y exfiltración.

> **ES:** Sala de defensa (SOC Level 1): con la capa MITRE ATT&CK Navigator de APT28 se identifican las técnicas del actor de principio a fin del kill chain.
>
> **EN:** Defensive room (SOC Level 1): using the MITRE ATT&CK Navigator layer for APT28 to identify the actor's techniques across the whole attack lifecycle.

## Solucionario

### Task 1: Investigación del APT / APT Investigation

**Explicación:** Usando la capa del MITRE ATT&CK Navigator del grupo APT, se responde qué técnica comparte Reconocimiento y Acceso Inicial, qué cuentas podría comprometer el actor, cómo ejecuta código, con qué persiste, descubre, se mueve lateralmente, recolecta y exfiltra información.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Técnica usada tanto para reconocimiento como para acceso inicial | `Spearphishing link` |
| 2 | Cuentas que el APT podría comprometer al desarrollar recursos | `Email accounts` |
| 3 | Técnicas de ejecución por parte del usuario (dos) | `Malicious file and malicious link` |
| 4 | Intérpretes de comandos y scripting observados (dos) | `Powershell and Windows Command shell` |
| 5 | Mecanismo de persistencia en el registro | `Registry run keys` |
| 6 | Herramienta de ejecución utilizada en el host | `Rundll32` |
| 7 | Técnica de descubrimiento de red | `Network sniffing` |
| 8 | Movimiento lateral sobre recursos compartidos | `SMB/Windows Admin shares` |
| 9 | Repositorio de recolección de datos | `Sharepoint` |
| 10 | Mecanismos de exfiltración (dos) | `external proxy and multi-hop proxy` |
| 11 | Cierre de la investigación | `No answer needed` |

---

**Metodología:** Se carga la capa del MITRE ATT&CK Navigator proporcionada por la sala y se recorren las tácticas del actor APT dentro del rango completo del ataque a E-Corp. Para cada pregunta se correlaciona la táctica indicada con las técnicas presentes en la capa, anotando las sub-técnicas exactas y las respuestas que verifica la plataforma.

### Cadena de ataque / Attack Chain

Reconocimiento (Spearphishing link) → Desarrollo de recursos (Email accounts) → Acceso inicial/Phishing → Ejecución (Malicious file & link; PowerShell; Rundll32) → Persistencia (Registry run keys) → Descubrimiento (Network sniffing) → Movimiento lateral (SMB/Windows Admin shares) → Recolección (SharePoint) → Exfiltración (proxy externo y multi-hop).

**Learning chain:** Threat intelligence → MITRE ATT&CK Navigator → APT TTPs → Attack lifecycle for SOC analysts

**Lección:** *El MITRE ATT&CK Navigator convierte la inteligencia de amenazas en un mapa accionable: conocer las TTPs de un APT permite perseguir proactivamente sus huellas dentro de la red antes de que complete su misión.*

**MITRE ATT&CK:** T1598.003 - Phishing for Information: Spearphishing Link, T1586.002 - Compromise Accounts: Email Accounts, T1204.002 - User Execution: Malicious File, T1204.001 - User Execution: Malicious Link, T1059.001 - Command and Scripting Interpreter: PowerShell, T1218.011 - System Binary Proxy Execution: Rundll32, T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys, T1040 - Network Sniffing, T1021.002 - Remote Services: SMB/Windows Admin Shares, T1213 - Data from Information Repositories, T1090.003 - Proxy: Multi-hop Proxy

**Fuente:** [TryHackMe - Eviction](https://tryhackme.com/room/eviction)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.