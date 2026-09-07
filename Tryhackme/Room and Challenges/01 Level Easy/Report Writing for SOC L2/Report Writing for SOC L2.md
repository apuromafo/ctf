# Report Writing for SOC L2 [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `reportwritingsocl2`
* **Link:** https://tryhackme.com/room/reportwritingsocl2
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + dos simuladores estáticos (C-Level App y DFIR App)
* **Componentes:** Comunicación L1 vs L2 · reportes a C-level y a clientes MSSP · handover notes para DFIR · uso responsable de GenAI · SAL2
* **Impacto rol:** Habilidades blandas del SOC: escribir lo que los jefes entienden (C-level), lo que el cliente necesita (MSSP) y lo que un DFIR puede ejecutar (Attack Timeline con IoCs).

## Solucionario de Tareas / Task Solutions

> **ES:** En L2 el trabajo cambia: además de triar alertas, **escribes reportes** hacia fuera del SOC. Para **C-level**: foco en negocio, tono formal, sin jerga, hechos, no alarmismo. Para **clientes MSSP**: canal oficial (email con copia), y nunca parar el análisis ni aislar al equipo: **Yea / Yea**. Para **DFIR**: notas técnicas sin adornos (audiencia técnica → **Nay**), con la **Attack Timeline** historiada y raw indicators. Si usas **GenAI**: dale **context** (perfil del cliente, activos, TI, contexto histórico, notas de monitorización) y **no te apoyes al 100%** en crítico (**Nay**). Los dos simuladores corrigen errores en un reporte ejecutivo y en unas handover notes (flags: ver tareas).
> **EN:** At L2 the job shifts: besides triage, **you write reports** aimed outside the SOC. For **C-level**: business focus, formal tone, no jargon, facts, no panic. For **MSSP customers**: official channel (email with copies), and never stop analysis nor starve the team: **Yea / Yea**. For **DFIR**: raw technical notes (technical audience → **Nay**), with a chronological **Attack Timeline** and raw indicators. If using **GenAI** (LLM): give it **context** (customer profile, assets, TI, historical context, monitoring notes) and **do not rely 100%** on it for critical decisions (**Nay**). The two simulators fix mistakes in an executive report and in handover notes (flags: see tasks).

### Task 1 — Introducción / Introduction

* **Check:** `Let's go!`
* **ES:** L2 = comunicación + técnica; room SOC Level 2.
* **EN:** L2 = communication + technical; SOC Level 2 room.

### Task 2 — Comunicación L1 vs L2 / L1 vs L2 Communication

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which SOC tier, L1 or L2, **bridges the SOC and the outside world**? | `L2` |
| What do L2 analysts write to summarize SOC findings (one word)? | `Reports` |

* **L2:** comunica con C-level, clientes MSSP y DFIR/CTI.
* **Reports:** el entregable es el reporte formal.

### Task 3 — Comunicación a Liderazgo / Leadership Communication *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Should you **complete the analysis** after sharing the initial SOC report? (Yea/Nay) | `Yea` |
| Should you **keep your team informed** about the ongoing communication? (Yea/Nay) | `Yea` |
| What flag did you receive after completing the task's challenge? | `???` *(se obtiene al corregir el reporte ejecutivo en el simulador; se captura en vivo — ver Metodología)* |

* **Simulador / Simulator:** `https://static-labs.tryhackme.cloud/apps/soc-l2-report-clevel` — "SOC L2 Report C-Level App". Revisa el reporte ejecutivo y corrige los fragmentos resaltados pulsando sobre ellos.
* **Errores típicos a corregir / typical mistakes:** *missing recipient* (falta incluir al equipo en el email) · *missing context - a login* (el login no identifica servicio: "¿VPN? ¿M365 portal?") · *data wipe del laptop de Tim Balmer* (respuesta demasiado dura para lo conocido) · *don't ignore this email* (tono/acción incorrecta para el destinatario no técnico).
* **Reglas C-level / rules:** focus on business · formal tone · keep it simple (sin jerga) · talk in facts · don't panic.

### Task 4 — Comunicación SOC/DFIR / SOC/DFIR Communication *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Are L2 handover notes meant for a **non-technical** audience? (Yea/Nay) | `Nay` |
| What part of the handover notes lists your findings **chronologically**? | `Attack Timeline` |
| What flag did you receive after completing the task's challenge? | `???` *(se obtiene al corregir el DFIR handover en el simulador; se captura en vivo)* |

* **Simulador / Simulator:** `https://static-labs.tryhackme.cloud/apps/soc-l2-report-dfir` — "SOC L2 Report DFIR App". Corrige las notas de handover al DFIR (TrySaveMe).
* **DFIR audience:** experta · **Nay** a "no técnica"; quieren hechos, TTPs y artifacts. Componentes: Incident Context, **Attack Timeline** (cronológico), Attack Scope, Performed Actions, Raw Indicators.
* **Ejemplo de timeline / example:** `Mar 6, 07:15 UTC | WEB-01 | Automated HTTP recon from 204.17.98.56...` → `07:32 | shell.php upload en /feedback/form.php` → C2 (beacon.exe), etc.

### Task 5 — Uso Responsable de IA / Responsible AI Usage

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What should you provide in the AI prompt to get the best reports? | `Context` |
| Should you fully rely on GenAI for critical decision making? (Yea/Nay) | `Nay` |

* **Context:** perfil del cliente, detalles de activos, threat intelligence, contexto histórico, notas de monitorización y requisitos de estilo/tamaño.
* **Nay:** no delegar decisiones críticas; la IA alucina (p. ej. marcar `explorer.exe` por comportamiento malicioso o recomendar aislamiento destructivo).

### Task 6 — Conclusión / Conclusion

* **Check:** `Complete the room!`
* **ES:** Consejos SAL2: investigar completo ANTES de escribir, fusionar informe inicial+final para C-level, analizar todos los logs antes del handover al DFIR.
* **EN:** SAL2 tips: fully investigate first, merge initial+final report for C-level, analyse all logs before DFIR handover.

## Metodología / Methodology

1. **Paso / Step:** Responder conceptos T2/T5 con las secciones (L2, Reports, Context, Nay).
2. **Paso / Step:** Simulador C-Level: abrir `soc-l2-report-clevel`, leer el reporte ejecutivo y pulsar sobre cada fragmento resaltado hasta corregirlo → se muestra el flag (T3 Q3).
3. **Paso / Step:** Simulador DFIR: abrir `soc-l2-report-dfir`, corregir las handover notes (timeline, acciones, destinatarios) → flag (T4 Q3).
4. **Paso / Step:** Anotar ambos flags en la correspondiente fila del índice al capturarlos en vivo (no precargados aquí porque son generados por el simulador según tus correcciones).

### Cadena de aprendizaje / Learning Chain

```
L2 -> reportes (fuera del SOC)
  -> C-level: negocio / formal / sin jerga / hechos / no pánico  (Yea-Yea)
  -> MSSP cliente: email oficial con copias, seguir analizando, equipo informado
  -> DFIR: notas técnicas (Nay) + Attack Timeline + raw indicators
  -> GenAI: dar contexto (context), no depender al 100% (Nay)
```

**Mapeo MITRE ATT&CK / relacionado:** no aplica técnicas; es comunicación/IR. Se alinea con los procesos de alert triage y escalado (SAL2/Min TLP igualmente recomendable).

**Lección:** *Un reporte bien dirigido vale más que diez páginas de logs.* El mismo incidente se cuenta distinto a C-level, al cliente y al DFIR; y la IA es redacción asistida, no árbitro.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.