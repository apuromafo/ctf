# BreachBlocker Unlocker

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | challenge | `sq4-aoc2025-32LoZ4zePK` | [TryHackMe](https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK) | Advent of Cyber 2025 (Side Quest 4) | THM | mobile app, timing attack, OTP bypass, SMTP | — Alto — bypass de autenticación móvil mediante timing attack y reintento OTP, con potencial de acceso a código fuente, servicios de streaming y banca |

---

**Contexto:** El Side Quest 4 plantea el análisis de una aplicación móvil de seguridad llamada BreachBlocker. El jugador debe encontrar la clave de desbloqueo, extraer código fuente de la app para descubrir vulnerabilidades, ejecutar un timing attack contra el mecanismo OTP, y finalmente explotar el bypass para obtener las flags de los distintos servicios (código, HopFlix y banco).

## Solucionario

### Task 1: Unlock

**Explicación:** Se parte de la clave de desbloqueo obtenida en el reto del Day 21 (análisis del HTA) para desbloquear la aplicación móvil BreachBlocker e iniciar el análisis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (from Day 21 HTA) | `throne123*` |

### Task 2: Challenges

**Explicación:** Tras extraer y revisar el código fuente de la app se descubren las vulnerabilidades (endpoint OTP expuesto a timing attack y bypass de verificación) y se explotan para acceder de forma progresiva a los servicios de código, HopFlix y banco, capturando la flag de cada uno.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the CODE_FLAG? | `THM{eggsposed_source_code}` |
| 2 | What's the HOPFLIX_FLAG? | `THM{fluffier_things_season_4}` |
| 3 | What's the BANK_FLAG? | `THM{neggative_balance}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (from Day 21 HTA) | `throne123*` |
| 2 | What's the CODE_FLAG? | `THM{eggsposed_source_code}` |
| 3 | What's the HOPFLIX_FLAG? | `THM{fluffier_things_season_4}` |
| 4 | What's the BANK_FLAG? | `THM{neggative_balance}` |

---

**Metodología:** Obtención de clave HTA del Day 21 → extracción y análisis de código fuente de la app móvil → identificación de endpoint OTP vulnerable a timing attack → explotación del bypass de verificación OTP → acceso progresivo a servicios (código → HopFlix → banco) → extracción de flags en cada servicio.

### Cadena de ataque / Attack Chain

```text
Clave HTA (Day 21) → extracción y descompilación APK → revisión de código fuente → identificación del endpoint OTP → timing attack → bypass de verificación OTP → acceso a servicios (código → HopFlix → banco) → extracción de flags
```

**Learning chain:** HTA extraction → mobile APK decompilation → source code review → timing attack → OTP bypass → multi-service flag hunting

**Lección:** *Un mecanismo OTP mal implementado y expuesto a timing attacks permite eludir la autenticación móvil y encadenar el compromiso de múltiples servicios a partir de una única clave inicial.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1040 (Network Sniffing — timing side-channel), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - BreachBlocker Unlocker](https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.