# Multi-Factor Authentication

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (autenticación/defensa) | `multifactorauthentication` | https://tryhackme.com/room/multifactorauthentication | 01 Level Easy | TryHackMe | MFA / factores de autenticación / rate limiting / phishing MFA / hashes | Fundamentos de la autenticación multifactor (MFA), sus factores y los métodos de bypass en ataques reales. |

---

**Contexto:** Sala dedicada a la autenticación multifactor (MFA). Se presentan los factores de autenticación (por ejemplo, "algo que tienes"), se debate si el MFA por sí solo es suficiente, se analiza el `rate limiting` como protección frente a fuerza bruta, y se estudian ataques reales de robo de tokens/sesiones que entregan tres hashes. Cierra con una tarea de lectura sin respuesta.

> **ES:** Qué es el MFA, sus factores ("algo que tienes"), cómo el rate limiting protege el login y cómo los ataques de phishing roban tokens.
> **EN:** What MFA is, its factors ("something you have"), how rate limiting protects logins and how phishing attacks steal tokens.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de la problemática del MFA. Tarea de lectura sin respuesta.

Contenido original de la tarea / Original task content:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 2: Factores de autenticación / Authentication factors

**Explicación:** Se repasa un factor clásico basado en la posesión: "algo que tienes" (`Something you have`).

Contenido original de la tarea / Original task content:

```text
2. Something you have
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Factor de autenticación por posesión / Possession-based authentication factor | `Something you have` |

### Task 3: ¿Es suficiente el MFA? / Is MFA enough?

**Explicación:** La pregunta de reflexión de la sala se responde afirmativamente (`yea`): el MFA es una capa adicional relevante de seguridad.

Contenido original de la tarea / Original task content:

```text
3. yea
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta a la pregunta de reflexión (yay/nay) / Reflection question answer (yay/nay) | `yea` |

### Task 4: Protección del login / Login protection

**Explicación:** La medida que limita el número de intentos de autenticación por unidad de tiempo, protegida frente a fuerza bruta del código MFA, es el `rate limiting`.

Contenido original de la tarea / Original task content:

```text
4. rate limiting
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Medida contra fuerza bruta del código MFA / Countermeasure against MFA code brute-force | `rate limiting` |

### Task 5: Primer hash del escenario / First scenario hash

**Explicación:** Primer hash recuperado durante el escenario de robo de tokens/cookies de sesión del laboratorio. Se conserva verbatim.

Contenido original de la tarea / Original task content:

```text
5. 904c8ac84e44f0ba942e9e11ee7037b8
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer hash del escenario / First hash of the scenario | `904c8ac84e44f0ba942e9e11ee7037b8` |

### Task 6: Segundo hash del escenario / Second scenario hash

**Explicación:** Segundo hash recuperado durante el escenario de robo de tokens/cookies de sesión del laboratorio. Se conserva verbatim.

Contenido original de la tarea / Original task content:

```text
6. 87880e9d27001affdff90989f351c46
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Segundo hash del escenario / Second hash of the scenario | `87880e9d27001affdff90989f351c46` |

### Task 7: Tercer hash del escenario / Third scenario hash

**Explicación:** Tercer hash recuperado durante el escenario de robo de tokens/cookies de sesión del laboratorio. Se conserva verbatim.

Contenido original de la tarea / Original task content:

```text
7. 20548e076dbb9ba30c9d94ae4aceb38e
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tercer hash del escenario / Third hash of the scenario | `20548e076dbb9ba30c9d94ae4aceb38e` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre de la sala sobre la posición del MFA dentro de una estrategia de defensa. Tarea de lectura sin respuesta.

Contenido original de la tarea / Original task content:

```text
8. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Factor de autenticación por posesión / Possession-based authentication factor | `Something you have` |
| 2 | Respuesta a la pregunta de reflexión (yay/nay) / Reflection question answer (yay/nay) | `yea` |
| 3 | Medida contra fuerza bruta del código MFA / Countermeasure against MFA code brute-force | `rate limiting` |
| 4 | Primer hash del escenario / First hash of the scenario | `904c8ac84e44f0ba942e9e11ee7037b8` |
| 5 | Segundo hash del escenario / Second hash of the scenario | `87880e9d27001affdff90989f351c46` |
| 6 | Tercer hash del escenario / Third hash of the scenario | `20548e076dbb9ba30c9d94ae4aceb38e` |

---

**Metodología:** Comprender los factores de autenticación (posesión), valorar el MFA como capa adicional, aplicar `rate limiting` para frenar la fuerza bruta sobre el código, y analizar los hashes resultantes de los escenarios de robo de tokens de sesión del laboratorio.

### Cadena de ataque / Attack Chain

```text
Login con MFA -> factor "algo que tienes" -> rate limiting (protección) -> bypass/robo de tokens de sesión -> hashes 904c8ac8... / 87880e9d... / 20548e07...
```

**Learning chain:** MFA -> factores (algo que tienes) -> suficiencia del MFA -> rate limiting -> phishing/robo de tokens -> hashes capturados.

**Lección:** *El MFA añade una capa de seguridad importante, pero no es infalible: el hurto de tokens de sesión y los ataques de fatiga lo evaden; el rate limiting y la monitorización son complementos necesarios.* 

**MITRE ATT&CK:** T1621 (Multi-Factor Authentication Request Generation), T1566 (Phishing), T1133 (External Remote Services)

**Fuente:** [TryHackMe - Multi-Factor Authentication](https://tryhackme.com/room/multifactorauthentication)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.