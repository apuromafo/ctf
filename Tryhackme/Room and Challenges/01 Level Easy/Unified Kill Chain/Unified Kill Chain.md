# Unified Kill Chain

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `unifiedkillchain` | [TryHackMe](https://tryhackme.com/room/unifiedkillchain) | 01 Level Easy | THM | Unified Kill Chain, Cyber Kill Chain, Threat Modelling, fases del ataque, MITRE ATT&CK | Resolución completa de la sala teórica |

---

**Contexto:** Sala teórica del módulo Cyber Defense Frameworks (SOC Level 1) que presenta el marco Unified Kill Chain (UKC) publicado por Paul Pols en 2017 y actualizado en 2022. El UKC establece las fases de un ataque (18 fases agrupadas en In/Through/Out) y sirve para identificar y mitigar riesgos sobre los activos de TI, complementando marcos como el Cyber Kill Chain de Lockheed Martin y MITRE ATT&CK.

> **ES:** Sala teórica que explica el Unified Kill Chain (UKC): el origen militar del concepto "kill chain", el threat modelling, las 18 fases de un ataque y las fases de alto nivel In/Through/Out, con preguntas aplicadas para analistas SOC.
> **EN:** Theoretical room that explains the Unified Kill Chain (UKC): the military origin of the "kill chain" concept, threat modelling, the 18 phases of an attack and the high-level In/Through/Out phases, with applied questions for SOC analysts.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de los objetivos de aprendizaje: entender el propósito y los beneficios de los marcos de cyber kill chain, explorar las 18 fases del UKC, comparar marcos y aplicar el UKC a escenarios reales.

No answer needed

### Task 2: ¿Qué es una "Kill Chain"? / What is a "Kill Chain"?

**Explicación:** Se explica el origen del término "Kill Chain", proveniente de la doctrina militar, donde describe la estructura de ataque en fases (encontrar, fijar, seguir, atacar).

1. `military`

### Task 3: ¿Qué es "Threat Modelling"? / What is "Threat Modelling"?

**Explicación:** Se introduce el concepto de threat modelling y el término técnico para referirse a una pieza de software o hardware en TI: un activo (asset).

1. `asset`

### Task 4: Presentando el Unified Kill Chain / Introducing the Unified Kill Chain

**Explicación:** Se presenta el marco UKC publicado en 2017: sus 18 fases, incluida la Defense Evasion (técnicas para evadir la detección), la Exfiltration (técnicas para extraer datos de una red) y los Objectives (cuando el atacante alcanza sus objetivos).

1. `2017`
2. `18`
3. `Defense Evasion`
4. `Exfiltration`
5. `Objectives`

### Task 5: Fase: In (Foothold Inicial) / Phase: In (Initial Foothold)

**Explicación:** Fases del UKC correspondientes al foothold inicial: Phishing, Social Engineering, Weaponization, Exploitation, Pivoting y Persistence.

1. `Phishing`
2. `Social Engineering`
3. `Weaponization`
4. `Exploitation`
5. `Pivoting`
6. `Persistence`

### Task 6: Fase: Through (Propagación en la Red) / Phase: Through (Network Propagation)

**Explicación:** Fases de propagación dentro de la red: Privilege Escalation y Credential dumping, planteadas mediante escenarios de detección para un analista SOC.

1. `Privilege Escalation`
2. `Credential dumping`

### Task 7: Fase: Out (Acción sobre los Objetivos) / Phase: Out (Action on Objectives)

**Explicación:** Fases finales del ataque: Exfiltration (pico de tráfico de red saliente hacia una IP desconocida) y el impacto en la Confidentiality de la tríada CIA al filtrarse datos personales (PII).

1. `Exfiltration`
2. `Confidentiality`

### Task 8: Aplicando el Unified Kill Chain / Practical

**Explicación:** Ejercicio práctico que empareja cada escenario con la fase correcta del Unified Kill Chain para revelar la flag final.

1. `THM{UKC_SCENARIO}`

### Task 9: Conclusión / Conclusion

**Explicación:** Cierre de la sala donde se integra lo aprendido sobre el UKC. No requiere respuesta.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1 | — | `No answer needed` |
| 2.1 | Where does the term "Kill Chain" originate from? For this answer, you must fill in the blank!: The ******** | `military` |
| 3.1 | What is the technical term for a piece of software or hardware in IT (Information Technology?)? | `asset` |
| 4.1 | In what year was the Unified Kill Chain framework released? | `2017` |
| 4.2 | According to the Unified Kill Chain, how many phases are there to an attack? | `18` |
| 4.3 | What is the name of the attack phase where an attacker employs techniques to evade detection? | `Defense Evasion` |
| 4.4 | What is the name of the attack phase where an attacker employs techniques to remove data from a network? | `Exfiltration` |
| 4.5 | What is the name of the attack phase where an attacker achieves their objectives? | `Objectives` |
| 5.1 | What is an example of a tactic to gain a foothold using emails? | `Phishing` |
| 5.2 | Impersonating an employee to request a password reset is a form of what? | `Social Engineering` |
| 5.3 | An adversary setting up the Command & Control server infrastructure is what phase of the Unified Kill Chain? | `Weaponization` |
| 5.4 | Exploiting a vulnerability present on a system is what phase of the Unified Kill Chain? | `Exploitation` |
| 5.5 | Moving from one system to another is an example of? | `Pivoting` |
| 5.6 | Leaving behind a malicious service that allows the adversary to log back into the target is what? | `Persistence` |
| 6.1 | As a SOC analyst, you pick up numerous alerts pointing to failed login attempts from an administrator account. What stage of the kill chain would an attacker be seeking to achieve? | `Privilege Escalation` |
| 6.2 | Mimikatz, a known post-exploitation tool, was recently detected running on the IT Manager's computer. What is the primary objective of this tool in such an attack scenario? | `Credential dumping` |
| 7.1 | While monitoring the network as a SOC analyst, you realise that there is a spike in the network activity, and all the traffic is outbound to an unknown IP address. What stage could describe this activity? | `Exfiltration` |
| 7.2 | Personally identifiable information (PII) has been released to the public by an adversary, and your organisation is facing scrutiny for the breach. What part of the CIA triad would be affected by this action? | `Confidentiality` |
| 8 | Match the scenario prompt to the correct phase of the Unified Kill Chain to reveal the flag at the end. What is the flag? | `THM{UKC_SCENARIO}` |
| 9 | — | `No answer needed` |

---

**Metodología:** 1) Establecer el origen militar del término "Kill Chain". 2) Introducir el threat modelling y el concepto de activo. 3) Presentar el UKC: año de publicación (2017), número de fases (18) y fases de evasión, exfiltración y objetivos. 4) Recorrer las fases de alto nivel In (Initial Foothold), Through (Network Propagation) y Out (Action on Objectives). 5) Aplicar el UKC a escenarios de analista SOC (Mimikatz, fallos de inicio de sesión, picos de tráfico saliente, filtración de PII) y cerrar con la flag del ejercicio práctico.

