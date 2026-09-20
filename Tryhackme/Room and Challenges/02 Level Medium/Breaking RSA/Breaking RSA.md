# Breaking RSA
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `breakingrsa` |
| **Link** | [TryHackMe](https://tryhackme.com/room/breakingrsa) |
| **Sección** | Cryptography / RSA |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | RSA encryption, key analysis, cryptographic weaknesses, flag extraction |
| **Impacto** | Enseña a analizar claves RSA débiles, identificar debilidades en la generación de parámetros y explotarlas para descifrar mensajes cifrados. |
---
**Contexto:** Breaking RSA es una sala de TryHackMe dedicada a la criptografía RSA. El participante debe analizar claves RSA débiles, identificar debilidades en los parámetros (exponentes públicos, tamaños de clave, factores compartidos) y explotarlas para descifrar los mensajes y obtener las flags.
*EN: Breaking RSA is a TryHackMe room dedicated to RSA cryptography. The participant must analyze weak RSA keys, identify parameter weaknesses (public exponents, key sizes, shared factors), and exploit them to decrypt messages and obtain the flags.*
## Solucionario
### Task 1 — RSA Analysis
**Explicación:** Se analizan múltiples claves RSA débiles: exponentes públicos pequeños, claves de tamaño insuficiente y factores comunes entre claves. Cada reto explota una debilidad distinta del RSA para descifrar el mensaje.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the public exponent? | `2` |
| 2 | What is the key size category? | `development` |
| 3 | What is the key size in bits? | `4096` |
| 4 | What is the factor found? | `1225222383` |
| 5 | Decryption task. | `No answer needed` |
| 6 | What is the factor? | `1502` |
| 7 | Decryption task. | `No answer needed` |
| 8 | What is the decrypted flag? | `breakingRSAissuperfun20220809134031` |
---
**Metodología:** Identificación de parámetros RSA → análisis de exponente público → verificación de tamaño de clave → factorización → descifrado → flags.
**Learning chain:** claves RSA débiles → exponente pequeño → tamaño insuficiente → factores compartidos → factorización → descifrado → flags.
**Lección:** *RSA solo es seguro si los parámetros son correctos: exponentes públicos pequeños, claves de bajo bits y factores compartidos son vulnerabilidades triviales de explotar.*
**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1140 (Deobfuscate/Decode Files or Information), T1573 (Encrypted Channel).
**Fuente:** [TryHackMe - Breaking RSA](https://tryhackme.com/room/breakingrsa)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
