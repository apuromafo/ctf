# Hydra

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hydra` | https://tryhackme.com/room/hydra | 01 Level Easy | TryHackMe | Hydra / fuerza bruta online / SSH / HTTP / wordlists | Automatizar ataques de fuerza bruta contra servicios de red para recuperar credenciales y acceder al objetivo. |

---

**Contexto:** Sala dedicada a la herramienta Hydra: ataque de fuerza bruta contra servicios online (SSH, HTTP, etc.) con diccionarios de contraseñas. Tras la introducción teórica se despliegan máquinas o servicios y se utilizan wordlists para encontrar las credenciales y obtener las flags.

> **ES:** Aprende a usar Hydra para atacar servicios de red con fuerza bruta y obtén las flags una vez comprometido el objetivo.
> **EN:** Learn to use Hydra to brute-force network services and get the flags once the target is compromised.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de Hydra y de los conceptos de fuerza bruta; tarea de lectura sin respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de introducción a Hydra. | `No answer needed` |

### Task 2: Hydra en práctica / Hydra in Practice

**Explicación:** Se despliega el objetivo y se lanza Hydra contra el servicio expuesto usando una wordlist; una vez obtenidas las credenciales válidas se accede al sistema y se recuperan las flags del reto.

1. 1. THM{2673a7dd116de68e85c48ec0b1f2612e}
   2. THM{c8eeb0468febbadea859baeb33b2541b}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{2673a7dd116de68e85c48ec0b1f2612e}` |
| 2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{c8eeb0468febbadea859baeb33b2541b}` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | Lee el material de introducción a Hydra. | `No answer needed` |
| 2 | 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{2673a7dd116de68e85c48ec0b1f2612e}` |
| 2 | 2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{c8eeb0468febbadea859baeb33b2541b}` |

---

**Metodología:** Identificar el servicio expuesto (SSH, HTTP, etc.), preparar una wordlist adecuada, lanzar Hydra con el módulo correspondiente, validar las credenciales encontradas, acceder al objetivo con ellas y recoger las flags.

### Cadena de ataque / Attack Chain

```text
identificar servicio -> wordlist -> hydra (-l/-L -p/-P) -> credenciales válidas -> acceso -> flags
```

**Learning chain:** Online Brute Force -> Hydra -> wordlists -> credenciales -> acceso -> flags.

**Lección:** *Hydra automatiza la fuerza bruta contra servicios de red; con wordlists adecuadas recupera credenciales débiles, pero solo debe usarse en entornos autorizados y como parte de una prueba de seguridad controlada.*

**MITRE ATT&CK:** T1110 (Brute Force)

**Fuente:** [TryHackMe - Hydra](https://tryhackme.com/room/hydra)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
