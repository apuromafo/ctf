# Crypto Failures

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Crypto |
| **Slug** | cryptofailures |
| **Link** | https://tryhackme.com/room/cryptofailures |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Cryptography, Web, Encryption, Password Cracking |
| **Impacto** | Alto — Compromiso de confidencialidad e integridad por fallos criptográficos |

---

**Contexto:** Esta sala explota los errores más comunes al implementar criptografía en aplicaciones reales. Cubre desde cifrado débil, uso inadecuado de algoritmos y manejo incorrecto de claves, hasta ataques prácticos contra implementaciones cifradas. El objetivo es identificar y explotar fallos criptográficos para obtener flags que demuestren el compromiso de los datos.

## Solucionario

### Task 1: Identificación de flags

**Explicación:** La sala presenta un conjunto de flags que demuestran diferentes fallos criptográficos. Se obtienen mediante la identificación de vulnerabilidades en la implementación de cifrado.

1. 1. THM{ok_you_f0und_w3b_fl4g_6cbe2bc}
   2. THM{Traditional_Own_Crypto_is_Always_Surprising!_and_this_hopefully_is_not_easy_to_crack_e41d20b5b0989cac65ed4a090cace944bf30e6d3ab88f9d447f52fd2140525b9}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag web | `THM{ok_you_f0und_w3b_fl4g_6cbe2bc}` |
| 1.2 | Flag crypto | `THM{Traditional_Own_Crypto_is_Always_Surprising!_and_this_hopefully_is_not_easy_to_crack_e41d20b5b0989cac65ed4a090cace944bf30e6d3ab88f9d447f52fd2140525b9}` |

---

**Metodología:** Análisis pasivo de la implementación criptográfica, identificación de algoritmos débiles, explotación de errores de diseño (ECB, IV reutilizado, claves predecibles) y recuperación de texto plano o claves.

**Learning chain:** Reconocimiento de algoritmos → Identificación de modo de operación → Explotación de debilidad → Obtención de flag

**Lección:** *Nunca inventes tu propia criptografía; usa primitivas estándar con parámetros seguros y auditados.*

**MITRE ATT&CK:**
- T1552.004 — Unsecured Credentials: Private Keys
- T1040 — Network Sniffing

**Fuente:** [TryHackMe - Crypto Failures](https://tryhackme.com/room/cryptofailures)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.