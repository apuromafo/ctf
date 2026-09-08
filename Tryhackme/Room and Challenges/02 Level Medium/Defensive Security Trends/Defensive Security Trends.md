# Defensive Security Trends

| **Dificultad** | MEDIUM | **Tipo** | Premium | **Slug** | `defensivesecuritytrends` |
| **Link** | [TryHackMe](https://tryhackme.com/room/defensivesecuritytrends) | **Sección** | 02 Level Medium | **Fuente** | Simon Taplin (writeup) |
| **Componentes** | Ransomware / Remote Access / Supply Chain / AI in SOC / Verizon DBIR / GitHub Breach / IABs | **Impacto** | Presenta las tendencias emergentes en ciberseguridad defensiva y casos reales recientes |

---

**Contexto:** Sala sobre tendencias emergentes en ciberseguridad defensiva: ransomware, acceso remoto, cadena de suministro e IA en SOC. Emerging defensive cybersecurity trends: ransomware, remote access, supply chain, AI in SOC.

## Solucionario

### Task 1: Ransomware Evolution

**Explicación:** Se analiza la evolución del ransomware y se referencia el reporte de Huntress. El tiempo promedio reportado hasta el ransomware (time-to-ransomware) es de 17 horas. Los SOC deben automatizar el triage rutinario para acelerar la respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Refer to the mentioned Huntress report. What is the reported average time-to-ransomware? | `17 hours` |
| 2 | What should SOCs do with triage routine to speed up response? | `Automate it` |

### Task 2: Remote Access Landscape

**Explicación:** Se examina el panorama del acceso remoto. La herramienta AnyDesk fue usada por el malware DarkGate. El perímetro de red en los entornos modernos es cada vez menos predecible, por lo que la respuesta a si se vuelve más predecible es Nay.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which of the mentioned remote access tools was used by DarkGate malware? | `AnyDesk` |
| 2 | Is the network perimeter becoming more predictable in modern environments? (Yea/Nay) | `Nay` |

### Task 3: Verizon 2026 DBIR Insights

**Explicación:** Se referencia el screenshot del reporte Verizon 2026. El porcentaje de incidentes que contenía cuentas válidas (Valid accounts) es 39%. A los cibercriminales que venden acceso a las redes de las organizaciones se les llama Initial Access Brokers (IAB).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Refer to the screenshot of the Verizon 2026 report. What percentage of incidents contained Valid accounts? | `39%` |
| 2 | How do you call cyber criminals who sell access to organizations' networks? | `Initial Access Brokers` |

### Task 4: Supply Chain Incidents

**Explicación:** Se explica el incidente de cadena de suministro de Vercel. El primer eslabón de la cadena de ataque fue el malware Lumma Stealer. Si un ataque de cadena de suministro golpea a una organización, los TTPs no difieren fundamentalmente de otras intrusiones (Nay) — los mismos patrones tácticos se aplican.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Refer to the explained Vercel supply chain incident. What malware was the first link in the attack chain? | `Lumma Stealer` |
| 2 | Imagine a supply chain attack hits your organization. Would attack TTPs fundamentally differ from other intrusions? (Yea/Nay) | `Nay` |

### Task 5: AI in the SOC

**Explicación:** Se analiza el rol de la IA en el SOC. La IA no debe convertirse en el tomador final de decisiones en un SOC (Nay) — debe complementar el juicio humano. El reporte señala que ninguna (None) técnica MITRE se volvió obsoleta debido a la IA.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Should AI become a final decision maker in a SOC? (Yea/Nay) | `Nay` |
| 2 | Which MITRE technique became obsolete due to AI? | `None` |

### Task 6: GitHub Breach Case Study

**Explicación:** El breach de GitHub comenzó con una infección del dispositivo de un empleado. La extensión de VS Code backdoored con un infostealer fue Nx Console. La extensión fue comprometida a través de otro ataque de cadena de suministro; el ecosistema de paquetes open-source que fue la causa raíz fue TanStack. Abriendo el reporte Verizon a la página 40 (System Intrusion), el crecimiento del uso de RMM por actores de amenaza año a año es 240%. Siguiendo a la sección de pipeline infostealer-to-ransomware, el tipo de acceso que los Initial Access Brokers venden más comúnmente es VPN.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The GitHub breach started from an infection of an employee's device. Which VS Code extension was backdoored with an infostealer? | `Nx Console` |
| 2 | The extension was compromised through another supply chain attack. Which open-source package ecosystem was the root cause? | `TanStack` |
| 3 | Open the Verizon report to page 40 (System Intrusion section). How much has threat actor RMM usage grown year-over-year? | `240%` |
| 4 | Continue to the Infostealer to ransomware pipeline section. Which access type do Initial Access Brokers most commonly sell? | `VPN` |

---

**Metodología:**
1. Revisar el reporte de Huntress sobre time-to-ransomware y la necesidad de automatizar el triage.
2. Conocer las herramientas de acceso remoto abusadas (AnyDesk por DarkGate) y la menor predecibilidad del perímetro.
3. Analizar los insights del Verizon 2026 DBIR: incidentes con cuentas válidas y el rol de los Initial Access Brokers.
4. Estudiar el incidente de cadena de suministro de Vercel y el rol del Lumma Stealer.
5. Evaluar el papel de la IA en el SOC: complemento, no decisor final.
6. Analizar el caso de estudio del breach de GitHub (Nx Console, TanStack, RMM growth, IAB VPN).

**Learning chain:** Ransomware → Huntress 17 hours → automate triage → remote access → AnyDesk/DarkGate → Nay perimeter predictable → Verizon DBIR → 39% Valid accounts → Initial Access Brokers → Vercel supply chain → Lumma Stealer → Nay TTPs differ → AI in SOC → Nay decision maker → None MITRE obsolete → GitHub breach → Nx Console → TanStack → 240% RMM → IAB VPN

**Lección:** *Las tendencias defensivas apuntan a automatizar el triage, vigilar el acceso remoto y la cadena de suministro, y usar la IA como apoyo (no decisor final) en el SOC.*

**MITRE ATT&CK:** T1195.002 (Supply Chain Compromise: Software Supply Chain), T1078.001 (Valid Accounts: Default Accounts), T1566.001 (Phishing: Spearphishing Attachment), T1071.001 (Application Layer Protocol)

**Fuente:** [TryHackMe - Defensive Security Trends](https://tryhackme.com/room/defensivesecuritytrends)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