### Cadena de ataque / Attack Chain

Kill Chain (origen militar) → Threat Modelling (activos) → UKC 2017 → 18 fases → Phase In (Initial Foothold): Phishing, Social Engineering, Weaponization, Exploitation, Pivoting, Persistence → Phase Through (Network Propagation): Privilege Escalation, Credential dumping → Phase Out (Action on Objectives): Exfiltration, Confidentiality → Practical: THM{UKC_SCENARIO}

**Learning chain:** Kill Chain → Threat Modelling → Unified Kill Chain → 18 phases → In (Initial Foothold) → Through (Network Propagation) → Out (Action on Objectives) → SOC scenario mapping

**Lección:** *El Unified Kill Chain permite mapear la fase exacta de un ataque (In/Through/Out): detectar el escalado de privilegios, el credential dumping o la exfiltración no depende de la herramienta, sino de saber en qué fase del marco se encuentra el adversario.*

**MITRE ATT&CK:** T1566 (Phishing), T1598 (Phishing for Information), T1078 (Valid Accounts), T1210 (Exploitation of Remote Services), T1068 (Exploitation for Privilege Escalation), T1003 (OS Credential Dumping), T1020 (Automated Exfiltration), T1114 (Email Collection)

**Fuente:** [TryHackMe - Unified Kill Chain](https://tryhackme.com/room/unifiedkillchain)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.