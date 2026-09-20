# JWT Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `jwtsecurity` | https://tryhackme.com/room/jwtsecurity | 01 Level Easy | TryHackMe | JWT / cabecera Authorization / algoritmos (Symmetric/Asymmetric) / JWE / ataques a firmas | Aprender la estructura y seguridad de los JSON Web Tokens: cabeceras de autorización, tipos de firma (simétrica/asimétrica), JWE y explotación de fallos de verificación. |

---

**Contexto:** Sala del catálogo de TryHackMe centrada en la seguridad de los JSON Web Tokens (JWT). Se repasa cómo se transmiten (cabecera `Authorization: Bearer`), los algoritmos de firma **Symmetric**/**Asymmetric**, el cifrado JWE y los ataques que permiten falsificar o decodificar tokens para obtener flags en cada tarea.

> **ES:** Sala de seguridad de JWT: transmisión en la cabecera Authorization, algoritmos de firma simétrica/asimétrica, JWE y retos prácticos de explotación de tokens.
> **EN:** JWT security room: Authorization header, symmetric/asymmetric signing algorithms, JWE and hands-on token exploitation challenges.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Lectura de la introducción a los JSON Web Tokens y a la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. / Read the room introduction. | `No answer needed` |

### Task 2: Transmisión del token / Token Transmission

**Explicación:** Los JWT se transmiten en el campo de cabecera `Authorization` con el esquema **Bearer**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué cabecera se envía el token? / In which header is the token sent? | `Authorization: Bearer` |

### Task 3: Algoritmos y tipos / Algorithms and Types

**Explicación:** Los tokens pueden firmarse con algoritmos **Symmetric** (una clave compartida) o **Asymmetric** (par de claves pública/privada). El formato cifrado de JWT se denomina **JWE**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer tipo de algoritmo de firma. / First signing algorithm type. | `Symmetric` |
| 2 | Segundo tipo de algoritmo de firma. / Second signing algorithm type. | `Asymmetric` |
| 3 | Formato de JWT cifrado. / Encrypted JWT format. | `JWE` |

### Task 4: Flag 1

**Explicación:** Tras completar el primer reto de explotación del token se obtiene la primera flag de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la tarea? / What is the flag of the task? | `THM{9cc039cc-d85f-45d1-ac3b-818c8383a560}` |

### Task 5: Flags del laboratorio / Lab Flags

**Explicación:** El laboratorio práctico de ataques JWT entrega cuatro flags, una por cada ejercicio de falsificación/verificación de tokens.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primera flag del laboratorio. / First lab flag. | `THM{6e32dca9-0d10-4156-a2d9-5e5c7000648a}` |
| 2 | Segunda flag del laboratorio. / Second lab flag. | `THM{fb9341e4-5823-475f-ae50-4f9a1a4489ba}` |
| 3 | Tercera flag del laboratorio. / Third lab flag. | `THM{e1679fef-df56-41cc-85e9-af1e0e12981b}` |
| 4 | Cuarta flag del laboratorio. / Fourth lab flag. | `THM{f592dfe2-ec65-4514-a135-70ba358f22c4}` |

### Task 6: Flag 3

**Explicación:** Tercer reto de la sala: al completar el ejercicio de explotación se obtiene la flag correspondiente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la tarea? / What is the flag of the task? | `THM{a450ae48-7226-4633-a63d-38a625368669}` |

### Task 7: Flag 4

**Explicación:** Cuarto reto de la sala: al completar el ejercicio de explotación se obtiene la flag correspondiente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la tarea? / What is the flag of the task? | `THM{f0d34fe1-2ba1-44d4-bae7-99bd555a4128}` |

### Task 8: Cierre / Wrap-up

**Explicación:** Cierre de la sala con el resumen de lo aprendido sobre JWT. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el resumen final de la room. / Read the final summary of the room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `No answer needed` |
| 2 | ¿En qué cabecera se envía el token? | `Authorization: Bearer` |
| 3 | Primer tipo de algoritmo de firma. | `Symmetric` |
| 4 | Segundo tipo de algoritmo de firma. | `Asymmetric` |
| 5 | Formato de JWT cifrado. | `JWE` |
| 6 | ¿Cuál es la flag de la tarea (Task 4)? | `THM{9cc039cc-d85f-45d1-ac3b-818c8383a560}` |
| 7 | Primera flag del laboratorio. | `THM{6e32dca9-0d10-4156-a2d9-5e5c7000648a}` |
| 8 | Segunda flag del laboratorio. | `THM{fb9341e4-5823-475f-ae50-4f9a1a4489ba}` |
| 9 | Tercera flag del laboratorio. | `THM{e1679fef-df56-41cc-85e9-af1e0e12981b}` |
| 10 | Cuarta flag del laboratorio. | `THM{f592dfe2-ec65-4514-a135-70ba358f22c4}` |
| 11 | ¿Cuál es la flag de la tarea (Task 6)? | `THM{a450ae48-7226-4633-a63d-38a625368669}` |
| 12 | ¿Cuál es la flag de la tarea (Task 7)? | `THM{f0d34fe1-2ba1-44d4-bae7-99bd555a4128}` |
| 13 | Lee el resumen final de la room. | `No answer needed` |

---

**Metodología:** Entender la estructura del JWT (header, payload, signature) y su transmisión en `Authorization: Bearer`, identificar el algoritmo de firma, distinguir cifrado (JWE) de firma, y explotar los fallos de verificación de cada laboratorio para falsificar tokens y recuperar las flags.

### Cadena de ataque / Attack Chain

```text
Analizar el token (header/payload/firma) -> identificar algoritmo (symmetric/asymmetric) -> detectar fallo de verificación -> falsificar token -> validar acceso -> flag
```

**Learning chain:** JWT -> Authorization: Bearer -> algoritmos -> JWE -> laboratorio -> flags.

**Lección:** *Un JWT solo es seguro si verifica correctamente la firma con el algoritmo adecuado; los fallos de verificación (ninguno, simétrico/asimétrico confundido, claves débiles) permiten falsificar tokens y ganar acceso.*

**MITRE ATT&CK:** T1557 (Adversary-in-the-Middle), T1213.004 (Security Software Management / token manipulation); N/A específico de token forgery en aplicaciones web

**Fuente:** [TryHackMe - JWT Security](https://tryhackme.com/room/jwtsecurity)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.