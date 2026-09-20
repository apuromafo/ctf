# Identity and Access Management

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `identityandaccessmanagement` | [TryHackMe](https://tryhackme.com/room/identityandaccessmanagement) | 01 Level Easy | THM | Identity and Access Management, AAA, Identity Management, Single Sign-On, Replay Attack, Access Control | Comprensión de los principios, componentes y ataques que conforman la gestión de identidades y accesos |

> **Objeto:** Comprender la definición de IAM, sus tres principios fundamentales, los componentes tecnológicos que la forman, el funcionamiento del Single Sign-On y los ataques típicos como el Replay Attack.

---

**Contexto:** Sala introductoria de TryHackMe sobre Identity and Access Management (IAM). Explica qué es IAM según la definición de NIST basada en "Security Principles", los tres principios que sostienen el modelo (Autorización, Identificación y Responsabilidad), los componentes tecnológicos (Identity Management e IAM), el concepto de Single Sign-On (SSO) y vectores de ataque como el Replay Attack. La sala culmina con la obtención de una flag relacionada con el control de acceso.

> **ES:** Una sala guiada para entender qué es IAM, sobre qué principios se asienta, qué componentes tecnológicos la implementan, cómo funciona el inicio de sesión único y qué ataques explotan un control de acceso débil.
> **EN:** A guided room to understand what IAM is, the principles it relies on, the technology components that implement it, how Single Sign-On works, and the attacks that exploit weak access control.

## Solucionario

### Task 1: Conceptos básicos de IAM / IAM Basics

**Explicación:** El primer módulo define IAM según NIST y presenta los tres principios sobre los que se construye: Autorización, Identificación y Responsabilidad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la definición de IAM según la descomposición de NIST? / What is the definition of IAM (per the NIST breakdown)? | `Security Principles` |
| 2.1 | Rellene el primer principio / Fill in the first principle | `Authorisation` |
| 2.2 | Rellene el segundo principio / Fill in the second principle | `Identification` |
| 2.3 | Rellene el tercer principio / Fill in the third principle | `Accountability` |

### Task 2: Principios, componentes y evaluación / Principles, Components & Assessment

**Explicación:** Se evalúan los distintos principios y componentes de IAM mediante ejercicios de emparejamiento y opción múltiple; algunas preguntas no requieren respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3.1 | Seleccione el valor correcto (opción 1) / Select the correct value (option 1) | `3` |
| 3.2 | Seleccione el valor correcto (opción 2) / Select the correct value (option 2) | `2` |
| 4.1 | Empareje el primer elemento / Match the first item | `1` |
| 4.2 | Empareje el segundo elemento / Match the second item | `4` |
| 4.3 | Empareje el tercer elemento / Match the third item | `1` |
| 4.4 | Empareje el cuarto elemento / Match the fourth item | `4` |
| 5.1 | Empareje el primer elemento / Match the first item | `1` |
| 5.2 | Empareje el segundo elemento / Match the second item | `2` |
| 5.3 | Empareje el tercer elemento / Match the third item | `1` |
| 6 | ¿Qué se obtiene al final del módulo? / What do you get at the end of the module? | `No answer needed` |

### Task 3: Identity Management y ataques / Identity Management & Attacks

**Explicación:** Se distinguen los conceptos de Identity Management e Identity and Access Management, y se analiza el Replay Attack como vector de ataque sobre las credenciales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7.1 | Identifique el primer término / Identify the first term | `Identity Management` |
| 7.2 | Identifique el segundo término / Identify the second term | `Identity and Access Management` |
| 8 | ¿Qué ataque permite capturar y reutilizar credenciales? / Which attack captures and reuses credentials? | `Replay Attack` |
| 9.1 | Seleccione el valor correcto (opción 1) / Select the correct value (option 1) | `2` |
| 9.2 | Seleccione el valor correcto (opción 2) / Select the correct value (option 2) | `1` |

### Task 4: Single Sign-On / Single Sign-On

**Explicación:** Se estudia el Single Sign-On (SSO), sus características mediante juicios Yea/Nay, y la flag final relacionada con el control de acceso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 10.1 | Identifique el término / Identify the term | `Single Sign-On` |
| 10.2 | ¿El juicio es correcto? / Is the statement correct? | `Yea` |
| 10.3 | ¿El juicio es correcto? / Is the statement correct? | `Nay` |
| 10.4 | ¿El juicio es correcto? / Is the statement correct? | `Yea` |
| 10.5 | ¿El juicio es correcto? / Is the statement correct? | `Yea` |
| 11 | Obtenga la bandera de control de acceso / Obtain the access control flag | `{THM_ACCESS_CONTROL}` |
| 12 | ¿Qué ocurre al final? / What happens at the end? | `No answer needed` |

---

**Metodología:** Se leyeron los conceptos de IAM desde la definición de NIST, aplicando la teoría de los tres principios y los componentes tecnológicos para responder los ejercicios de emparejamiento y opción múltiple. Para la flag final se resolvió el reto de control de acceso validando la comprensión del material de la sala.

### Cadena de ataque / Attack Chain

Reconocimiento de conceptos IAM → identificación de principios (Autorización, Identificación, Responsabilidad) → análisis de componentes (Identity Management, IAM) → estudio del SSO → comprensión del Replay Attack → obtención de la flag de control de acceso.

**Learning chain:** Definición de IAM (NIST, Security Principles) → principios AAA → componentes tecnológicos → Identity Management vs IAM → Single Sign-On → Replay Attack → flag de acceso.

**Lección:** *El IAM es una disciplina de seguridad que debe diseñarse sobre principios sólidos (autorización, identificación y responsabilidad); las implementaciones con control de acceso deficiente quedan expuestas a ataques como el Replay Attack o el abuso de credenciales.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1110 (Brute Force), T1557 (Adversary-in-the-Middle / credential replay), T1204 (User Execution).

**Fuente:** [TryHackMe - Identity and Access Management](https://tryhackme.com/room/identityandaccessmanagement)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.