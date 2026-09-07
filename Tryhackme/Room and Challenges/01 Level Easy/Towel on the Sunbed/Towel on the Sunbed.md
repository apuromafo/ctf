# Towel on the Sunbed

| **Dificultad** | Medium |
| **Tipo** | challenge |
| **Slug** | `hh-towelonthesunbed-61271709` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/hh-towelonthesunbed-61271709) |
| **Sección** | Hunt & Hack House |
| **Fuente** | THM |
| **Componentes** | double spending/NFC/contactless/mobile payments |
| **Impacto** | Explotación de vulnerabilidades en pagos contactless mediante técnica de doble gasto |

---

**Contexto:** En la playa, el protocolo de pago contactless del Sunbed presenta una vulnerabilidad crítica: double spending. Un atacante puede reproducir transacciones NFC para obtener servicios sin cargo, demostrando que la falta de validación en tiempo real de pagos contactless permite el doble gasto de la misma transacción.

## Solucionario

### Task 1: Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{t0w3l_0n_th3_sunb3d_d0ubl3_sp3nt}` |

---

**Metodología:** Se analiza el flujo de transacciones NFC/contactless implementado por el sistema de pagos del Sunbed. Mediante interceptación y replay de paquetes de pago contactless se explota la vulnerabilidad de double spending, permitiendo reproducir la misma transacción múltiples veces sin detección. La ausencia de validación criptográfica en tiempo real facilita la duplicación de pagos, revelando la flag ocuesta en el proceso.

**Learning chain:** NFC protocol analysis → contactless payment interception → transaction replay → double spending exploitation → mobile payment vulnerability → flag extraction

**MITRE ATT&CK:** T1557 (Adversary-in-the-Middle), T1185 (Browser Session Hijacking)

**Fuente:** [TryHackMe - Towel on the Sunbed](https://tryhackme.com/r/room/hh-towelonthesunbed-61271709)
