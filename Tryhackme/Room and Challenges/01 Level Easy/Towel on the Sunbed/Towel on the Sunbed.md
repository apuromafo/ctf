# Towel on the Sunbed

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `hh-towelonthesunbed-61271709` | [TryHackMe](https://tryhackme.com/room/hh-towelonthesunbed-61271709) | Hunt & Hack House | THM | double spending/NFC/contactless/mobile payments | Explotación de vulnerabilidades en pagos contactless mediante técnica de doble gasto |

---

**Contexto:**

> **ES:** En la playa, el protocolo de pago contactless del Sunbed presenta una vulnerabilidad crítica: double spending. Un atacante puede reproducir transacciones NFC para obtener servicios sin cargo, demostrando que la falta de validación en tiempo real de pagos contactless permite el doble gasto de la misma transacción.

> **EN:** At the beach, the Sunbed's contactless payment protocol has a critical vulnerability: double spending. An attacker can replay NFC transactions to obtain services without being charged, showing that the lack of real-time validation of contactless payments allows the same transaction to be double-spent.

## Solucionario

### Task 1: Flag / Flag

**Explicación:**

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{t0w3l_0n_th3_sunb3d_d0ubl3_sp3nt}` |

---

**Metodología:** Se analiza el flujo de transacciones NFC/contactless implementado por el sistema de pagos del Sunbed. Mediante interceptación y replay de paquetes de pago contactless se explota la vulnerabilidad de double spending, permitiendo reproducir la misma transacción múltiples veces sin detección. La ausencia de validación criptográfica en tiempo real facilita la duplicación de pagos, revelando la flag ocuesta en el proceso.

### Cadena de ataque / Attack Chain

NFC interception → contactless payment replay → double spending → flag extraction.

**Learning chain:** NFC protocol analysis → contactless payment interception → transaction replay → double spending exploitation → mobile payment vulnerability → flag extraction

**Lección:** *El pago sin contacto necesita validación criptográfica en tiempo real: confiar en la unicidad de una transacción sin verificarla permite duplicar su gasto.*

**MITRE ATT&CK:** T1557 (Adversary-in-the-Middle), T1185 (Browser Session Hijacking)

**Fuente:** [TryHackMe - Towel on the Sunbed](https://tryhackme.com/r/room/hh-towelonthesunbed-61271709)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.