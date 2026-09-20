# Cipher's Secret Message

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `cipherssecretmessage` | [TryHackMe](https://tryhackme.com/room/cipherssecretmessage) | 01 Level Easy | THM | Criptografía, cifrado César progresivo, Python | Introductorio |

---

**Contexto:** Room de criptografía para principiantes. Se entrega el mensaje cifrado `a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm` junto con el código Python usado para cifrarlo: un cifrado César progresivo que desplaza cada letra según su posición i (sumando i al desplazamiento). Hay que invertir la lógica (restar i en lugar de sumarla) para obtener el texto en claro y envolverlo en el formato THM{...}.

> **ES:** Descifrar un cifrado César de desplazamiento variable: se analiza el código Python del cifrado, se invierte la operación restando el índice i por carácter y se envuelve el resultado en el formato THM{} para obtener la flag.

> **EN:** Decrypt a variable-shift Caesar cipher: analyse the Python encryption code, reverse the operation by subtracting the per-character index i and wrap the result in the THM{} format to get the flag.

## Solucionario

### Task 1: Crypto — Cipher's Secret Message / Cifrado — Mensaje secreto

**Explicación:** Se analiza la función `enc()`: para cada carácter, si es alfabético se desplaza hacia delante según su índice de posición (base a/A + i) y los caracteres no alfabéticos (dígitos, guiones bajos) se conservan. Para descifrar basta cambiar el signo: `chr((ord(c) - base - i) % 26 + base)`. Aplicado al texto cifrado se obtiene el mensaje en claro, que se envuelve en THM{}.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the flag? | `THM{a_sm4ll_crypt0_message_to_st4rt_with_THM_cracks}` |

---

**Metodología:** Análisis del código Python de cifrado → comprensión del desplazamiento progresivo por índice → implementación del descifrado (restar i) → ejecución del script → obtención del texto en claro → envoltura en el formato THM{}.

### Cadena de ataque / Attack Chain

Identificación del cifrado César progresivo → inversión del desplazamiento (suma → resta de i) → descifrado del mensaje → formato de flag THM{} → flag.

**Learning chain:** Análisis de código → comprensión de cifrados basados en desplazamiento → modular arithmetic → ingeniería inversa del algoritmo → extracción del texto plano.

**Lección:** *Un cifrado casero basado en una única clave débil (el índice de posición) se revierte con un solo cambio de signo: conocer el algoritmo es tan valioso como conocer la clave.*

**MITRE ATT&CK:** T1132 (Data Encoding) — contexto académico/ctf.

**Fuente:** [TryHackMe - Cipher's Secret Message](https://tryhackme.com/room/cipherssecretmessage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.