# Phishing - Phishmas Greetings

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `spottingphishing-aoc2025-r2g4f6s8l0` | https://tryhackme.com/room/spottingphishing-aoc2025-r2g4f6s8l0 | Advent of Cyber 2025 | TryHackMe | Phishing, email classification, SOC | Alarmed — Multiple phishing campaigns targeting employees |

---

**Contexto:** Durante Advent of Cyber 2025 Day 12, el equipo SOC clasifica una serie de correos electrónicos sospechosos durante la campaña Phishmas. Cada email presenta indicadores distintivos de phishing — desde suplantación de identidad hasta spam — y cada clasificación correcta revela un flag de verificación.

> **ES:** Actúa como analista SOC durante la campaña Phishmas: clasifica cada uno de los 6 correos sospechosos según su tipo (phishing, spam, suplantación...) y obtén el flag de verificación de cada clasificación correcta.
> **EN:** Act as a SOC analyst during the Phishmas campaign: classify each of the 6 suspicious emails by type (phishing, spam, impersonation...) and retrieve the verification flag for each correct classification.

## Solucionario

### Task 1: Clasificación de Emails de Phishing

**Explicación:** El room presenta 6 correos a clasificar. Cada correo debe analizarse por sus indicadores: el 1º y el 3º son suplantación de identidad/impersonation, el 4º contiene un clic sospechoso, el 5º es spam y el 6º cierra la serie. Cada clasificación correcta devuelve un flag, de modo que se acumulan los 6 flags de verificación que confirman el análisis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Classify the 1st email flag | `THM{yougotnumber1-keep-it-going}` |
| 2 | Classify the 2nd email flag | `THM{nmumber2-was-not-tha-thard!}` |
| 3 | Classify the 3rd email flag | `THM{Impersonation-is-areal-thing-keepIt}` |
| 4 | Classify the 4th email flag | `THM{Get-back-SOC-mas!!}` |
| 5 | Classify the 5th email flag | `THM{It-was-just-a-sp4m!!}` |
| 6 | Classify the 6th email flag | `THM{number6-is-the-last-one!-DX!}` |

---

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

### Cadena de ataque / Attack Chain

```text
Campaña Phishmas -> 6 correos sospechosos -> análisis SOC (remitente, enlaces, urgencia, impersonation, spam) -> clasificación -> flag por correo
```

**Learning chain:** Email Header Analysis → Phishing Indicators → SOC Classification → Social Engineering Recognition

**Lección:** *Detectar phishing es clasificar en serie: remitente, enlaces, urgencia y estilo del contenido permiten etiquetar cada correo y, en entornos SOC, cada clasificación bien fundamentada es un indicador accionable, representado aquí como un flag.*

**MITRE ATT&CK:** T1566.001 — Phishing: Spearphishing Link; T1566.002 — Phishing: Spearphishing Attachment

**Fuente:** [TryHackMe - Phishing - Phishmas Greetings](https://tryhackme.com/r/room/spottingphishing-aoc2025-r2g4f6s8l0)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.