# Host-Server Configuration Reviews [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `hostserverconfigurationreviews`
* **Link:** https://tryhackme.com/room/hostserverconfigurationreviews
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + static-site con lab de revisión de configuración
* **Componentes:** Security baselines (CIS Benchmarks, DISA STIG) · Nessus · situational awareness · misconfigurations (SUID, permissions) · structured enumeration methodology · lab: linux-web-01 / win-dc-01 / linux-db-02
* **Impacto rol:** Auditoría de configuración: saber qué buscar, con qué framework (CIS/STIG), con qué herramienta (Nessus) y en qué orden (situational awareness primero).

## Solucionario de Tareas / Task Solutions

> **ES:** Una revisión de configuración no es un scan de vulnerabilidades; puede no encontrar nada malo y aun así ser vulnerable. Las baselines de seguridad son **CIS Benchmarks** y **DISA STIGs** (el **Category I** del STIG es el de mayor riesgo). **Nessus** (Tenable) es el scanner comercial que incluye auditoría de compliance. Misconfigurations típicas: bits **SUID** en Linux, permisos sueltos, servicios expuestos. La metodología estructurada ordena por **situational awareness** primero (definir qué tienes antes de buscar fallos). El lab práctico usa máquinas reales con controles a auditar.
> **EN:** A configuration review isn't a vulnerability scan; it can find zero findings and still be vulnerable. Security baselines are **CIS Benchmarks** and **DISA STIGs** (the highest-risk category is **Category I**). **Nessus** (Tenable) is the commercial scanner with CIS compliance checks. Common misconfigurations: Linux **SUID** bits, loose permissions, exposed services. The structured methodology orders by **situational awareness** first (know what you have before looking for issues). The practical lab uses real machines with auditable controls.

### Task 1 — Introducción / Introduction

* **ES/EN:** check sin pregunta.

### Task 2 — Qué es una Configuración / What Is a Configuration Review

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| **Yay or Nay:** a host that passes a vulnerability scan with no findings is guaranteed to have a secure configuration. | `Nay` |

* **Nay:** un scan de vulns no cubre misconfigurations (un servidor puede estar "clean" y tener SUID bit abierto o un servicio expuesto sin CVEs).

### Task 3 — Security Baselines y Frameworks

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In a **DISA STIG**, which severity category represents the **highest risk**? | `CAT I` (Category I) |

* **STIG severity / Severity Categories:** I (Category I = mayor riesgo, explotable con impacto grave), II, III. CIS usa niveles 1/2 (Level 1 = recomendado; Level 2 = high-security environments).

### Task 4 — Automated Compliance Tooling

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What **commercial vulnerability scanner**, developed by Tenable, includes compliance auditing against CIS Benchmarks? | `Nessus` |

* **Nessus:** escaneos de configuración/compliance con plantillas (CIS Benchmarks, STIGs). Otra opción open-source: **OpenSCAP**; el room pide el nombre de Tenable → Nessus.

### Task 5 — Categorías de Misconfigurations

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What special permission bit on **Linux** causes an executable to run with the **privileges of the file's owner**? | `SUID` (Set Owner User ID) |

* **SUID / `u+s`:** un binario con el bit set (p.ej. `/usr/bin/su`) se ejecuta como el owner (root). Abuso de SUID es una técnica clásica de escalada de privilegios.

### Task 6 — Metodología de Enumeración Estructurada

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In the methodology described, what is the **first phase** you should complete before checking for specific misconfigurations? | `Situational awareness` |

* **Situational awareness / Asset discovery:** definir el inventario, versiones, servicios, y configuración actual antes de auditar contra una baseline. Si no sabes qué tienes, no puedes decir si está bien configurado.

### Task 7 — Leyendo un CIS Benchmark

* **ES/EN:** sección informativa (explica cómo leer un CIS Benchmark: ID, perfil, descripción, auditoría, remediation).

### Task 8 — Práctica / Practical *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| On **linux-web-01**, what is the **actual permission value** observed on `/etc/shadow` in the failing check 7.1.5? | `0644` |
| On **linux-web-01**, how many **world-writable files** were detected by check 7.1.11? | `3` |
| On **linux-web-01**, what is the **full path** of the unexpected SUID binary found by check 7.1.13? | `/opt/admin-tools/logviewer` |
| On **win-dc-01**, what is the **minimum password length** currently configured (check 1.1.4)? | `8` |
| On **win-dc-01**, what is the current value of the **FilterAdministratorToken** registry key (check 2.3.17.1)? | `0x0` |
| How many **total checks** does **linux-db-02** pass? | `8` |

* **Lab / Simulador:** revisar los controles en el static-site. Las respuestas vienen del resultado de las herramientas de auditoría que usa el lab (state / actual vs. expected).

### Task 9 — Conclusión / Conclusion

* **Check:** `I can now do host-server configuration reviews!`

## Metodología / Methodology

1. **Paso / Step:** Leer T2–T4 para conceptos (CIS, STIG, Nessus, Category I).
2. **Paso / Step:** Categorías (T5) → SUID; methodology (T6) → situational awareness first.
3. **Paso / Step:** Completar el static-site (T8) → 6 respuestas del lab con las tres máquinas.

### Cadena de aprendizaje / Learning Chain

```
Config review != vuln scan (Nay)
  -> frameworks: CIS Benchmark + DISA STIG (Category I = highest)
  -> tool: Nessus (Tenable)
  -> misconfigurations: SUID, permissions, exposed services
  -> methodology: situational awareness first
  -> lab: linux-web-01 (0644 shadow, 3 world-writable, /opt/admin-tools/logviewer SUID)
             win-dc-01 (password length 8, FilterAdministratorToken = 0x0)
             linux-db-02 (8 checks pass)
```

**Mapeo MITRE ATT&CK:** T1078 (Valid Accounts) y T1548 (Abuse Elevation Control) si hay SUID malicioso · CWE-276 (Incorrect Default Permissions) / CWE-266 (Privilege Issues).

**Lección:** *El valor de una config review es el que no ves en el scan de vulns: permisos SUID, configuraciones no referenciadas y baselines cruzadas.*

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.