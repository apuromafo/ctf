# Phishing - Merry Clickmas

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `phishing-aoc2025-h2tkye9fzU` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/phishing-aoc2025-h2tkye9fzU) |
| **Sección** | Advent of Cyber 2025 |
| **Fuente** | THM |
| **Componentes** | SET phishing, credential harvesting, Roundcube |
| **Impacto** | Medio — obtención de credenciales de usuario para acceso al portal TBFC mediante campaña de phishing automatizada |

---

**Contexto:** En el día 2 de Advent of Cyber 2025, se ejecuta una campaña de phishing contra factory@wareville.thm utilizando el Social Engineering Toolkit (SET) para robar credenciales. Se configura un vector de ataque de credential harvesting que captura las credenciales del usuario objetivo y se permite acceder al portal Roundcube del TBFC para confirmar la explotación.

## Solucionario

### Task 1: Configuración del Phishing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password used to access the TBFC portal? | `unranked-wisdom-anthem` |

### Task 2: Confirmación y Resultados

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the total number of toys expected for delivery? | `1984000` |

---

**Metodología:** Se utilizó el Social Engineering Toolkit (SET) para configurar un servidor de credential harvesting, creando un vector de phishing dirigido a factory@wareville.thm. Se capturaron las credenciales enviadas por la víctima y se utilizó la contraseña obtenida para autenticarse en el portal Roundcube del TBFC, confirmando así la explotación exitosa de la campaña de phishing.
**Learning chain:** SET configuration → credential harvesting server → phishing email delivery → credential capture → Roundcube login → portal data exfiltration
**MITRE ATT&CK:** T1566.002 (Phishing: Spearphishing Link), T1557 (Adversary-in-the-Middle), T1078 (Valid Accounts)
**Fuente:** [TryHackMe - Phishing - Merry Clickmas](https://tryhackme.com/r/room/phishing-aoc2025-h2tkye9fzU)
