# Report Writing for SOC L2

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `reportwritingsocl2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/reportwritingsocl2) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + dos simuladores estáticos (C-Level App y DFIR App) |
| **Componentes** | Comunicación L1 vs L2 / reportes a C-level y a clientes MSSP / handover notes para DFIR / uso responsable de GenAI / SAL2 |
| **Impacto** | Habilidades blandas del SOC: escribir lo que los jefes entienden (C-level), lo que el cliente necesita (MSSP) y lo que un DFIR puede ejecutar (Attack Timeline con IoCs) |

---

**Contexto:** En L2 el trabajo cambia: además de triar alertas, **escribes reportes** hacia fuera del SOC. Para **C-level**: foco en negocio, tono formal, sin jerga, hechos, no alarmismo. Para **clientes MSSP**: canal oficial (email con copia), y nunca parar el análisis ni aislar al equipo: **Yea / Yea**. Para **DFIR**: notas técnicas sin adornos (audiencia técnica → **Nay**), con la **Attack Timeline** historiada y raw indicators. Si usas **GenAI**: dale **context** (perfil del cliente, activos, TI, contexto histórico, notas de monitorización) y **no te apoyes al 100%** en crítico (**Nay**). Los dos simuladores corrigen errores en un reporte ejecutivo y en unas handover notes.

## Solucionario

### Task 1: Introducción / Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's go! | `No answer needed` |

**Explicación:** L2 = comunicación + técnica; room del nivel SOC Level 2.

### Task 2: Comunicación L1 vs L2 / L1 vs L2 Communication

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which SOC tier, L1 or L2, **bridges the SOC and the outside world**? | `L2` |
| 2 | What do L2 analysts write to summarize SOC findings (one word)? | `Reports` |

**Explicación:**
- **L2:** comunica con C-level, clientes MSSP y DFIR/CTI.
- **Reports:** el entregable es el reporte formal.

### Task 3: Comunicación a Liderazgo / Leadership Communication *(static-site)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Should you **complete the analysis** after sharing the initial SOC report? (Yea/Nay) | `Yea` |
| 2 | Should you **keep your team informed** about the ongoing communication? (Yea/Nay) | `Yea` |
| 3 | What flag did you receive after completing the task's challenge? | `???` *(se obtiene al corregir el reporte ejecutivo en el simulador; se captura en vivo — ver Metodología)* |

**Explicación:**
- **Simulador:** `https://static-labs.tryhackme.cloud/apps/soc-l2-report-clevel` — "SOC L2 Report C-Level App". Revisa el reporte ejecutivo y corrige los fragmentos resaltados pulsando sobre ellos.
- **Errores típicos a corregir:** *missing recipient* (falta incluir al equipo en el email) · *missing context - a login* (el login no identifica servicio: "¿VPN? ¿M365 portal?") · *data wipe del laptop de Tim Balmer* (respuesta demasiado dura para lo conocido) · *don't ignore this email* (tono/acción incorrecta para el destinatario no técnico).
- **Reglas C-level:** focus on business · formal tone · keep it simple (sin jerga) · talk in facts · don't panic.

### Task 4: Comunicación SOC/DFIR / SOC/DFIR Communication *(static-site)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are L2 handover notes meant for a **non-technical** audience? (Yea/Nay) | `Nay` |
| 2 | What part of the handover notes lists your findings **chronologically**? | `Attack Timeline` |
| 3 | What flag did you receive after completing the task's challenge? | `???` *(se obtiene al corregir el DFIR handover en el simulador; se captura en vivo)* |

**Explicación:**
- **Simulador:** `https://static-labs.tryhackme.cloud/apps/soc-l2-report-dfir` — "SOC L2 Report DFIR App". Corrige las notas de handover al DFIR (TrySaveMe).
- **DFIR audience:** experta · **Nay** a "no técnica"; quieren hechos, TTPs y artifacts. Componentes: Incident Context, **Attack Timeline** (cronológico), Attack Scope, Performed Actions, Raw Indicators.
- **Ejemplo de timeline:** `Mar 6, 07:15 UTC | WEB-01 | Automated HTTP recon from 204.17.98.56...` → `07:32 | shell.php upload en /feedback/form.php` → C2 (beacon.exe), etc.

