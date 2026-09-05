# Intro to Offensive Security [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `introtooffensivesecurity`
* **Link:** https://tryhackme.com/room/introtooffensivesecurity
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** ElectronicsReference, CYB3RM3 (lougerard.github.io), Motasem Notes (motasem-notes.net), thmflags.gitbook.io, OWASP10

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala introduce los conceptos fundamentales de la seguridad ofensiva (Red Team). Incluye un laboratorio práctico donde se hackea una aplicación web bancaria falsa utilizando reconocimiento con gobuster para encontrar páginas ocultas y transferencia de fondos no autorizada. También cubre las diferencias entre seguridad ofensiva y defensiva, y las carreras profesionales en el ámbito.
> **EN:** This room introduces fundamental concepts of offensive security (Red Team). It includes a practical lab where you hack a fake bank web application using reconnaissance with gobuster to find hidden pages and unauthorized fund transfer. It also covers differences between offensive and defensive security, and professional careers in the field.

### Task 1 - Hacking Your First Machine

> **ES:** Se presenta una aplicación web bancaria vulnerable en `http://fakebank.com`. El objetivo es encontrar páginas ocultas utilizando la herramienta de fuerza bruta `gobuster`. Se ejecuta un escaneo con gobuster contra el objetivo usando un wordlist predeterminado (`wordlist.txt` en el escritorio). Gobuster identifica `/images` (301) y `/bank-transfer` (200). Se navega a `/bank-transfer` y se realiza una transferencia de $2000 desde la cuenta 2276 a la cuenta 8881. Al volver a la página principal, aparece el mensaje de confirmación.
> **EN:** A vulnerable bank web application is presented at `http://fakebank.com`. The goal is to find hidden pages using the brute force tool `gobuster`. A scan is run with gobuster against the target using a default wordlist (`wordlist.txt` on the Desktop). Gobuster identifies `/images` (301) and `/bank-transfer` (200). Navigate to `/bank-transfer` and transfer $2000 from account 2276 to account 8881. Returning to the main page reveals the confirmation message.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| When you've transferred money to your account, go back to your bank account page. What is the answer shown on your bank balance page? | `BANK-HACKED` |

### Task 2 - What is Offensive Security?

> **ES:** La seguridad ofensiva se centra en romper sistemas para identificar vulnerabilidades. Incluye la simulación de acciones de un hacker para encontrar debilidades en un sistema. Las opciones que mejor representan este proceso son: explotar bugs, abusar de configuraciones inseguras, y aprovechar políticas de control de acceso no aplicadas. Esto se realiza legalmente como penetration tester o ilegalmente como hacker.
> **EN:** Offensive security focuses on breaking systems to identify vulnerabilities. It includes simulating a hacker's actions to find weaknesses in a system. The options that best represent this process are: exploiting bugs, abusing insecure setups, and taking advantage of unenforced access control policies. This is done legally as a penetration tester or illegally as a hacker.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system? | `Offensive Security` |

### Task 3 - Careers in Cyber Security

> **ES:** Esta tarea describe las carreras profesionales en seguridad ofensiva y defensiva. Los roles ofensivos incluyen Penetration Tester y Red Team. Los roles defensivos incluyen SOC Analyst y Threat Intelligence Analyst. También se mencionan certificaciones relevantes como OSCP y CompTIA Security+.
> **EN:** This task describes professional careers in offensive and defensive security. Offensive roles include Penetration Tester and Red Team. Defensive roles include SOC Analyst and Threat Intelligence Analyst. Relevant certifications like OSCP and CompTIA Security+ are also mentioned.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Read the above, and continue with the next room! | `No answer needed` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento con gobuster:** Ejecutar `gobuster -u http://fakebank.com -w wordlist.txt` para descubrir endpoints ocultos en el servidor web.
2. **Paso / Step - Análisis de resultados:** Identificar que `/bank-transfer` retorna código HTTP 200 (accesible) mientras `/images` retorna 301 (redirección).
3. **Paso / Step - Navegación a página oculta:** Acceder a `http://fakebank.com/bank-transfer` para encontrar el portal de transferencia de fondos.
4. **Paso / Step - Explotación de la vulnerabilidad:** Realizar una transferencia no autorizada de $2000 de la cuenta 2276 a la cuenta 8881.
5. **Paso / Step - Verificación del resultado:** Volver a la página principal para confirmar que el mensaje de estado de la cuenta indica que la transferencia fue exitosa.
6. **Paso / Step - Comprensión conceptual:** Entender que esta práctica demuestra por qué el pensamiento ofensivo es crucial para diseñar sistemas seguros.

### Cadena de ataque / Attack Chain

```
Objetivo identificado (fakebank.com)
        |
        v
Reconocimiento con gobuster (wordlist.txt)
        |
        v
Descubrimiento de /bank-transfer (HTTP 200)
        |
        v
Acceso al portal de transferencia
        |
        v
Explotación: transferencia no autorizada ($2000)
        |
        v
Verificación: BANK-HACKED en página principal
```

**Lección:** El pensamiento ofensivo es una herramienta esencial para diseñar sistemas seguros; si no consideras la perspectiva de un atacante, es fácil crear aplicaciones web vulnerables como la demonstrada en esta sala.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
