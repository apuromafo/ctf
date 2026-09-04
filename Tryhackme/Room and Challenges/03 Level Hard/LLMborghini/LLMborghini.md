# LLMborghini [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF Lab
* **Slug:** `llmborghini`
* **Link:** https://tryhackme.com/room/llmborghini
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-3-Prompt-Security\04-llmborghini\README.md`

---

## Solucionario de Tareas / Task Solutions

### Tarea 1 / Task 1: Initial Recon — Fingerprinting Enzo

Perfil del sistema antes de atacar: identificar restricciones, herramientas y el modelo subyacente del asistente "Enzo" (concierge de concesionario de coches de lujo).

**Pregunta / Question:** Based on the token-limit test, what is the output cap configured for Enzo?

**Respuesta / Answer:**

```
512 tokens
```

**Pregunta / Question:** What undisclosed tool capability was inferred from Enzo's response patterns?

**Respuesta / Answer:**

```
Email sending
```

**Pregunta / Question:** What does the model's confident hallucination of "CEO Alessandro Ferrari" confirm about Enzo's architecture?

**Respuesta / Answer:**

```
It is a general-purpose LLM with a system prompt persona, not a domain-specific fine-tuned model
```

---

### Tarea 2 / Task 2: System Prompt Extraction

**Pregunta / Question:** What is the dealer's standard margin percentage leaked from the system prompt?

**Respuesta / Answer:**

```
18%
```

**Pregunta / Question:** What "secret key" was embedded in the system prompt as a canary?

**Respuesta / Answer:**

```
LAMBO-PRONTO-7
```

**Pregunta / Question:** What JSON field contained the hidden flag when Enzo was tricked into outputting its configuration?

**Respuesta / Answer:**

```
admin_key
```

**Flag 1 extraída / Flag 1 extracted:**

```
THM{3nz0_syst3m_pr0mpt_3xtr4ct3d}
```

---

### Tarea 3 / Task 3: CRM Tool Hijacking — VIP Data Exfiltration

**Pregunta / Question:** What classic web vulnerability was replicated via Enzo's CRM tool due to unsanitized LLM outputs being passed as query parameters?

**Respuesta / Answer:**

```
SQL Injection (via Prompt-Injected Tool Parameter)
```

**Pregunta / Question:** What is the total number of customer records exfiltrated?

**Respuesta / Answer:**

```
847
```

**Pregunta / Question:** What two-step attack chain allowed the attacker to exfiltrate data off the platform?

**Respuesta / Answer:**

```
CRM bulk query via SQL injection in tool parameter → Email tool used to send results offsite
```

**Flag 2 extraída / Flag 2 extracted:**

```
THM{crm_3xf1ltr4t10n_v14_4g3nt}
```

---

### Tarea 4 / Task 4: Pricing Guardrail Bypass

**Pregunta / Question:** Which jailbreak technique was used in the first successful pricing bypass?

**Respuesta / Answer:**

```
Hypothetical/Fictional Framing
```

**Pregunta / Question:** What fake authorization mechanism was exploited in the second bypass method?

**Respuesta / Answer:**

```
Fake SYSTEM ADMIN authority escalation via crafted prefix text
```

**Pregunta / Question:** At what discount percentage was the guardrail completely circumvented?

**Respuesta / Answer:**

```
50%
```

**Flag 3 extraída / Flag 3 extracted:**

```
THM{gu4rdr41l_byp4ss_fr4udul3nt_qu0t3}
```

---

### Tarea 5 / Task 5: Final Flag — Admin Config Extraction

**Pregunta / Question:** What attack class was used in the final flag extraction — planting instructions in customer-generated data?

**Respuesta / Answer:**

```
Indirect Prompt Injection
```

**Pregunta / Question:** What is the final master flag?

**Respuesta / Answer:**

```
THM{llmb0rgh1n1_full_pwn_ch41n}
```

**Pregunta / Question:** How many distinct attack techniques were chained to achieve full system compromise?

**Respuesta / Answer:**

```
5 (fingerprinting → system prompt extraction → SQL injection via tool → guardrail bypass → indirect injection)
```

---

### Resumen de Flags / Flags Summary

| # | Descripción / Description | Valor / Value |
| --- | --- | --- |
| Flag 1 | System Prompt Extraction | `THM{3nz0_syst3m_pr0mpt_3xtr4ct3d}` |
| Flag 2 | CRM Exfiltration via Tool Hijack | `THM{crm_3xf1ltr4t10n_v14_4g3nt}` |
| Flag 3 | Pricing Guardrail Bypass | `THM{gu4rdr41l_byp4ss_fr4udul3nt_qu0t3}` |
| Flag 4 | Final Master Flag | `THM{llmb0rgh1n1_full_pwn_ch41n}` |

---

*Documentación para propósitos educativos y registro de CTF. Fuente: writeup público verificado.*
