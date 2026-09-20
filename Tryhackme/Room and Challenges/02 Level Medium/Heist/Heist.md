# Heist

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | heist | https://tryhackme.com/room/heist | 02 Level Medium | TryHackMe | Blockchain/web3, smart contracts, cast/Foundry, Ethereum | Compromiso del contrato (treasury drain) |

---

**Contexto:** **Heist** es el reto de blockchain/web3 del evento Hackfinity Battle (Encore) de TryHackMe. El objetivo es comprometer un contrato Ethereum con diseño inseguro: una función `changeOwnership()` sin comprobaciones permite hacerse dueño del contrato y `withdraw()` drena el tesoro (200 ETH) a la wallet del atacante. Se opera con las herramientas `cast` de Foundry desde terminal/scripts.

## Solucionario

### Task 1

**Explicación:** El reto entrega la dirección del contrato y sus ABI/fuente. Se identifica que `changeOwnership()` no valida el llamador (no hay `onlyOwner`), de modo que cualquier cuenta puede ejecutarla y quedarse con la propiedad; después `withdraw()` transfiere el balance (200 ETH) a la wallet atacante. El flag se obtiene al completar el robo del tesoro.

```bash
# Foundry / cast
cast send <CONTRACT> "changeOwnership()" --private-key <KEY> --rpc-url <RPC>
cast send <CONTRACT> "withdraw()" --private-key <KEY> --rpc-url <RPC>
```

Respuestas de la tarea:

1. `THM{web3_h31st_d0ne}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | What is the flag? | `THM{web3_h31st_d0ne}` |

---

**Metodología:** Revisión del diseño del smart contract (control de acceso ausente en `changeOwnership`), interacción con el contrato vía `cast` (Foundry) y drenaje del balance (auditoría de smart contracts / blockchain CTF).

**Learning chain:** contrato Ethereum expuesto → review del código (sin `onlyOwner` en changeOwnership) → cast send changeOwnership() → propiedad transferida → withdraw() → treasury drain (200 ETH) → flag.

**Lección:** *El diseño de un contrato sin control de acceso (`onlyOwner`) en funciones sensibles permite a cualquiera transferirse la propiedad y drenar el tesoro: los checks de quién puede llamar son tan importantes como la lógica de negocio.*

**MITRE ATT&CK:** T1595 Active Scanning (revisión de ABI/fuente del contrato) · T1078 Valid Accounts (abuso de una función sin control de acceso) · T1068 Exploitation for Privilege Escalation (apropiación del ownership).

**Fuente:** [TryHackMe - Heist](https://tryhackme.com/room/heist)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.