### Task 5: Uso Responsable de IA / Responsible AI Usage

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What should you provide in the AI prompt to get the best reports? | `Context` |
| 2 | Should you fully rely on GenAI for critical decision making? (Yea/Nay) | `Nay` |

**Explicación:**
- **Context:** perfil del cliente, detalles de activos, threat intelligence, contexto histórico, notas de monitorización y requisitos de estilo/tamaño.
- **Nay:** no delegar decisiones críticas; la IA alucina (p. ej. marcar `explorer.exe` por comportamiento malicioso o recomendar aislamiento destructivo).

### Task 6: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room! | `No answer needed` |

**Explicación:** Consejos SAL2: investigar completo ANTES de escribir, fusionar informe inicial+final para C-level, analizar todos los logs antes del handover al DFIR.

**Metodología:**
1. **Comunicación L1 vs L2:** L2 comunica con C-level, clientes MSSP y DFIR/CTI; el entregable es el reporte formal.
2. **Simulador C-Level:** abrir `https://static-labs.tryhackme.cloud/apps/soc-l2-report-clevel` — "SOC L2 Report C-Level App". Revisar el reporte ejecutivo y corregir los fragmentos resaltados pulsando sobre ellos: *missing recipient* (falta incluir al equipo en el email), *missing context - a login* (el login no identifica servicio: "¿VPN? ¿M365 portal?"), *data wipe del laptop de Tim Balmer* (respuesta demasiado dura para lo conocido) y *don't ignore this email* (tono/acción incorrecta para el destinatario no técnico). Reglas C-level: focus on business, formal tone, keep it simple (sin jerga), talk in facts, don't panic.
3. **Q3 de Task 3:** el flag se muestra al corregir el reporte ejecutivo en el simulador; se captura en vivo (no precargado porque lo genera el simulador según tus correcciones).
4. **Simulador DFIR:** abrir `https://static-labs.tryhackme.cloud/apps/soc-l2-report-dfir` — "SOC L2 Report DFIR App". Corregir las notas de handover al DFIR (TrySaveMe). La audiencia DFIR es experta: **Nay** a "no técnica"; quieren hechos, TTPs y artifacts. Componentes: Incident Context, **Attack Timeline** (cronológico), Attack Scope, Performed Actions, Raw Indicators. Ejemplo de timeline: `Mar 6, 07:15 UTC | WEB-01 | Automated HTTP recon from 204.17.98.56...` → `07:32 | shell.php upload en /feedback/form.php` → C2 (beacon.exe), etc.
5. **Q3 de Task 4:** el flag se muestra al corregir el DFIR handover en el simulador; se captura en vivo.
6. **Responsible AI:** dar **Context** (perfil del cliente, detalles de activos, threat intelligence, contexto histórico, notas de monitorización y requisitos de estilo/tamaño) y **Nay** a delegar decisiones críticas: la IA alucina (p. ej. marcar `explorer.exe` por comportamiento malicioso o recomendar aislamiento destructivo).
7. **Cierre (SAL2):** investigar completo ANTES de escribir, fusionar informe inicial+final para C-level, analizar todos los logs antes del handover al DFIR.

```
L2 -> reportes (fuera del SOC)
  -> C-level: negocio / formal / sin jerga / hechos / no pánico  (Yea-Yea)
  -> MSSP cliente: email oficial con copias, seguir analizando, equipo informado
  -> DFIR: notas técnicas (Nay) + Attack Timeline + raw indicators
  -> GenAI: dar contexto (context), no depender al 100% (Nay)
```

**Lección:** *Un reporte bien dirigido vale más que diez páginas de logs.* El mismo incidente se cuenta distinto a C-level, al cliente y al DFIR; y la IA es redacción asistida, no árbitro.

**Learning chain:** L2 → reportes (fuera del SOC) → C-level: negocio / formal / sin jerga / hechos / no pánico (Yea-Yea) → MSSP cliente: email oficial con copias, seguir analizando, equipo informado → DFIR: notas técnicas (Nay) + Attack Timeline + raw indicators → GenAI: dar contexto (context), no depender al 100% (Nay)

**MITRE ATT&CK:** No aplica técnicas ofensivas directas; se alinea con los procesos de alert triage y escalado (SAL2/Min TLP igualmente recomendable)

**Fuente:** [TryHackMe - Report Writing for SOC L2](https://tryhackme.com/room/reportwritingsocl2)
