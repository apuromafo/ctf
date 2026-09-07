# Re-Testing

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `retesting` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/retesting) |
| **Sección** | Reporting |
| **Fuente** | THM |
| **Componentes** | SOW, remediation window, risk acceptance, CVEs, SQLi verification |
| **Impacto** | Medium |

---

**Contexto:** Este room aborda el proceso de re-testing tras una fase de remediación, cubriendo cómo verificar si las vulnerabilidades reportadas han sido corregidas correctamente. Aprenderemos a distinguir entre re-test y reevaluación completa, a leer el SOW para entender el alcance del re-test, y a ejecutar pruebas de verificación (como SQLi) contra payloads originales y variantes para determinar si el fix es efectivo. También vemos casos donde un vendor patch es incompleto.
**Learning chain:** SOW Review → Remediation Window → Risk Acceptance → Payload Re-test → CVE Verification → Report Status
**MITRE ATT&CK:** N/A
**Fuente:** [TryHackMe - Re-Testing](https://tryhackme.com/r/room/retesting)

---

## Solucionario

### Task 1: Re-Testing Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A client rebuilt their entire e-commerce platform after remediation. Should they request a re-test or a full reassessment? (Answer Format: two words) | `Full reassessment` |
| 2 | What document governs whether re-testing is included in the original engagement, and should be reviewed before the original assessment ends? (Answer Format: abbreviation) | `SOW` |
| 3 | What is the term for the period between report delivery and the re-test, during which the client implements fixes? (Answer Format: two words) | `Remediation window` |

### Task 2: Understanding Re-Test Outcomes

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A client signs a formal document stating they will not fix a medium-severity finding due to business constraints. What is this outcome recorded as in the re-test report? (Answer Format: two words) | `Risk Accepted` |
| 2 | The original SQLi payload `' OR '1'='1` is now blocked, returning a generic error. A variant payload `' OR 1=1--` still returns all user records. What is the re-test outcome for this finding? (Answer Format: one word) | `Fail` |

### Task 3: Vulnerability Analysis - Incomplete Patches

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | CVE-2023-43208 arose directly from an incomplete patch for which earlier CVE? (Answer Format: CVE-YYYY-NNNNN) | `CVE-2023-37679` |
| 2 | Vendor patches themselves are sometimes incomplete, which pitfall would this failure lie in? | `Incomplete Vendor Patches` |

### Task 4: Re-Test Scenario

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the original SQLi payload (`' OR '1'='1`) against the login form. What HTTP response code does the application return? (Answer Format: three-digit number) | `200` |
| 2 | Submit the variant payload `' OR 1=1--` in the username field. What URL path does the application redirect to on success? (Answer Format: /path) | `/dashboard` |
| 3 | Based on your testing, what is the overall re-test result for Finding F-01? (Answer Format: one word) | `Fail` |
| 4 | In the re-test report findings status table, which column captures the specific fix the developer applied (e.g., "Blocklist added for specific payload")? (Answer Format: column name) | `Notes` |

---

**Metodología:** El room se desarrolla en tres fases: primero se establecen los conceptos del re-testing (SOW, ventana de remediación, aceptación de riesgo), luego se analizan patrones de fallos comunes (patches de vendor incompletos con CVE-2023-37679 → CVE-2023-43208), y finalmente se ejecuta un escenario práctico de re-test contra SQLi donde se verifica que el fix original solo bloquea el payload exacto pero falla ante variantes, resultando en un Fail.
