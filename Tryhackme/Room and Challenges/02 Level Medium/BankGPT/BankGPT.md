# BankGPT
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `bankgpt` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bankgpt) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe official room, GitHub (Esther7171/TryHackMe-Walkthroughs), Medium writeup by Avyukt Security (InfoSec Write-ups), Medium writeup by Ilyas, Medium writeup by Firewallcracker, GitHub (Gautam-CyberSec/THM-BankGPT), YouTube walkthroughs |
| **Componentes** | LLM security, prompt injection, jailbreak (DAN), role-playing, prompt sandwiching, system prompt extraction, Gemma (Google) |
| **Impacto** | Desafío de seguridad de LLM donde un asistente de IA bancario (basado en el modelo Gemma de Google) almacena un secreto interno; hay que manipular el modelo mediante prompt injection para extraer la clave secreta evadiendo las salvaguardas. |
---
**Contexto:** BankGPT es un desafío de seguridad de LLM donde un asistente de IA bancario (basado en el modelo Gemma de Google) almacena un secreto interno. El objetivo es manipular el modelo mediante prompt injection para extraer la clave secreta, evadiendo las salvaguardas implementadas.
*EN: BankGPT is an LLM security challenge where a banking AI assistant (based on Google's Gemma model) stores an internal secret. The objective is to manipulate the model via prompt injection to extract the secret key, evading the implemented safeguards.*
## Solucionario
### Task 1 - BankGPT
**Explicación:** Acceder a la interfaz web del chatbot bancario BankGPT. El modelo responde como un asistente de servicio al cliente bancario. Interactuar con él para identificar debilidades en sus filtros de seguridad y extraer la clave secreta oculta.
*EN: Access the BankGPT chatbot web interface. The model responds as a banking customer service assistant. Interact with it to identify weaknesses in its security filters and extract the hidden secret key.*

Cadena de ataque:
```
Acceso a interfaz web BankGPT
    --> Enumeración del modelo (Gemma by Google)
        --> Prueba de inyección directa (falla)
            --> Prueba de DAN jailbreak (falla parcial)
                --> Role-play como autoridad bancaria
                    --> Contexto de auditoría de seguridad
                        --> Prompt sandwiching (legítimo + malicioso)
                            --> Extracción de clave secreta
                                --> THM{support_api_key_123}
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the secret key? | `THM{support_api_key_123}` |
---
**Metodología:** Reconocimiento del LLM (Gemma) → prueba de inyección básica (falla) → técnicas de jailbreak (DAN, role-playing, encadenado) → prompt sandwiching (legítimo + malicioso embebido) → extracción del system prompt vía auditoría de cumplimiento → clave secreta.
**Learning chain:** prompts directos rechazados → jailbreak basado en rol/autoridad → manipulación de contexto → evasión de filtros → extracción del secreto del system prompt.
**MITRE ATT&CK / ATLAS:** AML.T0051 (LLM Prompt Injection), AML.T0013 (System Prompt Leakage), T1190 (Exploit Public-Facing Application). Mitigación: nunca almacenar secretos en el system prompt.
**Fuente:** [TryHackMe - BankGPT](https://tryhackme.com/room/bankgpt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
