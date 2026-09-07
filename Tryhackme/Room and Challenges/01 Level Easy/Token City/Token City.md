# Token City

| **Dificultad** | Medium |
| **Tipo** | challenge |
| **Slug** | `tokencity` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/tokencity) |
| **Sección** | AI Security (AI Odyssey 2026) |
| **Fuente** | THM |
| **Componentes** | ML security, agentic AI, prompt injection, DFIR |
| **Impacto** | Explotación de agentes de IA, exfiltración de datos y bypass de confianza |

---

**Contexto:** "Token City" es un CTF de AI Odyssey 2026 centrado en la seguridad de sistemas con IA agentica y modelos de ML. A lo largo de varios retos se explotan colisiones de espacios de nombres en feature stores, commits maliciosos inyectados en pipelines de IA, infraestructuras OT protegidas por modelos, agentes que abusan de la confianza cliente-side y tokens de datos exfiltrados. El objetivo es combinar abusos de confianza, inyección de prompts y extracción de datos para recuperar las banderas.

## Solucionario

### Task 1: The Loan Arranger

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{f34tur3_st0r3_n4m3sp4c3_c0ll1s10n}` |

### Task 2: Rogue Commit

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{Wh0_Kn3w_AI_Apps_C4n_B3_m4lic10us}` |

### Task 3: Sealed Substation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{n3ur4l_n3v3r_l34k_th3_v4ult_4ed91}` |

### Task 4: ShopFlow

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{4g3nt_tru5t_byp4ss_w3n_r15k_15_cl13nt_s1d3d}` |

### Task 5: Catch Me If You Scan Part I

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{n3ur4l_n3v3r_d4t4_3xtr4ct10n_c0mpl3t3}` |

### Task 6: Clearance Codes (Vectara, Syntax Prime, Metadatera)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Clearance Code ALPHA (Vectara) | `ORACLE_INITIATES_HARVEST` |
| 2 | Clearance Code BETA (Syntax Prime) | `S3SS10N_3XF1LTR4T3D` |
| 3 | Clearance Code GAMMA (Metadatera) | `DR1FT_SHADOW_3XT` |

### Task 7: Catch Me If You Scan Part II

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{0racle9r3memb3rs}` |

### Task 8: Shipped With Malice

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del reto | `THM{tool_poisoning_protocol_a7f9c3d1}` |

---

**Metodología:** El CTF se resuelve explotando diferentes superficies de ataque de sistemas con IA: colisión de namespaces en el feature store para contaminar datos (Loan Arranger); commits maliciosos que envenenan el pipeline de la IA (Rogue Commit); bypass de protección de un agente que custodia infraestructura OT (Sealed Substation); abuso de la confianza de un agente cuando la autenticación de riesgo es solo cliente-side (ShopFlow); y exfiltración de datos a través de un escaneo orquestado por IA (Catch Me If You Scan I y II). Los Clearance Codes se obtienen como credenciales intermedios de los sistemas Vectara/Syntax Prime/Metadatera para desbloquear etapas posteriores. Finalmente, Shipped With Malice demuestra el envenenamiento de herramientas (tool poisoning) dentro del protocolo.

**Learning chain:** Feature store namespace collision → ML pipeline poisoning → prompt injection en agentes → client-side trust bypass → data exfiltration por agentes → tool poisoning.

**MITRE ATT&CK:** T1195 (Supply Chain Compromise), T1656 (Impersonation), T1565 (Data Manipulation), T1041 (Exfiltration Over C2), T1550 (Use of Valid Accounts).

**Fuente:** [TryHackMe - Token City](https://tryhackme.com/r/room/tokencity)
