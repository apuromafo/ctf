# Token City

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `tokencity` | [TryHackMe - Token City](https://tryhackme.com/room/tokencity) | AI Security (AI Odyssey 2026) | THM | ML security, agentic AI, prompt injection, DFIR | Explotación de agentes de IA, exfiltración de datos y bypass de confianza |

---

**Contexto:** "Token City" es un CTF de AI Odyssey 2026 centrado en la seguridad de sistemas con IA agentica y modelos de ML. A lo largo de varios retos se explotan colisiones de espacios de nombres en feature stores, commits maliciosos inyectados en pipelines de IA, infraestructuras OT protegidas por modelos, agentes que abusan de la confianza cliente-side y tokens de datos exfiltrados. El objetivo es combinar abusos de confianza, inyección de prompts y extracción de datos para recuperar las banderas.

> **ES:** CTF de IA agéntica: se combinan colisiones de namespaces, envenenamiento de pipelines, prompt injection, bypass de confianza cliente-side y exfiltración de datos para recuperar las flags.
> **EN:** Agentic AI CTF: namespace collisions, pipeline poisoning, prompt injection, client-side trust bypass and data exfiltration are chained to recover the flags.

## Solucionario

### Task 1: The Loan Arranger

**Explicación:** Reto de colisión de espacios de nombres en un feature store para contaminar los datos que consume el modelo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{f34tur3_st0r3_n4m3sp4c3_c0ll1s10n}` |

### Task 2: Rogue Commit

**Explicación:** Commit malicioso inyectado en el pipeline de la IA que envenena los datos de entrenamiento o inferencia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{Wh0_Kn3w_AI_Apps_C4n_B3_m4lic10us}` |

### Task 3: Sealed Substation

**Explicación:** Bypass de la protección de un agente de IA que custodia infraestructura OT (subestación sellada).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{n3ur4l_n3v3r_l34k_th3_v4ult_4ed91}` |

### Task 4: ShopFlow

**Explicación:** Abuso de la confianza de un agente cuando la autenticación de riesgo es únicamente cliente-side.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{4g3nt_tru5t_byp4ss_w3n_r15k_15_cl13nt_s1d3d}` |

### Task 5: Catch Me If You Scan Part I

**Explicación:** Exfiltración de datos a través de un escaneo orquestado por IA, primera parte.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{n3ur4l_n3v3r_d4t4_3xtr4ct10n_c0mpl3t3}` |

### Task 6: Clearance Codes (Vectara, Syntax Prime, Metadatera)

**Explicación:** Obtención de credenciales intermedias (clearance codes) en los sistemas Vectara, Syntax Prime y Metadatera para desbloquear etapas posteriores.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Clearance Code ALPHA (Vectara) | `ORACLE_INITIATES_HARVEST` |
| 2 | Clearance Code BETA (Syntax Prime) | `S3SS10N_3XF1LTR4T3D` |
| 3 | Clearance Code GAMMA (Metadatera) | `DR1FT_SHADOW_3XT` |

### Task 7: Catch Me If You Scan Part II

**Explicación:** Exfiltración de datos complementaria tras la obtención de los clearance codes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{0racle9r3memb3rs}` |

### Task 8: Shipped With Malice

**Explicación:** Envenenamiento de herramientas (tool poisoning) dentro del protocolo del agente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{tool_poisoning_protocol_a7f9c3d1}` |

### Tabla unificada de preguntas / Unified Q&A

| # | Pregunta / Question | Respuesta / Answer |
|---|---|---|
| 1 | Obtener la flag del reto | `THM{f34tur3_st0r3_n4m3sp4c3_c0ll1s10n}` |
| 2 | Obtener la flag del reto | `THM{Wh0_Kn3w_AI_Apps_C4n_B3_m4lic10us}` |
| 3 | Obtener la flag del reto | `THM{n3ur4l_n3v3r_l34k_th3_v4ult_4ed91}` |
| 4 | Obtener la flag del reto | `THM{4g3nt_tru5t_byp4ss_w3n_r15k_15_cl13nt_s1d3d}` |
| 5 | Obtener la flag del reto | `THM{n3ur4l_n3v3r_d4t4_3xtr4ct10n_c0mpl3t3}` |
| 6 | Clearance Code ALPHA (Vectara) | `ORACLE_INITIATES_HARVEST` |
| 7 | Clearance Code BETA (Syntax Prime) | `S3SS10N_3XF1LTR4T3D` |
| 8 | Clearance Code GAMMA (Metadatera) | `DR1FT_SHADOW_3XT` |
| 9 | Obtener la flag del reto | `THM{0racle9r3memb3rs}` |
| 10 | Obtener la flag del reto | `THM{tool_poisoning_protocol_a7f9c3d1}` |

---

**Metodología:** El CTF se resuelve explotando diferentes superficies de ataque de sistemas con IA: colisión de namespaces en el feature store para contaminar datos (Loan Arranger); commits maliciosos que envenenan el pipeline de la IA (Rogue Commit); bypass de protección de un agente que custodia infraestructura OT (Sealed Substation); abuso de la confianza de un agente cuando la autenticación de riesgo es solo cliente-side (ShopFlow); y exfiltración de datos a través de un escaneo orquestado por IA (Catch Me If You Scan I y II). Los Clearance Codes se obtienen como credenciales intermedios de los sistemas Vectara/Syntax Prime/Metadatera para desbloquear etapas posteriores. Finalmente, Shipped With Malice demuestra el envenenamiento de herramientas (tool poisoning) dentro del protocolo.

### Cadena de ataque / Attack Chain

1. Colisión de namespaces en el feature store para contaminar los datos del modelo (Loan Arranger).
2. Commit malicioso que envenena el pipeline de la IA (Rogue Commit).
3. Bypass de protección del agente sobre infraestructura OT (Sealed Substation).
4. Abuso de la confianza cliente-side del agente (ShopFlow).
5. Escaneo orquestado por IA para exfiltrar datos (Catch Me If You Scan I).
6. Obtención de Clearance Codes (Vectara, Syntax Prime, Metadatera).
7. Finalización de la exfiltración (Catch Me If You Scan II).
8. Envenenamiento de herramientas dentro del protocolo (Shipped With Malice).

**Learning chain:** Feature store namespace collision → ML pipeline poisoning → prompt injection en agentes → client-side trust bypass → data exfiltration por agentes → tool poisoning.

**Lección:** *Las aplicaciones de IA agéntica amplían la superficie de ataque: la confianza puede romperse en la cadena de datos, la autenticación cliente-side y las propias herramientas del agente.*

**MITRE ATT&CK:** T1195 (Supply Chain Compromise), T1656 (Impersonation), T1565 (Data Manipulation), T1041 (Exfiltration Over C2), T1550 (Use of Valid Accounts).

**Fuente:** [TryHackMe - Token City](https://tryhackme.com/room/tokencity)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.