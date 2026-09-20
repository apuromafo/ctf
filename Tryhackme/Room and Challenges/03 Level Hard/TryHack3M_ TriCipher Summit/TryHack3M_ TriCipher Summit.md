# TryHack3M_ TriCipher Summit

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Criptografía | tryhack3mencryptionchallenge | https://tryhackme.com/room/tryhack3mencryptionchallenge | 03 Level Hard | TryHackMe | Criptografía, Cifrados personalizados, Multi-estancia | Alto |

---

**Contexto:**
> **ES:** Reto de criptografía de la serie TryHack3M: un mensaje cifrado debe superar tres capas de cifrado personalizadas para recuperar las tres flags completas. Demuestra la fragilidad de los esquemas de cifrado caseros frente a criptoanálisis básico.
> **EN:** Cryptography challenge from the TryHack3M series: a ciphertext must go through three layers of custom cipher to recover the three complete flags. It demonstrates the fragility of homemade cipher schemes against basic cryptanalysis.

## Solucionario

### Task 1: Los tres cifrados / The three ciphers
**Explicación:**
1. THM{the.quieter.you.become.the.more.you.will.hear}
2. THM{Custom.crypto.can't.stop.you}
3. THM{emptying_the_deposit_3_million}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{the.quieter.you.become.the.more.you.will.hear}` |
| 1.2 | `THM{Custom.crypto.can't.stop.you}` |
| 1.3 | `THM{emptying_the_deposit_3_million}` |

---

**Metodología:**
Análisis del texto cifrado en tres fases: identificar el cifrado de cada capa (codificación, cifrado por sustitución o desplazamiento, etc.), invertir el proceso capa a capa y extraer las flags literales.

### Cadena de ataque / Attack Chain
1. Identificación de la primera capa de cifrado.
2. Descifrado de la primera fase.
3. Aplicación recursiva de las fases restantes.
4. Recuperación de la cadena final y extracción de las tres flags.

**Learning chain:**
Cifrado 1 → Cifrado 2 → Cifrado 3 → Flags completas.

**Lección:** *Tres capas de cifrado casero no añaden seguridad real si el criptoanálisis básico permite invertirlas una a una.*

**MITRE ATT&CK:**
- No aplica (reto de criptografía — debilidad de cifrado personalizado, CWE-327).

**Fuente:** [TryHackMe - TryHack3M_ TriCipher Summit](https://tryhackme.com/room/tryhack3mencryptionchallenge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.