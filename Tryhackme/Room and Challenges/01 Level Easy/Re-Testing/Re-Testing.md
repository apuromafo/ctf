# Re-Testing

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `retesting` | https://tryhackme.com/room/retesting | Reporting | TryHackMe | SOW, remediation window, risk acceptance, CVEs, SQLi verification | Medium |

---

**Contexto:** Este room aborda el proceso de re-testing tras una fase de remediación, cubriendo cómo verificar si las vulnerabilidades reportadas han sido corregidas correctamente. Aprenderemos a distinguir entre re-test y reevaluación completa, a leer el SOW para entender el alcance del re-test, y a ejecutar pruebas de verificación (como SQLi) contra payloads originales y variantes para determinar si el fix es efectivo. También vemos casos donde un vendor patch es incompleto.

> **ES:** "Re-Testing" — cómo verificar que las vulnerabilidades fueron corregidas: re-test vs reevaluación, revisión del SOW, ventana de remediación, aceptación de riesgo y verificación práctica de SQLi con payloads originales y variantes.
> **EN:** "Re-Testing" — how to verify that vulnerabilities were fixed: re-test vs full reassessment, SOW review, remediation window, risk acceptance and hands-on SQLi verification with original and variant payloads.

## Solucionario

### Task 1: Introducción al Re-Testing / Re-Testing Introduction

