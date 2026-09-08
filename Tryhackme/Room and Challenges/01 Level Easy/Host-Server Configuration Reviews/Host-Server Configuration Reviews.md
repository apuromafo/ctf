# Host-Server Configuration Reviews

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `hostserverconfigurationreviews` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hostserverconfigurationreviews) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + static-site con lab de revisión de configuración |
| **Componentes** | Security baselines (CIS Benchmarks, DISA STIG) / Nessus / situational awareness / misconfigurations (SUID, permissions) / structured enumeration methodology / lab: linux-web-01 / win-dc-01 / linux-db-02 |
| **Impacto** | Auditoría de configuración: saber qué buscar, con qué framework (CIS/STIG), con qué herramienta (Nessus) y en qué orden (situational awareness primero). |

---

**Contexto:** Una revisión de configuración no es un scan de vulnerabilidades; puede no encontrar nada malo y aun así ser vulnerable. Las baselines de seguridad son **CIS Benchmarks** y **DISA STIGs** (el **Category I** del STIG es el de mayor riesgo). **Nessus** (Tenable) es el scanner comercial que incluye auditoría de compliance. Misconfigurations típicas: bits **SUID** en Linux, permisos sueltos, servicios expuestos. La metodología estructurada ordena por **situational awareness** primero (definir qué tienes antes de buscar fallos). El lab práctico usa máquinas reales con controles a auditar.

## Solucionario

### Task 1: Introducción

**Explicación:** Introducción a la configuración de hosts y servidores. Sin pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - introduction. | `No answer needed` |

### Task 2: Qué es una Configuración (Configuration Review)

**Explicación:** Un scan de vulnerabilidades no cubre misconfigurations: un servidor puede estar "clean" en vulnerabilidades y tener un SUID bit abierto o un servicio expuesto sin CVEs. Por eso la respuesta es Nay.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | **Yay or Nay:** a host that passes a vulnerability scan with no findings is guaranteed to have a secure configuration. | `Nay` |

### Task 3: Security Baselines y Frameworks

**Explicación:** Severity Categories del STIG: **I** (Category I = mayor riesgo, explotable con impacto grave), **II**, **III**. CIS usa niveles 1/2 (Level 1 = recomendado; Level 2 = high-security environments).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a **DISA STIG**, which severity category represents the **highest risk**? | `CAT I` (Category I) |

### Task 4: Automated Compliance Tooling

**Explicación:** **Nessus** (Tenable) es el scanner comercial con plantillas de escaneo de configuración/compliance (CIS Benchmarks, STIGs). Otra opción open-source es **OpenSCAP**; el room pide el nombre de Tenable → Nessus.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What **commercial vulnerability scanner**, developed by Tenable, includes compliance auditing against CIS Benchmarks? | `Nessus` |

### Task 5: Categorías de Misconfigurations

**Explicación:** **SUID / `u+s`** (Set Owner User ID): un binario con el bit set (p.ej. `/usr/bin/su`) se ejecuta como el owner (root). El abuso de SUID es una técnica clásica de escalada de privilegios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What special permission bit on **Linux** causes an executable to run with the **privileges of the file's owner**? | `SUID` (Set Owner User ID) |

### Task 6: Metodología de Enumeración Estructurada

**Explicación:** **Situational awareness / Asset discovery:** definir el inventario, versiones, servicios y configuración actual antes de auditar contra una baseline. Si no sabes qué tienes, no puedes decir si está bien configurado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In the methodology described, what is the **first phase** you should complete before checking for specific misconfigurations? | `Situational awareness` |

### Task 7: Leyendo un CIS Benchmark

**Explicación:** Sección informativa que explica cómo leer un CIS Benchmark: ID, perfil, descripción, auditoría y remediation. Sin pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - how to read a CIS Benchmark. | `No answer needed` |

### Task 8: Práctica (static-site)

**Explicación:** Lab/simulador: revisar los controles en el static-site con las tres máquinas. Las respuestas vienen del resultado de las herramientas de auditoría que usa el lab (state / actual vs. expected).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | On **linux-web-01**, what is the **actual permission value** observed on `/etc/shadow` in the failing check 7.1.5? | `0644` |
| 2 | On **linux-web-01**, how many **world-writable files** were detected by check 7.1.11? | `3` |
| 3 | On **linux-web-01**, what is the **full path** of the unexpected SUID binary found by check 7.1.13? | `/opt/admin-tools/logviewer` |
| 4 | On **win-dc-01**, what is the **minimum password length** currently configured (check 1.1.4)? | `8` |
| 5 | On **win-dc-01**, what is the current value of the **FilterAdministratorToken** registry key (check 2.3.17.1)? | `0x0` |
| 6 | How many **total checks** does **linux-db-02** pass? | `8` |

### Task 9: Conclusión

**Explicación:** Cierre de la sala: ya puedes hacer revisiones de configuración de hosts y servidores.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - I can now do host-server configuration reviews! | `No answer needed` |

---

**Metodología:**
1. Leer T2–T4 para conceptos (CIS, STIG, Nessus, Category I).
2. Categorías (T5) → SUID; methodology (T6) → situational awareness first.
3. Completar el static-site (T8) → 6 respuestas del lab con las tres máquinas.

**Learning chain:** Config review != vuln scan (Nay) → frameworks: CIS Benchmark + DISA STIG (Category I = highest) → tool: Nessus (Tenable) → misconfigurations: SUID, permissions, exposed services → methodology: situational awareness first → lab: linux-web-01 (0644 shadow, 3 world-writable, /opt/admin-tools/logviewer SUID) · win-dc-01 (password length 8, FilterAdministratorToken = 0x0) · linux-db-02 (8 checks pass).

**Lección:** *El valor de una config review es el que no ves en el scan de vulns: permisos SUID, configuraciones no referenciadas y baselines cruzadas.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1548 (Abuse Elevation Control Mechanism), T1068 (Exploitation for Privilege Escalation).

**Fuente:** [TryHackMe - Host-Server Configuration Reviews](https://tryhackme.com/room/hostserverconfigurationreviews)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
