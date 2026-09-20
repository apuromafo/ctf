# Decryptify

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web + Crypto |
| **Slug** | decryptify |
| **Link** | https://tryhackme.com/room/decryptify |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Cryptography, Command Execution, Web, Decryption |
| **Impacto** | Alto — Vulnerable de descifrado que deriva en ejecución de comandos remotos |

---

**Contexto:** Decryptify es un reto CTF centrado en una aplicación de cifrado/descifrado web. El objetivo es encontrar una manera de romper el mecanismo de descifrado para lograr una ejecución de comandos remota (RCE) y así obtener las flags que demuestran el compromiso.

## Solucionario

### Task 1: Explotación de la aplicación

**Explicación:** Se explota la funcionalidad de descifrado de la aplicación para ejecutar comandos de forma remota.

1. 1. THM{CryptographyPwn007}
   2. THM{GOT_COMMAND_EXECUTION001}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag criptografía | `THM{CryptographyPwn007}` |
| 1.2 | Flag ejecución de comandos | `THM{GOT_COMMAND_EXECUTION001}` |

---

**Metodología:** Análisis de la aplicación web → Identificación de la función de descifrado → Manipulación del input → Inyección de comandos → Obtención de flags.

**Learning chain:** Web app analysis → Decryption logic review → Payload crafting → Command injection → Flag capture

**Lección:** *Función de descifrado mal validada puede convertirse en una puerta de entrada a ejecución remota de comandos.*

**MITRE ATT&CK:**
- T1190 — Exploit Public-Facing Application
- T1059.004 — Unix Shell

**Fuente:** [TryHackMe - Decryptify](https://tryhackme.com/room/decryptify)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.