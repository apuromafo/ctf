# Phishing - Phishmas Greetings

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `spottingphishing-aoc2025-r2g4f6s8l0` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/spottingphishing-aoc2025-r2g4f6s8l0) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Phishing, email classification, SOC |
| **Impacto** | Alarmed — Multiple phishing campaigns targeting employees |

---

**Contexto:** Durante Advent of Cyber 2025 Day 12, el equipo SOC clasifica una serie de correos electrónicos sospechosos durante la campaña Phishmas. Cada email presenta indicadores distintivos de phishing — desde suplantación de identidad hasta spam — y cada clasificación correcta revela un flag de verificación.

## Solucionario

### Task 1: Clasificación de Emails de Phishing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Classify the 1st email flag | `THM{yougotnumber1-keep-it-going}` |
| 2 | Classify the 2nd email flag | `THM{nmumber2-was-not-tha-thard!}` |
| 3 | Classify the 3rd email flag | `THM{Impersonation-is-areal-thing-keepIt}` |
| 4 | Classify the 4th email flag | `THM{Get-back-SOC-mas!!}` |
| 5 | Classify the 5th email flag | `THM{It-was-just-a-sp4m!!}` |
| 6 | Classify the 6th email flag | `THM{number6-is-the-last-one!-DX!}` |

---

**Metodología:** Se clasificaron 6 correos electrónicos aplicando criterios de análisis de phishing: remitente sospechoso, enlaces fraudulentos, urgencia artificial, suplantación de identidad y contenido spam. Cada clasificación correcta generó el flag correspondiente.
**Learning chain:** Email Header Analysis → Phishing Indicators → SOC Classification → Social Engineering Recognition
**MITRE ATT&CK:** T1566.001 — Phishing: Spearphishing Link; T1566.002 — Phishing: Spearphishing Attachment
**Fuente:** [TryHackMe - Phishing - Phishmas Greetings](https://tryhackme.com/r/room/spottingphishing-aoc2025-r2g4f6s8l0)