**Explicación:** La tarea establece cuándo corresponde hacer un re-test. Como el cliente reconstruyó toda su plataforma e-commerce tras la remediación, debe solicitar una reevaluación completa (`Full reassessment`). El documento que determina si el re-test está incluido en el compromiso original, y que hay que revisar antes de que termine la evaluación inicial, es el SOW. El periodo entre la entrega del informe y el re-test, durante el cual el cliente aplica los fixes, se denomina ventana de remediación (`Remediation window`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A client rebuilt their entire e-commerce platform after remediation. Should they request a re-test or a full reassessment? (Answer Format: two words) | `Full reassessment` |
| 2 | What document governs whether re-testing is included in the original engagement, and should be reviewed before the original assessment ends? (Answer Format: abbreviation) | `SOW` |
| 3 | What is the term for the period between report delivery and the re-test, during which the client implements fixes? (Answer Format: two words) | `Remediation window` |

### Task 2: Resultados del Re-Test / Understanding Re-Test Outcomes

**Explicación:** Los posibles resultados de un re-test se registran en el informe. Si el cliente firma un documento formal en el que declara que no corregirá un hallazgo de severidad media por restricciones de negocio, el resultado se registra como `Risk Accepted`. Si el payload SQLi original `' OR '1'='1` queda bloqueado pero la variante `' OR 1=1--` sigue devolviendo todos los registros de usuarios, el resultado del hallazgo es `Fail`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A client signs a formal document stating they will not fix a medium-severity finding due to business constraints. What is this outcome recorded as in the re-test report? (Answer Format: two words) | `Risk Accepted` |
| 2 | The original SQLi payload `' OR '1'='1` is now blocked, returning a generic error. A variant payload `' OR 1=1--` still returns all user records. What is the re-test outcome for this finding? (Answer Format: one word) | `Fail` |

### Task 3: Análisis de Vulnerabilidades - Parches Incompletos / Vulnerability Analysis - Incomplete Patches

**Explicación:** Los vendor patches también pueden ser incompletos: CVE-2023-43208 surgió directamente de un parche incompleto de un CVE anterior (CVE-2023-37679). Este tipo de fallo entra dentro del pitfall denominado `Incomplete Vendor Patches`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | CVE-2023-43208 arose directly from an incomplete patch for which earlier CVE? (Answer Format: CVE-YYYY-NNNNN) | `CVE-2023-37679` |
| 2 | Vendor patches themselves are sometimes incomplete, which pitfall would this failure lie in? | `Incomplete Vendor Patches` |

### Task 4: Escenario de Re-Test / Re-Test Scenario

**Explicación:** En el escenario práctico se re-testea el hallazgo F-01 (SQLi). Enviar el payload original `' OR '1'='1` contra el formulario de login devuelve el código HTTP `200`. Enviar la variante `' OR 1=1--` en el campo de username redirige a `/dashboard`, lo que demuestra que el fix solo bloquea el payload exacto. El resultado global del re-test para F-01 es `Fail`, y en la tabla de estado de hallazgos del informe, la columna que captura el fix específico que aplicó el desarrollador es `Notes`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the original SQLi payload (`' OR '1'='1`) against the login form. What HTTP response code does the application return? (Answer Format: three-digit number) | `200` |
| 2 | Submit the variant payload `' OR 1=1--` in the username field. What URL path does the application redirect to on success? (Answer Format: /path) | `/dashboard` |
| 3 | Based on your testing, what is the overall re-test result for Finding F-01? (Answer Format: one word) | `Fail` |
| 4 | In the re-test report findings status table, which column captures the specific fix the developer applied (e.g., "Blocklist added for specific payload")? (Answer Format: column name) | `Notes` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A client rebuilt their entire e-commerce platform after remediation. Should they request a re-test or a full reassessment? (Answer Format: two words) | `Full reassessment` |
| 2 | What document governs whether re-testing is included in the original engagement, and should be reviewed before the original assessment ends? (Answer Format: abbreviation) | `SOW` |
| 3 | What is the term for the period between report delivery and the re-test, during which the client implements fixes? (Answer Format: two words) | `Remediation window` |
| 4 | A client signs a formal document stating they will not fix a medium-severity finding due to business constraints. What is this outcome recorded as in the re-test report? (Answer Format: two words) | `Risk Accepted` |
| 5 | The original SQLi payload `' OR '1'='1` is now blocked, returning a generic error. A variant payload `' OR 1=1--` still returns all user records. What is the re-test outcome for this finding? (Answer Format: one word) | `Fail` |
| 6 | CVE-2023-43208 arose directly from an incomplete patch for which earlier CVE? (Answer Format: CVE-YYYY-NNNNN) | `CVE-2023-37679` |
| 7 | Vendor patches themselves are sometimes incomplete, which pitfall would this failure lie in? | `Incomplete Vendor Patches` |
| 8 | Submit the original SQLi payload (`' OR '1'='1`) against the login form. What HTTP response code does the application return? (Answer Format: three-digit number) | `200` |
| 9 | Submit the variant payload `' OR 1=1--` in the username field. What URL path does the application redirect to on success? (Answer Format: /path) | `/dashboard` |
| 10 | Based on your testing, what is the overall re-test result for Finding F-01? (Answer Format: one word) | `Fail` |
| 11 | In the re-test report findings status table, which column captures the specific fix the developer applied (e.g., "Blocklist added for specific payload")? (Answer Format: column name) | `Notes` |

---

**Metodología:** El room se desarrolla en tres fases: primero se establecen los conceptos del re-testing (SOW, ventana de remediación, aceptación de riesgo), luego se analizan patrones de fallos comunes (patches de vendor incompletos con CVE-2023-37679 → CVE-2023-43208), y finalmente se ejecuta un escenario práctico de re-test contra SQLi donde se verifica que el fix original solo bloquea el payload exacto pero falla ante variantes, resultando en un Fail.

### Cadena de ataque / Attack Chain

```text
Entrega del informe -> Ventana de remediación -> Revisión del SOW -> Re-test con payload original y variantes -> Verificación de CVEs / vendor patches -> Resultado (Risk Accepted o Fail) -> Estado final en la tabla del informe
```

**Learning chain:** SOW Review → Remediation Window → Risk Acceptance → Payload Re-test → CVE Verification → Report Status

**Lección:** *Un fix que solo bloquea el payload exacto reportado no es suficiente: el re-test debe probar variantes del payload original para confirmar que la vulnerabilidad quedó realmente corregida.*

**MITRE ATT&CK:** N/A

**Fuente:** [TryHackMe - Re-Testing](https://tryhackme.com/room/retesting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.