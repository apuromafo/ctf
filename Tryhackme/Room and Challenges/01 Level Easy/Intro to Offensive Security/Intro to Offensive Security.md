# Intro to Offensive Security

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `introtooffensivesecurity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introtooffensivesecurity) |
| **Sección** | 01 Level Easy |
| **Fuente** | ElectronicsReference, CYB3RM3 (lougerard.github.io), Motasem Notes (motasem-notes.net), thmflags.gitbook.io, OWASP10 |
| **Componentes** | Red Team / gobuster / fuerza bruta de directorios / transferencia de fondos / web app bancaria / carreras de ciberseguridad |
| **Impacto** | Introduce los conceptos fundamentales de la seguridad ofensiva (Red Team) con un laboratorio práctico: hackear una app web bancaria falsa con gobuster y una transferencia de fondos no autorizada. |

---

**Contexto:** Esta sala introduce los conceptos fundamentales de la seguridad ofensiva (Red Team). Incluye un laboratorio práctico donde se hackea una aplicación web bancaria falsa utilizando reconocimiento con gobuster para encontrar páginas ocultas y transferencia de fondos no autorizada. También cubre las diferencias entre seguridad ofensiva y defensiva, y las carreras profesionales en el ámbito.

## Solucionario

### Task 1: Hacking Your First Machine

**Explicación:** Se presenta una aplicación web bancaria vulnerable en `http://fakebank.com`. El objetivo es encontrar páginas ocultas con la herramienta de fuerza bruta **gobuster**. Se ejecuta un escaneo contra el objetivo con el wordlist predeterminado (`wordlist.txt` en el escritorio). Gobuster identifica `/images` (301) y `/bank-transfer` (200). Se navega a `/bank-transfer` y se realiza una transferencia de $2000 desde la cuenta 2276 a la cuenta 8881. Al volver a la página principal aparece el mensaje de confirmación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When you've transferred money to your account, go back to your bank account page. What is the answer shown on your bank balance page? | `BANK-HACKED` |

### Task 2: What is Offensive Security?

**Explicación:** La seguridad ofensiva se centra en romper sistemas para identificar vulnerabilidades. Incluye la simulación de acciones de un hacker para encontrar debilidades: explotar bugs, abusar de configuraciones inseguras y aprovechar políticas de control de acceso no aplicadas. Se realiza legalmente como penetration tester o ilegalmente como hacker.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system? | `Offensive Security` |

### Task 3: Careers in Cyber Security

**Explicación:** Carreras profesionales en seguridad ofensiva y defensiva. Roles ofensivos: **Penetration Tester** y **Red Team**. Roles defensivos: **SOC Analyst** y **Threat Intelligence Analyst**. Certificaciones relevantes: **OSCP** y **CompTIA Security+**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above, and continue with the next room! | `No answer needed` |

---

**Metodología:**
1. **Reconocimiento con gobuster:** ejecutar `gobuster -u http://fakebank.com -w wordlist.txt` para descubrir endpoints ocultos en el servidor web.
2. **Análisis de resultados:** identificar que `/bank-transfer` retorna HTTP 200 (accesible) mientras `/images` retorna 301 (redirección).
3. **Navegación a página oculta:** acceder a `http://fakebank.com/bank-transfer` para encontrar el portal de transferencia de fondos.
4. **Explotación de la vulnerabilidad:** realizar una transferencia no autorizada de $2000 de la cuenta 2276 a la cuenta 8881.
5. **Verificación del resultado:** volver a la página principal para confirmar que el mensaje de estado de la cuenta indica que la transferencia fue exitosa.
6. **Comprensión conceptual:** entender que esta práctica demuestra por qué el pensamiento ofensivo es crucial para diseñar sistemas seguros.

**Attack chain:** Objetivo identificado (fakebank.com) → Reconocimiento con gobuster (wordlist.txt) → Descubrimiento de /bank-transfer (HTTP 200) → Acceso al portal de transferencia → Explotación: transferencia no autorizada ($2000) → Verificación: BANK-HACKED en página principal.

**Lección:** El pensamiento ofensivo es una herramienta esencial para diseñar sistemas seguros; si no consideras la perspectiva de un atacante, es fácil crear aplicaciones web vulnerables como la demonstrada en esta sala.

**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1071.001 (Application Layer Protocol: Web Protocols).

**Fuente:** [TryHackMe - Intro to Offensive Security](https://tryhackme.com/room/introtooffensivesecurity)