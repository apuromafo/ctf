# Advent of Cyber '23 Side Quest

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF • Side Quest | adventofcyber23sidequest | https://tryhackme.com/room/adventofcyber23sidequest | 03 Level Hard | TryHackMe | Retos extra, pistas cifradas, credenciales ofuscadas | Alto |

---

**Contexto:**
> **ES:** Side Quest del evento Advent of Cyber 2023: una secuencia de retos adicionales con pistas cifradas y credenciales ofuscadas para completar la aventura.
> **EN:** Advent of Cyber 2023 Side Quest: an additional sequence of challenges with encrypted hints and obfuscated credentials to complete the adventure.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
1. No answer needed

### Task 2: Reconocimiento / Recon
**Explicación:**
1. No answer needed

### Task 3: Acceso inicial / Initial access
**Explicación:**
1. No answer needed

### Task 4: Pistas y credenciales / Hints and credentials
**Explicación:**
1. 1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834
2. 2-K@bWJ5oHFCR8o%whAvK5qw8Sp$5qf!nCqGM3ksaK
3. 3-d2dc6a02db03401177f0511a6c99007e945d9cb9b96b8c6294f8c5a2c8e01f60
4. 4-3f$FEBwD6AoqnyLjJ!!Hk4tc*V6w$UuK#evLWkBp

### Task 5: Sin pistas / NO HINTS
**Explicación:**
1. NO HINTS

### Task 6: Cierre / Wrap-up
**Explicación:**
1. No answer needed

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2 | `No answer needed` |
| 3 | `No answer needed` |
| 4.1 | `1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834` |
| 4.2 | `2-K@bWJ5oHFCR8o%whAvK5qw8Sp$5qf!nCqGM3ksaK` |
| 4.3 | `3-d2dc6a02db03401177f0511a6c99007e945d9cb9b96b8c6294f8c5a2c8e01f60` |
| 4.4 | `4-3f$FEBwD6AoqnyLjJ!!Hk4tc*V6w$UuK#evLWkBp` |
| 5 | `NO HINTS` |
| 6 | `No answer needed` |

---

**Metodología:**
Resolución secuencial del Side Quest: cada tarea exige completar retos previos (No answer needed) y el uso de pistas cifradas (formato SHA256) y credenciales ofuscadas para avanzar a los retos extra.

### Cadena de ataque / Attack Chain
1. Compleción de los retos principales para desbloquear el Side Quest.
2. Procesamiento de pistas cifradas en formato `<n>-<hash>`.
3. Decodificación de credenciales ofuscadas en formato `<n>-<secret>`.
4. Uso de las credenciales para acceder a servicios adicionales.
5. Captura de las banderas finales.

**Learning chain:**
Cifrado -> Descifrado de pistas -> Reutilización de credenciales -> Resolución de retos encadenados.

**Lección:** *Un reto extendido muestra que pistas cifradas y credenciales ofuscadas forman una cadena única de acceso.*

**MITRE ATT&CK:**
- T1078 Valid Accounts
- T1110 Brute Force
- T1021 Remote Services

**Fuente:** [TryHackMe - Advent of Cyber '23 Side Quest](https://tryhackme.com/room/adventofcyber23sidequest)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.